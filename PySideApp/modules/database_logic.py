import psycopg2
import re
import datetime

class DataBaseAgent:
    def __init__(self):
        self._dbname = None
        self._user = None
        self._password = None
        self._host = None
        self._port = None
        self.data = None
        self.conn = None
        self.cur = None
        self.isConnect = False

    def __bool__(self):
        return self.isConnect

    def connect(self, dbname, user, password, host, port):
        self._dbname = dbname
        self._user = user
        self._password = password
        self._host = host
        self._port = port
        try:
            self.conn = psycopg2.connect(dbname=dbname, user=user, password=password, host=host, port=port)
            self.data = self.get_persons_embeddings()
            self.isConnect = True
        except psycopg2.OperationalError:
            return False
        return True

    def add_an_entry(self,
                     first_name,
                     second_name,
                     gender_female,
                     department,
                     access_level,
                     birthdate,
                     passport_id,
                     phone_number,
                     email,
                     photo,
                     embedding
                     ):
        # Email to lower
        email = email.lower()

        # Photo path to bin
        with open(photo, 'rb') as file:
            photo_data = file.read()


        # SQL-запросы
        insert_person_query = """
            INSERT INTO person (passport_id, first_name, second_name, gender_female, birthday, department, access_level, embedding, photo)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
        """

        insert_contact_query = """
            INSERT INTO person_contact (fk_passport_id, phone, email)
            VALUES (%s, %s, %s)
        """


        def validate_email(email):
            pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
            return re.match(pattern, email) is not None

        if not validate_email(email):
            return "incorrect_email"

        # Данные для вставки
        person_data = (
            passport_id,
            first_name,
            second_name,
            gender_female,
            birthdate,
            department,
            access_level,
            embedding,
            photo_data
        )
        contact_data = (
            passport_id,
            phone_number,
            email
        )
        try:
            self.cur = self.conn.cursor()
            self.cur.execute(insert_person_query, person_data)  # Вставка данных в таблицу person
            self.cur.execute(insert_contact_query, contact_data)  # Вставка данных в таблицу person_contact
            self.conn.commit()  # Фиксация изменений
            return "ok"
        except AttributeError:
            return "not_connected"
        except psycopg2.errors.UniqueViolation:
            self.conn.rollback()
            return "already_exist"
        except (Exception, psycopg2.Error) as error:
            print("Ошибка при добавлении данных в базу данных:", error)
            self.conn.rollback()
        self.cur.close()

    def get_persons_embeddings(self):
        sql_request = """
            SELECT passport_id, embedding FROM person
        """
        cur = self.conn.cursor()
        cur.execute(sql_request)
        data = cur.fetchall()
        cur.close()
        return dict(data)

    def add_to_history(self, id_person, id_location):
        sql_request = """
            INSERT INTO history (fk_id_person, fk_location, date_event)
            VALUES (%s, %s, CURRENT_TIMESTAMP)
        """
        cur = self.conn.cursor()
        cur.execute(sql_request, (id_person, id_location))
        self.conn.commit()
        cur.close()

    def add_location(self, title, access_level):
        sql_request = """
            INSERT INTO location (name, access_level)
            VALUES (%s, %s)
        """
        cur = self.conn.cursor()
        try:
            cur.execute(sql_request, (title, access_level))
        except psycopg2.errors.UniqueViolation:
            self.conn.rollback()
            return "already_exist"

        self.conn.commit()
        cur.close()

    def get_all_location(self):
        sql_request = """
            SELECT name, access_level FROM location;
        """
        cur = self.conn.cursor()
        cur.execute(sql_request)
        data = cur.fetchall()
        cur.close()
        return data

    def get_main_data_by_id(self, id):
        sql_request = """
                    SELECT first_name, second_name, birthday, gender_female, department, access_level, photo  FROM person
                    WHERE passport_id = %s;
                """
        cur = self.conn.cursor()
        cur.execute(sql_request, (id,))
        data = cur.fetchall()
        cur.close()
        return data

    def get_all_main_data(self):
        sql_request = """
                    SELECT passport_id, first_name, second_name, birthday, gender_female FROM person
                """
        cur = self.conn.cursor()
        cur.execute(sql_request)
        data = cur.fetchall()
        sql_request = """
                            SELECT fk_passport_id, phone, email  FROM person_contact
                        """
        cur.execute(sql_request)
        contact_data = cur.fetchall()
        cur.close()
        return data, contact_data

    def remove_person_by_id(self, id):
        sql_request = """
                    DELETE FROM person_contact
                    WHERE fk_passport_id = %s;
                """
        cur = self.conn.cursor()
        cur.execute(sql_request, (id,))
        sql_request = """
                    DELETE FROM person
                    WHERE passport_id = %s;
                """
        cur.execute(sql_request, (id,))
        self.conn.commit()
        cur.close()






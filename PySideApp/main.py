import threading
import time
import sys
import os
from datetime import date
import cv2
import numpy as np

# IMPORT / GUI AND MODULES AND WIDGETS
# ///////////////////////////////////////////////////////////////
from PySide6.QtCore import Qt, QRect
from modules import *
import insightface
from nn_models.Detection.my_faceboxes_wrapper import pad_faces
from modules.database_logic import *
from modules.right_box import *
from modules.location import *
os.environ["QT_FONT_DPI"] = "96"  # FIX Problem for High DPI and Scale above 100%


def find_cosine_distance(source_representation, test_representation):
    a = np.matmul(np.transpose(source_representation), test_representation)
    b = np.sum(np.multiply(source_representation, source_representation))
    c = np.sum(np.multiply(test_representation, test_representation))
    return 1 - (a / (np.sqrt(b) * np.sqrt(c)))


class FrameCounter:
    def __init__(self, print_mode=True):

        self.print_mode = print_mode
        self.start_time = time.time()
        self.count = 0

    def __call__(self, *args, **kwargs):
        self.count += 1
        if time.time() - self.start_time > 1:
            self.start_time = time.time()
            for_return = self.count
            self.count = 0
            if self.print_mode:
                print(f"FPS: {for_return}")
            else:
                return for_return


# SET AS GLOBAL WIDGETS
# ///////////////////////////////////////////////////////////////
widgets = None


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.frame_counter = FrameCounter(print_mode=False)
        self.current_embedding = None
        self.first_open_right_box = True
        self.last_people = None
        # confidence
        self.number_of_last_persons = deque(maxlen=3)
        self.number_of_last_persons.append(("dumpy", "dumpy2", "dumpy3"))
        self.distance_threshold = 0.7

        self.last_recognized_time = time.time()
        # SET AS GLOBAL WIDGETS
        # ///////////////////////////////////////////////////////////////
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.db_agent = DataBaseAgent()
        global widgets
        widgets = self.ui

        # USE CUSTOM TITLE BAR | USE AS "False" FOR MAC OR LINUX
        # ///////////////////////////////////////////////////////////////
        Settings.ENABLE_CUSTOM_TITLE_BAR = True

        # APP NAME
        # ///////////////////////////////////////////////////////////////
        title = "CourseWork"
        # description = "PyDracula APP - Theme with colors based on Dracula for Python." # можно раскоментить
        # APPLY TEXTS
        self.setWindowTitle(title)
        # widgets.titleRightInfo.setText(description)# можно раскоментить

        # TOGGLE MENU
        # ///////////////////////////////////////////////////////////////
        widgets.toggleButton.clicked.connect(lambda: UIFunctions.toggleMenu(self, True))

        # SET UI DEFINITIONS
        # ///////////////////////////////////////////////////////////////
        UIFunctions.uiDefinitions(self)

        # QTableWidget PARAMETERS
        # ///////////////////////////////////////////////////////////////
        widgets.view_tabble.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        # ///////////////////////////////////////////////////////////////
        self.add_all_fields = {
            "first_name": self.ui.add_first_name.text(),
            "second_name": self.ui.add_last_name.text(),
            "gender_female": self.ui.add_female.isChecked(),
            "department": self.ui.add_department.text(),
            "access_level": self.ui.add_access_level.currentText(),
            "birthdate": self.ui.add_birthday.text(),
            "passport_id": self.ui.add_passport_id.text(),
            "phone_number": self.ui.add_phone_number.text(),
            "email": self.ui.add_email.text(),
            "photo": self.ui.add_text_path.text(),
        }

        # LEFT MENUS
        widgets.btn_home.clicked.connect(self.buttonClick)
        widgets.btn_add.clicked.connect(self.buttonClick)
        widgets.btn_base.clicked.connect(self.buttonClick)
        widgets.btn_history.clicked.connect(self.buttonClick)
        widgets.btn_locations.clicked.connect(self.buttonClick)
        self.ui.choose_location_addnew.clicked.connect(self.buttonClick)
        self.ui.add_location_back.clicked.connect(self.buttonClick)
        # EXTRA RIGHT MENUS
        widgets.settings_database.clicked.connect(self.buttonClick)
        widgets.settings_for_developers.clicked.connect(self.buttonClick)
        widgets.adb_cancel.clicked.connect(self.buttonClick)
        widgets.adb_connect.clicked.connect(self.buttonClick)
        widgets.db_successful_back.clicked.connect(self.buttonClick)
        widgets.add_add_person.clicked.connect(self.buttonClick)
        widgets.add_clear_person.clicked.connect(self.buttonClick)
        widgets.view_dellete.clicked.connect(self.buttonClick)
        widgets.dev_setting_cancel.clicked.connect(self.buttonClick)

        # ADD PERSON INNER
        widgets.add_first_name.textChanged.connect(self.check_add_field_status)
        widgets.add_last_name.textChanged.connect(self.check_add_field_status)
        widgets.add_department.textChanged.connect(self.check_add_field_status)
        widgets.add_access_level.activated.connect(self.check_add_field_status)
        widgets.add_birthday.textChanged.connect(self.check_add_field_status)
        widgets.add_passport_id.textChanged.connect(self.check_add_field_status)
        widgets.add_phone_number.textChanged.connect(self.check_add_field_status)
        widgets.add_email.textChanged.connect(self.check_add_field_status)
        widgets.add_text_path.textChanged.connect(self.check_add_field_status)
        widgets.add_male.toggled.connect(self.check_add_field_status)
        widgets.add_female.toggled.connect(self.check_add_field_status)
        # ADD PERSON DATA EDITING
        widgets.add_birthday.textChanged.connect(self.format_date)
        widgets.add_phone_number.textChanged.connect(self.format_phone_number)
        # ADD PERSON GENDER
        widgets.add_male.toggled.connect(lambda x: widgets.add_photo_place.setStyleSheet(style_add_photo_man))
        widgets.add_female.toggled.connect(lambda x: widgets.add_photo_place.setStyleSheet(style_add_photo_woman))
        # IMAGE FOLDER OPEN
        widgets.add_button_path.clicked.connect(lambda x: self.open_file_dialog())
        widgets.add_text_path.textChanged.connect(
            lambda x: self.set_image_to_label(widgets.add_text_path.text(), widgets.add_photo_place))
        # OTHER


        # EXTRA LEFT BOX
        def openCloseLeftBox():
            UIFunctions.toggleLeftBox(self, True)

        # widgets.toggleLeftBox.clicked.connect(openCloseLeftBox)
        widgets.extraCloseColumnBtn.clicked.connect(openCloseLeftBox)

        # EXTRA RIGHT BOX
        def openCloseRightBox():
            if self.first_open_right_box:
                widgets.db_incorrect_data.setVisible(False)
                widgets.stackedWidget_adb.setCurrentWidget(widgets.frame_settings)
                self.first_open_right_box = False
            UIFunctions.toggleRightBox(self, True)

        widgets.settingsTopBtn.clicked.connect(openCloseRightBox)

        # SHOW APP
        # ///////////////////////////////////////////////////////////////
        self.show()

        # SET CUSTOM THEME
        # ///////////////////////////////////////////////////////////////
        useCustomTheme = False
        themeFile = "themes\py_dracula_light.qss"

        # SET THEME AND HACKS
        if useCustomTheme:
            # LOAD AND APPLY STYLE
            UIFunctions.theme(self, themeFile, True)

            # SET HACKS
            AppFunctions.setThemeHack(self)

        # SET HOME PAGE AND SELECT MENU
        # ///////////////////////////////////////////////////////////////
        widgets.stackedWidget.setCurrentWidget(widgets.home)
        widgets.btn_home.setStyleSheet(UIFunctions.selectMenu(widgets.btn_home.styleSheet()))

        # Camera
        widgets.home_start_system.clicked.connect(self.start_capture)
        # Создание объекта VideoCapture для захвата изображения с вебкамеры
        self.video_capture = cv2.VideoCapture(0)
        # Флаг для остановки потока
        self.stopped = False

        # FACE DETECTION OPTIONS
        self.backend_detector = "ssd"

        # BOUNDING BOX OPTIONS
        self.bounding_box_thickness = 2
        self.bounding_box_color = (0, 255, 255)

        self.dev_setting = DevSetting(self, self.db_agent)
        self.location = Location(self, self.db_agent)

    # BUTTONS CLICK
    # Post here your functions for clicked buttons
    # ///////////////////////////////////////////////////////////////
    def buttonClick(self):
        # GET BUTTON CLICKED
        btn = self.sender()
        btnName = btn.objectName()


        # SHOW HOME PAGE
        if btnName == "btn_home":
            widgets.stackedWidget.setCurrentWidget(widgets.home)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))

        # SHOW WIDGETS PAGE
        if btnName == "btn_add":
            self.ui.add_message.setVisible(False)

            widgets.stackedWidget.setCurrentWidget(widgets.add)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))

        # SHOW NEW  PAGE

        if btnName == "btn_base":
            self.update_table()
            widgets.stackedWidget.setCurrentWidget(widgets.base)  # SET PAGE
            UIFunctions.resetStyle(self, btnName)  # RESET ANOTHERS BUTTONS SELECTED
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))  # SELECT MENU

        if btnName == "btn_history":
            widgets.stackedWidget.setCurrentWidget(widgets.history)  # SET PAGE
            UIFunctions.resetStyle(self, btnName)  # RESET ANOTHERS BUTTONS SELECTED
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))  # SELECT MENU

        if btnName == "btn_locations":
            self.location.location_update()
            self.location.location_changed()

            widgets.stackedWidget.setCurrentWidget(widgets.location)  # SET PAGE
            UIFunctions.resetStyle(self, btnName)  # RESET ANOTHERS BUTTONS SELECTED
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))  # SELECT MENU

        if btnName == "settings_database":
            widgets.stackedWidget_adb.setCurrentWidget(widgets.frame_settings_db)  # SET PAGE

        if btnName == "settings_for_developers":
            widgets.stackedWidget_adb.setCurrentWidget(widgets.for_developers)  # SET PAGE

        if btnName in ("adb_cancel", "dev_setting_cancel"):
            widgets.stackedWidget_adb.setCurrentWidget(widgets.frame_settings)  # SET PAGE

        if btnName == "adb_connect":
            dict_db_params = {
                "dbname": self.ui.adb_name.text(),
                "user": self.ui.adb_user.text(),
                "password": self.ui.adb_password.text(),
                "host": self.ui.adb_host.text(),
                "port": self.ui.adb_port.text(),
            }
            if self.db_agent.connect(**dict_db_params):
                widgets.stackedWidget_adb.setCurrentWidget(widgets.frame_db_connect_successful)  # SET PAGE
                widgets.db_incorrect_data.setVisible(False)
            else:
                widgets.db_incorrect_data.setVisible(True)

        if btnName == "db_successful_back":
            widgets.stackedWidget_adb.setCurrentWidget(widgets.frame_settings)

        if btnName == "add_add_person":
            face_image = cv2.imread(self.ui.add_text_path.text())
            face, coord = pad_faces(face_image)
            model = insightface.model_zoo.get_model(f"../nn_models/Recognition/arcface{100 if self.dev_setting.applied_settings['backbone'][-2:] == '00' else self.dev_setting.applied_settings['backbone'][-2:]}.onnx")
            model.prepare(ctx_id=-1 if self.dev_setting.applied_settings["device"] == "CPU" else 0)
            embedding = model.get_feat(imgs=face)

            status = self.db_agent.add_an_entry(**self.add_all_fields, embedding=embedding[0].tolist())
            if status == "ok":
                self.add_clean_fields()
                self.set_add_message("Person added successfully", "green")

            elif status == "already_exist":

                self.set_add_message("The entry already exist", "red")

            elif status == "not_connected":
                self.set_add_message("DataBase isn't connected", "red")

            elif status == "incorrect_email":
                self.set_add_message("Email address is incorrect", "red")

        if btnName == "add_clear_person":
            self.add_clean_fields()

        if btnName == "view_dellete":
            self.delete_row()

        if btnName == "choose_location_addnew":
            widgets.stackedWidget.setCurrentWidget(widgets.add_location)  # SET PAGE

        if btnName == "add_location_back":
            self.location.location_update()
            self.location.location_changed()
            widgets.stackedWidget.setCurrentWidget(widgets.location)  # SET PAGE


    def add_clean_fields(self):
        add_text_fields = [
            self.ui.add_first_name,
            self.ui.add_last_name,
            self.ui.add_department,
            self.ui.add_phone_number,
            self.ui.add_birthday,
            self.ui.add_passport_id,
            self.ui.add_email,
            self.ui.add_text_path,
        ]
        for i in add_text_fields:
            i.clear()
        # self.ui.add_female.setChecked(False)
        self.ui.add_male.setChecked(True)

    def open_file_dialog(self, add_mode=True):
        file_dialog = QFileDialog(self)
        file_dialog.setFileMode(QFileDialog.ExistingFile)
        file_dialog.setNameFilter("Изображения (*.png *.jpg *.jpeg *.bmp)")

        if file_dialog.exec():
            selected_file = file_dialog.selectedFiles()[0]
            if add_mode:
                self.ui.add_text_path.setText(selected_file)
            else:
                print(add_mode)

    def check_add_field_status(self):
        self.add_all_fields = {
            "first_name": self.ui.add_first_name.text(),
            "second_name": self.ui.add_last_name.text(),
            "gender_female": self.ui.add_female.isChecked(),
            "department": self.ui.add_department.text(),
            "access_level": self.ui.add_access_level.currentText(),
            "birthdate": self.ui.add_birthday.text(),
            "passport_id": self.ui.add_passport_id.text(),
            "phone_number": self.ui.add_phone_number.text(),
            "email": self.ui.add_email.text(),
            "photo": self.ui.add_text_path.text(),
        }
        if all(filter(lambda x: type(x) is str, self.add_all_fields.values())):
            self.ui.add_add_person.setEnabled(True)
            self.ui.add_add_person.setStyleSheet(style_add_button_on)
        else:
            self.ui.add_add_person.setEnabled(False)
            self.ui.add_add_person.setStyleSheet(style_add_button_off)

    def set_add_message(self, message: str, color: str):
        self.ui.add_message.setVisible(True)
        self.ui.add_message.setText(message)
        self.ui.add_message.setStyleSheet(f"color: {color};")

    def set_image_to_label(self, path_or_data, label, padding=35):
        if type(path_or_data) is str:
            pixmap = QPixmap(path_or_data)
        elif type(path_or_data) is QPixmap:
            pixmap = path_or_data
        elif type(path_or_data) is memoryview:
            pixmap = QPixmap()
            pixmap.loadFromData(path_or_data.tobytes())
        image_width = pixmap.width()
        image_height = pixmap.height()
        target_width = label.width() - padding
        target_height = label.height() - padding
        if image_width / target_width < image_height / target_height:
            pixmap = pixmap.scaledToWidth(target_width)
        else:
            pixmap = pixmap.scaledToHeight(target_height)

        image_width = pixmap.width()
        image_height = pixmap.height()
        crop_x = (image_width - target_width) // 2
        crop_y = (image_height - target_height) // 2
        crop_width = target_width
        crop_height = target_height
        crop_rect = QRect(crop_x, crop_y, crop_width, crop_height)
        cropped_pixmap = pixmap.copy(crop_rect)

        QMetaObject.invokeMethod(label, "setPixmap", Qt.QueuedConnection,
                                 Q_ARG('QPixmap', self.rounded_pixmap(cropped_pixmap, degree=9)))
        # label.setPixmap(self.rounded_pixmap(cropped_pixmap, degree=9))

    def format_date(self, text):
        if len(text) == 3 and int(text[:2]) > 12:
            text = "12" + text[2:]
        if len(text) == 5 and int(text[3:5]) > 31:
            text = text[:3] + "31" + text[5:]
        if len(text) and not text[-1].isdigit():
            text = text[:-1]
        text = text.replace('/', '')
        if len(text) > 2:
            text = text[:2] + '/' + text[2:]
        if len(text) > 5:
            text = text[:5] + '/' + text[5:]
        self.ui.add_birthday.setText(text)

    def format_phone_number(self, text: str):
        if len(text) and not text[-1].isdigit():
            text = text[:-1]
        text = text.replace(' ', '')
        if len(text) and text[0] == "8":
            text = "+7 " + text[1:]
        elif len(text) and text[0].isdigit():
            text = f"+{text[0]} " + text[1:]
        if len(text) > 2:
            text = text[:2] + ' ' + text[2:]
        if len(text) > 6:
            text = text[:6] + ' ' + text[6:]
        if len(text) > 10:
            text = text[:10] + ' ' + text[10:]
        if len(text) > 13:
            text = text[:13] + ' ' + text[13:]
        self.ui.add_phone_number.setText(text)

    def rounded_pixmap(self, pixmap, degree=10):
        rounded = QPixmap(pixmap.size())
        rounded.fill(Qt.transparent)
        path = QPainterPath()
        path.addRoundedRect(rounded.rect(), degree, degree)
        painter = QPainter(rounded)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.setClipPath(path)
        painter.drawPixmap(0, 0, pixmap)
        painter.end()
        return rounded

    def start_capture(self):
        if not self.stopped:
            self.ui.home_video_place.setText('Loading...')
            # Создание отдельного потока для захвата изображения
            t = threading.Thread(target=self.capture_thread)
            t.start()
            self.ui.home_start_system.setText('Stop')

        else:
            self.stopped = False
            self.ui.home_start_system.setText('Start')

    def capture_thread(self):
        self.stopped = True
        model = insightface.model_zoo.get_model(f"../nn_models/Recognition/arcface{100 if self.dev_setting.applied_settings['backbone'][-2:] == '00' else self.dev_setting.applied_settings['backbone'][-2:]}.onnx")
        model.prepare(ctx_id=-1 if self.dev_setting.applied_settings["device"] == "CPU" else 0)  # 0 is cuda, -1 is cpu
        fps = 0
        while self.stopped:
            ret, frame = self.video_capture.read()
            fps = self.frame_counter() or fps
            if self.dev_setting.applied_settings["show_fps"]:
                cv2.putText(frame, str(fps), (15, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 255, 255), 2)

            result = pad_faces(frame)
            if result:
                face, coord = result
                embedding = model.get_feat(imgs=face)[0]
                y, x, y1, x1, = coord
                cv2.rectangle(frame, (x, y), (x1, y1), (0, 255, 0), 2)

                if self.db_agent:
                    a = {k: find_cosine_distance(np.array(v), embedding) for k, v in self.db_agent.data.items()}
                    person_id, distance = min(a.items(), key=lambda x: x[1])
                    cv2.putText(frame, str(round(distance, 3)), (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)
                    if distance < self.dev_setting.applied_settings["distance_threshold"]:
                        self.show_recognized_person(self.db_agent.get_main_data_by_id(person_id), person_id)
                    else:
                        self.show_recognized_person(False, False)

            if ret:
                # Преобразование изображения из формата BGR в RGB
                frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

                # Преобразование изображения в объект QImage
                image = QImage(
                    frame_rgb,
                    frame_rgb.shape[1],
                    frame_rgb.shape[0],
                    QImage.Format_RGB888
                )

                # Обновление изображения в QLabel
                self.update_image(image)
        else:
            self.update_image(QImage())
            time.sleep(0.05)
            self.ui.home_video_place.setText("Place for video stream")

    def update_image(self, image):
        self.set_image_to_label(QPixmap.fromImage(image), self.ui.home_video_place, padding=18)
        # QMetaObject.invokeMethod(self.ui.home_video_place, "setPixmap", Qt.QueuedConnection,
        #                          Q_ARG('QPixmap', self.rounded_pixmap(QPixmap.fromImage(image))))

    def show_recognized_person(self, data, person_id):
        if not data:
            data = [data]
        self.number_of_last_persons.append(data[-1])
        if time.time() - self.last_recognized_time > 0.5 and len(set(self.number_of_last_persons)) == 1:
            if not data[0]:
                self.ui.home_name.setText("Unknown person")
                self.ui.home_age.clear()
                self.ui.home_gender.clear()
                self.ui.home_department.clear()
                self.ui.home_level_access.clear()
                self.ui.home_photo_place.clear()
                self.last_people = None
                return
            first_name, second_name, birthday, gender_female, department, access_level, photo = data[0]
            self.ui.home_name.setText(first_name + " " + second_name)
            self.ui.home_age.setText(str(self.calculate_age(birthday)))
            self.ui.home_gender.setText("Female" if gender_female else "Male")
            self.ui.home_department.setText(department)
            self.ui.home_level_access.setText(access_level)

            if self.last_people != person_id:
                self.last_people = person_id
                self.set_image_to_label(photo, self.ui.home_photo_place, padding=0)
                self.last_recognized_time = time.time()
                #
                self.db_agent.add_to_history(person_id, 0)


    def update_table(self):
        while self.ui.view_tabble.rowCount() > 1:
            self.ui.view_tabble.removeRow(1)
        data, contact_data = self.db_agent.get_all_main_data()
        for i in range(len(data)):
            current_data, current_contact_data = data[i], contact_data[i]
            row = self.ui.view_tabble.rowCount()  # Получение текущего количества строк
            self.ui.view_tabble.insertRow(row)  # Вставка новой строки

            age = self.calculate_age(current_data[3])
            self.ui.view_tabble.setItem(row, 0, QTableWidgetItem(
                current_data[1] + " " + current_data[2]))  # Установка значения в ячейке
            self.ui.view_tabble.setItem(row, 1, QTableWidgetItem(str(age)))
            self.ui.view_tabble.setItem(row, 2, QTableWidgetItem("Female" if current_data[4] else "Male"))
            self.ui.view_tabble.setItem(row, 3, QTableWidgetItem(str(current_data[0])))
            self.ui.view_tabble.setItem(row, 4, QTableWidgetItem(str(current_contact_data[1])))
            self.ui.view_tabble.setItem(row, 5, QTableWidgetItem(str(current_contact_data[2])))

    def delete_row(self):
        selected_row = self.ui.view_tabble.currentRow()  # Получение индекса выбранной строки
        if selected_row > 0:
            id_for_remove = self.ui.view_tabble.item(selected_row, 3).text()
            self.db_agent.remove_person_by_id(id_for_remove)
            self.ui.view_tabble.removeRow(selected_row)  # Удаление выбранной строки


    # RESIZE EVENTS
    # ///////////////////////////////////////////////////////////////
    def resizeEvent(self, event):
        # Update Size Grips
        UIFunctions.resize_grips(self)
        self.set_image_to_label(self.ui.add_text_path.text(), self.ui.add_photo_place)

    # MOUSE CLICK EVENTS
    # ///////////////////////////////////////////////////////////////
    def mousePressEvent(self, event):
        # SET DRAG POS WINDOW
        self.dragPos = event.globalPos()

        # PRINT MOUSE EVENTS
        if event.buttons() == Qt.LeftButton:
            print('Mouse click: LEFT CLICK')
        if event.buttons() == Qt.RightButton:
            print('Mouse click: RIGHT CLICK')

    @staticmethod
    def calculate_age(birthdate):
        today = date.today()
        age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
        return age


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("icon.ico"))
    window = MainWindow()
    sys.exit(app.exec())

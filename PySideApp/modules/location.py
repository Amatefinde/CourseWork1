class Location:
    def __init__(self, instance, db_agent):
        self.instance = instance
        self.ui = instance.ui
        self.ui.add_location_successfully.setVisible(False)
        self.db_agent = db_agent
        self.ui.add_location_titles.textChanged.connect(self.add_string_changed)
        self.current_location = None
        self.ui.add_location_add.clicked.connect(self.add_location_pressed)
        self.ui.choose_location_choose.currentTextChanged.connect(self.location_changed)
        self.location_options = {}

    def add_string_changed(self):
        self.ui.add_location_successfully.setVisible(False)
        if self.ui.add_location_titles.text():
            self.ui.add_location_add.setEnabled(True)
        else:
            self.ui.add_location_add.setEnabled(False)

    def add_location_pressed(self):
        location_name = self.ui.add_location_titles.text()
        access_level = self.ui.add_location_access.currentText()
        self.ui.add_location_successfully.setVisible(True)

        if self.db_agent.add_location(location_name, access_level) == "already_exist":
            self.ui.add_location_successfully.setText("Already exist!")
            self.ui.add_location_successfully.setStyleSheet("color: red;")
        else:
            self.ui.add_location_successfully.setText("Location added successfully")
            self.ui.add_location_successfully.setStyleSheet("color: green;")

    def location_update(self):
        while self.ui.choose_location_choose.itemText(0):
            self.ui.choose_location_choose.removeItem(0)
        for name in self.db_agent.get_all_location():
            self.ui.choose_location_choose.addItem(name[0])
            self.location_options[name[0]] = name[1]

    def location_changed(self):
        option = self.ui.choose_location_choose.currentText()
        access = self.location_options.get(option)
        self.ui.choose_location_access_level.setText(access)

    def apply_location_pressed(self):
        self.current_location = self.ui.choose_location_choose.currentText()




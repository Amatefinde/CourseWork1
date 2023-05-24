import os.path
from collections import deque
from . custom_styles import *
import pickle


class DevSetting:
    def __init__(self, class_instance, db_agent):
        """Get self and database agent"""
        self.ui = class_instance.ui
        self.instance = class_instance
        self.db_agent = db_agent
        self.applied_settings = self.get_current()
        self.current_settings = self.get_current()
        self.ui.dev_setting_apply.clicked.connect(self.apply_setting)
        self.connect_signal()
        # Load data if exits
        self.load_setting_from_file()
        self.update_value()
        # Lock button
        self.ui.dev_setting_apply.setStyleSheet(style_add_button_off)
        self.ui.dev_setting_apply.setEnabled(False)

        self.instance.number_of_last_persons = deque(maxlen=self.applied_settings["last_persons_number"])

    def get_current(self):
        setting_current = {
            # "last_persons_deque": deque(maxlen=int(self.ui.dev_setting_number_slider.value())),
            "last_persons_number": int(self.ui.dev_setting_number_slider.value()),
            "distance_threshold": float(self.ui.dev_setting_distance_lbl.text()),
            "backbone": self.ui.dev_setting_backbone.currentText(),
            "device": self.ui.dev_setting_device.currentText(),
            "gpu_memory": self.ui.dev_setting_gpu_memory_slider.value() / 10,
            "show_fps": self.ui.dev_setting_show_fps.isChecked()
        }
        return setting_current

    def connect_signal(self):
        self.ui.dev_setting_number_slider.valueChanged.connect(self.update_value)
        self.ui.dev_setting_distance_slider.valueChanged.connect(self.update_value)
        self.ui.dev_setting_backbone.currentTextChanged.connect(self.update_value)
        self.ui.dev_setting_device.currentTextChanged.connect(self.update_value)
        self.ui.dev_setting_gpu_memory_slider.valueChanged.connect(self.update_value)
        self.ui.dev_setting_show_fps.stateChanged.connect(self.update_value)

    def update_value(self):

        num = self.ui.dev_setting_number_slider.value()
        dist = self.ui.dev_setting_distance_slider.value()
        gpu_mem = self.ui.dev_setting_gpu_memory_slider.value()
        self.ui.dev_setting_number_lbl.setText(str(num))
        self.ui.dev_setting_distance_lbl.setText(str(round(dist / 1000, 2)).ljust(4, "0"))
        self.ui.dev_setting_gpu_memory_lbl.setText(str(round(gpu_mem / 10))+"%")

        # update current setting dict
        self.current_settings = self.get_current()

        # manage apply button
        if self.current_settings == self.applied_settings:
            self.ui.dev_setting_apply.setEnabled(False)
            self.ui.dev_setting_apply.setStyleSheet(style_add_button_off)
        else:
            self.ui.dev_setting_apply.setEnabled(True)
            self.ui.dev_setting_apply.setStyleSheet(style_add_button_on)

        # manage gpu memory
        if self.ui.dev_setting_device.currentText() == "CPU":
            self.ui.dev_setting_gpu_memory_slider.setEnabled(False)
        else:
            self.ui.dev_setting_gpu_memory_slider.setEnabled(True)

    def apply_setting(self):
        self.applied_settings = self.get_current()
        self.ui.dev_setting_apply.setEnabled(False)
        self.ui.dev_setting_apply.setStyleSheet(style_add_button_off)
        # write in file
        with open("dev_settings.pickle", "wb") as file:
            pickle.dump(self.get_current(), file)

        self.instance.number_of_last_persons = deque(maxlen=self.applied_settings["last_persons_number"])


    def load_setting_from_file(self):
        if os.path.exists("dev_settings.pickle"):
            with open("dev_settings.pickle", "rb") as file:
                my_dict = pickle.load(file)

            self.ui.dev_setting_number_slider.setValue(my_dict["last_persons_number"])
            self.ui.dev_setting_distance_slider.setValue(int(my_dict["distance_threshold"]*1000))
            self.ui.dev_setting_backbone.setCurrentText(my_dict["backbone"])
            self.ui.dev_setting_device.setCurrentText(my_dict["device"])
            self.ui.dev_setting_gpu_memory_slider.setValue(int(my_dict["gpu_memory"]*10))
            self.ui.dev_setting_show_fps.setChecked(my_dict["show_fps"])

            self.applied_settings = my_dict
        else:
            print("File read is failed")



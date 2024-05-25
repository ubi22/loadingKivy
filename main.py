import threading
import time

from kivymd.uix.tab import MDTabsBase
from kivymd.uix.floatlayout import MDFloatLayout
from kivy.core.window import Window
from kivy.clock import mainthread
from kivy.lang import Builder
from kivymd.uix.filemanager import MDFileManager
from kivy.properties import ObjectProperty
from kivymd.uix.textfield import MDTextField
from kivymd.uix.datatables import MDDataTable
from kivy.metrics import dp
from kivy.properties import StringProperty
from kivymd.uix.button import MDFlatButton
from kivymd.uix.dialog import MDDialog
from kivymd.app import MDApp
from kivy.uix.modalview import ModalView
from kivymd.uix.spinner import MDSpinner
from kivy.animation import Animation
from kivymd.uix.progressbar import MDProgressBar
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.list import ThreeLineIconListItem
from kivymd.uix.list import OneLineAvatarIconListItem
Window.size = (520, 900)
#auto_dismiss=False отключение авто закрытия окна


class Content(MDBoxLayout):
    pass


class MDLoading(MDApp):
    dialog = None

    # def on_start(self):
    #     button = self.root.ids.niga
    #     animation = Animation(opacity=0, duration=0.5)
    #     animation.start(button)

    def build(self):
        return Builder.load_file('kivy.kv')

    def Threading_start(self):
        threading.Thread(target=self.loading).start()

    def loading(self):
        data = ['1','1','1','1','1','1','1']
        print("adada")
        for i in range(len(data)):
            print(i)
            self.loading_windows(i, data)
            time.sleep(1)


    @mainthread
    def loading_windows(self, i, data):
        if not self.dialog:
            self.dialog = MDDialog(
                title="Загрузка...",
                text=f'{i}/',
                auto_dismiss=False
            )
        self.dialog.open()
        self.dialog.text = f"{i+1}/{len(data)} Человек"
        if i+1 == len(data):
            self.dialog.dismiss()
        # self.root.ids.spinner.active = True

    def spinner(self):
        button = self.root.ids.niga
        animation = Animation(opacity=1, duration=0.5)
        animation.start(button)
        self.root.ids.spinner.active = "True"


MDLoading().run()
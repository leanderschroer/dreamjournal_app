import json
from math import ceil

import kivy
import datetime
from kivy.app import App
from kivy.properties import DictProperty, ObjectProperty, StringProperty
from kivy.uix import button
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.screenmanager import ScreenManager, Screen

kivy.require('1.11.1')

from kivy.config import Config

Config.set('graphics', 'width', '350')
Config.set('graphics', 'height', '600')


class Manager(ScreenManager):
    def change_screen(self, name: str):
        self.current = name
    pass


class HomeScreen(Screen):
    pass


class EditScreen(Screen):
    date = StringProperty()
    body = StringProperty()


class Archive(BoxLayout):
    display = DictProperty()
    sm = ObjectProperty()

    def build_from(self, archive: DictProperty()):
        self.display = archive
        self.clear_widgets()
        for key in self.display.keys():
            self.add_widget(
                Button(text=str(key),
                       size_hint_y=None,
                       height=100,
                       on_release=lambda x: self.sm.change_screen(x.text)
                       )
                )


class ImageButton(ButtonBehavior, Image):
    pass


class MainApp(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.archive = DictProperty()
        self.manager = ObjectProperty()
        self.archive = {}
        # dummy archive
        # abc = [i for i in 'abcdefghifjklmnop']
        # for i, a in enumerate(abc):
        #     self.archive[str(i)] = str(a)
        self.date = StringProperty()
        self.date = str(datetime.date.today())

    def build(self):
        try:
            self.load_json()
        except:
            print('[APP-INFO] No Archive found.')
        sm = Manager()
        self.manager = sm
        sm.add_widget(HomeScreen(name='Home'))
        sm.add_widget(EditScreen(name='New', date=str(self.date)))
        for key in self.archive.keys():
            sm.add_widget(
                EditScreen(name=str(key),
                           date=key,
                           body=self.archive[key]
                           )
            )
        return sm

    def save_entry(self, date: str, text: str):
        assert isinstance(text, str)
        assert isinstance(date, str)
        print(date+' '+text)
        self.archive[date] = text
        if date not in self.manager.screen_names:
            self.manager.add_widget(
                EditScreen(name=str(date),
                           date=date,
                           body=text
                           )
            )
        self.save_json()

    def save_json(self):
        with open('journal_data.txt', 'w') as outfile:
            json.dump(self.archive, outfile)

    def load_json(self):
        with open('journal_data.txt', 'r') as json_file:
            self.archive = json.load(json_file)


if __name__ == '__main__':
    App = MainApp()
    App.run()

# DONE reformat everything to be screens added to the sm
# DONE make everything work again
# DONE create Archive widget with Object Property, add Archive to Home Screen
# DONE make Add Button bubbly
# TODO save archive locally
# TODO hook up archive to cloud

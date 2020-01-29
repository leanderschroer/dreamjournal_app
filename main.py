from math import ceil

import kivy
import datetime
from kivy.app import App
from kivy.properties import DictProperty, ObjectProperty, StringProperty
from kivy.uix import button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
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


class HomeButton(Button):
    sm = ObjectProperty()
    pass


class MainApp(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.archive = DictProperty()
        self.manager = ObjectProperty()
        # dummy archive
        self.archive = {'test key': 'test text'}
        abc = [i for i in 'abcdefghifjklmnop']
        for i, a in enumerate(abc):
            self.archive[str(i)] = str(a)
        self.date = StringProperty()
        self.date = str(datetime.date.today())

    def build(self):
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
        self.archive[date] = text
        self.manager.add_widget(
            EditScreen(name=str(date),
                       date=date,
                       body=text
                       )
        )


if __name__ == '__main__':
    App = MainApp()
    App.run()

# DONE reformat everything to be screens added to the sm
# DONE make everything work again
# DONE create Archive widget with Object Property, add Archive to Home Screen
# TODO make Add Button bubbly
# TODO hook up archive to cloud

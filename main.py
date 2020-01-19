import kivy
import datetime
from kivy.app import App
from kivy.uix import button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.screenmanager import ScreenManager, Screen

kivy.require('1.11.1')


class Manager(ScreenManager):
    pass


class HomeScreen(BoxLayout):
    pass


class LoginScreen(GridLayout):
    pass


class MainApp(App):
    def build(self):
        return Manager()


if __name__ == '__main__':
    MainApp().run()

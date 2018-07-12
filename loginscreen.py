__author__ = 'David'

import kivy
kivy.require('1.9.0')

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.graphics import Color, Rectangle

# With a box layout we arrange widgets in a horizontal
# or vertical box

class LoginScreenApp(App):

    def build(self):
        return GridLayout()

blApp = LoginScreenApp()

blApp.run()

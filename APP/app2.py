from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button


class SimpleKivy(App):
    def build(self):
        return Label()




if __name__ == '__main__':
    SimpleKivy().run()
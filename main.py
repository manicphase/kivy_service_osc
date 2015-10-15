__version__ = '0.1'

from kivy.app import App
from kivy.lang import Builder
from kivy.utils import platform
import urllib2
platform = platform()

kv = '''
BoxLayout:
    orientation: 'vertical'
    BoxLayout:
        size_hint_y: None
        height: '30sp'
        Button:
            text: 'start service'
            on_press: app.start_service()
        Button:
            text: 'stop service'
            on_press: app.stop_service()

    ScrollView:
        Label:
            id: label
            size_hint_y: None
            height: self.texture_size[1]
            text_size: self.size[0], None

    BoxLayout:
        size_hint_y: None
        height: '30sp'
        Button:
            text: 'get'
            on_press: app.get()
        Button:
            text: 'clear'
            on_press: label.text = ''

'''


class ClientServerApp(App):
    def build(self):
        self.service = None
        self.start_service()
        self.root = Builder.load_string(kv)
        return self.root

    def start_service(self):
        if platform == 'android':
            from android import AndroidService
            service = AndroidService('my pong service', 'running')
            service.start('service started')
            self.service = service

    def stop_service(self):
        if self.service:
            self.service.stop()
            self.service = None

    def get(self):
        message = urllib2.urlopen('http://127.0.0.1:5000/random').read()
        self.display_message(message)

    def display_message(self, message):
        if self.root:
            self.root.ids.label.text += '%s\n' % message


if __name__ == '__main__':
    ClientServerApp().run()

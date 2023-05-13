from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label


class DynamicLabelsApp(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.names = ['Alice', 'Bob', 'Charlie']

    def build(self):
        layout = BoxLayout(orientation='vertical')
        for name in self.names:
            label = Label(text=name)
            layout.add_widget(label)
        return layout


if __name__ == '__main__':
    DynamicLabelsApp().run()

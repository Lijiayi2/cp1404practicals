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

    def create_labels(self):
        """Create labels from data and add them to the GUI."""
        for name in self.name_list:
            label = Label(text=name)
            self.root.ids.main_layout.add_widget(label)

    def clear_all_labels(self):
        """Clear all labels"""
        self.root.ids.main_layout.clear_widgets()


if __name__ == '__main__':
    DynamicLabelsApp().run()

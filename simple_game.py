from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.clock import Clock

class SimpleGameApp(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical')
        self.label = Label(text="Touch the button to score points!", font_size='20sp')
        self.score_label = Label(text="Score: 0", font_size='20sp')
        self.button = Button(text="Click me!", font_size='30sp', on_press=self.increase_score)

        self.layout.add_widget(self.label)
        self.layout.add_widget(self.button)
        self.layout.add_widget(self.score_label)

        self.score = 0
        return self.layout

    def increase_score(self, instance):
        self.score += 1
        self.score_label.text = f"Score: {self.score}"
        if self.score >= 10:
            self.label.text = "You win!"

if __name__ == "__main__":
    SimpleGameApp().run()

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

class MyApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')

        btn1 = Button(text="Submit 1")
        btn2 = Button(text="Submit 1")
        btn3 = Button(text="Submit 1")
                
        layout.add_widget(btn1)
        layout.add_widget(btn2)
        layout.add_widget(btn3)
  
        return layout

if __name__ == '__main__':
    MyApp().run()

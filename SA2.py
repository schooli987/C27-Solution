from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout

class MyApp(App):
    def build(self):
        layout = GridLayout(cols=2)  # 1 column, rows adjust automatically

        btn1 = Button(text="Submit 1")
        btn2 = Button(text="Submit 2")
        btn3 = Button(text="Submit 3")
        btn4 = Button(text="Submit 4")  

        layout.add_widget(btn1)
        layout.add_widget(btn2)
        layout.add_widget(btn3)
        layout.add_widget(btn4)

        return layout

if __name__ == '__main__':
    MyApp().run()

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label

class BMICalculatorApp(App):

    def build(self):
        # Layout for BMI calculator
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        # TextInput for weight (kg)
        self.weight_input = TextInput(hint_text="Enter weight in kg", font_size=30)
        layout.add_widget(self.weight_input)

        # TextInput for height (cm)
        self.height_input = TextInput(hint_text="Enter height in cm", font_size=30)
        layout.add_widget(self.height_input)

        # Button to calculate BMI
        self.calculate_btn = Button(text="Calculate BsMI")
        layout.add_widget(self.calculate_btn)

        # Label to show BMI result
        self.result_label = Label(text="BMI: ", font_size=30, size_hint=(1, 0.2))
        layout.add_widget(self.result_label)

        return layout
    
if __name__ == "__main__":
    BMICalculatorApp().run()
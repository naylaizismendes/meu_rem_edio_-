from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivymd.app import MDApp
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.textfield import MDTextField
from kivy.clock import Clock
#pip install kivy kivymd

Builder.load_string("""
<MyLayout>:
    orientation: "vertical"

    MDTextField:
        id: medicine_input
        hint_text: "Medicamento"
        size_hint_x: None
        width: 300

    MDTextField:
        id: time_input
        hint_text: "Horário (HH:MM)"
        size_hint_x: None
        width: 300

    MDRaisedButton:
        text: "Adicionar Medicamento"
        on_press: app.add_medication()

    MDRaisedButton:
        text: "Iniciar Alarme"
        on_press: app.start_alarm()
""")

class MyLayout(BoxLayout):
    pass

class MedicationApp(MDApp):
    def build(self):
        return MyLayout()

    def add_medication(self):
        medicine = self.root.ids.medicine_input.text
        time = self.root.ids.time_input.text
        # Aqui você pode adicionar a lógica para armazenar os medicamentos e horários

    def start_alarm(self):
        # Aqui você pode adicionar a lógica para iniciar o alarme com base nos medicamentos e horários definidos
        pass

if __name__ == "__main__":
    MedicationApp().run()

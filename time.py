from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivymd.app import MDApp
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.textfield import MDTextField
from kivy.clock import Clock
from plyer import notification

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
        self.medications = []  # Lista para armazenar medicamentos e horários
        return MyLayout()

    def add_medication(self):
        medicine = self.root.ids.medicine_input.text
        time = self.root.ids.time_input.text
        self.medications.append((medicine, time))
        self.root.ids.medicine_input.text = ""
        self.root.ids.time_input.text = ""

    def start_alarm(self):
        for medicine, time in self.medications:
            Clock.schedule_once(lambda dt, med=medicine: self.show_notification(med), self.calculate_time(time))

    def show_notification(self, medicine):
        notification.notify(
            title="Lembrete de Medicamento",
            message=f"Tome seu medicamento: {medicine}",
            app_icon=None,  # e.g. 'C:\\icon_32x32.ico'
            timeout=10,  # Tempo em segundos antes da notificação desaparecer
        )

    def calculate_time(self, input_time):
        # Adapte esta função conforme necessário para calcular o tempo até o próximo alarme
        # Aqui, ela simplesmente pega os minutos diretamente
        hours, minutes = map(int, input_time.split(":"))
        return hours * 60 + minutes

if __name__ == "__main__":
    MedicationApp().run()

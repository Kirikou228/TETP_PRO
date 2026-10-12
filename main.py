from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.core.window import Window

class TEPGPro(App):
    def build(self):
        self.title = "TEPG PRO"
        root = BoxLayout(orientation="vertical", padding=20, spacing=12)
        root.add_widget(Label(text="TEPG PRO\nÉlectricité et Plomberie",
                             font_size=24, halign="center"))
        self.client = TextInput(hint_text="Nom du client", multiline=False)
        self.materiel = TextInput(hint_text="Prix du matériel", input_filter="float", multiline=False)
        self.main_oeuvre = TextInput(hint_text="Main-d'œuvre", input_filter="float", multiline=False)
        self.resultat = Label(text="Total : 0 FCFA", font_size=20)
        bouton = Button(text="Calculer le devis", size_hint_y=None, height=55)
        bouton.bind(on_press=self.calculer)
        root.add_widget(self.client)
        root.add_widget(self.materiel)
        root.add_widget(self.main_oeuvre)
        root.add_widget(bouton)
        root.add_widget(self.resultat)
        return root

    def calculer(self, instance):
        try:
            total = float(self.materiel.text or 0) + float(self.main_oeuvre.text or 0)
            self.resultat.text = f"Total : {total:,.0f} FCFA"
        except ValueError:
            self.resultat.text = "Vérifie les montants saisis"

TEPGPro().run()

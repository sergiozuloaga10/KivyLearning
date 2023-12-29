from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button

class ContadorApp(App):
    def build(self):
        self.counter = 0

        # Layout principal
        layout = BoxLayout(orientation='vertical', spacing=10, padding=40)

        # Componentes de la interfaz de usuario
        self.label = Label(text='Contador: 0', font_size=20)
        increment_button = Button(text='+', on_press=self.incrementar)
        decrement_button = Button(text='-', on_press=self.decrementar) 

        # Agregar componentes al layout
        layout.add_widget(self.label)
        layout.add_widget(increment_button)
        layout.add_widget(decrement_button)

        return layout

    def incrementar(self, instance):
        self.counter += 1
        self.label.text = f'Contador: {self.counter}'
    
    def decrementar(self, instance):
        self.counter -= 1
        self.label.text = f'Contador: {self.counter}'

if __name__ == '__main__':
    ContadorApp().run()

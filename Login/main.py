from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class LoginApp(App):
    def build(self):
        # Layout principal
        layout = BoxLayout(orientation='vertical', spacing=10, padding=40)

        # Componentes de la interfaz de usuario
        username_label = Label(text='Usuario:')
        username_input = TextInput(hint_text='Ingresa tu usuario', multiline=False)
        password_label = Label(text='Contraseña:')
        password_input = TextInput(hint_text='Ingresa tu contraseña', multiline=False, password=True)
        login_button = Button(text='Iniciar Sesión', on_press=self.login)

        # Agregar componentes al layout
        layout.add_widget(username_label)
        layout.add_widget(username_input)
        layout.add_widget(password_label)
        layout.add_widget(password_input)
        layout.add_widget(login_button)

        return layout

    def login(self, instance):
        username = self.root.children[0].text
        password = self.root.children[1].text

        if username == 'usuario' and password == 'contraseña':
            print('Inicio de sesión exitoso')
        else:
            print('Inicio de sesión fallido')

if __name__ == '__main__':
    LoginApp().run()

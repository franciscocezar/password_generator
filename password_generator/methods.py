import string as s
from random import SystemRandom as sr
from tkinter import messagebox


class PasswordsGenerator:

    def create_password(self, spinbox_value, radiobutton_value):
        if radiobutton_value == 1:
            gen_password = ''.join(sr().choices(s.punctuation + s.ascii_letters + s.digits,  k=int(spinbox_value)))
            return gen_password

        elif radiobutton_value == 2:
            gen_password = ''.join(sr().choices(s.ascii_letters + s.digits, k=int(spinbox_value)))
            return gen_password

        elif radiobutton_value == 3:
            gen_password = sr().choices(s.ascii_letters, k=int(spinbox_value))
            return gen_password

    def generate_password(self):
        if self.radio_var.get() == 0:
            messagebox.showwarning(message="Escolha o formato da senha.")
        else:
            number_caractere = self.spin.get()
            radiobutton = self.radio_var.get()

            self.new_password = self.create_password(number_caractere, radiobutton)
            self.label_password.configure(text="*" * len(self.new_password))
            self.button_show_password.configure(text="Mostrar Senha")
            self.button_show_password.configure(command=self.showing_password)
            self.button_show_password.configure(state="enable")
            self.button_gen_password.configure(text="Copiar Senha")
            self.button_gen_password.configure(command=self.coping_password)
            self.button_gen_password.configure(fg_color='green')

    def showing_password(self):
        if self.button_show_password:
            self.label_password.configure(text=self.new_password)
            self.button_show_password.configure(text="Ocultar Senha")
            self.button_show_password.configure(command=self.hiding_password)

    def hiding_password(self):
        if self.button_show_password:
            self.label_password.configure(text="*" * len(self.new_password))
            self.button_show_password.configure(text="Mostrar Senha")
            self.button_show_password.configure(command=self.showing_password)

    def coping_password(self):
        password_copied = self.new_password
        self.frame_2.clipboard_append(password_copied)
        self.button_gen_password.configure(text="Gerar Senha")
        self.button_gen_password.configure(command=self.generate_password)
        self.button_gen_password.configure(fg_color=None)
        messagebox.showinfo(message="Senha copiada com sucesso!",)

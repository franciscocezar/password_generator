import customtkinter
import tkinter
from methods import PasswordsGenerator


class App(customtkinter.CTk, PasswordsGenerator):

    def __init__(self):
        super().__init__()

        self.title("Gerador de Senhas")
        self.resizable(False, False)
        self.center_window()
        self.frames()
        self.widgets()

    def center_window(self):
        APP_WIDTH = 300
        APP_HEIGHT = 150

        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        app_center_coordinate_x = (screen_width / 2) - (APP_WIDTH / 2)
        app_center_coordinate_y = (screen_height / 2) - (APP_HEIGHT / 2)

        # Position App to the Centre of the Screen
        self.geometry(f"{APP_WIDTH}x{APP_HEIGHT}+{int(app_center_coordinate_x)}+{int(app_center_coordinate_y)}")

    def frames(self):
        self.frame_1 = customtkinter.CTkFrame(master=self, width=180, corner_radius=15)
        self.frame_1.place(relx=0.03, rely=0.02, relwidth=0.94, relheight=0.6)

        self.frame_2 = customtkinter.CTkFrame(master=self, width=180, corner_radius=10)
        self.frame_2.place(relx=0, rely=0.7, relwidth=1, relheight=1)

    def widgets(self):
        # #------------ WIDGETS FRAME 1 --------------------------------------------------------#
        # ------------ GENERATE PASSWORD BUTTON -------------------------------------------------
        self.button_gen_password = customtkinter.CTkButton(master=self.frame_1, text="Gerar Senha",
                                                           border_width=1, fg_color=None,
                                                           command=self.generate_password)
        self.button_gen_password.place(relx=0.5, rely=0.61, relwidth=0.4)

        # ------------ SPINBOX ----------------------------------------------------------------
        spin_var = tkinter.IntVar()
        self.spin = tkinter.Spinbox(master=self.frame_1, from_=15, to=80, width=5, textvariable=spin_var, wrap=False)
        self.spin.place(relx=0.6, rely=0.12, relwidth=0.2)

        # ------------ RADIO BUTTON ------------------------------------------------------------
        self.radio_var = tkinter.IntVar(value=0)

        self.strong_password = customtkinter.CTkRadioButton(master=self.frame_1, text="alfanum + símbolos",
                                                            variable=self.radio_var, value=1,
                                                            width=15, height=15)

        self.strong_password.place(relx=0.02, rely=0.12)

        self.medium_password = customtkinter.CTkRadioButton(master=self.frame_1, text="alfanúmerico",
                                                            variable=self.radio_var, value=2,
                                                            width=15, height=15)
        self.medium_password.place(relx=0.02, rely=0.388)

        self.low_password = customtkinter.CTkRadioButton(master=self.frame_1, text="letras (Aa)",
                                                         variable=self.radio_var, value=3,
                                                         width=15, height=15)
        self.low_password.place(relx=0.02, rely=0.67)

        # #------------ WIDGETS FRAME 2 --------------------------------------------------------#
        # ------------ PASSWORD LABEL -----------------------------------------------------------

        self.label_password = customtkinter.CTkLabel(master=self.frame_2, text="",
                                                     fg_color="white", text_color='black',
                                                     corner_radius=8)
        self.label_password.place(relx=0, rely=0, relwidth=1, relheight=0.15)

        # ------------ SHOW PASSWORD BUTTON -----------------------------------------------------
        self.button_show_password = customtkinter.CTkButton(master=self.frame_2, text="Mostrar Senha",
                                                            fg_color=None, hover_color=None,
                                                            state="disabled", text_color='white',
                                                            text_font=('helvetica', 11),
                                                            command=self.showing_password)
        self.button_show_password.place(relx=0.276, rely=0.148)

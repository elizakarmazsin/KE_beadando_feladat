import tkinter as tk
from tkinter import ttk, messagebox
import ke_utils
import demo_module


class App:
    def __init__(self, master):
        self.master = master
        master.title("KE Jelszó Ellenőrző és Generátor")
        master.geometry("600x400")
        master.resizable(False, False)

        self.ke_helper = ke_utils.KE_DataHelper(prefix="[ERŐSSÉG]")

        style = ttk.Style()
        style.configure('TFrame', background='#f0f0f0')
        style.configure('TLabel', background='#f0f0f0', font=('Arial', 10))
        style.configure('TButton', font=('Arial', 10, 'bold'), padding=10)
        style.configure('Success.TLabel', foreground='green', font=('Arial', 12, 'bold'))
        style.configure('Warning.TLabel', foreground='orange', font=('Arial', 12, 'bold'))
        style.configure('Danger.TLabel', foreground='red', font=('Arial', 12, 'bold'))

        main_frame = ttk.Frame(master, padding="25")
        main_frame.pack(fill='both', expand=True)

        ttk.Label(main_frame, text="Jelszó Erősség Ellenőrző és Generátor", font=('Arial', 16, 'bold'),
                  anchor='center').pack(pady=(0, 20), fill='x')

        ttk.Label(main_frame, text="Írja be a jelszót:").pack(anchor='w')
        self.password_var = tk.StringVar(value="")
        self.text_input = ttk.Entry(main_frame, textvariable=self.password_var, width=60, show='*')
        self.text_input.pack(pady=5, fill='x')

        ttk.Label(main_frame, text="Jelszó Erőssége:").pack(pady=(15, 0), anchor='w')
        self.strength_label = ttk.Label(main_frame, text="Nincs ellenőrizve", style='TLabel', anchor='center')
        self.strength_label.pack(pady=5, fill='x')

        button_frame = ttk.Frame(main_frame)
        button_frame.pack(pady=20, fill='x')

        ttk.Button(button_frame, text="Erősség Ellenőrzése", command=self.handle_check_password).pack(side='left',
                                                                                                      expand=True,                                                                                                padx=10)
        ttk.Button(button_frame, text="Jelszó Generálása", command=self.handle_generate_password).pack(side='left',
                                                                                                       expand=True,
                                                                                                       padx=10)
        ttk.Separator(main_frame, orient='horizontal').pack(fill='x', pady=10)
        ttk.Label(main_frame, text="Generált Jelszó:").pack(anchor='w')
        self.generated_var = tk.StringVar(value="")
        self.generated_display = ttk.Entry(main_frame, textvariable=self.generated_var, width=60, state='readonly')
        self.generated_display.pack(pady=5, fill='x')

        ttk.Button(main_frame, text="Formázás Saját Fv-nyel (KE_format_text)", command=self.handle_format_text).pack(
            pady=5)

    def check_password_strength(self, password):

        score = 0
        if len(password) >= 8:
            score += 1
        if any(c.islower() for c in password):
            score += 1
        if any(c.isupper() for c in password):
            score += 1
        if any(c.isdigit() for c in password):
            score += 1
        if any(c in "!@#$%^&*()-_+=<>?/[]{}|~" for c in password):
            score += 1

        if len(password) == 0:
            message = "Üres jelszó. Kérem, írja be a jelszót."
            style = 'TLabel'
        elif score >= 4:
            message = self.ke_helper.format_for_display("Erős jelszó! (Pontszám: " + str(score) + "/5)")
            style = 'Success.TLabel'
        elif score >= 2:
            message = self.ke_helper.format_for_display("Közepes jelszó. Adj hozzá speciális karaktereket.")
            style = 'Warning.TLabel'
        else:
            message = self.ke_helper.format_for_display("Gyenge jelszó. Túl rövid vagy túl egyszerű.")
            style = 'Danger.TLabel'

        self.strength_label.config(text=message, style=style)

    def handle_check_password(self):

        password = self.password_var.get()
        self.check_password_strength(password)

    def handle_generate_password(self):

        try:
            new_password = demo_module.generate_secure_password(length=16)
            self.generated_var.set(new_password)

            self.check_password_strength(new_password)

        except Exception as e:
            messagebox.showerror("Hiba", f"Hiba a jelszógenerálás közben: {e}")

    def handle_format_text(self):

        text_to_format = self.generated_var.get()
        if not text_to_format:
            messagebox.showwarning("Figyelem", "Először generáljon egy jelszót!")
            return

        formatted_text = ke_utils.ke_format_text(text_to_format)

        messagebox.showinfo("KE Függvény Eredmény",
                            f"Eredeti jelszó: {text_to_format}\n\n"
                            f"Formázott (KE_format_text) eredmény: \n{formatted_text}")

if __name__ == "__main__":
    root = tk.Tk()

    app = App(root)

    root.mainloop()
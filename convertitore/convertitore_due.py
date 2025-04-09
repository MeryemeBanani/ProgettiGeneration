import tkinter as tk
from calendar import month_name
from tkinter import ttk


class FinestraDue(tk.Toplevel):

    def __init__(self, principale):
        super().__init__(master=principale)
        self.title("Finestra Secondaria")
        self.geometry(f"400x400+{(principale.winfo_width() - 400) // 2}+{(principale.winfo_height() - 400) // 2}")

        self.contenitore = self.generazione_contenitore()

        # Check singolo
        self.controllo_check_singolo = tk.BooleanVar()
        self.check_singolo = self.generazione_check_singolo()

        # Check multipli
        self.schema_check_multipli = {
            "Cinema": tk.BooleanVar(),
            "Musica": tk.BooleanVar(),
            "Teatro": tk.BooleanVar()
        }
        self.generazione_check_multipli(60)

        # Radiobutton
        self.controllo_genere = tk.StringVar(value="Nessuno")
        self.generazione_radiobutton()

        # Combobox
        self.combobox = self.generazione_combobox()

    def generazione_contenitore(self):
        frame = tk.Frame(self, width=400, height=400, bg="lightblue", borderwidth=2)
        frame.pack(padx=20, pady=20)
        return frame

    def generazione_check_singolo(self):
        check = tk.Checkbutton(master=self.contenitore, text="Accetta La Privacy",
                               command=self.selezione_check_singolo, variable=self.controllo_check_singolo)
        check.place(x=20, y=20, width=200, height=25)
        return check

    def selezione_check_singolo(self):
        if self.controllo_check_singolo.get():
            print("Il check è selezionato")
        else:
            print("Il check non è selezionato")

    def generazione_check_multipli(self, posizione_y):
        for testo, variabile in self.schema_check_multipli.items():
            check = tk.Checkbutton(master=self.contenitore, text=testo, variable=variabile)
            check.place(x=20, y=posizione_y, width=200, height=25)
            posizione_y += 25

        button = tk.Button(master=self.contenitore, text="Invia", command=self.recupero_stati_check_multipli)
        button.place(x=20, y=140, width=100, height=25)

    def recupero_stati_check_multipli(self):
        preferenze_utente = [testo for testo, var in self.schema_check_multipli.items() if var.get()]
        print(f"Preferenze selezionate: {preferenze_utente}")

    def generazione_radiobutton(self):
        radio_uomo = tk.Radiobutton(master=self.contenitore, text="Uomo", value="Uomo", variable=self.controllo_genere)
        radio_uomo.place(x=20, y=180, width=200, height=25)

        radio_donna = tk.Radiobutton(master=self.contenitore, text="Donna", value="Donna",
                                     variable=self.controllo_genere)
        radio_donna.place(x=20, y=205, width=200, height=25)

        button = tk.Button(master=self.contenitore, text="Invia", command=self.recupero_selezione_radio)
        button.place(x=20, y=240, width=100, height=25)

    def recupero_selezione_radio(self):
        print(f"L'Utente è {self.controllo_genere.get()}")

    def generazione_combobox(self):
        lista_mesi = [month_name[mese] for mese in range(1, 13)]
        combo = ttk.Combobox(self.contenitore, state="readonly", values=lista_mesi)
        combo.set("Scegli il mese")
        combo.place(x=20, y=290, width=200, height=25)

        button = tk.Button(self.contenitore, text="Invia", command=self.controllo_item_combo)
        button.place(x=20, y=320, width=100, height=25)

        combo.bind("<<ComboboxSelected>>", self.selezione_item_combo)
        return combo

    def selezione_item_combo(self, event):
        print(f"Selezionato il mese {self.combobox.get()}")

    def controllo_item_combo(self):
        print(f"L'utente è nato nel mese di {self.combobox.get()}")


from kivy.app import App
from kivy.uix.button import Button
import tkinter as tk
from tkinter import messagebox

from pandas.core.window import Expanding


class Finestra(tk.Tk):
        # metodo di inizializzazione
    def __init__(self):
            super().__init__()
            self.title("Convertitore di metri")
            # dimensionamento e posizionamento fisso (largh x alt + coordX + coordY)
            self.geometry("600x600+300+50")
            # dimensionamento fisso e posizionamento dinamico al centro dello schermo
            self.geometry(f"600x600+{(self.winfo_screenwidth()-600) // 2}+{(self.winfo_screenheight() - 600) // 2}")
            # estensione a tutto schermo al momento del run
            self.state("zoomed")
            #generazione contenitore
            #self.generazione_contenitore()
            self.laterale,self.superiore,self.inferiore,self.centrale = self.generazione_sezioni()

    def generazione_contenitore(self):
            frame = tk.Frame(master=self, background="lightblue")
            frame.pack(fill=tk.BOTH, expand=True)

    #method per generazione di 4 frame contenitori sezioni di interfaccia
    def generazione_sezioni(self):
            laterale = tk.Frame(master=self, background="lightblue", width=300)  # width: larghezza
            superiore = tk.Frame(master=self, background="lightyellow", height=150)
            inferiore = tk.Frame(master=self, background="lightgreen", height=150)
            centrale = tk.Frame(master=self, background="lightgray")
            laterale.pack(side=tk.LEFT, fill=tk.BOTH, expand=False)
            superiore.pack(side=tk.TOP, fill=tk.BOTH, expand=False)
            inferiore.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=False)
            centrale.pack( fill=tk.BOTH, expand=False)
            return laterale,superiore,inferiore,centrale


# istruzione di avvio
Finestra().mainloop()
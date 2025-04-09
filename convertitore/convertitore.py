import tkinter as tk
from convertitore_due import FinestraDue
from tkinter import messagebox, colorchooser

from PIL import Image, ImageTk
from PIL.ImageTk import PhotoImage
from pandas.core.window import Expanding
from skimage.color.rgb_colors import lightyellow


class Convertitore(tk.Tk):

    def __init__(self):
        super().__init__()
        self.icon = PhotoImage(file="icona_app(3).jpg")
        self.iconphoto(True, self.icon)
        self.title("Convertitore")

        # dimensionamento e posizionamento fisso (largh x alt + coordX + coordY)
        #self.geometry("600x600+300+50")

        # dimensionamento fisso e posizionamento dinamico al centro dello schermo
        self.geometry(f"800x600+{(self.winfo_screenwidth() - 600) // 2}+{(self.winfo_screenheight() - 600) // 2}")

        #PER NON DEFORMARE TROPPO LA PAGINA:
        self.minsize(800, 600)

        # estensione a tutto schermo al momento del run, PER ORA NON MI SERVE
        #self.state("zoomed")
        # generazione contenitore, NON MI SERVE
        # self.generazione_contenitore()

        #IMMAGINI PER LE SEZIONI AI BORDI
        self.img_sx = Image.open("sfondo1.jpg").resize((200, 600))
        self.img_dx = Image.open("sfondo2.jpg").resize((200, 600))

        #CONVERTO L'IMMAGINE PERCHE' PRIMA C'ERA UN ERRORE
        self.img_sx = ImageTk.PhotoImage(self.img_sx)
        self.img_dx = ImageTk.PhotoImage(self.img_dx)

        #SEZIONI:
        self.laterale_sx, self.laterale_dx, self.centrale = self.generazione_sezioni()

        #INSERISCO UN TITOLO PIù BELLO
        self.titolo = tk.Label(self.centrale,text="Convertitore ", font=("Ubuntu", 30, "bold"),fg="#7c9494",pady=20,bg="#ffffff")
        self.titolo.pack(side=tk.TOP, anchor="center")
        self.sotto_titolo = tk.Label(self.centrale, text="Metri ➡️ Miglia, Pollici", font=("Segoe UI Emoji", 18), fg="#7c9494", pady=5,bg="#ffffff")
        self.sotto_titolo.pack(side=tk.TOP, anchor="center")

        #TITOLO PER IL BOX
        self.metri = tk.Label(self.centrale, text="Inserisci i metri:", font=("Ubuntu", 14),pady=20,  bg="#ffffff")
        self.metri.pack(side=tk.TOP, anchor="center")

        #BOX
        self.entry_metri = tk.Entry(self.centrale,font=("Ubuntu", 14), bg="#ffffff")
        self.entry_metri.pack(side=tk.TOP, anchor="center")

        #BOTTONE PERSONALIZZATO:
        self.img_bottone = Image.open("bottone.jpg")
        self.img_bottone_tk = ImageTk.PhotoImage(self.img_bottone)#CONVERTO PER EVITARE ERRORI
        self.bottone = tk.Button(self.centrale, image=self.img_bottone_tk,command=self.converti_valore)
        self.bottone.pack(side=tk.TOP, anchor="center", pady=20)

        self.img_bottone_reset = Image.open("bottone_reset.jpg")
        self.img_bottone_reset_tk = ImageTk.PhotoImage(self.img_bottone_reset)  # CONVERTO PER EVITARE ERRORI
        self.bottone = tk.Button(self.centrale, image=self.img_bottone_reset_tk, command=self.reset)
        self.bottone.pack(side=tk.TOP, anchor="center", pady=20)



        #RIQUADRO DOVE VEDERE IL RISULTATO:
        self.ris = tk.Label(self.centrale, text="", font=("Ubuntu", 12), bg="white", padx=20, pady=20)
        self.ris.pack(side=tk.TOP, anchor="center", pady=20)

        self.bottone_apri_finestra_due = tk.Button(self.centrale, text="Apri Seconda Finestra", font=("Ubuntu", 14),
                                                   bg="#7c9494", fg="white", command=self.apri_seconda_finestra)
        self.bottone_apri_finestra_due.pack(side=tk.TOP, anchor="center", pady=20)

    def apri_seconda_finestra(self):
        FinestraDue(self)

    def converti_valore(self):

        try:

            valore_metri = float(self.entry_metri.get())


            valore_miglia = valore_metri * 1609.34
            valore_pollici = valore_metri/0.0254


            self.ris.config(text=f"{valore_metri} metri = {valore_miglia} miglia\n{valore_metri} metri = {valore_pollici} pollici")
            self.ris.config(bg="lightyellow")


        except ValueError:

            self.ris.config(text="Inserisci un numero valido!")
            self.ris.config(bg="lightcoral")



    def reset(self):

        # Resetta l'input dell'Entry
        self.entry_metri.delete(0,tk.END)

        # Resetta il testo del risultato
        self.ris.config(text="")
        self.ris.config(bg="white")




    def generazione_sezioni(self):
        laterale_sx = tk.Frame(master=self, width=200, height=600)
        laterale_dx = tk.Frame(master=self, width=200, height=600)
        centrale = tk.Frame(master=self, width=400, height=600, background="#ffffff")

        # Inserisci l'immagine di sfondo nel laterale sinistro
        label_sx = tk.Label(laterale_sx, image=self.img_sx, background="#e6f7ff")
        label_sx.place(relwidth=1, relheight=1)

        # Inserisci l'immagine di sfondo nel laterale destro
        label_dx = tk.Label(laterale_dx, image=self.img_dx,background="#e6f7ff" )
        label_dx.place(relwidth=1, relheight=1)

        # Posiziona i frame
        laterale_sx.pack(side=tk.LEFT, fill=tk.BOTH, expand=False)
        laterale_dx.pack(side=tk.RIGHT, fill=tk.BOTH, expand=False)
        centrale.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        return laterale_sx, laterale_dx, centrale




Convertitore().mainloop()
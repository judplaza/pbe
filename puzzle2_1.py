from Read import Leer #del fitxer Read.py importem la classe Leer
import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk


class MyWindow(Gtk.Window):
    def __init__(self):
        super().__init__(title="Puzzle_1")

        self.button = Gtk.Button(label="Click Here") #creo el botó
        self.button.connect("clicked", self.on_button_clicked) #li assigno una funció
        self.add(self.button)  #agrego el botó                      

    def on_button_clicked(self, widget):        
        uid = Leer.hacer_una_lectura(self) #accedeixo a la classe del puzzle 1
        print("UID hex8: " , uid) #mostro la uid a la Shell
        
win = MyWindow() #creo una finestra buida
win.connect("destroy", Gtk.main_quit) #connecto l’esborrador d’esdeveniments amb la x de 
tancar finestra
win.show_all() #mostro la finestra creada
Gtk.main() #inicio el bucle

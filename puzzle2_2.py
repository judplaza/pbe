from Read import Leer
import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

class MyWindow(Gtk.Window):
    def __init__(self):
        super().__init__(title="Label Example")
        
        self.box= Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
		#per tal de inserir un botó i un label a a finestra creo una “box”
        self.button = Gtk.Button(label="Connect")
        self.button.connect("clicked", self.on_button_clicked)        
        
        self.label = Gtk.Label(label= "benvingut al pas 1")

        self.box.pack_start(self.label, True, True, 0)  #afegeixo el label a la “box”                             
        self.box.pack_start(self.button, True, True, 0)  #afegeixo el botó a la “box”       
        self.add(self.box) #ageixo la “box” a la finestra

    def on_button_clicked(self, widget):
        
        uid = Leer.hacer_una_lectura(self)            
        self.label.set_text("uid: " + uid)        

window = MyWindow()
window.connect("destroy", Gtk.main_quit)
window.show_all()
Gtk.main()

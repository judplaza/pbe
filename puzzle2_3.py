from Read import Leer
import gi, threading, time, sys

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Gdk, GLib, GObject


class MyWindow(Gtk.Window):
    def __init__(self):
        super().__init__(title="Label Example")
        self.preparat_lectura = True #marquem que estem esperant per fer una lectura
        self.box= Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)

        self.button = Gtk.Button(label="Inicia")
        self.button.connect("clicked", self.Reset_button)        
        
        self.label = Gtk.Label(label= "benvingut al pas 1")
        self.box.pack_start(self.label, True, True, 0)              
                
        self.box.pack_start(self.button, True, True, 0)
        self.add(self.box)
        
        self.create_thread()
        
    def Read(self):        
        uid = Leer.hacer_una_lectura(self)            
        self.label.set_text("uid: " + uid)
        self.preparat_lectura = False #fins que no reiniciem el sistema, no podem fer cap 
lectura
        
    def Reset_button(self, widget):
        self.label.set_text("login_again") 
        if self.preparat_lectura is False: #en cas que ja estiguem preparats per lectura no 
caldria realitzar cap operació
            self.preparat_lectura = True
            self.create_thread()
            
    def create_thread(self):
        thread = threading.Thread(target=self.Read) #creo el thread
        thread.setDaemon(True) #volem que quan el fil principal mori, el thread també
        thread.start() #iniciem el thread

window = MyWindow()
window.connect("destroy", Gtk.main_quit)
window.show_all()
Gtk.main()


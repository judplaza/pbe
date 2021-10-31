from Read import Leer
import gi, threading, time, sys

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Gdk, GLib, GObject


class MyWindow(Gtk.Window):
    def __init__(self):
        super().__init__(title="UID indentification")

	 #connecto la classe amb le fitxer .css
        css_provider = Gtk.CssProvider()        
        css_provider.load_from_path("style/interface_style.css")
        context = Gtk.StyleContext()
        screen = Gdk.Screen.get_default()
        context.add_provider_for_screen(screen, css_provider, Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION)
        
        self.preparat_lectura = True #marquem que estem esperant per fer una lectura
        self.box= Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)

        self.button = Gtk.Button(label="clear")
        self.button.connect("clicked", self.Reset_button)        
        
        self.label = Gtk.Label(label= "Please, login with your university card")
        self.label.get_style_context().add_class("welcome") #indico quina classe definida al 
                                                                #.css tindrà el label
        self.label.set_size_request(350,70)
        self.box.pack_start(self.label, True, True, 0)              
                
        self.box.pack_start(self.button, True, True, 0)
        self.add(self.box)
        
        self.create_thread()
                            
    
    def Read(self):        
        self.uid = Leer.hacer_una_lectura(self)            
        GLib.idle_add(self.actualitzar) #els canvis d’estil s’han de realitzar fora del fil
        self.preparat_lectura = False #fins que no reiniciem el sistema, no podem fer cap 
                                        #lectura

        
    def actualitzar(self): #aquesta funció actualitza l’estil del label fora del fil
        self.label.get_style_context().remove_class("welcome")
        self.label.get_style_context().add_class("uid_text")
        self.label.set_text("uid: " + self.uid)        
        

    def Reset_button(self, widget): #no cal utilitzar cap funció “actualitzar” perquè la funció 
                                    #s’executa al fil prinicpal
        self.label.set_text("login_again")
        self.label.get_style_context().remove_class("uid_text")
        self.label.get_style_context().add_class("welcome")
        if self.preparat_lectura is False: #en cas que ja estiguem preparats per lectura no 
                                            #caldria realitzar cap operació
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

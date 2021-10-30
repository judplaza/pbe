
from Read import Leer
import gi, threading, time, sys

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Gdk, GLib, GObject


import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk


class MyWindow(Gtk.Window):
    def __init__(self):
        super().__init__(title="UID indentification")
        css_provider = Gtk.CssProvider()        
        css_provider.load_from_path("style/interface_style.css")
        context = Gtk.StyleContext()
        screen = Gdk.Screen.get_default()
        context.add_provider_for_screen(screen, css_provider, Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION)
        
        self.preparat_lectura = True
        self.box= Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)

        self.button = Gtk.Button(label="clear")
        self.button.connect("clicked", self.Reset_button)        
        
        self.label = Gtk.Label(label= "Please, login with yout university card")
        self.label.get_style_context().add_class("welcome")
        self.label.set_size_request(350,70)
        self.box.pack_start(self.label, True, True, 0)              
                
        self.box.pack_start(self.button, True, True, 0)
        self.add(self.box)
        
        thread = threading.Thread(target=self.Read)
        thread.setDaemon(True)
        thread.start()                
        
        
        
    
    
    def Read(self):        
        self.uid = Leer.hacer_una_lectura(self)            
        #self.label.get_style_context().remove_class("welcome")
        #self.label.get_style_context().add_class("uid_text")
        #self.label.set_text("uid: " + uid)
        GLib.idle_add(self.actualitzar)
        self.preparat_lectura = False
        #return self.prpreparat_lectura
        
    def actualitzar(self):
        self.label.get_style_context().remove_class("welcome")
        self.label.get_style_context().add_class("uid_text")
        self.label.set_text("uid: " + self.uid)        
    
    

    def Reset_button(self, widget):
        self.label.set_text("login_again")
        self.label.get_style_context().remove_class("uid_text")
        self.label.get_style_context().add_class("welcome")
        if self.preparat_lectura is False: #ahorra pasos
            self.preparat_lectura = True
            self.create_thread()            
            
    def create_thread(self):
        thread = threading.Thread(target=self.Read)
        thread.start()
        
window = MyWindow()
window.connect("destroy", Gtk.main_quit)
window.show_all()
Gtk.main()
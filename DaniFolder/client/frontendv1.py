import gi
gi.require_version("Gtk","3.0")
from Rfid import Rfid
import threading
from gi.repository import Gdk
from gi.repository import Gtk
from gi.repository import GLib


class Finestra(Gtk.Window):
    def _init_(self):
        #creem finestra
        Gtk.Window._init_(self, title="P2")
        css= Gtk.CssProvider()        
        css.load_from_path("interface.css")
        context = Gtk.StyleContext()
        screen = Gdk.Screen.get_default()
        context.add_provider_for_screen(screen, css, Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION)
        self.primera_pantalla()
        
    
    def primera_pantalla(self):
        self.grid = Gtk.Grid()
        self.label= Gtk.Label()
        self.label.get_style_context().add_class("primera_pantalla")
        self.label.set_text("Please, login with your university card")
        self.grid.attach(self.label,0,1,1,1)
        self.add(self.grid)
        self.thread = threading.Thread(target = self.read_uid)        
        self.thread.start()

    def segona_pantalla(self):
        self.grid1 = Gtk.Grid()
        self.add(self.grid1)
        self.grid2 = Gtk.Grid()
        self.label= Gtk.Label()
        self.label.set_text("Welcome")
        self.grid2.add(self.label)
        self.grid2.set_column_spacing(300)
        self.grid2.set_row_spacing(1)
        self.button = Gtk.Button(label="Logout")
        self.grid2.attach_next_to(self.button, self.label, Gtk.PositionType.RIGHT, 1, 1)
        self.grid2.set_size_request(250,100)
        self.button.connect('pressed',self.pressed)
        self.grid1.add(self.grid2)
        self.entry = Gtk.Entry()
        self.entry.set_text("")
        self.entry.set_editable(True)
        self.entry.set_visibility(True)
        self.grid1.attach_next_to(self.entry, self.grid2, Gtk.PositionType.BOTTOM, 1, 1)


    def read_uid(self):
        rf = Rfid()
        self.uid = rf.read_uid()
        GLib.idle_add(self.update1to2)
        #self.label.set_text("UID: " + self.uid)
    def update1to2(self):  
        self.remove(self.grid)
        self.segona_pantalla()
        self.show_all()
        
        
    def pressed(self, widget):
        GLib.idle_add(self.update2to1)
        
    def update2to1(self):
        self.remove(self.grid1)
        self.primera_pantalla()
        self.show_all()
        
        #self.thread = threading.Thread(target = self.read_uid)
        #self.thread.start()
        
win = Finestra()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()




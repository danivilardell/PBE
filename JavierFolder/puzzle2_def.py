import gi
gi.require_version('Gtk','3.0')
import threading
from gi.repository import Gtk
from gi.repository import GLib
from Rfid import Rfid

class MainWindow(Gtk.Window):
    
    def __init__(self):
        Gtk.Window.__init__(self)
        #Creem label
        self.label= Gtk.Label()
        self.label.set_text("Please, login with your university card")
        self.label.set_justify(Gtk.Justification.CENTER)
        self.label.set_size_request(270,50)
        
        #Creem botó
        self.button = Gtk.Button(label='Clear')
        self.button.connect('pressed',self.pressed)
        self.button.set_border_width
        
        #Creem Grid
        self.grid = Gtk.Grid()
        self.grid.add(self.label)
        self.grid.attach_next_to(self.button, self.label, Gtk.PositionType.BOTTOM, 1, 1)
        self.add(self.grid)
        #Creem els threads
        self.thread = threading.Thread(target = self.read_uid)
        self.thread.start()
       
        #Configurem finestra
        self.connect('delete-event',Gtk.main_quit)
        self.show_all()
        Gtk.main()
        
    def pressed(self, widget):
        self.label.set_text("Please, login with your university card")
        self.thread = threading.Thread(target = self.read_uid)
        self.thread.start()
        
    def read_uid(self):
        rf = Rfid()
        self.uid = rf.read_uid()
        GLib.idle_add(self.update)
        
    def update(self):
        self.label.set_text("UID: " + self.uid)



win = MainWindow()


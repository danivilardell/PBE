import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

from Readuserid import Rfid

class MyWindow(Gtk.Window):
    def __init__(self):
        super().__init__(title="rfid_gtk.py")
        
        self.read=Rfid()

        #Definim els botons
        label = Gtk.Label()
        label.set_markup("<span color='blue'>Please, login with your university card </span>")
        button1 = Gtk.Button(label="Clear")
        button1.connect("clicked", self.on_button1_clicked)
        button2 = Gtk.Button(label="Enter card")
        button2.connect("clicked", self.on_button2_clicked(label))
        
        
        #textview = Gtk.TextView()
        #escriure dins del textview
        
        #Definim el grid principal
        grid = Gtk.Grid()
        grid.set_border_width(5)
        grid.set_row_spacing(10)
        grid.set_column_spacing(5)
        
        grid.add(label)
        #grid.add(button1)
        grid.attach_next_to(button1, label, Gtk.PositionType.BOTTOM, 1, 2)
        grid.attach_next_to(button2, button1, Gtk.PositionType.RIGHT, 1, 2)
        
        self.add(grid)
                
    def on_button1_clicked(self, widget):
        print("Clear")
        
    def on_button2_clicked(self, widget):    
        self.read.readid()
        label.set_markup("etoo")




win = MyWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()

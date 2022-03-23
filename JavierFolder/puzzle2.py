import gi
gi.require_version('Gtk','3.0')
from gi.repository import Gtk
from Rfid import Rfid

class MainWindow(Gtk.Window):
    
    def __init__(self):
        
        Gtk.Window.__init__(self)
        self.button = Gtk.Button(label='Clear')
        self.label= Gtk.Label()
        self.label.set_text("Please, login with your university card")
        self.button.connect('pressed',self.print_button_name)
        self.grid = Gtk.Grid()
        self.grid.add(self.label)
        self.grid.attach_next_to(self.button, self.label, Gtk.PositionType.BOTTOM, 1, 1)
        self.add(self.grid)
     #   rf=Rfid()
      #  uid=rf.read_uid()
       # self.label.set_text(uid)
    def print_button_name(self, widget):
        self.label.set_text("Please, login with your university card")
       

win = MainWindow()
win.show_all()
win.connect('delete-event',Gtk.main_quit)
Gtk.main()
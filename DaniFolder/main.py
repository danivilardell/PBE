import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

from lcd import Rfid

class MyWindow(Gtk.Window):
    def __init__(self):
        super().__init__(title="LSD puzzle 2")

        self.rfid = Rfid()
        
        self.textview = Gtk.TextView()
        self.textview.set_size_request(300,200)

        self.button1 = Gtk.Button(label="Write")
        self.button1.connect("clicked", self.on_button1_clicked)
        
        self.grid = Gtk.Grid()
        self.grid.add(self.textview)
        self.grid.attach_next_to(self.button1, self.textview, Gtk.PositionType.BOTTOM, 1, 1)
        
        self.add(self.grid)
        
    def getText(self, textview):
        buffer = textview.get_buffer()
        startIter, endIter = buffer.get_bounds()    
        text = buffer.get_text(startIter, endIter, False) 
        return text

    def on_button1_clicked(self, widget):
        text = self.getText(self.textview)
        self.rfid.write(text)

win = MyWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()

import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

from lcd.LCD import Rfid

class MyWindow(Gtk.Window):
    def __init__(self):
        super().__init__(title="LSD puzzle 2")

        self.rfid = Rfid()

        #self.box = Gtk.Box(spacing=6)
        #self.add(self.box)
        #self.set_default_size(500, 60)

        #self.entry = Gtk.Entry()
        #self.box.pack_start(self.entry, True, True, 0)
        
        self.textview = Gtk.TextView()
        self.textview.set_size_request(300,200)
        #self.box.pack_start(self.textview, True, True, 0)

        self.button1 = Gtk.Button(label="Write")
        self.button1.connect("clicked", self.on_button1_clicked)
        #self.box.pack_start(self.button1, True, True, 0)
        
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

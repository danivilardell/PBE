import gi
import requests
import json

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

from lcd import Rfid

class MyWindow(Gtk.Window):
    def __init__(self):
        super().__init__(title="LSD CDR")

        self.set_default_size(1000, 600);
        #self.textview = Gtk.TextView()
        #self.textview.set_size_request(300,200)

        self.entry = Gtk.Entry()
        self.entry.set_width_chars(100)

        self.button1 = Gtk.Button(label="Write")
        self.button1.connect("clicked", self.on_button1_clicked)

        self.grid = Gtk.Grid()
        #self.grid.add(self.textview)
        self.grid.add(self.entry)
        self.grid.attach_next_to(self.button1, self.entry, Gtk.PositionType.BOTTOM, 1, 1)

        self.add(self.grid)

    def getText(self, textview):
        buffer = textview.get_buffer()
        startIter, endIter = buffer.get_bounds()
        text = buffer.get_text(startIter, endIter, False)
        return text

    def on_button1_clicked(self, widget):
        #text = self.getText(self.textview)
        text = self.entry.get_text()
        url = 'http://192.168.3.2/?' + text
        response = makeRequest(url)

    def makeRequest(url):
        return json.loads(requests.post(url).text.encode('utf-8'))
        


win = MyWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()

import Rfid 
import threading
import gi
gi.require_version("Gtk","3.0")
from gi.repository import Gdk
from gi.repository import Gtk

class Window(Gtk.Window):

  def __init__(self):
      
    #finestra
    Gtk.Window.__init__(self, title="Puzzle 2")
    self.connect("destroy", Gtk.main_quit)
    self.set_default_size(400,70)
    self.set_border_width(4)

    #box
    self.box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=4)
    self.add(self.box)
    self.evbox = Gtk.EventBox() #caixa evbox per posar el color
    self.evbox.override_background_color(0, Gdk.RGBA(0,0,8,1))
    self.box.pack_start(self.evbox, True, True, 0)
    
    #boto
    self.button = Gtk.Button(label="Clear")
    self.button.connect("pressed", self.pressed)
    self.box.pack_start(self.button, True, True, 0)
    
   
    #label
    self.label = Gtk.Label()
    self.label.set_text('<span foreground="white">Please, login with your university card</span>')
    self.label.set_use_markup(True)
    self.label.set_size_request(400,70)
    self.evbox.add(self.label)
    
    #thread
    self.thread = threading.Thread(target=self.read_uid)
    self.thread.start()
    
  def pressed(self, widget):
      self.label.set_label('<span foreground="white">Please, login with your university card</span>')
      self.evbox.override_background_color(0, Gdk.RGBA(0,0,8,1))
      self.thread = threading.Thread(target=self.read_uid)
      self.thread.start()
      
  def read_uid(self):
      self.uid = Rfid.Rfid().read_uid()
      self.label.set_label('<span foreground="white">UID: '+self.uid+'</span>') 
      self.evbox.override_background_color(0, Gdk.RGBA(8,0,0,1))

win = Window()
win.connect("delete-event", Gtk.main_quit)
win.show_all()
Gtk.main()
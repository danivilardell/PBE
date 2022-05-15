import gi
import json
import requests

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
        self.entry.set_width_chars(120)

        self.button1 = Gtk.Button(label="Run Query")
        self.button1.connect("clicked", self.on_button1_clicked)

        self.grid = Gtk.Grid()
        #self.grid.add(self.textview)
        self.grid.add(self.entry)
        self.grid.attach_next_to(self.button1, self.entry, Gtk.PositionType.BOTTOM, 1, 1)

        self.add(self.grid)

    def on_button1_clicked(self, widget):
        #text = self.getText(self.textview)
        text = self.entry.get_text()
        print('http://192.168.3.2/' + text)
        url = 'http://192.168.3.2/' + text
        response = self.makeRequest(url)

        if(text.split(".")[0] == "timetable"):
            taula = {"timetable": response}
        elif(text.split(".")[0] == "tasks"):
            taula = {"tasks": response}
        elif(text.split(".")[0] == "marks"):
            taula = {"marks": response}
        self.mostrar_taula(taula)

    def mostrar_taula(self, taula):

        color1 ="#96d0ff" #blau fluix
        color2 ="#249dff" #blau fort
        tipustaula = list(taula.keys())[0]

        self.scrollable_treelist = Gtk.ScrolledWindow()
        self.scrollable_treelist.set_vexpand(True)

        try:

            # tasques i notes

            if tipustaula == 'tasks' or tipustaula == 'marks':

                self.tasks_marks = Gtk.ListStore(str, str, str, str)

                i=0

                columnes = list(taula[tipustaula][0].keys())

                for fila in taula[tipustaula]:
                    if i%2==0:
                        self.tasks_marks.append([fila[columnes[0]],fila[columnes[1]],fila[columnes[2]], color1])
                    else:
                        self.tasks_marks.append([fila[columnes[0]],fila[columnes[1]],fila[columnes[2]], color2])
                    i=i+1

                self.treeview = Gtk.TreeView.new_with_model(self.tasks_marks)

                for i, titols in enumerate([columnes[0],columnes[1],columnes[2]]):
                    renderer = Gtk.CellRendererText()
                    renderer.set_fixed_size(333,30)
                    renderer.set_property("xalign",0.5)

                    columna = Gtk.TreeViewColumn(titols,renderer,text=i)
                    columna.set_alignment(0.5)
                    columna.add_attribute(renderer, "background", 3)
                    self.treeview.append_column(columna)

                self.scrollable_treelist = Gtk.ScrolledWindow()
                self.scrollable_treelist.set_vexpand(True)
                self.grid.attach_next_to(self.scrollable_treelist, self.button1, Gtk.PositionType.BOTTOM, 1, 1)

                self.scrollable_treelist.add(self.treeview)

                self.show_all()

            #horari

            elif tipustaula == 'timetable':
                self.horari= Gtk.ListStore(str, str, str, str, str)
                columnes = list(taula[tipustaula][0].keys())
                i=0

                for fila in taula[tipustaula]:
                    # una fila 1 color, 1 l'altre
                    if i%2==0:
                        self.horari.append(list([fila[columnes[0]],fila[columnes[1]],fila[columnes[2]],fila[columnes[3]], color1]))
                    else:
                        self.horari.append(list([fila[columnes[0]],fila[columnes[1]],fila[columnes[2]],fila[columnes[3]], color2]))
                    i=i+1
                    print([fila[columnes[0]],fila[columnes[1]],fila[columnes[2]],fila[columnes[3]]])

                self.treeview = Gtk.TreeView.new_with_model(self.horari)

                for i, titols in enumerate([columnes[0],columnes[1],columnes[2],columnes[3]]):
                    renderer = Gtk.CellRendererText()
                    renderer.set_fixed_size(250,30)
                    renderer.set_property("xalign",0.5)

                    columna = Gtk.TreeViewColumn(titols,renderer,text=i)
                    columna.set_alignment(0.5)
                    columna.add_attribute(renderer, "background", 4)
                    self.treeview.append_column(columna)

                self.scrollable_treelist = Gtk.ScrolledWindow()
                self.scrollable_treelist.set_vexpand(True)
                self.grid.attach_next_to(self.scrollable_treelist, self.button1, Gtk.PositionType.BOTTOM, 1, 1)

                self.scrollable_treelist.add(self.treeview)

                self.show_all()


        except IndexError as err:
            self.label_error_menu.set_text("Error")

    def makeRequest(self, url):
        return json.loads(requests.post(url).text.encode('utf-8'))

win = MyWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()

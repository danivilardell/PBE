gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

def mostrar_taula(self, taula):

        color1 ="#96d0ff" #blau fluix
        color2 ="#249dff" #blau fort
        tipustaula = list(taula.keys())[0]
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

                self.treeview = Gtk.TreeView.new_with_model(self.task_marks_list)

                for i, titols in enumerate([columnes[0],columnes[1],columnes[2]]):
                    renderer = Gtk.CellRendererText()
                    renderer.set_fixed_size(120,50)
                    renderer.set_property("xalign",0.5)

                    columna = Gtk.TreeViewColumn(titols,renderer,text=i)
                    columna.set_alignment(0.7)
                    columna.add_attribute(renderer, "background", 3)
                    self.treeview.append_column(columna)

            #horari

            elif tipustaula == 'timetables':

                self.horari= Gtk.ListStore(str, str, str, str, str)
                columnes = list(taula[tipustaula][0].keys())
                i=0

                for fila in taula[tipustaula]:
                    # una fila 1 color, 1 l'altre
                    if i%2==0:
                        self.horari.append([fila[columnes[0]],fila[columnes[1]],fila[columnes[2]],fila[columnes[3]], color1])
                    else:
                        self.horari.append([fila[columnes[0]],fila[columnes[1]],fila[columnes[2]],fila[columnes[3]], color2])
                    i=i+1

                self.treeview = Gtk.TreeView.new_with_model(self.horari)

                for i, titols in enumerate([columnes[0],columnes[1],columnes[2],columnes[3]]):
                    renderer = Gtk.CellRendererText()
                    renderer.set_fixed_size(120,50)
                    renderer.set_property("xalign",0.5)

                    columna = Gtk.TreeViewColumn(titols,renderer,text=i)
                    columna.set_alignment(0.7)
                    columna.add_attribute(renderer, "background", 4)
                    self.treeview.append_column(columna)


        except IndexError as err:
            self.label_error_menu.set_text("Error")


taula = {"timetable": [{"Day":"Mon","Hour":"08:00:00","Subject":"AST","Room":"A2-102"},{"Day":"Mon","Hour":"10:00:00","Subject":"AST","Room":"A2-102"},{"Day":"Tue","Hour":"08:00:00","Subject":"TD","Room":"A4-105"},{"Day":"Wed","Hour":"11:00:00","Subject":"ICOM","Room":"A1-102"}]}
mostrar_taula(taula)

            if tipustaula == 'tasks' or tipustaula == 'marks':

                self.tasks_marks = Gtk.ListStore(str, str, str)
                columnes = list(taula[tipustaula][0].keys())
                i=0

                for fila in taula[tipustaula]:
                    if i%2==0:
                        self.tasks_marks.append(list([fila[columnes[0]],fila[columnes[1]],fila[columnes[2]]]))
                    else:
                        self.tasks_marks.append(list([fila[columnes[0]],fila[columnes[1]],fila[columnes[2]], color2]))
                    i=i+1

                self.treeview = Gtk.TreeView.new_with_model(self.task_marks_list)

                for i, titols in enumerate([columnes[0],columnes[1],columnes[2]]):
                    renderer = Gtk.CellRendererText()
                    renderer.set_fixed_size(120,50)
                    renderer.set_property("xalign",0.5)

                    columna = Gtk.TreeViewColumn(titols,renderer,text=i)
                    columna.set_alignment(0.7)
                    columna.add_attribute(renderer, "background", 3)
                    self.treeview.append_column(columna)

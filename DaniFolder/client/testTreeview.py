import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

# list of tuples for each software, containing the software name, initial release, and main programming languages used
software_list = [
    ("Firefox", 2002, "C++"),
    ("Eclipse", 2004, "Java"),
    ("Pitivi", 2004, "Python"),
    ("Netbeans", 1996, "Java"),
    ("Chrome", 2008, "C++"),
    ("Filezilla", 2001, "C++"),
    ("Bazaar", 2005, "Python"),
    ("Git", 2005, "C"),
    ("Linux Kernel", 1991, "C"),
    ("GCC", 1987, "C"),
    ("Frostwire", 2004, "Java"),
]


class TreeViewFilterWindow(Gtk.Window):
    def __init__(self):
        super().__init__(title="Treeview Filter Demo")
        self.set_border_width(100)

        # Setting up the self.grid in which the elements are to be positioned
        self.grid = Gtk.Grid()
        self.grid.set_column_homogeneous(True)
        self.grid.set_row_homogeneous(True)
        self.add(self.grid)

        # Creating the ListStore model
        self.software_liststore = Gtk.ListStore(str, int, str)
        for software_ref in software_list:
            self.software_liststore.append(list(software_ref))
        self.current_filter_language = None

        # Creating the filter, feeding it with the liststore model
        self.language_filter = self.software_liststore.filter_new()
        # setting the filter function, note that we're not using the

        # creating the treeview, making it use the filter as a model, and adding the columns
        self.treeview = Gtk.TreeView(model=self.language_filter)
        for i, column_title in enumerate(
            ["Software", "Release Year", "Programming Language"]
        ):
            renderer = Gtk.CellRendererText()
            column = Gtk.TreeViewColumn(column_title, renderer, text=i)
            self.treeview.append_column(column)

        # setting up the layout, putting the treeview in a scrollwindow, and the buttons in a row
        self.scrollable_treelist = Gtk.ScrolledWindow()
        self.scrollable_treelist.set_vexpand(True)
        self.grid.attach(self.scrollable_treelist, 0, 0, 8, 10)

        self.scrollable_treelist.add(self.treeview)

        self.show_all()



win = TreeViewFilterWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()

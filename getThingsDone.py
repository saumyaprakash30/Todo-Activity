import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk,GLib
from gi.repository import Gdk
from sugar3.activity import activity
from sugar3.graphics.toolbarbox import ToolbarBox
from sugar3.activity.widgets import ActivityButton
from sugar3.activity.widgets import TitleEntry
from sugar3.activity.widgets import StopButton
from sugar3.activity.widgets import ShareButton
from sugar3.activity.widgets import DescriptionItem

class listForm(Gtk.Box):
    def __init__(self):
        Gtk.Box.__init__(self,orientation = Gtk.Orientation.HORIZONTAL)
        self.set_margin_left(5)
        self.set_margin_top(5)
        self.b1 = Gtk.CheckButton()
        self.add(self.b1)
        self.label = Gtk.Entry()
        self.add(self.label)     
        self.btn_del = Gtk.Button(label="-")
        self.b1.connect("toggled",self.modifyEntry)
        self.add(self.btn_del)
        self.text=''
    
    def modifyEntry(self,entry):
        if (self.b1.get_active()):
            a = self.label.get_text()
            if (len(a)) !=0:
                self.text=a
            if len(a)==0:
                self.b1.set_active(False)
            else:
                res=''
                for c in a:
                    res = res+c+'\u0336'
                self.label.set_text(res)
                self.label.props.editable = False
        else:
            self.label.set_text(self.text)
            


    
class getThingDone(activity.Activity):
    def __init__(self,handle):
        """Set up the ToDo activity."""
        activity.Activity.__init__(self, handle)

        # we do not have collaboration features
        # make the share option insensitive
        self.max_participants = 1

        # toolbar with the new toolbar redesign
        toolbar_box = ToolbarBox()

        activity_button = ActivityButton(self)
        toolbar_box.toolbar.insert(activity_button, 0)
        activity_button.show()

        title_entry = TitleEntry(self)
        toolbar_box.toolbar.insert(title_entry, -1)
        title_entry.show()

        description_item = DescriptionItem(self)
        toolbar_box.toolbar.insert(description_item, -1)
        description_item.show()

        share_button = ShareButton(self)
        toolbar_box.toolbar.insert(share_button, -1)
        share_button.show()

        separator = Gtk.SeparatorToolItem()
        separator.props.draw = False
        separator.set_expand(True)
        toolbar_box.toolbar.insert(separator, -1)
        separator.show()

        stop_button = StopButton(self)
        toolbar_box.toolbar.insert(stop_button, -1)
        stop_button.show()

        self.set_toolbar_box(toolbar_box)
        toolbar_box.show()

        self.scrollabeWindow = Gtk.ScrolledWindow()
        # self.window.add(self.scrollabeWindow)
        self.vbox = Gtk.Box(orientation= Gtk.Orientation.VERTICAL)
        self.scrollabeWindow.add(self.vbox)
        self.todo = {}
        self.count = 0
        self.btnAdd = Gtk.Button(label = "Add")
        self.btnAdd.connect("clicked",self.create)
        # self.vbox.pack_start(self.btnAdd,False,False,0)
        self.create()
        
        
        self.set_canvas(self.scrollabeWindow)
        self.scrollabeWindow.show_all()

        # self.vbox.connect("activate",self.create)
        # self.scrollabeWindow.set_halign(Gtk.Align.START)
        # self.scrollabeWindow.set_valign(Gtk.Align.START)
        # self.vbox2 = Gtk.Box(orientation= Gtk.Orientation.VERTICAL)
        # self.l1 = listForm()
        # self.l1.btn_del.hide()
        # self.vbox.pack_start(self.l1,False,False,0)
        # self.l1.label.connect("activate",self.create,self.l1)
        # b = Gtk.Button(label="add")
        # self.vbox.pack_start(b,False,False,0)
        # self.vbox.pack_start(self.vbox2,False,False,0)
        # b.connect('clicked',self.create)
        # # self.l1.btn_del.connect('clicked',self.delete)
        # self.l1.label.connect('activate',self.create)
        
        # # self.b = Gtk.Button(label="ffff")
        # # self.scrollabeWindow.add(self.b)
        # # self.scrollabeWindow.remove(self.l1)



        # self.window.show_all()
        # Gtk.main()

    def create(self):
        self.count+=1
        l = listForm()
        self.vbox.pack_start(l,False,False,0)
        self.vbox.show_all()
        l.btn_del.connect("clicked",self.delete)
        self.todo[l.btn_del]=l
        l.label.grab_focus()
        # print(self.todo)
        l.label.connect('activate',self.create2)
    def create2(self,widget):
        self.count+=1
        l = listForm()
        self.vbox.pack_start(l,False,False,0)
        self.vbox.show_all()
        l.btn_del.connect("clicked",self.delete)
        self.todo[l.btn_del]=l
        l.label.grab_focus()
        # print(self.todo)
        l.label.connect('activate',self.create2)

        
    def delete(self,button):
        self.vbox.remove(self.todo[button])
        self.count-=1
        self.vbox.show_all()
        if self.count==0:
            self.create()
        

    
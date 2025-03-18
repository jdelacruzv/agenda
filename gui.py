import tkinter as tk
from tkinter import ttk, messagebox
#import ttkthemes


class GuiMain(tk.Tk):
    """ Class that works as the application view """
    def __init__(self, main):
        super().__init__()
        # add theme to whole application
        #self.style = ttkthemes.ThemedStyle()
        # self.style.theme_use('arc')  # arc, plastik, clearlooks, elegance
        self.title('Agenda')
        self.iconphoto(True, tk.PhotoImage(file='img/ico.png'))
        self.resizable(False, False)
        self.center_window(870, 455)   # 860, 490
        self.main = main
        self.add_components()
        self.view_contact()


    def add_components(self):
        """ Add components to the main window """
        # main frame
        self.frm_main = ttk.Frame(self, borderwidth=1)
        self.frm_main.pack(fill=tk.BOTH, expand=tk.YES)
        # top frame
        self.frm_top = ttk.Frame(self.frm_main)
        self.frm_top.pack(side=tk.TOP, fill=tk.BOTH, expand=tk.YES, padx=10, pady=5)
        # row 0: name
        lbl_name = ttk.Label(self.frm_top, text='Nombre:', foreground='black', font=('Helvatica', 8, 'bold'))
        lbl_name.grid(row=0, column=0, sticky=tk.E, padx=5, pady=5)
        self.ety_name = ttk.Entry(self.frm_top, width=25)
        self.ety_name.grid(row=0, column=1, sticky=tk.EW, pady=5)
        # row 0: phone
        lbl_phone = ttk.Label(self.frm_top, text='Teléfono:', foreground='black', font=('Helvatica', 8, 'bold'))
        lbl_phone.grid(row=0, column=2, sticky=tk.E, padx=5, pady=5)
        self.ety_telephone = ttk.Entry(self.frm_top, width=12)
        self.ety_telephone.grid(row=0, column=3, sticky=tk.EW, pady=5)
        # row 0: birthdate
        lbl_birth = ttk.Label(self.frm_top, text='Fecha de Nacimiento:', foreground='black', font=('Helvatica', 8, 'bold'))
        lbl_birth.grid(row=0, column=4, sticky=tk.E, padx=5, pady=5)
        self.ety_birthdate = ttk.Entry(self.frm_top, width=10)
        self.ety_birthdate.grid(row=0, column=5, sticky=tk.EW, pady=5)
        self.ety_birthdate.insert(0, self.main.system_date())
        # row 0: clear button
        self.img_clear = tk.PhotoImage(file='img/clear.png')
        bnt_clear = ttk.Button(self.frm_top, text='Limpiar', image=self.img_clear,
            compound=tk.LEFT, width=10, command=self.clean_text_fields)
        bnt_clear.grid(row=0, column=6, sticky=tk.E, padx=5, pady=5)
        # row 1: email
        lbl_email = ttk.Label(self.frm_top, text='E-mail:', foreground='black', font=('Helvatica', 8, 'bold'))
        lbl_email.grid(row=1, column=0, sticky=tk.E, padx=5)
        self.ety_email = ttk.Entry(self.frm_top, width=25)
        self.ety_email.grid(row=1, column=1, sticky=tk.EW)
        # row 1: country
        lbl_country = ttk.Label(self.frm_top, text='País de Res:', foreground='black', font=('Helvatica', 8, 'bold'))
        lbl_country.grid(row=1, column=2, sticky=tk.E, padx=5)
        self.ety_country = ttk.Entry(self.frm_top, width=15)
        self.ety_country.grid(row=1, column=3, sticky=tk.EW)
        # row 1: save button
        self.img_save = tk.PhotoImage(file='img/save.png')
        btn_save = ttk.Button(self.frm_top, text='Grabar', image=self.img_save,
            compound=tk.LEFT, width=10, command=self.add_contact)
        btn_save.grid(row=1, column=4, sticky=tk.E, padx=5)
        # row 1: edit button
        self.img_edit = tk.PhotoImage(file='img/edit.png')
        btn_edit = ttk.Button(self.frm_top, text='Editar', image=self.img_edit,
            compound=tk.LEFT, width=10, command=self.open_edit_window)
        btn_edit.grid(row=1, column=5, sticky=tk.E)
        # row 1: delete
        self.img_delete = tk.PhotoImage(file='img/delete.png')
        btn_delete = ttk.Button(self.frm_top, text='Borrar', image=self.img_delete,
            compound=tk.LEFT, width=10, command=self.delete_contact)
        btn_delete.grid(row=1, column=6, sticky=tk.E, padx=5)
        # row 2: about button
        self.img_about = tk.PhotoImage(file='img/about.png')
        btn_about = ttk.Button(self.frm_top, text='Acerca de', image=self.img_about,
            compound=tk.LEFT, width=10, command=self.about_diary)
        btn_about.grid(row=2, column=6, sticky=tk.NS, pady=5)
        # bottom frame
        self.frm_bottom = ttk.Frame(self.frm_main)
        self.frm_bottom.pack(side=tk.TOP, fill=tk.BOTH, expand=tk.YES, padx=10)
        # treeview style
        tv_style = ttk.Style()
        tv_style.configure('Treeview', foreground='blue')
        tv_style.configure('Treeview.Heading', foreground='black', font=('Helvatica', 8, 'bold'))
        # treeview widget
        self.tv_table = ttk.Treeview(self.frm_bottom, height=15, column=('1', '2', '3', '4'))
        self.tv_table.grid(row=2, column=0, columnspan=7)
        self.tv_table.heading('#0', text='Nombre', anchor=tk.CENTER)
        self.tv_table.column('#0', width=180)
        self.tv_table.heading('#1', text='Teléfono', anchor=tk.CENTER)
        self.tv_table.column("#1", width=120)
        self.tv_table.heading('#2', text='Fecha de Nac.', anchor=tk.CENTER)
        self.tv_table.column('#2', width=115)
        self.tv_table.heading('#3', text='E-mail', anchor=tk.CENTER)
        self.tv_table.column('#3', width=280)
        self.tv_table.heading('#4', text='País de Res.', anchor=tk.CENTER)
        self.tv_table.column('#4', width=135)
        # scroll bar widget
        self.sb_vertical = ttk.Scrollbar(self.frm_bottom, orient=tk.VERTICAL, command=self.tv_table.yview)
        self.sb_vertical.grid(row=2, column=7, sticky=tk.NS)
        # add scroll bar to treeview
        self.tv_table.configure(yscrollcommand=self.sb_vertical.set)


    def view_contact(self):
        """ View the records obtained from the database """
        # get rows from table
        items = self.tv_table.get_children()
        # leave the table blank
        for i in items:
            self.tv_table.delete(i)
        # call read_contact() method
        data = self.main.read_contact()
        # insert records into table
        for row in data:
            self.tv_table.insert('', tk.END, text=row[0], values=(
                row[1], row[2], row[3], row[4]))
        self.ety_name.focus()


    def clean_text_fields(self):
        """ Clean text fields """
        self.ety_name.delete(0, tk.END)
        self.ety_telephone.delete(0, tk.END)
        self.ety_birthdate.delete(0, tk.END)
        self.ety_birthdate.insert(0, self.main.system_date())
        self.ety_email.delete(0, tk.END)
        self.ety_country.delete(0, tk.END)
        self.view_contact()


    def validate_contact(self):
        """ Validate that the text fields are not empty """
        name = len(self.ety_name.get())
        telephone = len(self.ety_telephone.get())
        birthdate = len(self.ety_birthdate.get())
        email = len(self.ety_email.get())
        country = len(self.ety_country.get())
        return (name != 0) and (telephone != 0) and (birthdate != 0) and (email != 0) and (country != 0)


    def add_contact(self):
        """ Add new contact to the database """
        if self.validate_contact():
            name = self.ety_name.get()
            telephone = self.ety_telephone.get()
            birthdate = self.ety_birthdate.get()
            email = self.ety_email.get()
            country = self.ety_country.get()
            self.main.create_contact(
                name, telephone, birthdate, email, country)
            self.view_contact()
            self.clean_text_fields()
            messagebox.showinfo('Information', 'El contacto fue creado')
        else:
            messagebox.showwarning('Aviso', 'Ingrese datos en los campos')
            self.view_contact()


    def open_edit_window(self):
        """ Open contact edit window """
        # get the focus of the row
        current_item = self.tv_table.focus()
        if current_item:
            # call child class GuiEdit
            GuiEdit(self, self.main)
            self.view_contact()
        else:
            messagebox.showwarning('Aviso', 'Seleccione un elemento')
            self.ety_name.focus()


    def delete_contact(self):
        """ Delete contact """
        # get the focus of the row
        current_item = self.tv_table.focus()
        if current_item:
            # get the text of the name field
            name = self.tv_table.item(self.tv_table.selection())['text']
            valor = messagebox.askquestion(
                'Agenda', '¿Desea eliminar el registro?')
            if valor == 'yes':
                self.main.delete_contact(name)
                messagebox.showinfo('Information', 'El contacto fue eliminado')
                self.view_contact()
        else:
            messagebox.showwarning('Aviso', 'Seleccione un elemento')
            self.ety_name.focus()


    @staticmethod
    def about_diary():
        """ Program description """
        msg = 'Realizado por José De La Cruz'
        messagebox.showinfo('Agenda', msg)


    def center_window(self, w, h):
        """ Center window """
        x = (self.winfo_screenwidth() - w) / 2
        y = (self.winfo_screenheight() - h) / 2
        self.geometry('%dx%d+%d+%d' % (w, h, x, y))


    def start_mainloop(self):
        """ Run the main window loop """
        self.mainloop()


class GuiEdit(tk.Toplevel):
    """ Crea la ventana de editar registro """
    def __init__(self, master, main):
        super().__init__()
        self.transient(master)  # make the window transient(transitorio)
        self.grab_set()  		# make the window modal
        self.title('Actualizar contacto')
        self.resizable(False, False)
        self.main = main
        self.center_window(385, 155)  # 330, 145
        self.focus_set()

        # get text and values from the treeview fields of the GuiMain class
        name = self.master.tv_table.item(self.master.tv_table.selection())['text']
        telephone = self.master.tv_table.item(self.master.tv_table.selection())['values'][0]
        birthdate = self.master.tv_table.item(self.master.tv_table.selection())['values'][1]
        email = self.master.tv_table.item(self.master.tv_table.selection())['values'][2]
        country = self.master.tv_table.item(self.master.tv_table.selection())['values'][3]

        # create gui
        tk.Label(self, text='Nombre:').grid(row=0, column=0, sticky=tk.E)
        tk.Entry(self, width=35, textvariable=tk.StringVar(
            self, value=name), fg='red', state='readonly').grid(row=0, column=1)

        tk.Label(self, text='Fecha de Nac:').grid(row=1, column=0, sticky=tk.E)
        self.ety_birthdate = tk.Entry(self, width=35, textvariable=tk.StringVar(
            self, value=birthdate), fg='red', state='readonly')
        self.ety_birthdate.grid(row=1, column=1)

        tk.Label(self, text='Teléfono:').grid(row=2, column=0, sticky=tk.E)
        self.ety_telephone = tk.Entry(self, width=35, textvariable=tk.StringVar(self, value=telephone))
        self.ety_telephone.grid(row=2, column=1)
        self.ety_telephone.focus()

        tk.Label(self, text='E-mail:').grid(row=3, column=0, sticky=tk.E)
        self.ety_email = tk.Entry(self, width=35, textvariable=tk.StringVar(self, value=email))
        self.ety_email.grid(row=3, column=1)

        tk.Label(self, text='País de Res:').grid(row=4, column=0, sticky=tk.E)
        self.ety_country = tk.Entry(self, width=35, textvariable=tk.StringVar(self, value=country))
        self.ety_country.grid(row=4, column=1)

        # update record button
        self.img_update = tk.PhotoImage(file='img/update.png')
        self.btn_update = ttk.Button(self, text='Actualizar', image=self.img_update, compound='left',
            command=lambda: self.update_contact(self.ety_telephone.get(), self.ety_email.get(), 
            self.ety_country.get(), birthdate, name))
        self.btn_update.grid(row=5, column=1, sticky=tk.E, pady=5)

    
    def update_contact(self, telephone, email, country, birthdate, name):
        """ Update contact """
        self.main.update_contact(telephone, email, country, birthdate, name)
        self.master.view_contact()
        messagebox.showinfo('Info Agenda', 'El contacto fue actualizado')
        self.destroy()

    
    def center_window(self, w, h):
        """ Center window """
        x = (self.winfo_screenwidth() - w) / 2
        y = (self.winfo_screenheight() - h) / 2
        self.geometry('%dx%d+%d+%d' % (w, h, x, y))

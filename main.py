import datetime
from diary import Diary
from gui import GuiMain


class Main:
    """ Class that works as the application controller """    
    def __init__(self):
        self.diary = Diary()
        self.gui_main = GuiMain(self)

    
    def read_contact(self):
        """ Get records from the database """
        query_contact = self.diary.read_contact()
        return query_contact

    
    def create_contact(self, name, telephone, birthdate, email, country):
        """ call create_contact method Diary class """
        self.diary.create_contact(name, telephone, birthdate, email, country)

    
    def update_contact(self, telephone, email, country, birthdate, name):
        """ call update_contact method Diary class """
        self.diary.update_contact(telephone, email, country, birthdate, name)

    
    def delete_contact(self, name):
        """ call delete_contact method Diary class """
        self.diary.delete_contact(name)

    
    @staticmethod
    def system_date():
        """ Get the system date """
        x = datetime.datetime.now()
        date = '%s/%s/%s' % (x.day, x.month, x.year)
        return date

    
    def start_gui(self):
        """ Call method Gui class """
        self.gui_main.start_mainloop()


if __name__ == '__main__':
    main = Main()
    main.start_gui()

<<<<<<< HEAD
=======

>>>>>>> 226f2e00ca4a8a3a39e10b35e793ce0c908d3e81
"""

Используется для запуска программ,
входящих в состав приложения.

"""


import tkinter as tk

from Apps import App
<<<<<<< HEAD

# Подпрограммы
from Apps.TimeApps import Watch

=======
>>>>>>> 226f2e00ca4a8a3a39e10b35e793ce0c908d3e81

class Launcher:
    
    
    def execute(self):
        
        self.root = tk.Tk()
        self.root.title("Organizer Launcher v0.1")
        self.root.geometry("480x480+800+200")
        self.root.resizable(False, False)
        
<<<<<<< HEAD
        self.root.mainloop()
        
    
    def add_app(self, app: App):
        
        self.add_button(name=app.name, execute=app.execute)
    
    
    def add_button(self, image_filename, name, execute):
        
        app_button = tk.Button(self.root, text=f"{name}")
=======
        root.mainloop()

    def add_app(self):
        
        self.add_button()

    def add_button(self, image_filename, text):
        pass
>>>>>>> 226f2e00ca4a8a3a39e10b35e793ce0c908d3e81


if __name__ == "__main__":
    launcher = Launcher()
<<<<<<< HEAD
    
    watch = Watch()
    
    launcher.add_app(Watch)
    
    launcher.execute()
=======

    launcher.execute()

>>>>>>> 226f2e00ca4a8a3a39e10b35e793ce0c908d3e81

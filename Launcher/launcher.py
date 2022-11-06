"""

Используется для запуска программ,
входящих в состав приложения.

"""


import tkinter as tk

from Apps import App

# Подпрограммы
from Apps.TimeApps import Watch


class Launcher():
    
    
    def execute(self):
        
        self.root = tk.Tk()
        self.root.title("Organizer Launcher v0.1")
        self.root.geometry("480x480+800+200")
        self.root.resizable(False, False)
        
        self.root.mainloop()
        
    
    def add_app(self, app: App):
        
        self.add_button(name=app.name, execute=app.execute)
    
    
    def add_button(self, image_filename, name, execute):
        
        app_button = tk.Button(self.root, text=f"{name}")

if __name__ == "__main__":
    launcher = Launcher()
    
    watch = Watch()
    
    launcher.add_app(Watch)
    
    launcher.execute()

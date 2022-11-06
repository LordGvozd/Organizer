"""

Используется для запуска программ,
входящих в состав приложения.

"""


import tkinter as tk


class Launcher():
    
    
    def execute(self):
        
        root = tk.Tk()
        root.title("Organizer Launcher v0.1")
        root.geometry("480x480+800+200")
        root.resizable(False, False)
        
        root.mainloop()
        
    
    def add_app(self):
        
        self.add_button()
    
    
    def add_button(self, image_filename, text):
        pass

if __name__ == "__main__":
    launcher = Launcher()
    
    
    launcher.execute()
import tkinter as tk

from Apps import App


class Watch(App.App):
    def __init__(self):
        super(Watch, self).__init__("Watch")

    def execute(self):
        print("I am " + self.name)


if __name__ == "__main__":
    watch = Watch()
    watch.execute()




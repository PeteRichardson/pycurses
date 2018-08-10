#!/usr/bin/env python
from cursesapp import CursesApp, Window

class CountWindow(Window):
    def __init__(self, bottom, right, top, left, stdscr, start_val=0):
        self.start_val = start_val
        self.reset_data()
        super(CountWindow, self).__init__(bottom, right, top, left, stdscr)

    def __str__(self):
        return str(self.rint)

    def reset_data(self):
        self.rint = self.start_val

    def increment(self):
        self.rint = self.rint + 1

    def decrement(self):
        self.rint = self.rint - 1

class StringWindow(Window):
    def __init__(self, bottom, right, top, left, stdscr, start_string):
        self.lstr = start_string
        super(StringWindow, self).__init__(bottom, right, top, left, stdscr)

    def __str__(self):
        return self.lstr

class MyCursesApp(CursesApp):

    def layout(self):
        y, x = self.stdscr.getmaxyx()
        self.lwin = StringWindow(y,x/3,0,0,self.stdscr, "Wokka Wokka")
        self.rwin = CountWindow(y,2*x/3,0,x/3,self.stdscr,4)
        self.windows = [self.lwin, self.rwin]
        self.render()

    def handle_key(self, key):
        if key == ord('q'):
            self.quit = True
        elif key == ord('r'):
            self.rwin.reset_data()
        elif key == ord('+'):
            self.rwin.increment()
        elif key == ord('-'):
            self.rwin.decrement()

    def render2(self):
        for win in [self.lwin, self.rwin]: 
            win.content.addstr(0,0,win.__str__())

app = MyCursesApp()
app.run()


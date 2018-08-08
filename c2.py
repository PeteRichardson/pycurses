#!/usr/bin/env python
import curses

class Window:
    def __init__(self, bottom, right, top, left, stdscr):
        self.win = stdscr.subwin(bottom, right, top, left)
        self.win.box()
        self.content =  stdscr.subwin(bottom-2, right-2, top+1, left+1)
        self.win.refresh()

class CursesApp:
    def __init__(self):
        self.windows =  {}
        self.quit = False

    def layout(self):
        y, x = self.stdscr.getmaxyx()
        self.windows["lwin"] = Window(y,x/2,0,0,self.stdscr).content
        self.windows["rwin"] = Window(y,x/2,0,x/2,self.stdscr).content

    def render(self):
        self.windows["lwin"].addstr(0,0,"Pete Richardson")
        self.windows["rwin"].addstr(0,0,"Pete Richardson")
        #rwin.refresh()

    def handle_key(self, key):
        if key == ord('q'):
            self.quit = True

    def loop(self):
        NO_KEY_PRESSED = -1
        key_pressed = NO_KEY_PRESSED
        while self.quit != True:
            self.render()
            key_pressed = self.stdscr.getch()
            self.handle_key(key_pressed)

    def cleanup(self):
        pass

    def run(self, stdscr):
        self.stdscr = stdscr    
        self.layout() 
        self.loop()
        self.cleanup()

app = CursesApp()
curses.wrapper(app.run)

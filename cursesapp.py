#!/usr/bin/env python
import curses
from curses import wrapper

class Window:
    def __init__(self, bottom, right, top, left, stdscr):
        self.win = stdscr.subwin(bottom, right, top, left)
        self.win.box()
        self.content =  stdscr.subwin(bottom-2, right-2, top+1, left+1)
        self.win.refresh()

class CursesApp:
    def __init__(self):
        self.stdscr = curses.initscr()
        self.stdscr.nodelay(True)

        # Enable the keypad ncurses return (instead of 16 bit value)
        self.stdscr.keypad(True)

        # Refresh after attributes
        self.stdscr.refresh()

        # No echo to screen
        curses.noecho()

        # Remove cursor
        curses.curs_set(0)

        # Colors
        if curses.has_colors():
            curses.start_color()
            curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLUE)
            curses.init_pair(2, curses.COLOR_WHITE, curses.COLOR_RED)
            curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_YELLOW)
            curses.init_pair(4, curses.COLOR_BLACK, curses.COLOR_BLUE)

        self.windows =  {}
        self.quit = False

    def layout(self):
        y, x = self.stdscr.getmaxyx()
        self.windows["lwin"] = Window(y,x/2,0,0,self.stdscr).content
        self.windows["rwin"] = Window(y,x/2,0,x/2,self.stdscr).content

    def render(self):
        self.windows["lwin"].addstr(0,0,"Pete Richardson")
        self.windows["rwin"].addstr(0,0,"Pete Richardson")

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
        curses.endwin()

    def run(self):
        self.layout() 
        self.loop()
        self.cleanup()
        

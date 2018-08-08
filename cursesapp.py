#!/usr/bin/env python
import curses
import signal

class Window:
    def __init__(self, bottom, right, top, left, stdscr):
        self.win = stdscr.subwin(bottom, right, top, left)
        self.win.box()
        self.content =  stdscr.subwin(bottom-2, right-2, top+1, left+1)
        self.win.refresh()

def signal_handler(signal, frame):
	curses.echo()
	curses.endwin()

signal.signal(signal.SIGINT, signal_handler)


class CursesApp:
    def __init__(self):

        self.stdscr = curses.initscr()
        self.stdscr.nodelay(True)
        self.stdscr.keypad(True)
        curses.noecho()

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
        curses.nocbreak()
	self.stdscr.keypad(False)
	curses.echo()
        curses.endwin()

    def run(self):
	try:
	    self.layout() 
	    self.loop()
	    self.cleanup()
        except Exception as e:
	    self.cleanup()
	    raise

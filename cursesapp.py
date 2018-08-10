#!/usr/bin/env python
import curses
import signal
import time

class Window(object):
    def __init__(self, bottom, right, top, left, stdscr):
        self.win = stdscr.subwin(bottom, right, top, left)
        self.win.box()
        self.content =  stdscr.subwin(bottom-2, right-2, top+1, left+1)
        self.win.refresh()

def signal_handler(signal, frame):
	curses.echo()
	curses.endwin()

signal.signal(signal.SIGINT, signal_handler)


class CursesApp(object):
    def __init__(self):

        self.stdscr = curses.initscr()
        self.stdscr.nodelay(True)
        curses.curs_set(0)
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
        pass

    def render(self):
        for win in self.windows:
            win.content.addstr(0,0,win.__str__())
            win.content.refresh()

    def handle_key(self, key):
        if key == ord('q'):
            self.quit = True

    def loop(self):
        NO_KEY_PRESSED = -1
        key_pressed = NO_KEY_PRESSED
        while self.quit != True:
            key_pressed = self.stdscr.getch()
            if key_pressed != NO_KEY_PRESSED:
                self.handle_key(key_pressed)
                self.render()
                self.stdscr.refresh()
            time.sleep(0.1)

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

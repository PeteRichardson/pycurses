#!/usr/bin/env python
import curses

class Window:
    def __init__(self, height, width, top, left, stdscr):
        self.win = stdscr.subwin(height, width, top, left)
        self.win.box()
        self.content =  stdscr.subwin(height-2, width-2, top+1, left+1)

def main(stdscr):

    NO_KEY_PRESSED = -1

    y, x = stdscr.getmaxyx()

    lwin = Window(y,x/2,0,0,stdscr).content
    lwin.addstr(0,0,"Pete Richardson")
    rwin = Window(y,x/2,0,x/2,stdscr).content
    rwin.addstr(0,0,"Pete Richardson")
    lwin.addstr(1,0,"Wendy Wilson")
    
    key_pressed = NO_KEY_PRESSED
    while key_pressed != ord('q'):
        key_pressed = stdscr.getch()


curses.wrapper(main)

#!/usr/bin/env python
import curses

y,x = -1,-1

def main(stdscr):

    NO_KEY_PRESSED = -1

    y, x = stdscr.getmaxyx()
    w = stdscr.subwin(y-1,x-1,1,1)
    w.addstr(0,0,"Pete Richardson")
    w.refresh()

    key_pressed = NO_KEY_PRESSED
    while key_pressed != ord('q'):
        key_pressed = stdscr.getch()


curses.wrapper(main)

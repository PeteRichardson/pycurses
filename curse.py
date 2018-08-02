#!/usr/bin/env python
import curses

def main(stuff):
    w1 = curses.newwin(5,20,0,0)
    w2 = curses.newwin(5,20,0,21)
    w1.addstr(0,2,"w1")
    w2.addstr(0,2,"w2",curses.A_REVERSE)
    w2.refresh()
    while 1:
        c = w1.getch()
        if c == ord('p'):
            w2.addstr(0, 0, "Current mode: Typing mode", curses.A_REVERSE)
            w2.refresh()
        elif c == ord('q'):
            break  # Exit the while()


curses.wrapper(main)

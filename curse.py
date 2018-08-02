#!/usr/bin/env python
import curses
stdscr = curses.initscr()
curses.noecho()
curses.cbreak()

stdscr.addstr("Hello, World!")

while 1:
    c = stdscr.getch()
    if c == ord('p'):
        stdscr.addstr("Pete")
    elif c == ord('q'):
        break  # Exit the while()

curses.nocbreak(); stdscr.keypad(0); curses.echo()
curses.endwin()

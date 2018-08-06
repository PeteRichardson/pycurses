#!/usr/bin/env python
import curses
import random

numbers = []

def main(stuff):
    NO_KEY_PRESSED = -1

    for i in xrange(10):
        numbers.append(str(random.random()*40))

    stdscr = curses.initscr()
    stdscr.nodelay(True)

    y, x = stdscr.getmaxyx()
    w1_border = stdscr.subwin(y-10,x/2-6,5,3)
    w1 = stdscr.subwin(y-12,x/2-8,6,4)
    txt = "\n".join(numbers)
    w1.addstr(0,0,txt)
    w1_border.box()
    w1_border.refresh()
    #w1.refresh()


    key_pressed = NO_KEY_PRESSED
    while key_pressed != ord('q'):
        key_pressed = stdscr.getch()

        if key_pressed == ord('p'):
            w1.addstr(1,1, "Current mode: Typing mode", curses.A_REVERSE)
            w1.refresh()

        stdscr.refresh()


curses.wrapper(main)

#!/usr/bin/env python
import curses
import random

numbers1 = []
numbers2 = []

def prep_data():
    for i in xrange(10):
        numbers1.append(str(random.random()*40))
        numbers2.append(str(random.random()*40))

def add_list_to_window(window, numlist):
    txt = "\n".join(numlist)
    window.addstr(0,0,txt)

def win1(y,x,stdscr):
    w1 = stdscr.subwin(18,x/2,0,0)
    w1.box()
    w1.bkgd(' ', curses.color_pair(1))
    add_list_to_window(w1,numbers1)
    w1.refresh()
    return w1

def win2(y,x,stdscr):
    w2 = stdscr.subwin(18,x/2,0,x/2)
    w2.box()
    w2.bkgd(' ', curses.color_pair(2))
    add_list_to_window(w2,numbers1)
    w2.refresh()
    return w2

def main(stuff):
    NO_KEY_PRESSED = -1

    prep_data()

    stdscr = curses.initscr()
    stdscr.nodelay(True)

    # Colors
    if curses.has_colors():
        curses.start_color()
        curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLUE)
        curses.init_pair(2, curses.COLOR_WHITE, curses.COLOR_RED)
        curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_YELLOW)
        curses.init_pair(4, curses.COLOR_BLACK, curses.COLOR_BLUE)

    y, x = stdscr.getmaxyx()
    w1 = win1(y,x,stdscr)
    w2 = win2(y,x,stdscr)

    key_pressed = NO_KEY_PRESSED
    while key_pressed != ord('q'):
        key_pressed = stdscr.getch()

        if key_pressed == ord('p'):
            w2.addstr(1,1, "Current mode: Typing mode", curses.A_REVERSE)
            w2.refresh()

        stdscr.refresh()


curses.wrapper(main)

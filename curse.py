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

def win(h,w,start_y,start_x,stdscr,color,numbers):
    w =  stdscr.subwin(h,w,start_y,start_x)
    w.box()
    w.bkgd(' ', curses.color_pair(color))
    add_list_to_window(w,numbers)
    w.refresh()
    return w

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
    w1 = win(y,x/2,0,0,stdscr,1,numbers1)
    w2 = win(y,x/2,0,x/2,stdscr,2,numbers2)

    key_pressed = NO_KEY_PRESSED
    while key_pressed != ord('q'):
        key_pressed = stdscr.getch()

        if key_pressed == ord('p'):
            w2.addstr(1,1, "Current mode: Typing mode", curses.A_REVERSE)
            w2.refresh()

        stdscr.refresh()


curses.wrapper(main)

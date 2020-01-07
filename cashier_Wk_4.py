"""
File: cashier_Wk_3.py
Name: Theodore Thompson
Date: 12/12/2019
Course: DSC510-T302 Introduction to Programming (2203-1)
Desc: The program offer a simple menu. Press 1 to begin, zx to return to top menu.
            The program receives the name of the customer company and the number of feet
            of fiber optic cable being purchased. Then Outputs the total cost.
            The program decides what level of charge depending on the quantity ordered
            <= 100 is .87/ft, <= 250 is .80/ft, <= 500 is .87/ft, high amount is .50/ft
Usage: The user is allowed to enter any string for the company name and a float or integer
            number for the number of feet of optical cable being purchased.

"""

import sys


def ted_class_header(assignment_name):
    print("Hello my name is Theodore Thompson")
    print("The name of this assignment is " + assignment_name)


def ted_menu1():
    ted_class_header("Cashier Program Week 4")
    print("\n\nMenu")
    print("zx.   Please enter 'zx' to start over")
    print("quit. Please enter 'quit' to exit")
    print("1.    Please enter '1' to cash out: ")
    menu1 = input()
    if menu1 == "zx":
        ted_menu1()

    if menu1 == "quit":
        input("\n\nThank you. \nPress enter key to quit")
        return

    if menu1 == "1":
        ted_menu2()
    else:
        print("\n")
        ted_menu1()


def ted_line_total(unit_price, qty):  # Critical function for week 4, heavy lifting, cost calculation
    return unit_price * qty


def ted_menu2():
    qty = ""
    print("\n\nCash out Menu")
    print("zx. Please enter 'zx' to start over")
    print("1.  Please enter your company name: ")
    company = input()
    if company == "zx":
        ted_menu1()
        return
    else:
        qty = ted_menu3()

    while qty != "zx":
        try:
            qty_num = float(qty)

        except ValueError:
            qty = input("Please enter number of feet between 1 and 100,000: ")
            continue
        if qty_num < 100001.0:
            if qty_num > 0.0:
                # ans = round((0.87 * qty_num), 2)
                if qty_num <= 100.00:
                    print("The total fiber installation cost for, " + company +
                          " is $%.2f" % ted_line_total(0.87, qty_num))
                elif qty_num <= 250.00:
                    print("The total fiber installation cost for, " + company +
                          " is $%.2f" % ted_line_total(0.80, qty_num))
                elif qty_num <= 500.00:
                    print("The total fiber installation cost for, " + company +
                          " is $%.2f" % ted_line_total(0.70, qty_num))
                else:
                    print("The total fiber installation cost for, " + company +
                          " is $%.2f" % ted_line_total(0.5, qty_num))

                input("\n\nPress enter to start over ")
                break
        print("Please enter number of feet between 1 and 100,000: ")
        qty = input()
        # qty_num = float(qty)
    ted_menu1()


def ted_menu3():
    print("\n\nCash out Menu")
    print("zx. Please enter 'zx' to start over")
    print("1.  Please enter the number of feet you'd like installed: ")
    qty = input()
    if qty == "zx":
        ted_menu1()
    else:
        return qty


ted_menu1()


it = 0

def set_it(newit):
    global it
    it = newit

def double_it():
    global it
    it = it * 2
    return it


print ( "ya this file is changed....." )

# Automated Test
if __name__ == "__main__":
    n_err = 0
    x = set_it ( 3 )
    set_it(5)
    x = double_it()
    if x !=  10:
        n_err = n_err + 1
        print ( "Error: Test 1: conversion not working, expected {} got {}".format (  10, x ) )

    # Now 2nd test is dependent on 1st test
    x = double_it()
    if x != 20:
        n_err = n_err + 1
        print ( "Error: Test 2: conversion not working, expected {} got {}".format ( 20, x ) )

    if n_err == 0 :
        print ( "PASS" )
    else:
        print ( "FAILED" )


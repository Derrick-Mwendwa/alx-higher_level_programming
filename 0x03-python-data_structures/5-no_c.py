#!/usr/bin/python3

def no_c(my_string):
    new_list = [elm for elm in my_string if elm != 'c' and elm != 'C']
    new_string = "".join(new_list)
    return (new_string)

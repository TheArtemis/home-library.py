from addBook import add_book
from database_actions import show_database

welcome_igm = "             `::`             \n          -///``///-          \n      `///-`h/oo/h`-///`      \n   ://:`   `h.//.h`   `://:   \n+yh+////////+osso+///////..hy+\n /+o////+o////++////o+////o+/ \n   +s//s++s//s++s//s++s//s+   \n    y:/h  y//h  h//y  h/:y    \n    y:/h  y//h  h//y  h/:y    \n    y:/h  y//h  h//y  h/:y    \n    y:/h  y//h  h//y  h/:y    \n   :dood::dood::dood::dood:   \n  +y////yy////yy////yy////y+  \n :y//////////////////////.`y: \n .//////////////////////////."
print(welcome_igm)

print("\n WELCOME TO YOUR HOME LIBRARY!")

print("\n Select Action:\n")

print(" [ 1 ] - Add Book")

print(" [ 2 ] - Show Database")

action = input("input number: ")

if int(action) == 1:
    add_book()

if int(action) == 2:
    show_database()

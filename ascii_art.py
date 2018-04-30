import pyfiglet
from termcolor import colored

valid_colors = ("red", "green", "yellow", "blue", "magenta", "white", "cyan")

msg = input("What would you like to print? ")
color = input("What color? ")

if color not in valid_colors:
    color = "magenta"

art = pyfiglet.figlet_format(msg)
colored_art = colored(art, color=color)
print(colored_art)

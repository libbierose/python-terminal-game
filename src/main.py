import os
from rich.console import Console
from rich.align import Align
from rich.text import Text
from rich.panel import Panel
from rich.markdown import Markdown

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

clear_screen()

console = Console()

# This is the ASCII art that will be displayed at the top of the main menu.
dbd_ascii_art = r"""
 ______   ______   ______     _________  _______     _____  ____   ____  _____       _       
|_   _ `.|_   _ \ |_   _ `.  |  _   _  ||_   __ \   |_   _||_  _| |_  _||_   _|     / \      
  | | `. \ | |_) |  | | `. \ |_/ | | \_|  | |__) |    | |    \ \   / /    | |      / _ \     
  | |  | | |  __'.  | |  | |     | |      |  __ /     | |     \ \ / /     | |     / ___ \    
 _| |_.' /_| |__) |_| |_.' /    _| |_    _| |  \ \_  _| |_     \ ' /     _| |_  _/ /   \ \_  
|______.'|_______/|______.'    |_____|  |____| |___||_____|     \_/     |_____||____| |____| 
                                                                                             
"""

# This is the welcome text that will be displayed at the top of the main menu, along with the ASCII art.
# It provides instructions on how to play the game and explains the lifelines that the player can use.
welcome_text = """
# Welcome to DBD Trivia!

This is a simple command-line trivia game based on the popular game *Dead by Daylight*.  
You will be asked a series of questions about the game, and you will need to type the correct answer to score points.  
The game will keep track of your score and give you feedback on your answers.

## Lifelines

You have 3 lifelines that you can use:

- **50/50**: This will eliminate two incorrect answers, leaving you with a 50% chance of choosing the correct answer.  
- **Ask the Audience**: This will show you the percentage of people who chose each answer, giving you a hint on which one is correct.  
- **Phone a Friend**: This will give you a hint along with a random answer (*the hint will be correct 70% of the time*).
"""

username = ""

def print_ascii_art():
   console.print(Align.center(Text(dbd_ascii_art, style="bold red")))

def welcome_message():
   # clear the screen before showing the welcome message
   clear_screen()
   
   # print the ASCII art at the top of the welcome message
   print_ascii_art()
   
   # print the welcome message and instructions
   console.print(Panel(Markdown(welcome_text), border_style="bright_blue", title="[bold cyan]Instructions[/bold cyan]"))
   
   # prompt the user to enter their name
   user_name = console.input("[bold yellow]Please enter your name: [/bold yellow]")
   
   # return the user's name to be used in the main menu
   return user_name

def start_game():
   # initialize the error state variables to keep track of whether there is an error and what the error message is
   hasError = False
   errorMessage = ""
   
   while True:
      # clear the screen before showing the menu
      clear_screen()
      
      # print the ASCII art at the top of the menu
      print_ascii_art()

      # if there is an error, display the error message in a red panel at the top of the menu
      if hasError:
         console.print(Panel(f"[bold red]{errorMessage}[/bold red]", border_style="red", title="[bold red]Error[/bold red]"))

      # prompt the user to select an option from the game menu
      user_input = console.input("[bold yellow]This is just placeholder for now type 'back' to go to the main menu: [/bold yellow]")

      match user_input:
         case "back":
            # reset the error state before returning to the main menu
            hasError = False
            return
         case _:
            # if the user enters an invalid option, set the error state and display an error message
            hasError = True
            errorMessage = "Invalid option. Please type 'back' to return to the main menu."

def config_menu():
   # initialize the error state variables to keep track of whether there is an error and what the error message is
   hasError = False
   errorMessage = ""

   while True:
      # clear the screen before showing the menu
      clear_screen()
      
      # print the ASCII art at the top of the menu
      print_ascii_art()
      
      # print the configuration menu options
      if hasError:
         console.print(Panel(f"[bold red]{errorMessage}[/bold red]", border_style="red", title="[bold red]Error[/bold red]"))
      
      # prompt the user to select an option from the configuration menu
      user_input = console.input("[bold yellow]This is just placeholder for now type 'back' to go to the main menu: [/bold yellow]")

      match user_input:
         case "back":
            # reset the error state before returning to the main menu
            hasError = False
            return
         case _:
            # if the user enters an invalid option, set the error state and display an error message
            hasError = True
            errorMessage = "Invalid option. Please type 'back' to return to the main menu."

def main_menu(username):
   # initialize the error state variables to keep track of whether there is an error and what the error message is
   hasError = False
   errorMessage = ""
   
   while True:
      # clear the screen before showing the menu
      clear_screen()
      
      # print the ASCII art at the top of the menu
      print_ascii_art()
      
      # print the welcome message and instructions
      console.print(Panel(Markdown(welcome_text), border_style="bright_blue", title="[bold cyan]Instructions[/bold cyan]"))
      
      # print the main menu options
      console.print(Panel(f"Hiya {username}! please select one of the options below:\n[bold green]1.[/bold green] Start Game\n[bold green]2.[/bold green] Configuration\n[bold green]3.[/bold green] Exit", border_style="bright_blue", title="[bold cyan]Main Menu[/bold cyan]"))
      
      # if there is an error, display the error message in a red panel at the top of the menu
      if hasError:
         console.print(Panel(f"[bold red]{errorMessage}[/bold red]", border_style="red", title="[bold red]Error[/bold red]"))
      
      # prompt the user to select an option from the main menu   
      user_input = console.input("[bold yellow]Please select an option (1, 2, or 3): [/bold yellow]")
      
      # use a match statement to handle the user's input and call the appropriate function based on their selection
      match user_input:
         case "1":
            # reset the error state before starting the game
            hasError = False
            # call the start_game function to begin the game
            start_game()
         case "2":
            # reset the error state before showing the configuration menu
            hasError = False
            # call the config_menu function to show the configuration options
            config_menu()
         case "3":
            # reset the error state before exiting the game
            hasError = False
            # print a goodbye message and exit the game
            console.print("[bold red]Exiting game. Goodbye![/bold red]")
            exit()
         case _:
            # if the user enters an invalid option, set the error state and display an error message
            hasError = True
            errorMessage = "Invalid option. Please choose 1, 2, or 3."

# Start the game by showing the welcome message and then displaying the main menu with the user's name.
username = welcome_message()
main_menu(username)
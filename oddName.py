"""
William Robinson - Asks user for name and displays every second letter
"""

name = input("Please enter your name: ")
while name == "":
    print("Invalid name")
    name = input("Please enter your name: ")

for i in range(0, len(name), 2):
    word 
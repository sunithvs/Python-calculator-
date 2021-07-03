
"""
    All the buttons are define here
    Each button is a object having the keys text abd position
    text => text to be displayed on the button and passed to the onclick handler
    position => A tuple the coordinates of the button to be displayed on the screen
    Buttons starts from the second row (index 1)
    -
"""

buttons = [
    {
        "text": "9",
        "position": (1, 0)
    },
    {
        "text": "8",
        "position": (1, 1)
    },
    {
        "text": "7",
        "position": (1, 2)
    },
    {
        "text": "6",
        "position": (2, 0)
    },
    {
        "text": "5",
        "position": (2, 1)
    },
    {
        "text": "4",
        "position": (2, 2)
    },
    {
        "text": "3",
        "position": (3, 0)
    },
    {
        "text": "2",
        "position": (3, 1)
    },
    {
        "text": "1",
        "position": (3, 2)
    },
    {
        "text": "0",
        "position": (4, 0)
    },
    {
        "text": "+",
        "position": (2, 3)
    },
    {
        "text": "-",
        "position": (3, 3)
    },
    {
        "text": "/",
        "position": (4, 1)
    },
    {
        "text": "*",
        "position": (4, 2)
    },
    {
        "text": "Ac",
        "position": (1, 3)
    },
    {
        "text": "=",
        "position": (4, 3)
    },

]
print(buttons[1]["position"][1])
import tkinter as tk
from tkinter import messagebox
from random_word import RandomWords


class HangmanGame:
    def _init_(self, root):
        self.root = root
        self.root.title("Hangman Game")
        self.r = RandomWords()

        # Generating a random word
        self.random_word_string = self.r.get_random_word().lower()
        self.random_word_list = list(self.random_word_string)

        self.chances = 7
        self.dash_string_list = ["_" for _ in range(len(self.random_word_string))]
        self.user_string_list = []

        # Hangman stages
        self.hangman_stages = [
            r'''
  ___
 |/      |
 |       
 |       
 |       
 |       
 |       
|___
            ''',
            r'''
  ___
 |/      |
 |      (_)
 |       
 |       
 |       
 |       
|___
            ''',
            r'''
  ___
 |/      |
 |      (_)
 |       |
 |       |
 |       
 |       
|___
            ''',
            r'''
  ___
 |/      |
 |      (_)
 |      \|
 |       |
 |       
 |       
|___
            ''',
            r'''
  ___
 |/      |
 |      (_)
 |      \|/
 |       |
 |       
 |       
|___
            ''',
            r'''
  ___
 |/      |
 |      (_)
 |      \|/
 |       |
 |      / 
 |       
|___
            ''',
            r'''
  ___
 |/      |
 |      (_)
 |      \|/
 |       |
 |      / \
 |       
|___
            '''
        ]

        # Create the GUI components
        self.create_widgets()
        self.update_display()

    def create_widgets(self):
        # Frame for game display
        self.frame = tk.Frame(self.root, bg='#2b2b2b')
        self.frame.pack(pady=10)

        # Hangman stage display
        self.hangman_label = tk.Label(self.frame, text="", font=("Courier", 16), bg='#2b2b2b', fg='#dcdcdc')
        self.hangman_label.pack()

        # Word display
        self.word_label = tk.Label(self.frame, text="", font=("Courier", 28), bg='#2b2b2b', fg='#61afef')
        self.word_label.pack(pady=20)

        # Chances display
        self.chances_label = tk.Label(self.frame, text="", font=("Courier", 16), bg='#2b2b2b', fg='#98c379')
        self.chances_label.pack()

        # Keyboard display
        self.keyboard_frame = tk.Frame(self.root, bg='#2b2b2b')
        self.keyboard_frame.pack(pady=10)

        self.create_keyboard()

        # Message display
        self.message_label = tk.Label(self.frame, text="", font=("Courier", 16), bg='#2b2b2b', fg='#e06c75')
        self.message_label.pack()

    def create_keyboard(self):
        # Create virtual keyboard
        self.buttons = {}
        for i in range(26):
            letter = chr(65 + i)
            button = tk.Button(self.keyboard_frame, text=letter, width=3, height=2,
                               bg='#3e4451', fg='#dcdcdc', activebackground='#61afef', activeforeground='#282c34',
                               command=lambda l=letter: self.make_guess(l.lower()))
            button.grid(row=i // 9, column=i % 9, padx=2, pady=2)
            self.buttons[letter] = button

    def update_display(self):
        # Update display based on game state
        hangman_stage = self.hangman_stages[min(6, 7 - self.chances)]
        self.hangman_label.config(text=hangman_stage)

        current_word = ' '.join(self.dash_string_list)
        self.word_label.config(text=f"{current_word}")

        self.chances_label.config(text=f"Remaining chances: {self.chances}")

        if "_" not in self.dash_string_list:
            self.message_label.config(text="Congratulations! You've guessed the word!")
            self.disable_buttons()
        elif self.chances <= 0:
            self.message_label.config(text=f"Game over! The word was: {self.random_word_string}")
            self.disable_buttons()

    def make_guess(self, letter):
        # Process user guess
        if letter in self.user_string_list:
            self.message_label.config(text="You already guessed that letter!")
            return

        self.user_string_list.append(letter)
        self.buttons[letter.upper()].config(state=tk.DISABLED)

        if letter in self.random_word_list:
            for index, char in enumerate(self.random_word_list):
                if char == letter:
                    self.dash_string_list[index] = letter
            self.message_label.config(text="Good guess!")
        else:
            self.chances -= 1
            self.message_label.config(text="Wrong guess!")

        self.update_display()

    def disable_buttons(self):
        for button in self.buttons.values():
            button.config(state=tk.DISABLED)


if _name_ == "_main_":
    root = tk.Tk()
    game = HangmanGame(root)
    root.mainloop()

from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from pynput.keyboard import Key, Controller
import random as ran
win = Tk()
win.geometry("1000x1000")
label=Label(win, text="", font=("Courier 22 bold"))
label.pack()
frame1 = Frame(win)
frame1.pack(side=TOP)
frame2 = Frame(win)
frame2.pack(side=TOP)
frame3 = Frame(win)
frame3.pack(side=TOP)
frame4 = Frame(win)
frame4.pack(side=TOP)
frame5 = Frame(win)
frame5.pack(side=TOP)
frame6 = Frame(win)
frame6.pack(side=TOP)
def random():
    with open("wordleWords5.txt") as file:
        lines = file.readlines()
        return ran.choice(lines)
def colored(fg, bg, text):
    r, g, b = fg
    result = f"\033[38;2;{r};{g};{b}m{text}"
    r, g, b = bg
    result = f"\033[48;2;{r};{g};{b}m{result}\033[0m"
    return result
file1 = open("wordleWords5.txt", "r").read()
#guesses = 0
word1 = random()
while word1 not in file1:
  print(word1)
  word1 = random()
word = list(word1)
#print("enter word     ", end='')
def close():
  if messagebox.askokcancel("Quit?", "do you want to quit?"):
    win.destroy()
def wordle(en):
  global entry
  guesses = 0
  def change(a):
    var.set(1)
  bad = Label(win, text="")
  while guesses < 6:
    wordTemp = list(word)
    if guesses == 1:
      frameIter = frame2
    elif guesses == 2:
      frameIter = frame3
    elif guesses == 3:
      frameIter = frame4
    elif guesses == 4:
      frameIter = frame5
    elif guesses == 5:
      frameIter = frame6
    elif guesses == 0:
      frameIter = frame1
    var = IntVar()
    entry= Entry(win, width= 40)
    entry.bind("<Return>", change)
    entry.focus_set()
    entry.pack()
    button = ttk.Button(win, text="enter", command=lambda: var.set(1))
    button.pack()
    entry.wait_variable(var)
    guess1 = entry.get()
    guess = list(guess1)
    guess2 = guess
    result = ""
    if len(guess) != 5:
      bad.destroy()
      bad = Label(win, text="word must be five letters long", font=("Noto sans mono", 25), bg="#000000", fg="#ffffff")
      bad.pack(side=BOTTOM)
      entry.destroy()
      button.destroy()
    elif guess1 not in file1:
      bad.destroy()
      bad = Label(win, text="word not valid, try one that's actually a word :)", font=("Noto sans mono", 25), bg="#000000", fg="#ffffff")
      bad.pack(side=BOTTOM)
      entry.destroy()
      button.destroy()
    elif guess1 in file1:
      bad.destroy()
      bad = Label(win, text="")

      guesses += 1
      if guess1 == word1:
        #print(colored((0, 0, 0), (0, 120, 0), guess1))
        #print(f"congraulations, you guessed the word! it was {word1}")
        for g in guess:
          label = Label(frameIter, text=g, font=("Noto sans mono", 25), bg="#00ff00")
          label.pack(side=LEFT)
        label = Label(win, text="Congratulations", font=("cursive", 75), bg="#00ff00", fg="#000000")
        label.pack(side=BOTTOM)
        return False
        break
      for x in range(len(guess)):
#        print(wordTemp[x], " ", guess[x])
#        print(wordTemp)
        if guess[x] == wordTemp[x]:
#          print(guess[x], " ", wordTemp[x])
          wordTemp[x] = " "
          label = Label(frameIter, text=guess2[x], font=("Noto sans mono", 25), bg="#00ff00")
          label.pack(side=LEFT)
          result += colored((0, 0, 0), (0, 120, 0), guess[x])
        elif guess[x] in wordTemp:
#          print(guess2)
          for c in range(len(wordTemp)):
            if wordTemp[c] == guess[x]:
#              print("for ", guess2)
              wordTemp[c] = " "
#              print(wordTemp)
              break
#          print(guess2)
          label = Label(frameIter, text=guess2[x], font=("Noto sans mono", 25), bg="#ffff0f")
          label.pack(side=LEFT)

          result += colored((0, 0, 0), (180, 180, 0), guess[x])
        else:
#          print(guess2)
          label = Label(frameIter, text=guess2[x], font=("Noto sans mono", 25), bg="#000000", fg="#ffffff")
          label.pack(side=LEFT)
          result += colored((255, 255, 255), (0, 0, 0), guess[x])
      #print(result + "          ", end='')
        entry.destroy()
        button.destroy()
  label = Label(win, text=f"Oops, the word was {word1}", font=("cursive mono", 25), bg="#000000", fg="#ffffff")
  label.pack(side=BOTTOM)
  #print(f"Oops, the word was {word1}")
def display_text():
  global entry
  string= entry.get()
  label.configure(text=string, font=("cursive", 25), bg="#00ff00")
wordle(None)
win.mainloop()

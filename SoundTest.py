from cs101audio import *
import numpy as np
import random

Notes = []
notesSounds = []
noteStringsLetters = ["C","D","E","F","G","A","B"]
noteStringsNumbers = np.arange(0, 9).tolist()

for x in range(9):
    for y in range(7):
        notesSounds.append(generate_music_note(noteStringsLetters[y]+str(noteStringsNumbers[x]),4,"Square"))

class Note:
  def __init__(self, note, letter, octave):
      self.Sound = note
      self.Octave = octave
      if (letter == "C"): self.Letter = 0
      if (letter == "D"): self.Letter = 1
      if (letter == "E"): self.Letter = 2
      if (letter == "F"): self.Letter = 3
      if (letter == "G"): self.Letter = 4
      if (letter == "A"): self.Letter = 5
      if (letter == "B"): self.Letter = 6

count = 0
for note in range(9):
    for note2 in range(7):       
        Notes.append(Note(notesSounds[count],noteStringsLetters[note2],noteStringsNumbers[note]))
        count += 1

blank = Note(notesSounds[0],noteStringsLetters[0],noteStringsNumbers[0])
for scramble in range(63):
    blank = Notes[scramble]
    randIndex = random.randint(0,62)
    Notes[scramble] = Notes[randIndex]
    Notes[randIndex] = blank

for x in range(63):
    print(x)
    print("Random "+ str(Notes[x].Octave),str(Notes[x].Letter))
    Notes[x].Sound.play()

for x in range (len(Notes)):
    for y in range (len(Notes)-1):
        if Notes[y].Octave > Notes[y+1].Octave:
            blank = Notes[y+1]
            Notes[y+1] = Notes[y]
            Notes[y] = blank

        elif Notes[y].Letter > Notes[y+1].Letter:
            blank = Notes[y+1]
            Notes[y+1] = Notes[y]
            Notes[y] = blank
        Notes[y].Sound.play()

for x in range(63):
    print(x)
    print(Notes[x].Octave,Notes[x].Letter)
    Notes[x].Sound.play()
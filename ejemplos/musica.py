from musicpy import *

guitar = (C('CM7', 3, 1/4, 1/8)^2 |
          C('G7sus', 2, 1/4, 1/8)^2 |
          C('A7sus', 2, 1/4, 1/8)^2 |
          C('Em7', 2, 1/4, 1/8)^2 | 
          C('FM7', 2, 1/4, 1/8)^2 |
          C('CM7', 3, 1/4, 1/8)@1 |
          C('AbM7', 2, 1/4, 1/8)^2 |
          C('G7sus', 2, 1/4, 1/8)^2) * 2

play(guitar, bpm=100, instrument=25)
play((get_chord_by_interval('D#4', [5,7,10,7,5], 1/2, 1/8)*3 + get_chord_by_interval('F4', [1,0,-4], 1/2, 1/8)) * 3, 150)

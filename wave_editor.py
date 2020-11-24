#################################################################
# FILE : wave_editor.py
# EXERCISE : intro2cs2 ex6 2020
# DESCRIPTION:
# WEB PAGES WE USED:
# NOTES: -
#################################################################

import math

A_FREQUENCY = 440
B_FREQUENCY = 494
C_FREQUENCY = 523
D_FREQUENCY = 587
E_FREQUENCY = 659
F_FREQUENCY = 698
G_FREQUENCY = 784
Q_FREQUENCY = 0
MAX_VOLUME = 32767
SAMPLE_RATE_COMPOSITION = 2000
TIME_SAMPLE = 16


def read_input_file(file):
    comp_file = open(file, "r")
    input_str = comp_file.readlines()
    print(input_str)
    return input_str


def calc_sample_value(sample_rate: int, frequency: int, sample_index: int) -> int:
    samples_per_cycle = sample_rate/frequency
    sample = MAX_VOLUME*math.sin(math.pi*2*(sample_index/samples_per_cycle))
    return int(sample)


def create_one_sample(note: int, time: int) -> list:
    note_list = []
    for sample in range(int((time/TIME_SAMPLE) * SAMPLE_RATE_COMPOSITION)):
        sample_value = calc_sample_value(SAMPLE_RATE_COMPOSITION, note, sample)
        note_list.append([sample_value, sample_value])
    print(len(note_list))
    return note_list

def create_tune(sample_list):
    tune_list = []
    for sample in sample_list:
        tune_list.extend(create_one_sample(sample[0], sample[1]))
    print(len(tune_list))
    return tune_list

"""print(create_one_sample(F_FREQUENCY,16))
print(create_tune([[587,1],[784,1]]))"""

read_input_file("Composition Samples\sample1.txt")



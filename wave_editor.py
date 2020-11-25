#################################################################
# FILE : wave_editor.py
# EXERCISE : intro2cs2 ex6 2020
# DESCRIPTION:
# WEB PAGES WE USED:
# NOTES: -
#################################################################
import math
import wave_helper as helper
import os

# main menu Constants:
EDIT_FILE = '1'
COMPOSE_FILE = '2'
EXIT_PROGRAM = '3'
# edit menu Constants:
FLIP = '1'
NEGATE = '2'
SPEED_UP = '3'
SPEED_DOWN = '4'
VOLUME_UP = '5'
VOLUME_DOWN = '6'
LOW_PASS_FILTER = '7'
END_MENU = '8'

# create tune constants

A_FREQUENCY = 440
B_FREQUENCY = 494
C_FREQUENCY = 523
D_FREQUENCY = 587
E_FREQUENCY = 659
F_FREQUENCY = 698
G_FREQUENCY = 784
Q_FREQUENCY = 0
MAX_VOLUME = 32767
MIN_VOLUME = -32768
SAMPLE_RATE_COMPOSITION = 2000
TIME_SAMPLE = 16
TUNE_FREQ_DICT = {"A": A_FREQUENCY, "B": B_FREQUENCY, "C": C_FREQUENCY, "D": D_FREQUENCY,
             "E": E_FREQUENCY, "F": F_FREQUENCY, "G": G_FREQUENCY, "Q": Q_FREQUENCY}

from typing import List,Tuple


def flip_data(wav_file_data: List[int]):
    """
    this function inverts the order of the list items.
    :param wav_file_data: only the list of pairs inside the wav_file
     (without the sample rate)
    """
    print("Data Flipped!")
    return wav_file_data[::-1]
def negate_data(wav_file_data: List[int]):
    """
    this function multiply all the pairs in the list with (-1) except the
    numbers that the multiplication result will get a value that is bigger
    than MAX_VOLUME.
    :param wav_file_data: only the list of pairs inside the wav_file
     (without the sample rate)
    """
    for pair_index, pair in enumerate(wav_file_data):
        for value_index, value in enumerate(pair):
            if -1*value >= MAX_VOLUME:
                wav_file_data[pair_index][value_index] = MAX_VOLUME
            else:
                wav_file_data[pair_index][value_index] = -1*value
    print("Data Negated!")
    return wav_file_data
def speed_up_data(wav_file_data: List[int]):
    """
    this function returns a list that contains
     only the list members that are placed in even indexes.
    :param wav_file_data: only the list of pairs inside the wav_file
    """
    print("Raised Data speed!")
    return [wav_file_data[even] for even in range(0,len(wav_file_data),2)]
def pairs_average(wav_file_data: List[int],insert_index:int):
    """
    this function calculates the average pair of the pair in insert_index+1
    and the pair in index. average pair of (1,2)(3,2) is (2,2).
    :param wav_file_data: only the list of pairs inside the wav_file
    :param insert_index: the index of the first pair.
    """
    average_pair = []
    for value_in_pair in range(2):
        average_pair.append(int((wav_file_data[insert_index+1][value_in_pair]
                                 + wav_file_data[insert_index][value_in_pair])
                                / 2))
    return average_pair
def speed_down_data(wav_file_data: List[int]):
    """
    this function inserts an average pair between any 2 pairs on the
    wav_file_data list.
    :param wav_file_data: only the list of pairs inside the wav_file
    :return:
    """
    lowered_data = wav_file_data[:]
    # an index that grows in 1 on every insertion. this index helps to count
    # where will be the next insertion
    # (because of the fact that lowered_data always grows).
    insertion_number = 1
    for insert_index in range(0, len(wav_file_data)-1):
        lowered_data.insert(insert_index + insertion_number,
                            pairs_average(wav_file_data,insert_index))
        insertion_number += 1

    print("Lowered Data speed!")
    return lowered_data
def volume_up_data(wav_file_data: List[int]):
    """
    this function multiplies all the values on the wav_file_data list and
    returns the multiplied list. if the multiplied value is bigger than
    MAX_VOLUME or lower than MIN_VOLUME the function assigns them instead of
    the multiplied value.
    :param wav_file_data: only the list of pairs inside the wav_file
    """
    for pair_index, pair in enumerate(wav_file_data):
        for value_index, value in enumerate(pair):
            if int(value*1.2)>=MAX_VOLUME:
                wav_file_data[pair_index][value_index] = MAX_VOLUME
            elif int(value*1.2)<=MIN_VOLUME:
                wav_file_data[pair_index][value_index] = MIN_VOLUME
            else:
                wav_file_data[pair_index][value_index] = int(value*1.2)

    print("Data Volume Raised")
    return wav_file_data
def volume_down_data(wav_file_data: List[int]):
    """
        this function divides all the values on the wav_file_data list and
        returns the divided list.
        :param wav_file_data: only the list of pairs inside the wav_file
        """
    for pair_index, pair in enumerate(wav_file_data):
        for value_index, value in enumerate(pair):
            wav_file_data[pair_index][value_index] = int(value / 1.2)

    print("Data Volume Raised")
    return wav_file_data

def trio_average(wav_file_data: List[int],index:int):
    """
    this function calculates the average of three pairs
    in indexes: index, index-1,index-2 on wav_file_data list.
    :param wav_file_data: only the list of pairs inside the wav_file
    :param index: the biggest index from the indexes of the 3 pairs.
    :return: a pair that represent the average of the 3 pairs.
    """
    trio_average = []
    sum = 0
    for place_in_pair in range(2):
        for place_from_index in range(3):
            sum += wav_file_data[index - place_from_index][place_in_pair]
        trio_average.append(int(sum / 3))
        sum = 0
    return trio_average
def low_pass_average(wav_file_data: List[int],index:int):
    """
    this function return the value that need to be assigned in the index
    after activating a low pass filter on the file.
    :param wav_file_data: only the list of pairs inside the wav_file
    :param index: the index of the pair that its value after
    low_pass_filter need to be calculated
    """
    average = []
    if index == 0:
        average = pairs_average(wav_file_data,index)
    elif index == len(wav_file_data)-1:
        average = pairs_average(wav_file_data,index-1)
    else:
        average = trio_average(wav_file_data,index+1)
    return average
def low_pass_filter_data(wav_file_data: List[int]):
    """
    this function creates a new list that contains the low pass filter
     values of wav_file_data list.
    :param wav_file_data: only the list of pairs inside the wav_file
    """
    low_pass_data = []
    if len(wav_file_data)<=1:
        return wav_file_data
    else:
        for index in range(0, len(wav_file_data)):
            low_pass_data.append(low_pass_average(wav_file_data, index))

    print("Low pass filter Activated!")
    return low_pass_data

def edit_wav(wav_file_data: List[int]):
    """
    this function runs until the user chooses to go to the end menu (by
    entering END_MENU in the edit menu). on every iteration, the function
    call the chosen edit function.
    :param wav_file_data: a wav file data to edit.
    :return: the edited file.
    """
    while True:
        usr_input_edit = edit_menu()
        if usr_input_edit == FLIP:
            wav_file_data[1][:] = flip_data(wav_file_data[1])
        elif usr_input_edit == NEGATE:
            wav_file_data[1][:] = negate_data(wav_file_data[1])
        elif usr_input_edit == SPEED_UP:
            wav_file_data[1][:] = speed_up_data(wav_file_data[1])
        elif usr_input_edit == SPEED_DOWN:
            wav_file_data[1][:] = speed_down_data(wav_file_data[1])
        elif usr_input_edit == VOLUME_UP:
            wav_file_data[1][:] = volume_up_data(wav_file_data[1])
        elif usr_input_edit == VOLUME_DOWN:
            wav_file_data[1][:] = volume_down_data(wav_file_data[1])
        elif usr_input_edit == LOW_PASS_FILTER:
            wav_file_data[1][:] = low_pass_filter_data(wav_file_data[1])
        else:
            # if input is END_MENU:
            break
    return wav_file_data
def get_input_in_menu(good_answers:Tuple[str],msg:str):
    """
    this function is a general menu, that gets the message to show the user
    and the corrects answers the user can enter (0 can't be in the values).
    the function runs until the user enters a good answer.
    :return: the good answer the user entered
    """
    usr_input = input(msg)
    while not (usr_input in good_answers):
        print("You entered a wrong input. please follow the instructions!")
        usr_input = input(msg)
    return usr_input
def main_menu():
    """
    this function uses the general menu function with the message of the main
    menu.
    """
    good_answers_set = (EDIT_FILE, COMPOSE_FILE, EXIT_PROGRAM)
    msg = f"What would you like to do? " \
          f"(enter {EDIT_FILE}/{COMPOSE_FILE}/{EXIT_PROGRAM})\n"\
          "1.Edit wav file.\n" \
          "2.Composite a new melody in wav file format.\n" \
          "3.Exit Program\n"
    return get_input_in_menu(good_answers_set,msg)
def get_edit_filename_and_data():
    """
    this function asks the filename from the user (until he enters an existing
    file name) and return the data of it.
    :return:
    """
    msg = "What is the name of the file you want to edit?"
    filename_input = input(msg)
    file_data = helper.load_wave(filename_input)
    while file_data == -1:
        print("You entered a wrong file name.")
        filename_input = input(msg)
        file_data = helper.load_wave(filename_input)
    return file_data
def edit_menu():
    """
    this function uses the general menu function with the message of the edit
    menu.
    """
    good_answers_set = (FLIP,NEGATE,SPEED_UP,SPEED_DOWN,VOLUME_UP,VOLUME_DOWN,
                        LOW_PASS_FILTER,END_MENU)
    msg = "What would you like to do?" \
          f"(enter {FLIP}/{NEGATE}/{SPEED_UP}/{SPEED_DOWN}/{VOLUME_UP}" \
          f"/{VOLUME_DOWN}/{LOW_PASS_FILTER}/{END_MENU})\n" \
          "1.Flip the data.\n" \
          "2.Negate the sound.\n" \
          "3.Speed up the audio.\n" \
          "4.Speed down the audio\n" \
          "5.Turn the volume up.\n" \
          "6.Turn the volume down.\n" \
          "7.Activate low pass filter.\n" \
          "8.Go to end menu.\n"
    return get_input_in_menu(good_answers_set,msg)
def output_filename_valid(filename):
    #TODO: validate the name?
    pass
def end_menu_save_file(wav_file_data: List[int]):
    """
        this function asks the filename from the user (until he enters an existing
        file name) and return the data of it.
        :return:
        """
    msg = "enter the name of the file you want to save the data in?"
    filename_input = input(msg)
    good_name = helper.save_wave(wav_file_data[0],wav_file_data[1],
                                 filename_input)
    while good_name == -1:
        print("you entered a wrong file name!")
        filename_input = input(msg)
        if output_filename_valid(filename_input):
            good_name = helper.save_wave(wav_file_data[0], wav_file_data[1],
                                         filename_input)
def get_compose_filename():
    """
    this function asks the compose filename from the user
     (until he enters an existing file name) and return the data of it.
    :return: the legal file name.
    """
    filename_input = input("What is the name of the composition file?")
    while not os.path.isfile(filename_input):
        print("You entered a wrong file name.")
        filename_input = input("What is the name of the composition file?")
    return filename_input
def main():
    """
    this is the main function. it runs until the user enters EXIT_PROGRAM.
    """
    while True:
        usr_input_main = main_menu()
        if usr_input_main == EDIT_FILE:
            wav_file_data = get_edit_filename_and_data()
            wav_file_data = edit_wav(wav_file_data)
            end_menu_save_file(wav_file_data)
        elif usr_input_main == COMPOSE_FILE:
            #TODO: def composite(filename)
            composited_file_data = composite(get_compose_filename())
            composited_file_data = edit_wav(composited_file_data)
            end_menu_save_file(composited_file_data)
        else:
            break

def read_input_file(file):
    comp_file = open(file, "r")
    input_str = ""
    input_list = comp_file.readlines()
    for line in input_list:
        input_str += str(line)
    return input_str


def split_str_to_list(input_string):
    allowed_char = "ABCDEFGQ"
    #input_string = input_string.strip().replace("\n", " ")
    input_list = input_string.split(" ")
    note_list = []
    for char in input_list:
        if (char in allowed_char or char.isnumeric()) and char != "":
            note_list.append(char)
    tones_list = []
    pair_counter = 0
    while pair_counter < len(note_list):
        tones_list.append([note_list[pair_counter], note_list[pair_counter + 1]])
        pair_counter += 2
    return tones_list


def calc_sample_value(sample_rate: int, frequency: int, sample_index: int) -> int:
    if frequency == Q_FREQUENCY:
        return 0
    samples_per_cycle = sample_rate/frequency
    sample = MAX_VOLUME*math.sin(math.pi*2*(sample_index/samples_per_cycle))
    return int(sample)


def get_samples_number(time):
    return int((time/TIME_SAMPLE) * SAMPLE_RATE_COMPOSITION)


def create_one_sample(note: str, time: int, is_first: bool, index: int) -> list:
    note_list = []
    samples_number_needed = get_samples_number(time)
    if is_first and index != 0:
        sample_value = calc_sample_value(SAMPLE_RATE_COMPOSITION, TUNE_FREQ_DICT[note], 0)
        note_list.append([sample_value, sample_value])
    for sample in range(samples_number_needed):
        sample_value = calc_sample_value(SAMPLE_RATE_COMPOSITION, TUNE_FREQ_DICT[note], index)
        note_list.append([sample_value, sample_value])
        index += 1
    print(index)
    return note_list


def create_tune(sample_list):
    tune_list = []
    index = 0
    for sample in range(len(sample_list)):
        is_first = True
        if sample != 0 and sample_list[sample][0] == sample_list[sample - 1][0]:
            is_first = False
        tune_list.extend(create_one_sample(sample_list[sample][0], int(sample_list[sample][1]), is_first, index))
        index += get_samples_number(int(sample_list[sample][1]))
    return tune_list

if __name__ == "__main__":
    print(split_str_to_list(read_input_file("Composition Samples\sample6_over16.txt")))
    print(split_str_to_list(read_input_file("Composition Samples\sample4_spaces.txt")))

if __name__ == "__main__":
    main()


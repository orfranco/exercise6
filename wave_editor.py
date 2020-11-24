#################################################################
# FILE : wave_editor.py
# EXERCISE : intro2cs2 ex6 2020
# DESCRIPTION:
# WEB PAGES WE USED:
# NOTES: -
#################################################################
import math
import wave_helper as helper


# main menu Constants:
EDIT_FILE = '1'
COMPOSITE_FILE = '2'
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

# create tune constans

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



def get_input_in_menu(good_answers,msg):
    """
    this function is a general menu, that gets the message to show the user
    and the corrects answers the user can enter (0 can't be in the values).
    the function runs until the user enters a good answer.
    :return: the good answer the user entered
    """
    usr_input = 0
    while not (usr_input in good_answers):
        usr_input = input(msg)
    return usr_input
def main_menu():
    """
    this function uses the general menu function with the message of the main
    menu.
    """
    good_answers_set = (EDIT_FILE, COMPOSITE_FILE, EXIT_PROGRAM)
    msg = f"What would you like to do? " \
          f"(enter {EDIT_FILE}/{COMPOSITE_FILE}/{EXIT_PROGRAM})\n"\
          "1.Edit wav file.\n" \
          "2.Composite a new melody in wav file format.\n" \
          "3.Exit Program\n"
    return get_input_in_menu(good_answers_set,msg)
def get_filename_and_data():
    """
    this function asks the filename from the user (until he enters an existing
    file name) and return the data of it.
    :return:
    """
    file_data = -1
    while file_data == -1:
        filename_input = input("What is the name of the file"
                               " you want to edit?")
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
          f"(enter 1/2/3/4/5/6/7/8)\n" \
          "1.Flip the data.\n" \
          "2.Negate the sound.\n" \
          "3.Speed up the audio.\n" \
          "4.Speed down the audio\n" \
          "5.Turn the volume up.\n" \
          "6.Turn the volume down.\n" \
          "7.Activate low pass filter.\n" \
          "8.Go to end menu.\n"
    return get_input_in_menu(good_answers_set,msg)

def flip_data(wav_file_data):
    pass
def negate_data(wav_file_data):
    pass
def speed_up_data(wav_file_data):
    pass
def speed_down_data(wav_file_data):
    pass
def volume_up_data(wav_file_data):
    pass
def volume_down_data(wav_file_data):
    pass
def low_pass_filter_data(wav_file_data):
    pass

def edit_wav(wav_file_data):
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
            wav_file_data = flip_data(wav_file_data)
        elif usr_input_edit == NEGATE:
            wav_file_data = negate_data(wav_file_data)
        elif usr_input_edit == SPEED_UP:
            wav_file_data = speed_up_data(wav_file_data)
        elif usr_input_edit == SPEED_DOWN:
            wav_file_data = speed_down_data(wav_file_data)
        elif usr_input_edit == VOLUME_UP:
            wav_file_data = volume_up_data(wav_file_data)
        elif usr_input_edit == VOLUME_DOWN:
            wav_file_data = volume_down_data(wav_file_data)
        elif usr_input_edit == LOW_PASS_FILTER:
            wav_file_data = low_pass_filter_data(wav_file_data)
        else:
            # if input is END_MENU:
            break
    return wav_file_data

def end_menu():
    print("endmenu")
    return ""

def save_file(wav_file_data,file_path):
    print("save_file")
    pass

def main():
    usr_input_main = main_menu()
    if usr_input_main == EDIT_FILE:
        wav_file_data = get_filename_and_data()
        wav_file_data = edit_wav(wav_file_data)
        save_file(end_menu())
    if usr_input_main == COMPOSITE_FILE:
        composited_file_data = []
        save_file(composited_file_data,end_menu())

if __name__ == "__main__":
    main()
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
    return tune_list





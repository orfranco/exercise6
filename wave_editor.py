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



def get_input_in_menu(good_answers,msg):
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
def get_filename_and_data():
    """
    this function asks the filename from the user (until he enters an existing
    file name) and return the data of it.
    :return:
    """
    filename_input = input("What is the name of the file"
                           " you want to edit?")
    file_data = helper.load_wave(filename_input)
    while file_data == -1:
        print("You entered a wrong file name.")
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

def flip_data(wav_file_data):
    print("Data Flipped!")
    return wav_file_data[::-1]
def negate_data(wav_file_data):
    for pair_index, pair in enumerate(wav_file_data):
        for value_index, value in enumerate(pair):
            if -1*value >= MAX_VOLUME:
                wav_file_data[pair_index][value_index] = MAX_VOLUME
            else:
                wav_file_data[pair_index][value_index] = -1*value
    print("Data Negated!")
    return wav_file_data
def speed_up_data(wav_file_data):
    print("Raised Data speed!")
    return [wav_file_data[even] for even in range(0,len(wav_file_data),2)]
def pairs_average(wav_file_data,insert_index):
    average_pair = []
    for i in range(2):
        average_pair.append(int((wav_file_data[insert_index+1][i]
                            +wav_file_data[insert_index][i])/2))
    return average_pair
def speed_down_data(wav_file_data):
    lowered_data = wav_file_data[:]
    insertion_number = 1
    for insert_index in range(0, len(wav_file_data)-1):
        lowered_data.insert(insert_index + insertion_number,
                            pairs_average(wav_file_data,insert_index))
        insertion_number+=1

    print("Lowered Data speed!")
    return lowered_data
def volume_up_data(wav_file_data):
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
def volume_down_data(wav_file_data):
    for pair_index, pair in enumerate(wav_file_data):
        for value_index, value in enumerate(pair):
            wav_file_data[pair_index][value_index] = int(value / 1.2)

    print("Data Volume Raised")
    return wav_file_data

def trio_average(wav_file_data,index):
    trio_average = []
    sum = 0
    for place_in_pair in range(2):
        for cell_from_index in range(3):
            sum += wav_file_data[index-cell_from_index][place_in_pair]
        trio_average.append(int(sum / 3))
        sum = 0
    return trio_average
def low_pass_average(wav_file_data,index):
    average = []
    if index == 0:
        average = pairs_average(wav_file_data,index)
    elif index == len(wav_file_data)-1:
        average = pairs_average(wav_file_data,index-1)
    else:
        average = trio_average(wav_file_data,index+1)
    return average

def low_pass_filter_data(wav_file_data):
    low_pass_data = []
    for index in range(0, len(wav_file_data)):
        low_pass_data.append(low_pass_average(wav_file_data, index))

    print("Low pass filter Activated!")
    return low_pass_data

def edit_wav(wav_file_data):
    """
    this function runs until the user chooses to go to the end menu (by
    entering END_MENU in the edit menu). on every iteration, the function
    call the chosen edit function.
    :param wav_file_data: a wav file data to edit.
    :return: the edited file.
    """
    while True:
        print(wav_file_data)
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


def end_menu_save_file(wav_file_data):
    #TODO: validate the name?
    """
        this function asks the filename from the user (until he enters an existing
        file name) and return the data of it.
        :return:
        """
    filename_input = input("enter the name of the file you want to save "
                           "the data in?")
    good_name = helper.save_wave(wav_file_data[0],wav_file_data[1],
                                 filename_input)

    while good_name == -1:
        print("you entered a wrong file name!")
        filename_input = input("enter the name of the file you want to save "
                               "the data in?")
        print(wav_file_data)
        good_name = helper.save_wave(wav_file_data[0], wav_file_data[1],
                                     filename_input)



def main():
    while True:
        usr_input_main = main_menu()
        if usr_input_main == EDIT_FILE:
            wav_file_data = get_filename_and_data()
            wav_file_data = edit_wav(wav_file_data)
            end_menu_save_file(wav_file_data)
        elif usr_input_main == COMPOSE_FILE:
            #create_tune()
            composited_file_data = []
            composited_file_data = edit_wav()
            end_menu_save_file(composited_file_data)
        else:
            break
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





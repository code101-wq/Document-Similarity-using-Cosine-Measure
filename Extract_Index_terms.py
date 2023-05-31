import glob
import os
from striprtf.striprtf import rtf_to_text

commonwords = ['a', 'the', 'is', 'an', 'to', "\n", ' ', "The", "as", "it", "I"]
Common_words = []
file_directory = " "
doc_dict = {}
all_word_freq = {}  # Contain the count of words across all the input text files
wordbuffer = []  # Temporary storage for words which have just been received
wl = []
w = []

def start():
    print("Welcome to the document similarity Program\n\n")

    print("Enter the directory of the different files, if no directory enter a space character:\n ")
    # include the directory to the set of files
    file_directory = input()

    # ask for common words to be removed from the program else continue with the words in common words
    print("You are required to enter the list of common words which you will want to be removed from the similarity program \n")
    print("Enter a common word: ")
    Cw = input()
    while (Cw != " "):
        Common_words.append(Cw)
        print("Enter another common word or press the space bar to continue: ")
        Cw = input()

    print(Common_words)
    extract_words(file_directory, Common_words)

def read_files(path):  #  Read the files in the specified path
    if path == " ":
        os.chdir("/Users/mrfomfoh/Documents/Lobga/Learn/School/Third Year Second Semester/CSC498/My Project/Program/untitled folder")
    else:
        os.chdir(path)
    my_files = glob.glob("*.rtf")
    print(my_files)
    # write the names of the files to a file
    w_files = open('file_names', 'a')
    w_files.write(str(my_files))
    return my_files


def extract_words(a, b):    # a refers to the link to the different documents and b refers to the list of common words
    f = read_files(a)
    word_list = []  # Contains all distinct words in the different files in one list
    index_term = []  # Contains words and their repititions accross all the files
    word_list_c = []  # test
    word_list_count = [] # contains the words in the word list and their counts
    for l in f:
        p = open(l, 'r')
        plaintext = rtf_to_text(p.read())
        plaintext = plaintext.lower()
        wordbuffer = plaintext.split(" ")

        # remove common words
        if b == []:
            remove_common_words(wordbuffer)
        else:
            remove_common_words(b)

        # loop and store words and repetitions across all files in w_list
        for x in wordbuffer:
            word_list.append(x)

        # loop and store distinct words across all files in word_list
        for x in wordbuffer:
            if x not in index_term:
                index_term.append(x)

        # run count_words and save the appended list of dictionaries to lists
        lists = count_words(wordbuffer)
        print(lists)
        # end for loop

    # Write index terms into output2
    output2 = open("Output2", "a")
    output2.write(str(index_term))

    # count the occurence of the index terms accross all the documents
    word_list_c = count_words(word_list)
    word_list_count = word_list_c[-1]

    # Write the frequency of the index terms into a file
    output3 = open("Output3", "a")
    output3.write(str(word_list_count))

    print(lists)  # list of different files of words and their counts

    # store the lists and their file names in a file
    output = open("Output1", "a")
    i = 0
    for filename in f:
        output.write(str(filename + str(lists[i]) + "\n"))
        i = i + 1
    w = lists
    print("\n\n", w)

def remove_common_words(wb):
    for x in wb:
        if x in commonwords:
            wb.remove(x)


def count_words(wbf):
    doc_dict = {}
    doc_dict.clear()

    print("\n")

    for y in wbf:
        # count of words in the word buffer
        cnt = wbf.count(y)

        # create a dictionary which has y as its key(the string) and cnt as the data
        doc_dict[y] = cnt
        cnt = 0

    print(doc_dict)
    wl.append(doc_dict)
    return wl


start()

import datetime

from config import database
from key_words import keywords, wordsn, wordsd, wordsde

def read_file(file):
    with open(file, mode='r') as file:
        contents = file.read()
    return contents

def write_file(file, contents):
    with open(file, mode='w') as file:
        file.write(contents)



def checker(text):
    print(database.get_all_keywords())
    for i in database.get_all_keywords():
        #print(i[1])
        if i[1] in text.lower():
            print(i[1])
            return True

    return False
def read_file_s(filename):
    with open(filename, mode='r', encoding='UTF8') as file:
        contents = file.read()
    return contents.split()

def timee(user_id):
    dat = datetime.datetime.now().hour
    o = database.select_ints(user_id, "time")

    if  (int(o.split("-")[0]) > int(dat) and int(dat) < int(o.split("-")[0])):
        print("f")
        return False
    return True

from main import database
from key_words import wordsd, wordsn
import datetime
def choose_category(message):
    list = []
    dictkats = {"neiro": database.get_keywords("airu"),
                "design": database.get_keywords("designru")}
    if "помогу" in message.lower() or "#помогу" in message.lower() or "#реклама" in message.lower():
        return False

    for i in dictkats:
        for word in dictkats[i]:
            if word in message.lower():
                list.append(i)
    return list



def userkats(user_id, kats):
    dat = datetime.datetime.now().hour
    o = database.select_ints(user_id, "time")
    if  (int(o.split("-")[0]) >= int(dat) and int(dat) <= int(o.split("-")[0])):
        print("f")
        return
    print(database.select_kats(user_id))
    for i in kats:
        if i in database.select_kats(user_id):
            return True



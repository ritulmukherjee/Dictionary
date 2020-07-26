import mysql.connector
from difflib import get_close_matches

con = mysql.connector.connect(
user = "ardit700_student",
password = "ardit700_student",
host = "108.167.140.122",
database = "ardit700_pm1database"
)

cursor = con.cursor()


def fun(word):
    cursor.execute("SELECT Expression FROM Dictionary")
    results = cursor.fetchall()
    results = [i[0] for i in results]

    if word.lower() in results or word.title() in results or word.upper() in results:
        cursor.execute("SELECT Definition FROM Dictionary where Expression= '%s'" %word)
        return cursor.fetchall()
    elif len(get_close_matches(word,results))>0:
        yn= input( f" Did you mean {get_close_matches(word,results)[0]} instead? Press Y for yes and N for no: ") 
        if(yn=='Y'):
            cursor.execute("Select Definition From Dictionary where Expression = '%s'" % get_close_matches(word,results)[0])
            return cursor.fetchall()
        elif(yn=='N'):
            return("Sorry. Word not found")
        else:
            return("You are only supposed to press Y or N")

    else:
        return("No word found!")

w = input("Enter a word: ")
output= fun(w)
if type(output) == list:
    for item in output:
        print(item[0])
else:
    print(output)

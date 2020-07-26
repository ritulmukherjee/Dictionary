import json
from difflib import get_close_matches
data=json.load(open("data.json"))

def mean(x):
    x=x.lower()
    if x in data:
        return data[x]
    elif x.title() in data:
        return data[w]
    elif x.upper() in data:
        return data[w]
    elif len(get_close_matches(x,data.keys()))>0:
        yn= input( " Did you mean %s? Press Y for yes and N for no.: "  % get_close_matches(x,data.keys())[0] )
        if(yn=='Y'):
            return data[get_close_matches(x,data.keys())[0]]
        else:
            return("Sorry. Word not found")
    else: 
        return("Sorry. Word not found")

w = input("Enter a word: ")
output= (mean(w))
if type(output)==list:
    for item in output:
        print(item)
else:
    print(output)
    

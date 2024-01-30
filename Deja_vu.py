'''
You aren't paying attention and you accidentally type a bunch of random letters on your keyboard. You want to know if you ever typed the same letter twice, or if they are all unique letters.
Task: 
If you are given a string of random letters, your task is to evaluate whether any letter is repeated in the string or if you only hit unique keys while you typing.
Input Format: 
A string of random letter characters (no numbers or other buttons were pressed).
Output Format: 
A string that says 'Deja Vu' if any letter is repeated in the input string, or a string that says 'Unique' if there are no repeats.
Sample Input: 
aaaaaaaghhhhjkll
Sample Output: 
Deja Vu
'''
#first libraries!
import random
#define for com generate like a kasko
a1 = ("qwertyuiopasdfghjklzxcvbnm")
def kasgo(a1):
    jagh = random.choice(a1)
    return  str(jagh)
b1 = []
b1 = kasgo(a1)
#ask about opinion!
toti = str(input("ascci only:"))
#minaring                  
set_list1 = set(b1[0])
set_list2 = set(toti[0])
c_ph = len(set_list1.intersection(set_list2))

#anti coagulan test!!!
if c_ph > 0:
    print("DEJA_VU!")
else:
    print("you are very unglobally!")





    
    
    
    
    
        
        
    

import json
import os
name=input("Enter Name: ").upper()
print("=====================================")
print(f"Hi! {name} let's check your vocabulary")
print("=====================================")
with open('data.json') as f: 
	data = json.load(f) 
for key, value in data.items():
         if key == 'question':
             l=(data.get('question'))
             user_ans=[]

         elif key == 'answer':
             correct_ans=(data.get('answer'))

##correct_ans=['b','a','b','b','a','a','b']
n=input("enter 1 to play quiz\nenter 0 to quit\nEnter : ")
print()
count=0
st='abcd'
try:
    if n=='1':
        for i in range (len(l)):
            print(l[i])
            ans=input("\nEnter your answer fom a/b/c/d or q to quit: ").lower()
            print()
            if ans in st:
                user_ans.append(ans)
                
            elif ans=='q':
                break
            else:
                print("Enter from abcd")
                ans=input("Choose correctly: ")
                if ans not in st:
                    break
                else:
                    user_ans.append(ans)
                
                
    elif n=='0':
        print("------Try if you have good vocabulary------")
        os._exit(0)
                
except:
    print("give correct input :")

finally:
    print(name,'answers are ',user_ans)
    print('correct answers are ',correct_ans)
    for i in range (len(user_ans)):
        if user_ans[i]==correct_ans[i]:
            count=count+1
    success_rate=count/(len(correct_ans))
    print(f'{name} you attempted {len(user_ans)} out of {len(l)} and {count} is correct')
    print(f'your result is {success_rate*100:.2f}%')
    #print("BETTER LUCK NEXT TIME!!!")
    os._exit(0)              
                    
            




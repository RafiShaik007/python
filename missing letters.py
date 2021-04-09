import random
while True :
    user_name = input("Enter your name : ")
    if user_name.isalpha():
        while True :
            n = input("Enter no. of questions you want to answer :")
            if n.isnumeric():
                count=0
                with open("english words.txt", "r") as f: 
                    text = f.read() 
                    words = list(map(str,text.split()))
                    random_words = random.sample(words,k=int(n))
                for i in random_words :
                    a = list(i)
                    t = random.sample(a,k=2)

                    b = i.replace(t[0],"_")
                    c = b.replace(t[1],"_")
                    print(c)
                    user = input("Enter answer : ").lower()
                    if user == i:
                        count+=1

                        print ("correct")
                    else :
                        print("Incorrect")
                        print("Correct answer is",i)
                print("Hey",user_name,"you scored",count,"out of",n)
                break
            else :
                print("Please enter no.of questions in integers")
        break
    else :
        print ("please enter your name ")












##a=[]
##for i in range(10):
##    a.append(i)
##    if i%2==0:
##        a.append(a[-1])
##    else:
##        i%3==0
##        a.remove(a[-2])
##print(a)


##a=[1,2,3,4,5]
##a.extend([6,7])
##print(a[::-1])



##def fun(n):
##    if n>0:
##        value=(n*2)-1
##        return value+fun(n-1)
##    else:
##        return 0
##print(str(fun(5)))



##C={"a","b","c","b","d"}
##v=C.pop()
##print(v)
##print(C)
##
##d
##{'c', 'a', 'b'}

##
##a=set()
##b=set()
##a={1,2,3,5,6,7,9,10}
##b={1,3,5,7,9,11,13}
##if  len(a) and len(b):
##    a.intersection_update(b)
##else:
##    b.intersection_update(a)
##print(b)
##
##{1, 3, 5, 7, 9, 11, 13}

##a=4
##b="8.678"
##c=-5
##str1="{0:0.4f}{2}{1}".format(a,b,c)
##print(str1)
##4.0000-58.678

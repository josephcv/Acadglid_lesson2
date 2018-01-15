
# coding: utf-8

# In[21]:


# Assignment Problem 2.1

ip = input("Input numbers sequence separated by commas:")
l=ip.split(',')
print(l)
print(type(l))


# In[11]:


# Assigment Problem 2.2

var = input("Enter pyramid height?")
a=int(var)
for i in range(1,a):
    print ('')
    for j in range(i):
            print('*',end='')
            j+=1      
for x in range((a-2),0,-1):
    print('')
    for y in range(x):
        print('*',end='')
        y+=1


# In[10]:


# Assignment Problem 2.3

l=input("Input a word: ")
a=l[::-1]
print("Reverse of", l, "is:", a)


# In[6]:


# Assignment Problem 2.4
# Solution 1: Rudimentary version

s="WE, THE PEOPLE OF INDIA, having solemnly resolved to constitute India into a SOVEREIGN, SOCIALIST, SECULAR, DEMOCRATIC REPUBLIC and to secure to all its citizens"
list=s.split()
line1=list[0:5]
line2=list[5:14]
line2=line2+['!']
line3=list[14:18]
line4=list[18:]
l1=" ".join(line1)
l2=" ".join(line2)
l3=" ".join(line3)
l4=" ".join(line4)
print(l1)
print(' \t',end='')
print(l2)
print(' \t \t',end='')
print(l3)
print(' \t \t',end='')
print(l4)



# In[9]:


# Assignment Problem 2.4
# Solutions 2: Code based formatting where new line is inserted based on case change
s= "WE, THE PEOPLE OF INDIA, having solemnly resolved to constitute India into a SOVEREIGN, SOCIALIST, SECULAR, DEMOCRATIC REPUBLIC and to secure to all its citizens"
a=len(s)
uc_nl=1
for i in range(0,a):
    b=s[i] 
    if b.isspace() is True:
        print(b,end='')    
    elif b.isupper() is True:
        if b=='I':
            print(b,end='')
        else:
            if uc_nl ==1:
                print ('')
                print (b,end='')
                uc_nl=0
                cnl=1
            else:   
                print(b,end='')      
    elif b.islower() is True:
        if cnl == 1:
            print('')
            print(b,end='')
            cnl=0
            uc_nl=1
        else:
            print(b,end='')
    else:
        print(b,end='')
    


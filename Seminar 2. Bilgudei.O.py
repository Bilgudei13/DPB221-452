#!/usr/bin/env python
# coding: utf-8

# In[2]:


#1
def Palindrome(s):
    s = s.lower()
    l = len(s)
    if l<2:
        return True
    elif s[0] == s[l-1]:
        return Palindrome(s[1:l-1])
    
    else:
        return False
s="56"
ans=Palindrome(s)

if ans:
    print("Yes")
else:
    print("No") 


# In[3]:


#2
import collections

my_word = "ULaaNbaAtar"
c = collections.Counter("upper" if x.isupper() else "lower" if x.islower() else "" for x in my_word)
print(c)


# In[4]:


#3
def multiple(a):
    b=1
    for x in a:
        b=b*x
    return b
list=[3,4,5,4,3,6,5,1]
print(multiple(list))


# In[5]:


#4
def factorial(x):
    a=1
    while x>0:
        a=x*a
        x=x-1
        return a
x=int(input())
print(factorial(x)) 


# In[7]:


#5
def my_function(x):
    return x[::-1]

mytxt = my_function("I wonder how this text looks like backwards")
print(mytxt) 


# In[8]:


#6
numbers=[2,3,4,5,6,7]
sum=sum(numbers)
print(sum)


# In[9]:


#7
test_list=[1,3,5,6,3,5,6,1]
print("The original list is: " + str(test_list))
res=[]
[res.append(x) for x in test_list if x not in res]

print("The list after removing duplicates:" + str(res))


# In[11]:


#8
def maximum(a,b,c):
    if (a>=b) and (a >=c):
        largest=a
    elif (b >=a ) and (b>=c):
        largest = b
    else:
        largest = c
    return largest
a=int(input())
b=int(input())
c=int(input())
print("maximum of three numbers", maximum(a, b, c,))
    


# In[ ]:





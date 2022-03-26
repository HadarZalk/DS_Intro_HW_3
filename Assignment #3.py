#!/usr/bin/env python
# coding: utf-8

# In[277]:


def count_rows(file):
    file = 'ex3_text.txt'
    with open(file) as f:
        x = len(f.readlines())
        return(x)


# In[473]:


def read_line(n, file):
    try:
        f = open(file)           
    except FileNotFoundError:
        print("Wrong file or file path")
    try: 
        n = int(n)
        f = open(file)
        row = f.readlines()
        Rcount = 0
        with open(file,'r') as f:
            for line in f:
                Rcount +=1
            if n<Rcount: 
                print (row[n-1])
            else:
                print(f'line {n} does not exsit')

    except ValueError:  
        print("invalid value")
    
        

        
    


# In[559]:


#main 
n= input('enter row numbers to present: ')
file = input('enter file directory: ')
read_line(n, file)


# In[616]:


def longest_words(file): 
    try:
        f = open(file)           
    except FileNotFoundError:
        print("Wrong file or file path")
    f = open(file)
    f = f.read()
    f =  f.replace('.', ' ')
    f =  f.replace('-', ' ')
    f =  f.replace(',', ' ')
    words = f.split()
    words= sorted(words, key=len,reverse = True)
    print(words[0:5])


        


# In[617]:


#main 
file = input('enter file directory: ')
longest_words(file)


# In[ ]:





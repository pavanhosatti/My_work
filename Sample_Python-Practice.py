#!/usr/bin/env python
# coding: utf-8

# In[1]:


print('p')


# In[2]:


1+2


# In[3]:


2+5


# In[5]:


5+8


# In[1]:


8+8


# In[2]:


tax = 3.5


# In[3]:


price = 100


# In[4]:


price * tax


# In[5]:


price + _


# In[6]:


3 * pa + van


# In[7]:


3 * 'pa' + 'van'


# In[8]:


"pavan"


# In[9]:


'pav' 'an'


# In[10]:


word[] = 'Python'


# In[11]:


word = 'Python'


# In[12]:


word[0]


# In[13]:


word[0] = 'L'


# In[14]:


word[0] + 'avan'


# In[15]:


'J' + word[1:]


# In[16]:


'L' + word[:3]


# In[18]:


word[:2] + 'zy'


# In[19]:


len(word)


# In[7]:


a,b =0,1
while(a<10):
    print(a)
    a,b 
    b = a +b


# In[19]:


def hey_ho(start,end):
    for i in range (start, end):
        if (i % 3 == 0):
            x = 1
        elif (i % 5 == 0):
            x = 2
        else:
            print(i)
            
        if (x == 1):
            print ('Hey')
        elif (x == 2):
            print ('Ho')
        elif (x == 1) & (x == 2):
            print ('GO Tigers')


# In[14]:


hey_ho(6, 15)


# In[15]:


hey_ho(2,5)


# In[16]:


hey_ho(6, 15)


# In[17]:


hey_ho(6,15)


# In[20]:


hey_ho (6,15)


# In[71]:


def hey_ho(start,end):
    if start < end:
            for i in range (start, end+1, 1):
                if ((i % 3 == 0) & (i % 5 == 0)):
                    print ('GO Tigers!')
                elif (i % 5 == 0):
                    print ('Ho!')
                elif (i % 3 == 0):
                    print ('Hey!')
                else:
                    print(i)
            
    else:
        for i in range (start, end, -1):
            if ((i % 3 == 0) & (i % 5 == 0)):
                print ('GO Tigers!')
            elif (i % 5 == 0):
                print ('Ho!')
            elif (i % 3 == 0):
                print ('Hey!')
            else:
                print(i)


# In[30]:


hey_ho(2, 10)


# In[27]:


hey_ho(2, 16)


# In[28]:


hey_ho(1,50)


# In[33]:


hey_ho(2,15)


# In[37]:


hey_ho(2,15)


# In[72]:


hey_ho(15, 4)


# In[78]:


def hey_ho(start,end):
    if start < end:
            while(start <= end):
                if ((start % 3 == 0) & (start % 5 == 0)):
                    print ('GO Tigers!')
                elif (start % 5 == 0):
                    print ('Ho!')
                elif (start % 3 == 0):
                    print ('Hey!')
                else:
                    print(start)
                
                start = start + 1
            
    else:
            while(end <= start):
                if ((start % 3 == 0) & (start % 5 == 0)):
                    print ('GO Tigers!')
                elif (start % 5 == 0):
                    print ('Ho!')
                elif (start % 3 == 0):
                    print ('Hey!')
                else:
                    print(start)
                
                start = start - 1


# In[84]:


hey_ho(3.0,15.0)


# In[86]:


0.1+0.1+0.1 == 0.3


# In[ ]:






# coding: utf-8

# In[8]:


def pitagora(a,b):
    c = a**2 + b**2
    return c**.5


# In[9]:


c = pitagora(3,4)


# In[10]:


print(c)


# In[12]:


pitagora(5,12)


# In[13]:


def parallelepipedo(a,b,c):
    Vol = a*b*c
    Ab = a*b
    return Ab, Vol


# In[16]:


volume, areabase = parallelepipedo(13,11,10)
print(volume, areabase)


# In[18]:


c = parallelepipedo(13,11,10)


# In[19]:


c


# In[20]:


type(parallelepipedo)


# In[21]:


#Passiamo agli oggetti


# In[1]:


class animale:
    def __init__(self,nome, età, peso, altezza):
        self.name = nome
        self.age = età
        self.weight = peso
        self.height = altezza
    def cresci(self,diquanto):
        self.height += diquanto


# In[2]:


A = animale("giraffa",12,89,2.31)


# In[3]:


print(A.name)


# In[4]:


A.cresci(0.21)


# In[5]:


A.height


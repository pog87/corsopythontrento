
# coding: utf-8

# # Titolo
# ### Sottotitolo
# 
# testo normale
# *italico*
# **grassetto**
# [La mia pagina web](http://www.math.unipd.it/~poggiali/)
# ![la mia brutta faccia](http://www.math.unipd.it/~poggiali/images/davide.jpg)

# In[1]:


a=1
b=14
print(a+b)
#commento


# vediamo un po' di tipi diversi

# In[2]:


type("stringa")


# In[3]:


type(1)


# In[4]:


type(1.)


# In[5]:


c=11


# In[6]:


print(c)


# In[7]:


type(type)


# In[39]:


#la nostra prima lista
a=["latte","carote","merendine",2,1.]
type(a)


# In[18]:


print(a[0])


# In[19]:


print(a[0:3])


# In[24]:


a[0:5:2]
a[1:5:2]


# In[25]:


a[0:5]


# In[26]:


len(a)


# In[32]:


a[0:len(a)-1]


# In[33]:


a[:-1]


# In[31]:


a[::3]


# In[40]:


#le tuple
b=(2,1,'albero')
type(b)


# In[38]:


list(b)


# In[45]:


#insieme o set
c={1,2,'babbo',2,0,5,'anatra'}
type(c)


# In[46]:


print(c)


# In[48]:


#operatori booleani
f=True
g=False
type(f)


# In[49]:


True and False


# In[50]:


True or False


# In[54]:


True ^ True


# In[57]:


True and not False


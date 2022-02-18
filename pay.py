#!/usr/bin/env python
# coding: utf-8

# In[1]:


import streamlit as st
st.header ("'simple web app'")
st.write ("'*my app*'")
value= st.slider ('val')
st.write (value,"square is", value*value)


# In[1]:


import streamlit as st
st. header ("'looking your vote eligibility'")
age = st.number_input('what is your age')
if age >=18:
    st.write('you can vote')
else:
    st.write('you can not vote')

    


# In[1]:


import streamlit as st
st.header("'temperature conversion'")
st.write ("'**Change Celcius to Fahrenheit**'")
number = st.number_input("enter the value of temperature in Celcius")
C = ((number * (9/5))+32)
st.write (C,"°F")


# In[1]:


import streamlit as st


st.write ('''** Change Fahrenheit to Celcius**''')
number = st.number_input("enter the value of temperature in Fahrenheit")
F = ((number-32)*(5/9))
st.write (F,"°C")


# In[ ]:





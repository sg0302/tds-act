import streamlit as st
title = "Largest Number Among the 3 numbers"
st.set_page_config(page_title=title)

st.title('Largest Number from three')

x = st.number_input('Enter first number')
y = st.number_input('Enter second number')
z = st.number_input('Enter third number')

l=[x,y,z]
if x == y == z:
  st.write("The numbers are Equal")
else:
  st.write(max(l),"is the largest number")

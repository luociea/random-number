import streamlit as st
import random
import time

st.title('Welcome to Random Number Generator!')
time.sleep(0.05)
st.title('Generates a number on a range of 1 to 100.')
time.sleep(0.05)

if st.button('Roll Number!'):
    number = random.randint(1, 100)
    st.header(f" Your number is {number}!")

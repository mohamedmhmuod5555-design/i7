import random 
import streamlit as st 
num=0
num1=random.randint(1,20)
num2=random.randint(1,20)
sign=random.choice(['+','-','*','/'])
if 'num1' not in st.session_state:
  st.session_state.num1=random.randint(1,20)
  st.session_state.num2=random.randint(1,20)
  st.session_state.sign=random.choice(['+','-','*','/'])
num1=st.session_state.num1
num2=st.session_state.num2
sign=st.session_state.sign
if sign=='+':
 sc=num1+num2
if sign=='-':
 sc=num1-num2
if sign=='*':
 sc=num1*num2
if sign=='/':
 sc=num1/num2
st.title("welcome to our game")
st.write(num1,sign,num2)
number=st.number_input("What is the reselt")
if st.button("تاكيد التخمين "):
 if number==sc:
  st.success("you are winner ")
  num=+1
 else:
  st.error("you are not winner ")
  del num
if st.button("السؤال التالي "):
  del st.session_state.num1
  del st.session_state.num2
  del st.session_state.sign
  st.rerun()
st.write(num)

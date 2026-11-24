import streamlit as st

st.title("MY FIRST CALCULATOR")

st.header("Add")


a = st.number_input("enter number add 1")

b = st.number_input("enter number add 2")

st.write("Sum =", a+b)

st.header("Multiply")

c = st.number_input("enter number to multiply 1")

d = st.number_input("enter number to multiply 2")

st.write("Answer =", c * d)

st.header("Subtract")

e = st.number_input("enter number to subtract 1")

f = st.number_input("enter number to subtract 2")

st.write("Answer =", e - f)

st.header("Divide")

g = st.number_input("enter number to divide 1")

h = st.number_input("enter number to divide 2")

if g != 0:
    st.write("Answer =", g / h)

elif g == 0:
    st.error("This number cannot be divided.")

st.header("Power")

i = st.number_input("enter number to power 1")

j = st.number_input("enter number to power 2")

st.write("Answer =", i ** j)

st.header("Square")

k = st.number_input("enter a number to square")

st.write("Answer =", k * k)


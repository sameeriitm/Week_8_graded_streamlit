import streamlit as st
st.title("DIVISION OF TWO NUMBERS")
st.markdown("""## Enter First Number""")
num1 = st.number_input(label="num1")
st.markdown("""## Enter Second Number""")
num2 = st.number_input(label="num2")

if st.button("Result"):
    if num2==0:
        st.text("Please enter any number other than 0 for num2")
    else:
        st.markdown(""" ## Result of num1 divided by num2 is """)
        st.write(num1/num2)
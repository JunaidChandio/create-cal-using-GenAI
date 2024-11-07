import streamlit as st

# Streamlit app code
st.title("Simple Calculator")

# Input fields for numbers
num1 = st.number_input("Enter the first number", step=1e-6, format="%.6f")
num2 = st.number_input("Enter the second number", step=1e-6, format="%.6f")

# Dropdown for operation selection
operation = st.selectbox("Choose an operation", ("Add", "Subtract", "Multiply", "Divide"))

# Perform the calculation when the button is clicked
if st.button("Calculate"):
    if operation == "Add":
        result = num1 + num2
        st.write(f"The result of {num1} + {num2} is: {result}")
    elif operation == "Subtract":
        result = num1 - num2
        st.write(f"The result of {num1} - {num2} is: {result}")
    elif operation == "Multiply":
        result = num1 * num2
        st.write(f"The result of {num1} * {num2} is: {result}")
    elif operation == "Divide":
        if num2 != 0:
            result = num1 / num2
            st.write(f"The result of {num1} / {num2} is: {result}")
        else:
            st.write("Error: Division by zero.")

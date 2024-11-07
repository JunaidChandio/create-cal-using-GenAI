import streamlit as st
import math

# Streamlit app title
st.title("Scientific Calculator")

# Number inputs for binary operations
num1 = st.number_input("Enter the first number", step=1e-6, format="%.6f")
num2 = st.number_input("Enter the second number (optional for some operations)", step=1e-6, format="%.6f")

# Operation selection
operation = st.selectbox(
    "Choose an operation",
    (
        "Add",
        "Subtract",
        "Multiply",
        "Divide",
        "Square",
        "Square Root",
        "Power",
        "Logarithm (base 10)",
        "Natural Logarithm",
        "Sine",
        "Cosine",
        "Tangent",
    )
)

# Perform the calculation when the button is clicked
if st.button("Calculate"):
    try:
        # Basic arithmetic operations
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

        # Scientific operations
        elif operation == "Square":
            result = num1 ** 2
            st.write(f"The square of {num1} is: {result}")
        elif operation == "Square Root":
            if num1 >= 0:
                result = math.sqrt(num1)
                st.write(f"The square root of {num1} is: {result}")
            else:
                st.write("Error: Square root of a negative number.")
        elif operation == "Power":
            result = math.pow(num1, num2)
            st.write(f"The result of {num1} ^ {num2} is: {result}")
        elif operation == "Logarithm (base 10)":
            if num1 > 0:
                result = math.log10(num1)
                st.write(f"The base-10 logarithm of {num1} is: {result}")
            else:
                st.write("Error: Logarithm of a non-positive number.")
        elif operation == "Natural Logarithm":
            if num1 > 0:
                result = math.log(num1)
                st.write(f"The natural logarithm of {num1} is: {result}")
            else:
                st.write("Error: Logarithm of a non-positive number.")
        elif operation == "Sine":
            result = math.sin(math.radians(num1))
            st.write(f"The sine of {num1} degrees is: {result}")
        elif operation == "Cosine":
            result = math.cos(math.radians(num1))
            st.write(f"The cosine of {num1} degrees is: {result}")
        elif operation == "Tangent":
            result = math.tan(math.radians(num1))
            st.write(f"The tangent of {num1} degrees is: {result}")
    except ValueError:
        st.write("Invalid input for the selected operation.")


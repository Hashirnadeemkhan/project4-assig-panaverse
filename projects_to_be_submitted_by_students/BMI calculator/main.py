import streamlit as st

# Set the title of the web app
st.title("BMI Calculator")

# Add a brief description
st.write("Enter your weight and height to calculate your BMI.")

# Create input fields for weight and height
weight = st.number_input("Enter your weight (kg)", min_value=0.0, value=70.0)
height = st.number_input("Enter your height (m)", min_value=0.0, value=1.75)

# Function to calculate BMI
def calculate_bmi(weight, height):
    if height > 0:
        bmi = weight / (height ** 2)
        return round(bmi, 2)
    return None

# Function to get BMI category
def get_bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 25:
        return "Normal"
    elif 25 <= bmi < 30:
        return "Overweight"
    else:
        return "Obese"

# Button to calculate BMI
if st.button("Calculate BMI"):
    bmi = calculate_bmi(weight, height)
    if bmi is not None:
        st.write(f"Your BMI is: **{bmi}**")
        st.write(f"Category: **{get_bmi_category(bmi)}**")
    else:
        st.write("Please enter a valid height (greater than 0).")
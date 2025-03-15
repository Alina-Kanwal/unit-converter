# import streamlit as st
 

# def convert_units(value, unit_from, unit_to):
#    conversions = {
#       "meters_Kilometers":0.001,
#       "Kilometers_meters": 1000,
#       "grams_Kilograms":0.001,
#       "Kilograms_grams":1000

#    }

#    key = f"{unit_from}_{unit_to}"

#    if key in conversions:
#       conversion = conversions[key]
#       return value * conversion
#    else:
#       return "conversion not supported"
   

# st.title("unit converter")
# value = st.number_input("Enter the value: ")
# unit_from = st.selectbox("convert from :",["meters", "Kilometers", "grams", "Kilograms"])
# unit_to = st.selectbox("convert to:", ["meters", "Kilometers", "grams", "kilograms"])

# if st.button("convert"):
#    result = convert_units(value, unit_from, unit_to)
#    st.write(f"converted value: {result}")

import streamlit as st

def convert_units(value, unit_from, unit_to):
    conversions = {
        "meters_Kilometers": 0.001,
        "Kilometers_meters": 1000,
        "grams_Kilograms": 0.001,
        "Kilograms_grams": 1000
    }

    key = f"{unit_from}_{unit_to}"

   # Logic to covert units
    if key in conversions:
        conversion = conversions[key]
        return value * conversion
    else:
        return "Conversion not supported"

st.title("Unit Converter")

# usr input
value = st.number_input("Enter the value: " , min_value=1.0, step=1.0)
unit_from = st.selectbox("Convert from:", ["meters", "Kilometers", "grams", "Kilograms"])  # Fixed capitalization
unit_to = st.selectbox("Convert to:", ["meters", "Kilometers", "grams", "Kilograms"])  # Fixed capitalization

if st.button("Convert"):
    result = convert_units(value, unit_from, unit_to)
    st.write(f"Converted value: {result}")




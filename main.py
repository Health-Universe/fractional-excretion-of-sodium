import streamlit as st
import pandas as pd

def calculate_fena(urine_na, serum_na, urine_cr, serum_cr):
    fena = (urine_na/serum_na)/(urine_cr/serum_cr) * 100
    return fena

# Set up the app layout
st.title('FENa Calculator')
st.write('Enter the following values to calculate FENa:')

# Create input fields for the necessary values
urine_na = st.number_input('Urine Sodium Concentration (mmol/L)', value=0.01)
serum_na = st.number_input('Serum Sodium Concentration (mmol/L)', value=0.01)
urine_cr = st.number_input('Urine Creatinine Concentration (umol/L)', value=0.01)
serum_cr = st.number_input('Serum Creatinine Concentration (umol/L)', value=0.01)

# Call the calculate_fena function with the input values
fena = calculate_fena(urine_na, serum_na, urine_cr, serum_cr)

# Display the calculated FENa value
st.write('FENa:', round(fena, 2), '%')

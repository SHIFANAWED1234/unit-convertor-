#Project 01: Unit Convertor
#Build a Google Unit Convertor using Python and Streamlit 

import streamlit as st 
st.title("Unit Converter App ")

conversion_type = st.sidebar.selectbox("choose converversion type ",["lenght","weight","temperature "]) 
value = st.number_input("enter value",value=0.0,min_value=0.0,step=0.1)
col1, col2= st.columns (2)
 
if conversion_type == "lenght":
    with col1 : 
        from_unit = st.selectbox("from" , ["meters","kilograms","centimeter","milimeter","miles","yards","feet","inches"])
    with col2:
        to_unit = st.selectbox ("to",["meters","kilograms","centimeter","milimeter","miles","yards","feet","inches"])
elif conversion_type == "weight":
    with col1:
        from_unit = st.selectbox("from",["kilogram","grams","miligrams","pounds","miles","pounds"]) 
    with col2 :
        to_unit= st.selectbox("To",["kilogram","grams","miligrams","pounds","miles","pounds"] )
elif conversion_type == "temperature ": 
    with col1:
        from_unit = st.selectbox ("from",["celsis","fahrenheit","kelvin"])
    with col2:
        to_unit = st.selectbox ("to",["celsis","fahrenheit","kelvin"])
 

def lenght_convertor (value ,from_unit, to_unit):
    lenght_units ={
        'meters': 1, 'kilometers':0.01,'centimeters':100, 'millimeters':1000, 
         'miles': 0.000621371,'yards':1.09361,'feet':3.28 , 'inches':39.37 
         }
    
    return ( value / lenght_units [from_unit]) * lenght_units [to_unit]
    
def weight_convertor(value, from_unit, to_unit):
    weight_units = {
        'kilogram': 1,'grams':1000,'miligrams' : 1000000,'pounds': 2.2046
        }
    return (value / weight_units[from_unit]) * weight_units[to_unit]

def temperature_convertor(value, from_unit, to_unit):
    if from_unit == "celsius":
        return (value * 9/5 +32) if to_unit == "fahrenheit"else value +273.15 if to_unit == "kelvin" else value
    elif from_unit == "fahrenheit":
        return (value - 32) * 5/9 if to_unit == "celsius" else (value-32 )* 5/9 +273.15 if to_unit == "kelvin" else value 
    elif from_unit == "kelvin ":
        return value -273.15 if to_unit == "celsius " else (value -273.15) * 9/5+32 if to_unit == "fahrenheit" else value 
    return value 

if st.button ("convert ") :
    if conversion_type == "lenght ":
        result = lenght_convertor (value,from_unit,to_unit)  
    elif conversion_type == "weight":
        result = weight_convertor (value,from_unit,to_unit)
    elif  conversion_type == "temperature ":
        result = temperature_convertor (value,from_unit,to_unit)

 st.markdown(f"<div class='result-box'>Result: {result:.4f} {to_unit}</div>", unsafe_allow_html=True)
    except Exception as e:
        st.error(f"An error occurred: {e}")

st.markdown ("<div class = 'footer'> created by Shifa Nawed </div> ", unsafe_allow_html=True  )

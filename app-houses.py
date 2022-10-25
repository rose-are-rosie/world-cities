import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
plt.style.use('seaborn')

st.title('California housing data(1990)by ')
st.title('Boyan Yu')
df = pd.read_csv('housing.csv')

housing_price_filter = st.slider('Minimal Median House Price :', 0, 500001, 200000) 



location_filter = st.sidebar.multiselect(
     'Choose the location type',
     df.ocean_proximity.unique(),  
     df.ocean_proximity.unique()
)  

income_filter = st.sidebar.radio(
     "Choose income level",
     ('Low','Medium','High')
)
    

df = df[df.median_house_value >= housing_price_filter]   


df = df[df.ocean_proximity.isin(location_filter)]


if income_filter == 'Low':
    df = df[df.median_income<=2.5]
         
if income_filter == 'Medium':   
    df = df[(df.median_income > 2.5) & (df.median_income < 4.5 )]

if income_filter == 'High':
    df = df[df.median_income>4.5]

st.subheader('See more filters in the sidebar:')


st.map(df)


st.subheader('Historgam of the Median House Value')

fig, ax = plt.subplots()
pop_median_house_value = df.median_house_value.hist(bins=30)

st.pyplot(fig)
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from babel.numbers import format_currency

with st.sidebar:
    
    #st.image('download.jpeg')
    st.title('Rental Bikes')
    name = st.text_input(label='Nama', value='')
    st.write('Halo ', name, ' Selamat Datang di Rental Bikes')


st.header('Dicoding Rental Bike')

#main_df = pd.read_csv('main_data.csv')
day_df = pd.read_csv('day.csv')
hour_df = pd.read_csv('hour.csv')


st.subheader('Penyewaan Sepeda Per Hari')


daily_rentals = day_df.groupby(by="weekday").agg({"cnt": "sum"})


st.set_option('deprecation.showPyplotGlobalUse', False) 
st.bar_chart(daily_rentals)


st.subheader('Penyewa Sepeda Per Jam')

hourly_rentals = hour_df.groupby(by="hr").agg({"cnt": "sum"})

st.set_option('deprecation.showPyplotGlobalUse', False) 
st.line_chart(hourly_rentals)


st.subheader('Perbandingan Penyewa Casual dan Registered Per Bulan')


total_per_month = day_df.groupby(by="mnth").agg({
    "cnt": "sum",
    "casual": "sum",
    "registered": "sum"
})


st.set_option('deprecation.showPyplotGlobalUse', False)  
fig, ax = plt.subplots(figsize=(10, 6))


month = total_per_month.index
casual_rentals = total_per_month['casual']
registered_rentals = total_per_month['registered']

ax.bar(month, casual_rentals, width=0.4, label='Casual', color='skyblue')
ax.bar(month + 0.4, registered_rentals, width=0.4, label='Registered', color='orange')

ax.set_xticks(range(1, 13))  
ax.set_xticklabels(['Jan', 'Feb', 'Mar', 'April', 'Mei', 'Juni', 'Juli', 'Agust', 'Sept', 'Okt', 'Nov', 'Des'])  
ax.legend()

st.pyplot(fig)
    
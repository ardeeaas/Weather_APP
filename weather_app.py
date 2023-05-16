import streamlit as st
import requests
from datetime import datetime, timedelta
import pandas as pd

api_key='e2a69ac1530be4aec13d81106205e65b'
username='andreeasarighioleanu'
#api call
url_daily="https://api.openweathermap.org/data/3.0/onecall?lat={}&lon={}&appid={}"
url_country='http://api.geonames.org/findNearbyJSON?lat={}&lng={}&username={}'

    
def getweather(lat,lon):
    result=requests.get(url_daily.format(lat,lon, api_key))
    print(result)
    if result:
        resjson = result.json()
        lat=resjson["lat"]
        lon=resjson["lon"]
        temp=resjson["current"]['temp']-273.15
        temp_feels=resjson["current"]['feels_like']-273.15
        print(temp_feels)
        humid=resjson['current']['humidity']
        res=[round(temp,1), round(temp_feels,1), humid, lon, lat]

        return res, resjson
    else: 
        return ("Error in search")

def getcountry(lat,lon):
    
    res=requests.get(url_country.format(lat,lon,username))
    if res:
        resjson=res.json()
        country=resjson["geonames"][0]["countryName"]
        return country

    else: return "Error in search"
#app interface

st.title("Weather app")
col1, col2, col3 =st.columns(3)
with col1:
    latitude=st.text_input("Please enter a lat")
with col2:
    longitude=st.text_input("Please enter a lon")
  
with col3:

    res, resjson = getweather(latitude,longitude)
    st.success('Current temp: '+str(round(res[0],2)))
    st.info('Current temp feels like: '+str(round(res[1],2)))
    st.info('Humidity: '+str(res[2]))

with col2: 
    result=st.button("Press to get the country")
    if result:

        country=getcountry(latitude,longitude)
        st.success('Country: '+str(country))

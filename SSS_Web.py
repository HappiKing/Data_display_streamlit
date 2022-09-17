from ast import While
import csv
from email.utils import collapse_rfc2231_value
from logging import PlaceHolder
from pkgutil import get_data
from pydoc import visiblename
from tkinter import Grid
from turtle import width
from attr import define
from matplotlib import scale
from matplotlib.pyplot import grid
#from pyparsing import col
from sqlalchemy import column, create_engine, true
import streamlit as st
import pandas as pd
import matplotlib
import plotly.express as px # interactive charts 
import altair as alt
import time
import numpy as np
from page2 import page_more_graph
from page3 import page_reload_data
matplotlib.use('agg')






# set page title
st.set_page_config(
    page_title="Real-Time Data Science Dashboard",
    page_icon="✅",
    layout="wide",
)

def main_page():
    st.markdown("# Smart Sensor System")
    st.markdown("### Total Chart")
    st.sidebar.markdown("# Total_Graph")

    placeholder = st.empty()
    
    
    while True : 
        # set csv_file url
        dataDate = time.strftime("%Y-%m-%d")
        dataset_url = ("/home/pi/Desktop/SSS_Web_App/Data_source/" + dataDate + ".csv")
       
        with placeholder.container():
    
            csv_read = pd.read_csv(dataset_url)
            df = pd.DataFrame(csv_read)

            fig = px.line(df,x="time",
            y=["gas1","gas2","gas3","gas4","gas5","gas6"])
            #title='total graph')

            fig.update_traces(line=dict(width=2.5))
            fig.update_layout(plot_bgcolor="white", width=1200, height =500)
            fig.update_xaxes(showline = True, linewidth = 2, linecolor = "black", gridcolor = "black")
            fig.update_yaxes(showline = True, linewidth = 2, linecolor = "black", gridcolor = "black")
            

            st.write(fig)

            col1, col2, col3 = st.columns(3)

            with col1 :
                col1.metric(
                label="Time",
                value= time.strftime("%H:%M:%S")
                )
            
            with col2 :
                col2.metric(
                label="Temp",
                value=(round(df.iloc[-1,1]))
                )
            
            with col3 :
                col3.metric(
                label="Humi",
                value=(round(df.iloc[-1,2]))
                )

##각 센서별 작동 여부 디스플레이
            col_sensor1, col_sensor2, col_sensor3, col_sensor4, col_sensor5= st.columns(5)
            with col_sensor1 :
                if (df.iloc[-1,9] > 0) : 
                    st.text("Sensor1")
                    st.image("/home/pi/Desktop/SSS_Web_App/Img_source/On_source.png")
                elif (df.iloc[-1,9] == 0) : 
                    st.text("Sensor1")
                    st.image("/home/pi/Desktop/SSS_Web_App/Img_source/Off_source.png")
                else :
                    st.title("No working")

            with col_sensor2 :
                if (df.iloc[-1,10] > 0) : 
                    st.text("Sensor2")
                    st.image("/home/pi/Desktop/SSS_Web_App/Img_source/On_source.png")
                elif (df.iloc[-1,10] == 0) : 
                    st.text("Sensor2")
                    st.image("/home/pi/Desktop/SSS_Web_App/Img_source/Off_source.png")
                else :
                    st.title("No working")

            with col_sensor3 :
                if (df.iloc[-1,11] > 0) : 
                    st.text("Sensor3")
                    st.image("/home/pi/Desktop/SSS_Web_App/Img_source/On_source.png")
                elif (df.iloc[-1,11] == 0) : 
                    st.text("Sensor3")
                    st.image("/home/pi/Desktop/SSS_Web_App/Img_source/Off_source.png")
                else :
                    st.title("No working")    

            with col_sensor4 :
                if (df.iloc[-1,12] > 0) : 
                    st.text("Sensor4")
                    st.image("/home/pi/Desktop/SSS_Web_App/Img_source/On_source.png")
                elif (df.iloc[-1,12] == 0) : 
                    st.text("Sensor4")
                    st.image("/home/pi/Desktop/SSS_Web_App/Img_source/Off_source.png")
                else :
                    st.title("No working")

            with col_sensor5 :
                if (df.iloc[-1,13] > 0) : 
                    st.text("Sensor5")
                    st.image("/home/pi/Desktop/SSS_Web_App/Img_source/On_source.png")
                elif (df.iloc[-1,13] == 0) : 
                    st.text("Sensor5")
                    st.image("/home/pi/Desktop/SSS_Web_App/Img_source/Off_source.png")
                else :
                    st.title("No working")


    

            st.dataframe(df)

    

            #온습도 값 직접 받아서 연결

            time.sleep(1)

        


        placeholder.empty()
        
        

    

def page2():
    page_more_graph()

def page3():
    page_reload_data()


page_names_to_funcs = {
    "Total Graph": main_page,
    "Detailed-View Data": page2,
    "Re-View Data": page3
}

selected_page = st.sidebar.selectbox("Select a page", page_names_to_funcs.keys())
page_names_to_funcs[selected_page]()
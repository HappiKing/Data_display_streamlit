import streamlit as st
import plotly.express as px
import pandas as pd
import time



def page_more_graph():
    dataDate = time.strftime("%Y-%m-%d")

    dataset_url = ("/home/pi/Desktop/SSS_Web_App/Data_source/"+ dataDate +".csv")
    csv_read = pd.read_csv(dataset_url)
    df = pd.DataFrame(csv_read)
    st.sidebar.markdown("# more graph")

    placeholder = st.empty()

    lang_list = df.columns.tolist()
    print(lang_list)

    lang_list = lang_list [1:9]
    selected_lang_list = st.multiselect('Select Value', lang_list)
    print(selected_lang_list)

    if len(selected_lang_list) != 0: 
        df_selected = df[selected_lang_list]

        df_selected['time'] = pd.DataFrame(df, columns=['time'])
        


        while True: 
            with placeholder.container():
                csv_read = pd.read_csv(dataset_url)
                df = pd.DataFrame(csv_read)
                df_selected = df[selected_lang_list]


                fig = px.line(df_selected, x=df["time"], y= selected_lang_list)
                fig.update_traces(line=dict(width=2.5))
                fig.update_layout(plot_bgcolor="white", width=1200, height =500)
                fig.update_xaxes(showline = True, linewidth = 2, linecolor = "black", gridcolor = "black")
                fig.update_yaxes(showline = True, linewidth = 2, linecolor = "black", gridcolor = "black")
                st.write(fig)

                st.dataframe(df_selected)

                time.sleep(1)


            placeholder.empty()
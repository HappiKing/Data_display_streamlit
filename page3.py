import streamlit as st
import plotly.express as px
import pandas as pd
import altair as alt

# dataset_url = ("/Users/hb/Desktop/html_study/py_source/sensor_test_set.csv")
# csv_read = pd.read_csv(dataset_url)
# df = pd.DataFrame(csv_read)

def page_reload_data():
    st.markdown("Re_View Data")
    st.sidebar.markdown("# Re_View")

    uploaded_file = st.file_uploader("Choose a file")
    if uploaded_file is not None:
        # Can be used wherever a "file-like" object is accepted:
        dataframe = pd.read_csv(uploaded_file)
        df = pd.DataFrame(dataframe)

        fig = px.line(dataframe,x="time",
            y=["gas1","gas2","gas3","gas4","gas5","gas6"],
            title='total graph',
            )

        fig.update_traces(line=dict(width=2.5))
        fig.update_layout(plot_bgcolor="white", width=1200, height =500)
        fig.update_xaxes(showline = True, linewidth = 2, linecolor = "black", gridcolor = "black")
        fig.update_yaxes(showline = True, linewidth = 2, linecolor = "black", gridcolor = "black")

        

        st.write(fig)

        

        lang_list = dataframe.columns.tolist()
        print(lang_list)

        lang_list = lang_list [1:9]
        selected_lang_list = st.multiselect('Select Value', lang_list)
        print(selected_lang_list)

        if len(selected_lang_list) != 0: 
            df_selected = dataframe[selected_lang_list]

            df_selected['time'] = pd.DataFrame(dataframe, columns=['time'])
            


            fig = px.line(df_selected, x='time', y= selected_lang_list)
            fig.update_traces(line=dict(width=2.5))
            fig.update_layout(plot_bgcolor="white", width=1200, height =500)
            fig.update_xaxes(showline = True, linewidth = 2, linecolor = "black", gridcolor = "black")
            fig.update_yaxes(showline = True, linewidth = 2, linecolor = "black", gridcolor = "black")
            st.write(fig)

            st.dataframe(df_selected)

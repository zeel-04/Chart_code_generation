import streamlit as st
import pandas as pd
import plotly.express as px

st.title('Chart code generation')

tab1, tab2, tab3 = st.tabs(["Upload", "Select Viz", "Code"])

with tab1:
    uploaded_file = st.file_uploader("Choose a csv file", type='.csv')

with tab2:

    st.subheader('Visualization')
    option = st.selectbox('Select the chart type',
                          ('None', 'Bar', 'Line', 'Pie'))

    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        # st.dataframe(df)

        if option == 'Bar':
            x_column = st.selectbox('Select X axis', (df.columns))
            y_column = st.selectbox('Select Y axis', (df.columns))

            if x_column != y_column:
                fig = px.bar(df, x=x_column, y=y_column)
                st.plotly_chart(fig, use_container_width=True)
            else:
                st.error('Please select different axis')
    else:
        st.info('Please upload file')


with tab3:
    st.subheader('Code')

    if uploaded_file is not None:

        if option != 'None':
            if option == 'Bar':
                if x_column != y_column:
                    code = f'''import streamlit as st
import plotly.express as px
import pandas as pd

df = pd.read_csv('Path to your dataset')
fig = px.bar(df, x = df['{x_column}'], y = df['{y_column}'])
st.plotly_chart(fig, use_container_width=True)
'''
                    st.code(code, language='python')
                    fig = px.bar(df, x=x_column, y=y_column)
                    st.plotly_chart(fig, use_container_width=True)
                else:
                    st.error('Please select different axis')
        else:
            st.error('Please select chart type')
        
    else:
        st.info('Please upload file')

# code = f'''import streamlit as st
# import plotly.express as px
# import pandas as pd

# df = pd.read_csv('Path to your dataset')
# fig = px.bar(df, x = df['{x_column}'], y = df['{y_column}'])
# st.plotly_chart(fig, use_container_width=True)
# '''
# st.code(code, language='python')
import streamlit as st
import os
from zipfile import ZipFile
import shutil
from os.path import basename
import time

st.header("Keboola + ThoughtSpot: SpotApp Creation Tool")

st.image('static/keboola+thoughtspot.png', width=250)

st.markdown('''
Keboola SpotApp Helper is a tool to help you create ThoughtSpot SpotApps.  
''')

st.sidebar.title('Welcome!')
st.markdown('''
### Enter the database and schema name of your own Snowflake datawarehouse and click the button to automatically edit your TML.
''')

os.system("cd Shopify_SpotApp")

db = st.text_input('Enter your database name:', 'KEBOOLA_1234')
schema = st.text_input('Enter your schema name:', 'WORKSPACE_123456789') 


if st.button("Create TML"):
    st.write("you entered database name: ", db)
    st.write("you entered schema name: ", schema)
    os.system(
        f"find . -type f -name '*.table.tml' -exec sed -i '' -e 's/KEBOOLA_7615/{db}/g' {{}} \; && find . -type f -name '*.table.tml' -exec sed -i '' -e 's/WORKSPACE_23825284/{schema}/g' {{}} \;"
    )
    #os.system()
    os.system("cd ..")
    shutil.make_archive('Output_SpotApp', 'zip', 'Shopify_SpotApp')
    with open("Output_SpotApp.zip", "rb") as fp:
        btn = st.download_button(
        label="Download ZIP",
        data=fp,
        file_name="myfile.zip",
        mime="application/zip"
    )

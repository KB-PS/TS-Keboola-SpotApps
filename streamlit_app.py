import streamlit as st
import os
from zipfile import ZipFile
from os.path import basename

st.header("Keboola + ThoughtSpot: SpotApp Creation Tool")

st.image('static/keboola+thoughtspot.png', width=250)



st.markdown('''
Keboola SpotApp Helper is a tool to help you create ThoughtSpot SpotApps.  
''')

st.sidebar.title('Welcome!')
st.markdown('''
### Select a SpotApp to get started.
''')

db = st.text_input('Enter your database name:', 'KEBOOLA_1234')
schema = st.text_input('Enter your schema name:', 'WORKSPACE_123456789')

@st.cache
def activity_center(db, schema):
    def db_schema_replace():
        if  st.button('Replace Database Name and Schema Name'):    
            st.write(os.system("cd Activity_Center_SpotApp"))
            st.write(os.system(f"find . -type f -name '*.table.tml' -exec sed  's/KEBOOLA_5539/{db}/g' {{}} +"))
            st.write(os.system(f"find . -type f -name '*.table.tml' -exec sed 's/WORKSPACE_15606217/{schema}/g' {{}} +"))
            os.system("cd ..")
    db_schema_replace()
    with ZipFile('Output_SpotApp.zip', 'w') as zipObj:
        #EIterate over all the files in directory
        for folderName, subfolders, filenames in os.walk('Activity_Center_SpotApp'):
            for filename in filenames:
                #create complete fileath of file in directory
                filePath = os.path.join(folderName, filename)
                # Add file to zip
    return zipObj.write(filePath, basename(filePath))

@st.cache
def shopify(db, schema):
    """
    Shopify SpotApp - Replace Database Name and Schema Name

    """
    def db_schema_replace():
        if  st.button('Replace Database Name and Schema Name'):    
            st.write(os.system("cd Shopify_SpotApp"))
            st.write(os.system(f"find . -type f -name '*.table.tml' -exec sed  's/KEBOOLA_7615/{db}/g' {{}} +"))
            st.write(os.system(f"find . -type f -name '*.table.tml' -exec sed 's/WORKSPACE_23825284/{schema}/g' {{}} +"))
            os.system("cd ..")
    db_schema_replace()
    with ZipFile('Output_SpotApp.zip', 'w') as zipObj:
        #EIterate over all the files in directory
        for folderName, subfolders, filenames in os.walk('Shopify_SpotApp'):
            for filename in filenames:
                #create complete fileath of file in directory
                filePath = os.path.join(folderName, filename)
                # Add file to zip
    return zipObj.write(filePath, basename(filePath))
    

if st.button('Activity Center'):
    activity_center(db, schema)
    with open("Output_SpotApp.zip", "rb") as fp:
        btn = st.download_button(
        label="Download ZIP",
        data=fp,
        file_name="myfile.zip",
        mime="application/zip"
    )

if st.button('Shopify'):
    shopify(db, schema)
    with open("Output_SpotApp.zip", "rb") as fp:
        btn = st.download_button(
        label="Download ZIP",
        data=fp,
        file_name="myfile.zip",
        mime="application/zip"
    )
# create a ZipFile object
    
        

#st.sidebar.markdown('''
#Please enter the database name and schema name from your Snowflake database.
#''')
#
#
### if output/spotapps exists, delete it
#if os.path.exists('output/spotapps'):
#    os.system("rm -rf output/spotapps/*")
#
### remove all zip files from the current directory
#for file in os.listdir():
#    if file.endswith(".zip"):
#        os.remove(file)
#        os.system("rm -rf *.zip")
#
#files = st.file_uploader(
#                      "Upload a zip file containing your SpotApp", 
#                      type=["zip"], 
#                      accept_multiple_files=True
#                      )
#
##if not os.path.exists("output/spotapps"):
##    os.mkdir("output/spotapps")
#if files is not None:
#    for file in files:
#        with ZipFile(file, 'r') as zip_ref:
#            zip_ref.extractall('output/spotapps')
#    
#if st.button('Replace Database Name and Schema Name'):    
#    st.write(os.system("cd output/spotapps"))
#    st.write(os.system(f"find . -type f -name '*.table.tml' -exec sed  's/KEBOOLA_5984/{db}/g' {{}} +"))
#    st.write(os.system(f"find . -type f -name '*.table.tml' -exec sed 's/WORKSPACE_10706042/{schema}/g' {{}} +"))
#    os.system("cd ~")
## create a ZipFile object
#
#if st.button("Create Zip"):
#    with ZipFile('Output_SpotApp.zip', 'w') as zipObj:
#       # Iterate over all the files in directory
#       for folderName, subfolders, filenames in os.walk('output'):
#           for filename in filenames:
#               #create complete filepath of file in directory
#               filePath = os.path.join(folderName, filename)
#               # Add file to zip
#               zipObj.write(filePath, basename(filePath))
#    with open("Output_SpotApp.zip", "rb") as fp:
#        btn = st.download_button(
#            label="Download ZIP",
#            data=fp,
#            file_name="myfile.zip",
#            mime="application/zip"
#        )





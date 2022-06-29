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
st.sidebar.markdown('''
Please enter the database name and schema name from your Snowflake database.
''')
db = st.sidebar.text_input('Database Name', 'Enter Database Name')
schema = st.sidebar.text_input('Schema Name', 'Enter Schema Name')

## if output/spotapps exists, delete it
if os.path.exists('output/spotapps'):
    os.system("rm -rf output/spotapps/*")

## remove all zip files from the current directory
for file in os.listdir():
    if file.endswith(".zip"):
        os.remove(file)
        os.system("rm -rf *.zip")

files = st.file_uploader(
                      "Upload a zip file containing your SpotApp", 
                      type=["zip"], 
                      accept_multiple_files=True
                      )

#if not os.path.exists("output/spotapps"):
#    os.mkdir("output/spotapps")
if files is not None:
    for file in files:
        with ZipFile(file, 'r') as zip_ref:
            zip_ref.extractall('output/spotapps')
    
if st.button('Replace Database Name and Schema Name'):    
    os.system("cd output/spotapps")
    st.write(os.system("find . -type f -name '*.table.tml' -exec sed -i '' s/" + "KEBOOLA_5984" + "/" + db + "/g {\} +"))
    st.write(os.system("find . -type f -name '*.table.tml' -exec sed -i '' s/" + "WORKSPACE_10706042" + "/" + schema + "/g {\} +"))
    os.system("cd ~")
# create a ZipFile object

if st.button("Create Zip"):
    with ZipFile('Output_SpotApp.zip', 'w') as zipObj:
       # Iterate over all the files in directory
       for folderName, subfolders, filenames in os.walk('output'):
           for filename in filenames:
               #create complete filepath of file in directory
               filePath = os.path.join(folderName, filename)
               # Add file to zip
               zipObj.write(filePath, basename(filePath))
    with open("Output_SpotApp.zip", "rb") as fp:
        btn = st.download_button(
            label="Download ZIP",
            data=fp,
            file_name="myfile.zip",
            mime="application/zip"
        )



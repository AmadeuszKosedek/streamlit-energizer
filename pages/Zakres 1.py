import streamlit as st
import pandas as pd
from io import StringIO

st.set_page_config(
    page_title="Ex-stream-ly Cool App",
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Stacjonarne źródła spalania': 'https://www.extremelycoolapp.com/help',
        'Flota': "https://www.extremelycoolapp.com/bug",
        'Pojazdy niedrogowe': "# This is a header. This is an *extremely* cool app!"
    }
)

uploaded_file = st.file_uploader("Wgraj plik z danymi", type=['xls','xlsx','csv'])
if uploaded_file is not None:
    # To read file as bytes:
    bytes_data = uploaded_file.getvalue()
    st.write(bytes_data)

    # To convert to a string based IO:
    stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
    st.write(stringio)

    # To read file as string:
    string_data = stringio.read()
    st.write(string_data)

    # Can be used wherever a "file-like" object is accepted:
    dataframe = pd.read_csv(uploaded_file)
    st.write(dataframe)

tab1, tab2, tab3 = st.tabs(["Stacjonarne źródła spalania", "Flota", "Pojazdy niedrogowe", "Inne gazy"])

with tab1:
   st.header("A cat")
expander = st.expander("See explanation")
expander.write(\"\"\"
    The chart above shows some numbers I picked for you.
    I rolled actual dice for these, so they're *guaranteed* to
    be random.
\"\"\")
    
   option = st.selectbox(
    'Wybierz typ wykorzystywanego paliwa',
    ('Koks', 'Uran', 'Polon'))

st.write('You selected:', option)
   st.image("https://static.streamlit.io/examples/cat.jpg", width=200)

with tab2:
   st.header("A dog")
   st.image("https://static.streamlit.io/examples/dog.jpg", width=200)

with tab3:
   st.header("An owl")
   st.image("https://static.streamlit.io/examples/owl.jpg", width=200)
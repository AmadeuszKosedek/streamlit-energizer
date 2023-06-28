import streamlit as st

from streamlit_gallery import moja_firma, analityka
from streamlit_gallery.utils.page import page_group

def main():
    page = page_group("p")

    with st.sidebar:
        st.title("Analiza śladu węglowego")

        with st.expander("MOJA FIRMA", True):
            page.item("Podstawowe informacje", moja_firma.gallery, default=True)

        with st.expander("ANALITYKA", True):
            page.item("Zakres 1", analityka.zakres1)
            page.item("Zakres 2", analityka.zakres2)
    page.show()

if __name__ == "__main__":
    st.set_page_config(page_title="Streamlit Gallery by Okld", page_icon="🎈", layout="wide")
    main()
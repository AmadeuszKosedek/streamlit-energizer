import streamlit as st

from streamlit_gallery import apps, components
from streamlit_gallery.utils.page import page_group

def main():
    page = page_group("p")

    with st.sidebar:
        st.title("Analiza śladu węglowego")

        with st.expander("MOJA FIRMA", True):
            page.item("Podstawowe informacje", apps.gallery, default=True)

        with st.expander("ANALITYKA", True):
            page.item("Zakres 1", components.ace_editor)
            page.item("Zakres 2", components.disqus)
            page.item("Zalres 3", components.elements)
            page.item("Podsumowanie", components.pandas_profiling)
    page.show()

if __name__ == "__main__":
    st.set_page_config(page_title="Streamlit Gallery by Okld", page_icon="🎈", layout="wide")
    main()
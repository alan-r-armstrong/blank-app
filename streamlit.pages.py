import streamlit as st
from pages.page1 import page1
from pages.page2 import page2

def main():
    st.sidebar.subheader('Page selection')
    page_selection = st.sidebar.selectbox('Please select a page',['Main Page',
    'Page 1','Page 2'])
    pages_main = {
        'Main Page': main_page,
        'Page 1': page1,
        'Page 2': page2
    }

    # Run selected page
    pages_main[page_selection]()

def main_page():
    st.title('Main Page')
def page1():
    page1()
def page2():
    page2()
if __name__ == '__main__':
    main()
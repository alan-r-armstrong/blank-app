import streamlit as st
from pages.page_1 import page1
from pages.page_2 import page2
from datetime import datetime

st.set_page_config(

    page_title='Hello world',
    layout='centered',
    initial_sidebar_state='auto',
    menu_items={
        'Get Help': 'https://streamlit.io/',
        'Report a bug': 'https://github.com',
        'About': 'About your application: **Hello world**'
        }
)
st.sidebar.title("🎈 Hello World")
st.title('🎈 Hello world')

st.title("Clock")
clock = st.empty()
while True:
    time = datetime.now().strftime("%H:%M:%S")
    clock.info('**Current time: ** %s' % (time))
    if time == '22:08:00':
        clock.empty()
        st.warning("Time's up!")
        break

def main():
    st.sidebar.subheader('Page selection')
    page_selection = st.sidebar.selectbox('Please select a page',['Main Page',
    'Page 1','Page 2'])
    pages_main = {
        'Main Page': main_page,
        'Page 1': run_page1,
        'Page 2': run_page2
    }

    # Run selected page
    pages_main[page_selection]()

def main_page():
    st.title('Main Page')
def run_page1():
    page1()
def run_page2():
    page2()
if __name__ == '__main__':
    main()
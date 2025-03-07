import streamlit as st
from datetime import datetime
conn = st.connection('snowflake')

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

conn()

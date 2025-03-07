import streamlit as st
from datetime import datetime
conn = st.connection("snowflake")
df = conn.query("SELECT * FROM MYTABLE;", ttl="10m")

st.sidebar.title("🎈 Hello World")
st.title('🎈 Hello world')

st.title("Clock")
clock = st.empty()

for row in df.itertuples():
    st.write(f"{row.NAME} has a :{row.PET}:")

while True:
    time = datetime.now().strftime("%H:%M:%S")
    clock.info('**Current time: ** %s' % (time))
    if time == '22:08:00':
        clock.empty()
        st.warning("Time's up!")
        break

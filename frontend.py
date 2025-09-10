import streamlit as st
from crew import userquery  

st.set_page_config(page_title="News AI Agent", page_icon="📰")

st.title("📰 News AI Agent")
st.write("Enter a topic and let the AI crew research + write for you!")

topic = st.text_input("Enter a topic:")

if st.button("Generate Report"):
    if topic.strip():
        with st.spinner("Researching and writing..."):
            result = userquery(topic)
        st.success("Done!")
        st.write("### 📝 Final Report:")
        st.write(result)
    else:
        st.warning("Please enter a topic first.")

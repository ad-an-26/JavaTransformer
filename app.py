import streamlit as st
from transformer import transform_java_code

st.set_page_config(page_title="Java Modernizer: Java 8 ➜ Java 21", layout="wide")
st.title("Java Transformer")
st.write("Paste your Java 8 code below and get the modernized Java 21 version using GenAI!")

java8_code = st.text_area("Java 8 Code", height=300, placeholder="Paste your java 8 code here")

if st.button("Transform to Java 21!"):
  if not java8_code.strip():
    st.warning("Please enter Java 8 code to transform")
  else:
    with st.spinner("Transforming using GenAI..."):
      java21_code = transform_java_code(java8_code)
      st.success("Done! Here's your modernized java 21 code: ")
      st.code(java21_code, language='java')
    
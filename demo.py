
import streamlit as st
from langchain_openai import ChatOpenAI
model = ChatOpenAI(
    temperature=0.8,
    model="glm-4-plus",
    base_url="https://open.bigmodel.cn/api/paas/v4/",
    api_key="f529265e0e12a17191f0c08082d81bdf.nWtPvd98xBh3zlap"
)
st.title("AI demo小程序")
problem = st.chat_input("请输入你的问题")
if problem:
    with st.chat_message("user"):
        st.write(problem)
    result = model.invoke(problem)
    with st.chat_message("assistant"):
        st.write(result.content)
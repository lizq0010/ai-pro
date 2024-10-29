
import streamlit as st
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

model = ChatOpenAI(
    temperature=0.8,
    model="glm-4-plus",
    base_url="https://open.bigmodel.cn/api/paas/v4/",
    api_key="f529265e0e12a17191f0c08082d81bdf.nWtPvd98xBh3zlap"
)
prompt = PromptTemplate.from_template("你的名字叫小芳，你现在要扮演一个女朋友的角色，你的性格是霸道的，你现在要和你男朋友进行对话，你男朋友说的话是{input}")
chain = LLMChain(
    llm=model,
    prompt=prompt,
)
st.title("与小芳交谈")
if "cache" not in st.session_state:
    st.session_state.cache = []
else:
    for message in st.session_state.cache:
        with st.chat_message(message['role']):
            st.write(message)["contect"]

problem = st.chat_input("你的小芳在等待")
if problem:
    with st.chat_message("user"):
        st.write(problem)
        st.session_state.cache.append({"role":"user","contect":problem})
    result = chain.invoke({"input":problem})
    with st.chat_message("assistant"):
        st.write(result['text'])
    st.session_state.cache.append({"role":"assistant","contect":result['text']})
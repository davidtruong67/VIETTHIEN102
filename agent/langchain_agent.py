import os
import streamlit as st
from langchain.chat_models import ChatOpenAI
from langchain.agents import initialize_agent, Tool, AgentType
from .tidb_api import query_tidb

# Gán API key từ secrets vào biến môi trường
os.environ["OPENAI_API_KEY"] = st.secrets["OPENAI_API_KEY"]

llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0)

tool = Tool.from_function(
    func=query_tidb,
    name="Truy vấn TiDB",
    description="Dùng để truy vấn hệ thống công nợ, đơn hàng"
)

agent = initialize_agent([tool], llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION)

def ask_bot(question: str):
    return agent.run(question)

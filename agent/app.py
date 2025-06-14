import os
import streamlit as st
from agent.chroma_memory import recall_from_memory, add_to_memory
from agent.langchain_agent import ask_bot

# Gán API Key cho OpenAI
os.environ["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"] = st.secrets["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"]

st.set_page_config(page_title="Chatbot Việt Thiên", layout="wide")
st.title("🤖 Trợ lý AI - Việt Thiên")

if "history" not in st.session_state:
    st.session_state.history = []

user_input = st.chat_input("Hỏi AI về công nợ, đơn hàng, khách hàng hoặc quy trình làm việc...")

if user_input:
    if "quy trình" in user_input.lower() or "làm việc" in user_input.lower():
        context = '''
        Quy trình xử lý đơn hàng tại Việt Thiên:
        1. Sales tạo báo giá & xác nhận đơn hàng.
        2. Bộ phận logistics kiểm tra kho & lịch vận chuyển.
        3. Phòng kế toán xác nhận thanh toán.
        4. Kho xuất hàng, bộ phận CSKH theo dõi giao hàng.
        5. Hoàn tất, gửi chứng từ & nghiệm thu.
        '''
        full_query = f"Ngữ cảnh nội bộ:\n{context}\n\nCâu hỏi: {user_input}"
    else:
        docs = recall_from_memory(user_input)
        context = "\n".join([d.page_content for d in docs]) if docs else ""
        full_query = f"Ngữ cảnh từ trí nhớ:\n{context}\n\nCâu hỏi: {user_input}"

    response = ask_bot(full_query)
    add_to_memory(user_input + "\n" + response)
    st.session_state.history.append((user_input, response))

for msg, ans in st.session_state.history[::-1]:
    st.chat_message("user").write(msg)
    st.chat_message("assistant").write(ans)

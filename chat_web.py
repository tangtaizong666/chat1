import streamlit as st
from chat_h import get_chat_response
from langchain.memory import ConversationBufferMemory

st.header('💬聊天助手')
with st.sidebar:
    api_key=st.text_input('请输入你的api密钥')
    base_url=st.text_input('（如果是买的api）请输入你的base_url')
    st.write('我知道你没有，老江行👎')

#初始化memory和messages
if 'memory' not in st.session_state:
    st.session_state['memory']=ConversationBufferMemory(return_messages=True)
    st.session_state['messages']=[{'role':'ai','content':'你好，我是你的ai助手,有什么是我可以帮忙的吗'}]

#st.chat_message(role).write(content)，streamlit的聊天样式组件，根据role显示不同的聊天气泡
#这里遍历所有的消息并渲染到页面上，让用户可以看到之前的消息
for message in st.session_state['messages']:
    st.chat_message(message['role']).write(message['content'])

subject=st.chat_input()
if subject:
    if subject and not api_key:
        st.info('请输入你的api_key')
        st.stop()
    #保存用户消息到历史消息储存，并打印
    st.session_state['messages'].append({'role':'human','content':subject})
    st.chat_message('human').write(subject)

    with st.spinner('AI正在努力思考，清稍等...'):
        response=get_chat_response(subject,st.session_state['memory'],"sk-UmDxWlpFiAqen1tz0GU6SAadJFTdcaIC9KwbJppia7F9CXoD","https://www.chataiapi.com/v1")
        msg={'role':'ai','content':response}
        #保存ai回复的消息到历史消息并打印
        st.session_state['messages'].append(msg)
        st.chat_message('ai').write(response)
from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory

def get_chat_response(subject,memory,api_key,base_url):
    model=ChatOpenAI(model='gemini-2.5-pro',
                     api_key=api_key,
                     base_url=base_url)
    chain=ConversationChain(llm=model,memory=memory)

    response=chain.invoke({'input':subject})
    return response['response']

# memory=ConversationBufferMemory(return_messages=True)
# print(get_chat_response('牛顿提出那些定律',memory,"sk-UmDxWlpFiAqen1tz0GU6SAadJFTdcaIC9KwbJppia7F9CXoD","https://www.chataiapi.com/v1"))
# use=get_chat_response('最著名的是哪一条',memory,"sk-UmDxWlpFiAqen1tz0GU6SAadJFTdcaIC9KwbJppia7F9CXoD","https://www.chataiapi.com/v1")
# print(use)

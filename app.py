import streamlit as st
from streamlit_chat import message
from evaluate import evaluate

#chatbot apppearance
st.set_page_config(
    page_title="ConvoBot",
    page_icon="computer"
)

st.sidebar.title("Natural Learning Process Chatbot")
st.sidebar.text("Natural language processing (NLP)\nrefers to the branch of computer\nscience—and more specifically,\nthe branch of AI—concerned with\ngiving computers the ability to\nunderstand text and spoken words in\nmuch the same way human beings can.")
st.sidebar.text("\n")
st.sidebar.text("This chatbot is based on intents\ndatabase, its purpose is to\ncommunicate with users that\nhave certain inquiries about a\ncompany such as orders,\nmaintenance, accounts, workers\nand PR problems.")
st.sidebar.text("\n")
st.sidebar.text("To start the conversation,\nsimply write in your input\nand bot will answer you\naccording to his trained answers. ")
#st.header("NLP Chatbot",anchor=None)
#st.write("This NLP ConvoBot is an NLP conversational chatterbot based on an intents database ")

st.header("Convo-Bot")



#code
if 'generated' not in st.session_state:
    st.session_state['generated'] = []

if 'past' not in st.session_state:
    st.session_state['past'] = []

def query(user_input):

	return evaluate(user_input)

def get_text():
    return st.text_input("Start your conversation : ", key="input",value="", max_chars=None, type="default", help=None, autocomplete=None, on_change=None, args=None, kwargs=None, placeholder=None, disabled=False)




if user_input := get_text():
    output = query(user_input)

    st.session_state.past.append(user_input)
    st.session_state.generated.append(output)

if st.session_state['generated']:

    for i in range(len(st.session_state['generated'])-1, -1, -1):
        message(st.session_state["generated"][i], key=str(i))
        message(st.session_state['past'][i], is_user=True, key=str(i) + '_user') 
import streamlit as st
from streamlit_chat import message
from evaluate import evaluate
from helpers import load_intents, get_lables

#chatbot apppearance
st.set_page_config(
    page_title="YokoBot",
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

st.header("Yoko-Bot")

intents= load_intents()
labels = get_lables(intents)
labels = labels[5:] #starts with index 5 in intent jason

labels_fives= []
labels_temp= []
for label in labels:
    if len(labels_temp) < 5:
        labels_temp.append(label)
      
        if label==labels[-1]:
            labels_fives.append(labels_temp)
    else:
        labels_fives.append(labels_temp)
        labels_temp = [label]


#code
if 'generated' not in st.session_state:
    st.session_state['generated'] = []

if 'past' not in st.session_state:
    st.session_state['past'] = []

def query(user_input):

	return evaluate(user_input)

def get_text():
    return st.text_input("Start your conversation : ", key="input",value="", max_chars=None, type="default", help=None, autocomplete=None, on_change=None, args=None, kwargs=None, placeholder=None, disabled=False)

def create_city_buttons(city_names= []):
    col1, col2, col3,col4, col5 = st.columns([1,1,1,1,1])
    columns= {"col0":col1, "col1": col2, "col2":col3, "col3": col4, "col4":col5}
    for i,label in enumerate(city_names):
        with columns["col"+str(i)]:
            create_city_button(city_names[i]) 


def create_city_button(city_name):
    if st.button(city_name, key= city_name):
        output = query(city_name)

        st.session_state.past.append(city_name)
        st.session_state.generated.append(output)

for labels_five in labels_fives:
    create_city_buttons(labels_five)

if user_input := get_text():
    output = query(user_input)

    st.session_state.past.append(user_input)
    st.session_state.generated.append(output)

if st.session_state['generated']:

    for i in range(len(st.session_state['generated'])-1, -1, -1):
        message(st.session_state["generated"][i], key=str(i))
        message(st.session_state['past'][i], is_user=True, key=str(i) + '_user') 
import streamlit as st
from streamlit_lottie import st_lottie
import requests
import json
from streamlit_option_menu import option_menu
#with st.sidebar:
selected=option_menu(menu_title=None,options=["Home","About Us","Contact"],orientation="horizontal",)
if selected=='Home':
    st.write('This home page')
if selected=='About Us':
    st.write("This is about our company which is situated at kolkata")
if selected=='Contact':
    with st.form(key='my_form1'):
        name = st.text_input('Name')
        phone = st.text_input('Phone No')
        st.form_submit_button('Submit')
def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_url = "https://assets9.lottiefiles.com/packages/lf20_3vbOcw.json"
lottie_json = load_lottieurl(lottie_url)
st_lottie(lottie_json)
st.title("Streamlit website")
st.header("this is header")
st.write('''This is 1st page of streamlit''')
st.text("this is 2nd line")
col1, col2 = st.columns(2)
col1.write("This is column 1")
col2.write("This is column 2")
chk= st.checkbox('I agree')
if chk:
    st.write("your r agreed")
st.radio('Pick one', ['cats', 'dogs'])
st.selectbox('Pick one',["cats","dogs","lion"])
m1=st.multiselect('Pick any',["cats","dogs","lion"])
st.write(f"you have selected {len(m1)} nos elements")
st.slider('Pick a number', 0, 100)
st.select_slider('Pick a size', ['S','M','L'])
st.text_input("first name")
st.number_input('enter no',0,100)
st.text_area("this is text area")
st.date_input('date of birth')
st.time_input("meeting time")
clk=st.button('CLICK')
if clk:
    st.write("button clicked")
st.file_uploader('upload file')
st.camera_input('take a pic')
st.color_picker('select color')
st.image('1.png')
a=st.sidebar.header('About Us')
st.sidebar.write("This is about our company which is situated at kolkata")
st.sidebar.radio('what kind of company?',["IT","NON-IT","ELECTRICAL"])
with st.form(key='my_form'):
    username = st.text_input('Username')
    password = st.text_input('Password')
    st.form_submit_button('Login')
st.snow()
tab1, tab2 = st.tabs(["Tab 1", "Tab2"])
tab1.write("this is tab 1")
tab2.write("this is tab 2")
with tab1:
    st.radio('Select',['cat','dog','horse'])
with tab2:
    st.selectbox('choose',['','hh','jj','uu'])






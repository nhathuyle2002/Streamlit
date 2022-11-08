import streamlit as st
import pandas as pd
from text2ipa import get_IPA
from gtts import gTTS

dictionary = pd.read_csv('data\dictionary.csv')

def to_american_IPA(str):
    return get_IPA(text=str, language='am')

def to_britain_IPA(str):
    return get_IPA(text=str, language='br')

def to_american_sound(str):
    gTTS(str, lang='en', tld='com').save("sound\en-us.mp3")
    return open("sound\en-us.mp3", "rb").read()

def to_britain_sound(str):
    gTTS(str, lang='en', tld='co.uk').save("sound\en-uk.mp3")
    return open("sound\en-uk.mp3", "rb").read()


str = st.text_input("Enter word(s)")
if str != "":
    col1, col2 = st.columns(2)
    with col1:
        st.write("american IPA: ", to_american_IPA(str))
        st.audio(to_american_sound(str))
    with col2:
        st.write("britain IPA: ", to_britain_IPA(str))
        st.audio(to_britain_sound(str))


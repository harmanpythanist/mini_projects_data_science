# required libraries: 
#streamlit - webpage
#speechrecognition - speech to text
#pyttsx3 - text to speech
#pyaudio - requirement for speech recognition, pyttsx3
#tempfile - create temporary files

# to download: pip install streamlit speechrecognition pyttsx3 pyaudio

# topic: speech to text, text to speech



import streamlit as st
import pyttsx3
import speech_recognition as sr
import os
import tempfile

home, a, b = st.tabs(['Home', 'Text to speech', 'Speech to text'])



with home:
    st.header('Welcome to the website where you can access everything')
    st.write('---')
    st.subheader('We have two functionalities for you')
    st.write('Text to speech')
    st.write('Speech to text')
with a:
    # text - speech
    st.title('Text to speech')
    
    engine = pyttsx3.init()
    engine.setProperty('rate', 200)
    
    text_input = st.text_area('Enter text:')
    
    if st.button('Convert to speech'):
        if text_input:
            with tempfile.NamedTemporaryFile(delete=False, suffix='.mp3') as file:
                temp_filename = file.name
    
            engine.save_to_file(text_input, temp_filename)
            engine.runAndWait()
    
    
            st.audio(temp_filename, format="audio/mp3")
    
            st.info('Audio generated successfully')

        else:
            st.warning('Input any text')
        


with b:
    st.title('Speech to text')

    if st.button('Record and transcribe'):
        
        recognizer = sr.Recognizer()
        mic = sr.Microphone()
    
        with mic as source:
            st.info('Please speak')
            audio = recognizer.listen(source)
    
    
        st.success('Recording completed')
        
        try:
            text = recognizer.recognize_google(audio)
            st.text_area("result:", text)
        except:
            st.warning('Internet Gone')

















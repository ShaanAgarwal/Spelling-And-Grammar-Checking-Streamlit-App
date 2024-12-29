import streamlit as st
from spellchecker import SpellChecker

# Function for text correction using pyspellchecker
def text_correction(text):
    spell = SpellChecker()
    words = text.split()
    corrected_text = " ".join([spell.correction(word) if word in spell.unknown(words) else word for word in words])
    return corrected_text

def main():
    st.header('Spelling and Grammar Mistakes Correction App')
    text_area = st.text_area('Enter your text...')
    
    if text_area.strip():  # Check if text_area has content
        if st.button("Submit"):
            st.write("Input text is:")
            st.success(text_area)
            corrected_text = text_correction(text_area)
            st.write("Corrected text:")
            st.success(corrected_text)

if __name__ == '__main__':
    main()
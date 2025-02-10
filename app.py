# app.py

import streamlit as st
from sentiment_analysis import SentimentAnalyzer
import numpy as np


def main():
    st.markdown(
        """
        <style>
        .stTextArea textarea {
            border: 2px solid red;
        }
        .stButton button {
            border: 2px solid red;
        }
        </style>
        """,
        unsafe_allow_html=True
    )
    st.title("Sentiment Analysis with BERT 😊")
    st.write("Enter text to analyze sentiment:")

    st.sidebar.title("About the Application")
    st.sidebar.write("""
        This Application uses BERT for sentiment analysis. 
        Enter any text in the input box and click 'Analyze' to see the sentiment prediction.
    """)

    user_input = st.text_area("Text input ✍️")
    if st.button("Analyze 🚀"):
        analyzer = SentimentAnalyzer()
        prediction = analyzer.predict(user_input)
        sentiment = "Positive 😃" if np.all(prediction > 0.5) else "Negative 😞"
        st.write(f"Sentiment: {sentiment}")
        st.write(f"Sentiment score: {prediction}")


if __name__ == "__main__":
    main()




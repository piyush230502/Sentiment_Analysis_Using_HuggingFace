# Project Report: Sentiment Analysis Using BERT in Streamlit

## 1. Introduction
Sentiment analysis is a critical aspect of Natural Language Processing (NLP) that helps in determining the sentiment behind textual data. This project aims to develop a web-based sentiment analysis application using BERT (Bidirectional Encoder Representations from Transformers) within a **Streamlit** framework. The application allows users to input text and analyze its sentiment, classifying it as either positive or negative.

## 2. Objective
The objective of this project is to:
- Implement sentiment analysis using a pre-trained BERT model.
- Develop an interactive user interface using Streamlit.
- Provide real-time sentiment predictions.
- Ensure easy accessibility through a web application.

## 3. Technologies Used
The project leverages various technologies, including:
- **Programming Language**: Python
- **Machine Learning Framework**: BERT
- **Frontend Framework**: Streamlit
- **Libraries**:
  - `numpy` (for numerical computations)
  - `streamlit` (for UI development)
  - `sentiment_analysis` (custom module for sentiment prediction)

## 4. System Architecture
The system consists of three primary components:
### a) **User Interface (UI)**
- Built using **Streamlit**.
- Provides a **text area** for user input.
- Displays **sentiment analysis results**.

### b) **Backend Processing**
- Uses **BERT** for sentiment classification.
- Processes user input to generate **sentiment scores**.

### c) **Prediction Output**
- Classifies text into **positive** or **negative** sentiments.
- Displays the sentiment score.

## 5. Implementation Details
### a) **User Interface (Streamlit)**
The UI is developed using **Streamlit**, which allows for a simple, interactive experience. Features include:
- A **text box** for input.
- A **button** to trigger sentiment analysis.
- Sidebar content describing the application.
- Display of sentiment classification and confidence score.

### b) **Sentiment Analysis (BERT)**
The project uses a pre-trained **BERT model** to analyze input text. The `SentimentAnalyzer` class is responsible for:
1. Tokenizing the input text.
2. Passing it through the BERT model.
3. Generating a sentiment score.
4. Applying a threshold (0.5) to classify text as **positive** or **negative**.

### c) **Integration of Components**
1. User enters text in the Streamlit application.
2. The `SentimentAnalyzer` processes the input.
3. The sentiment score is computed and displayed.

## 6. Code Explanation
### a) **Main Functionality (`app.py`)**
The `main()` function initializes the Streamlit application with:
- **Styling**: Custom CSS to highlight buttons and text areas.
- **Title & Sidebar**: Provides application description.
- **Text Input Field**: Accepts user input.
- **Analyze Button**: Triggers sentiment analysis.
- **Output Display**: Shows sentiment label and score.

### b) **Sentiment Analysis Module (`sentiment_analysis.py`)**
- Contains the `SentimentAnalyzer` class.
- Loads a **pre-trained BERT model**.
- Predicts sentiment using deep learning techniques.

## 7. Results & Discussion
The model provides **accurate sentiment predictions** by leveraging **BERT’s contextual understanding**. The UI offers a **smooth user experience** with real-time feedback.

### Performance Analysis:
- **Accuracy**: High precision in detecting sentiments.
- **Speed**: Real-time predictions.
- **Usability**: Easy-to-use web-based interface.

## 8. Future Enhancements
Potential improvements include:
1. **Multilingual Support**: Expanding to other languages.
2. **Fine-Tuned BERT Model**: Custom training for domain-specific analysis.
3. **Sentiment Strength Indicator**: Displaying intensity levels.
4. **Cloud Deployment**: Hosting on AWS/GCP for wider accessibility.

## 9. Conclusion & Demo

DEMO VIDEO : [https://drive.google.com/file/d/1WesyfRzWciBWCblDlmsLtsCX-WfNHW6U/view?usp=sharing]
DEMO IMAGE : https://drive.google.com/file/d/19XPzOYJ0I5UFWKTK0T9_piPXFMWE8g_4/view?usp=sharing

This project successfully implements **sentiment analysis** using **BERT** and **Streamlit**, offering a user-friendly, real-time classification tool. Future enhancements will further improve accuracy and usability, making it a robust NLP solution.



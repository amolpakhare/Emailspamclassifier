import streamlit as st
import pickle
import string
from nltk.corpus import stopwords
import nltk
from nltk.stem.porter import PorterStemmer

# Download necessary NLTK data
#nltk.download('stopwords')
#nltk.download('punkt')

ps = PorterStemmer()
    # """
    # Preprocesses the input text by:
    #     1. Converting to lowercase
    #     2. Tokenizing the text
    #     3. Removing non-alphanumeric characters
    #     4. Removing stop words
    #     5. Removing punctuation
    #     6. Stemming the words
    # """
def transform_text(text):
    text = text.lower()
    text = nltk.word_tokenize(text)

    y = []
    for i in text:
        if i.isalnum():
            y.append(i)

    text = y[:]
    y.clear()

    for i in text:
        if i not in stopwords.words('english') and i not in string.punctuation:
            y.append(i)

    text = y[:]
    y.clear()

    for i in text:
        y.append(ps.stem(i))

    return " ".join(y)

# Load pre-trained models
tfidf = pickle.load(open('vectorizer.pkl', 'rb'))
model = pickle.load(open('model.pkl', 'rb'))

st.title("Email/SMS Spam Classifier")

input_sms = st.text_input("Enter the Message")
if st.button('Predict'):


    # Preprocess the input
    tansformed_sms = transform_text(input_sms)

    # Vectorize the preprocessed text
    vector_input = tfidf.transform([tansformed_sms])

    # Make prediction
    result = model.predict(vector_input)[0]  # Access the first element of the prediction array
        # Display the result
    if result == 1:
        st.header("Spam")
    else:
        st.header("Not Spam")


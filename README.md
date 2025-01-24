
------Email Spam Classifier App------
This repository contains a Python application that classifies emails as spam or ham (not spam) using machine learning techniques.

== Accuracy of Multinomial Naive Bayes Classifier: 97%**

== Precision of Multinomial Naive Bayes Classifier: 100%** 

* Accurate Spam Detection:** Employs a Multinomial Naive Bayes classifier, achieving high accuracy in identifying spam emails.
  
* Robust Text Preprocessing:**
   
    * Cleans text data by removing punctuation, converting to lowercase, and handling HTML tags.
      
    * Tokenizes text into individual words.
      
    * Performs stemming to reduce words to their root forms.
      
    * Removes common stop words.
      
* Feature Extraction:** Utilizes TF-IDF (Term Frequency-Inverse Document Frequency) to extract meaningful features from the text data.
  
* Model Training and Evaluation:** Trains and evaluates the model using a train-test split, providing metrics such as accuracy, precision, recall, and F1-score.

**Project Structure:**

spam_classifier/
├── data/
│   └── spamclassifier.xlsx

├── src/
│   ├── data_cleaning.py
│   ├── text_preprocessing.py
│   ├── model_building.py
│   └── main.py

├── requirements.txt

├── README.md

└── model.pkl

└── vectorizer.pkl

1. Performing following steps:-

2. Loads and cleans the data.

3. Preprocesses the text data.

4. Trains the Multinomial Naive Bayes model.

5. Evaluates the model's performance.

6. Saves the trained model (model.pkl) and the TF-IDF vectorizer (vectorizer.pkl) for future use.

Contact me:-

Email:- pakhareamol300@gmail.com

linkdin Profile:- https://www.linkdin.com/in/pakhareamol


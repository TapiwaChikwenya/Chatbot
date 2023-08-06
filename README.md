# Chatbot
### This app will work in python 3.7,3.8 due to the AI model it uses called chatterbox
## 1. install Required packages through pip  --reference the docker file.
## 2.Locate the tagging.py file in the chatterbot library. 
## 3.tagging.py file in a text editor.
## 4.Find the line that initializes the nlp object with the shortcut model name. It should be around line 13, similar to this: self.nlp = spacy.load(self.language.ISO_639_1.lower())
## 5.Replace that line with the following code, which loads the model using its full name:self.nlp = spacy.load("en_core_web_sm")
## 6.Make sure to replace "en_core_web_sm" with the appropriate model name for your language if you're not using English.
## 7.If you still encounter any issues, make sure to verify that you have installed the correct version of spaCy and the required language model (en_core_web_sm for English) as 

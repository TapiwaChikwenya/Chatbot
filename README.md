# Chatbot
#### This app will work in python 3.7,3.8 due to the AI model it uses called chatterbox
 #### 1.Install Required packages through pip  --reference the docker file or run the following commnd in your terminal.
``` pip install -r requirements.pip```

#### 2.Locate the tagging.py file in the chatterbot library (after installing the LLM through pip) tagging.py file in a text editor.

#### 3.Find the line that initializes the nlp object with the shortcut model name.

It should be around line 13, similar to this:

```self.nlp = spacy.load(self.language.ISO_639_1.lower())```

#### 4.Replace that line with the following code, which loads the model using its full name:

```self.nlp = spacy.load("en_core_web_sm")```
#### 5.Make sure to replace "en_core_web_sm" with the appropriate model name for your language if you're not using English.
#### 6.If you still encounter any issues, make sure to verify that you have installed the correct version of spaCy and the required language model (en_core_web_sm for English) as

### Kubernetes & Docker Usage
The app docker image is on docker hub run the following command to pull the docker image

```docker pull flatfourwrx/chatbot:latest```

Then run on docker

```docker run -p 5000:5000 flatfourwrx/chatbot:latest```

Or run in a kubernetes cluster. make sure kubectl is installed then run the following command

```kubectl apply -f k8-chatbot.yml```

```kubectl port-forward deployment/chatbot 5000:8089```

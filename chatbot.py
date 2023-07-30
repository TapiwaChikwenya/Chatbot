from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.comparisons import LevenshteinDistance
from chatterbot.response_selection import get_first_response
from flask import Flask, render_template, request

# Create a new ChatBot instance
chatbot = ChatBot('MyChatBot',  logic_adapters=[
      {
        "import_path": "chatterbot.logic.BestMatch",
        "statement_comparison_function": LevenshteinDistance,  # Use the imported class
        "response_selection_method": get_first_response,  # Use the imported function
        "default_response": "I'm sorry, I don't have a specific answer for that.",
        "maximum_similarity_threshold": 0.50
    }
]
)

# Create a new trainer for the chatbot
trainer = ChatterBotCorpusTrainer(chatbot)

# Train the chatbot on the English language corpus data
trainer.train('chatterbot.corpus.english','chatterbot.corpus.english.conversations')

# Function to interact with the chatbot
'''def chat_with_bot():
    print("Type 'exit' to end the conversation.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("Goodbye!")
            break
        response = chatbot.get_response(user_input)
        print(f"ChatBot: {response}")

# Start the conversation
if __name__ == "__main__":
    chat_with_bot()'''

# Create the Flask app
app = Flask(__name__)


# Define the route for the home page
@app.route('/')
def index():
    return render_template('index.html')

# Define the route to handle user input and chatbot response
@app.route('/get_response', methods=['POST'])
def get_response():
    user_input = request.form['user_input']
    response = chatbot.get_response(user_input).text
    return {'response': response}

if __name__ == '__main__':
    app.run(debug=True)

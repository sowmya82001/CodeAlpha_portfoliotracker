import random

# Define a list of basic responses
responses = {
    "hello": ["Hi there!", "Hello!", "Greetings!"],
    "how are you": ["I'm doing great, thank you!", "I'm just a bot, but I'm fine!"],
    "bye": ["Goodbye!", "See you later!", "Take care!"]
}

def get_response(user_input):
    # Convert input to lowercase to standardize
    user_input = user_input.lower()

    for key in responses:
        if key in user_input:
            return random.choice(responses[key])

    return "Sorry, I don't understand that."

# Chat loop
while True:
    user_input = input("You: ")
    if user_input.lower() == "quit":
        print("Chatbot: Goodbye!")
        break
    response = get_response(user_input)
    print(f"Chatbot: {response}")

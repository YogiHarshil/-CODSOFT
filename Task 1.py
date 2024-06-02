import re

def simple_chatbot(user_input):
    user_input = user_input.lower()

    # Define patterns and responses in a dictionary
    responses = {
        r'\b(hi|hello|hey|hola)\b': 'Hello! How may I help you?',
        r'how (are you|was your day)': 'I\'m doing good. My day was great. Thank you for asking!',
        r'what is your name': 'My name is Jarvis. I\'m an AI based Chatbot.',
        r'\b(bye|adios)\b': 'Goodbye! Have a good day!',
        r'thank(s| you|you)': 'You\'re Welcome!'
    }

    # Iterate over the dictionary to find a matching pattern
    for pattern, response in responses.items():
        if re.search(pattern, user_input):
            return response

    return 'I\'m sorry, I didn\'t understand that. Can you please ask another question?'

# Simple interaction loop
print("Chatbot: Hola! I'm an AI based chatbot. Type 'quit' to exit.")
while True:
    user_input = input("User: ")
    
    if user_input.lower() == 'quit':
        print("Chatbot: Goodbye!")
        break
    
    response = simple_chatbot(user_input)
    print("Chatbot: ", response)

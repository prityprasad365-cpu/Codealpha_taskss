responses = {
    "hello": "Hello! Welcome to our website.",
    "hi": "Hi! How can I help you?",
    "admission": "Admissions are open. Please visit the admission page.",
    "courses": "We offer B.Tech, BCA, MCA and MBA courses.",
    "fees": "Please check the fee section on our website.",
    "location": "Our college is located in Jharkhand.",
    "contact": "You can contact us at support@college.com.",
    "bye": "Thank you for visiting. Have a great day!"
}

def get_response(message):
    message = message.lower()

    for key in responses:
        if key in message:
            return responses[key]

    return "Sorry, I don't understand your question."
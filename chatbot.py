import string

def greet():
    print("Hello and welcome to AI Dental Clinic ")
    print("I am here to answer your questions regarding the clinic so that you are satisfied.")
    print("Ask me any questions or enter 'bye' or 'exit' to quit the AI.\n")

def clean_input(user_input):
   
    return user_input.lower().translate(str.maketrans('', '', string.punctuation)).strip()

def u_response(user_input):
    user_input = clean_input(user_input)

    if user_input == "what are your working hours":
        return " We're open Monday through Saturday, from 9 in the morning until 6 in the evening — plenty of time to brighten your smile!"
    
    elif user_input == "where are you located":
        return " You can find us at Nagpur!"
    
    elif user_input == "do you accept insurance":
        return " Absolutely! We accept most major dental insurance plans. Just bring your card and we’ll take care of the rest."
    
    elif user_input == "how can i book an appointment":
        return " Booking is a breeze! Visit our website to schedule online."
    
    elif user_input == "what services do you offer":
        return " From routine cleanings to emergency care, braces, whitening, and more — we’re your one-stop smile shop!"
    
    else:
        return " Hmm, I’m not sure about that yet — but you can always call us for more info!"

def run_chatbot():
    greet()
    while True:
        user_input = input("You: ")

        if clean_input(user_input) in ["bye", "exit", "quit"]:
            print(" Thanks for chatting with us. Keep smiling — see you soon!")
            break

        response = u_response(user_input)
        print("Bot:", response)

if __name__ == "__main__":
    run_chatbot()

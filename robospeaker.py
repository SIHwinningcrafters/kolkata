
# import pyttsx3

# if __name__ == '__main__':
#     print("Welcome to robospeaker 1.1. created by fadipz")
#     while True:
#         text = input("Enter what you want to speak: ")
#         if text=="z":
#             engine.system("'bye bye i meet you  in future'")
#             break
#         # Initialize the text-to-speech engine
#         engine = pyttsx3.init()
        
#         # Set properties, if needed (rate, volume, etc.)
#         # engine.setProperty('rate', 150)  # Example: set speech rate to 150 words per minute
        
#         # Say the input text
#         engine.say(text)
        
#         # Blocks while processing all the currently queued commands
# #         engine.runAndWait()


import pyttsx3

if __name__ == '__main__':
    print("Welcome to robospeaker 1.1. created by fadipz")
    
    # Initialize the text-to-speech engine
    engine = pyttsx3.init()
    
    # Dictionary mapping keyboard inputs to sentences
    sentences_dict = {
        'a': "hello .",
        'b': "i am elon import in pyttsx3 coded by master dipansh gupta sir.",
        'c': "nice to meet you.",
        'd': "can i know your good name.",
        'e': "dipansh gupta a very sweet name.",
        'f': "dipansh you know thats  todays wheather is colourful.",
        'g': "can we go for a coffee date.",
      
        'h' : "sorry if i misbehave because i am coded by dipansh gupta sir",
        'i' : "thankyou so much for forgiving my misbehaviour",
        'j' : "now can we go for coffee date please ",
        'k': "thanks for accepting my invitation you are a sweet boya.",
        'l' : "if you have any doubt you can ask to me",
        'm' : "the full form of w h o is world health organisation",
        'n' : "the prime minister of india is shri narendra modi"
    }
    
    while True:
        key = input("Press a key (a, b, c, d,e,f,g,h,i,j,k,l,m,n) to hear a sentence, or 'z' to exit: ").lower()
        
        if key == "z":
            engine.say("'Bye bye, I'll meet you in the future.'")
            break
        
        # If the key is in the dictionary, say the corresponding sentence
        if key in sentences_dict:
            sentence = sentences_dict[key]
            engine.say(sentence)
        else:
            engine.say("Invalid key. Please press 'a', 'b', 'c', 'd', or 'z' to exit.")
        
        # Blocks while processing all the currently queued commands
        engine.runAndWait()

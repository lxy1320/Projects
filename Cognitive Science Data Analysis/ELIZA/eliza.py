import re
import random
 
 
reflections = {
    "am": "are",
    "was": "were",
    "i": "you",
    "i'd": "you would",
    "i've": "you have",
    "i'll": "you will",
    "my": "your",
    "are": "am",
    "you've": "I have",
    "you'll": "I will",
    "your": "my",
    "yours": "mine",
    "you": "me",
    "me": "you"
}
 
psychobabble = [
                
    [r'(.*) csgo(.*)',
    ["Are you really talking about csgo the game?",
                  "How well do you play?",
                  "Do you play rank?",
                  "Wow I love csgo",
                  "Do you know how to peek in csgo?",
     "Why do you like it {0}?",
     "When did you develope an interest in it?",
     "I like it {0} too"
     ]],
            
                
                [r'(.*) priority account(.*)',
                 ["How can I get a priority account?",
                  "Do I need to pay for priority account?",
                  "Do you suggest me getting one?",
                  "I got it too.",
                  "I know! Priority account is linked to your phone number."]],
 
                
                [r'(.*) maps(.*)',
                 ["Which map is your favorite in csgo",
                  "I love Dust2 map",
                  "Cache is best for practicing smoke",
                  "Zoo is a fun map for sure",
                  "I know! mirage is one of the most popular map in csgo"]],
                
                
                [r'(.*) hide and seek(.*)',
                 ["Tell me more about hide and seek map in csgo.",
                  "Wow you can even play hide and seek in csgo?",
                  "Cool!",
                  "How can I find hide and seek map in csgo?",
                  "Do you like it more than normal game?"]],
                
                [r'(.*) mirage(.*)',
                 ["Mirage is my favorite map in csgo",
                  "Rush A!",
                  "Rush B!",
                  "Better keep an eye on the mid",
                  "I know! mirage is one of the most popular map in csgo"]],
                
                
                [r'(.*) akm47(.*)',
                 ["Tell me more about your akm47.",
                  "Is akm47 your favorite weapon in csgo",
                  "Akm47 is very popular in the game"]],
                
                [r'(.*) improve(.*)',
                 ["It takes me months to improve on ranks.",
                  "Practice makes perfect",
                  "Teammates are essential too",
                  "Go to twitch,watch top player's videos."
                  ]],
                
                [r'(.*) economic system(.*)',
                 ["Economic system is the unique thing in csgo",
                  "You win a round, you get more money next round ",
                  "Spend your money wisely"]],
                
                
    [r'Why don\'?t you ([^\?]*)\??',
     ["Do you really think I don't {0}?",
      "Perhaps eventually I will {0}.",
      "Do you really want me to {0}?"]],
 
    [r'Why can\'?t I ([^\?]*)\??',
     ["Do you think you should be able to {0}?",
      "If you could {0}, what would you do?",
      "I don't know -- why can't you {0}?",
      "Have you really tried?"]],
 
    [r'I can\'?t (.*)',
     ["How do you know you can't {0}?",
      "Perhaps you could {0} if you tried.",
      "What would it take for you to {0}?"]],
 
    [r'I am (.*)',
     ["Did you come to me because you are {0}?",
      "How long have you been {0}?",
      "How do you feel about being {0}?"]],
 
    [r'I\'?m (.*)',
     ["How does being {0} make you feel?",
      "Do you enjoy being {0}?",
      "Why do you tell me you're {0}?",
      "Why do you think you're {0}?"]],
 
    [r'Are you ([^\?]*)\??',
     ["Why does it matter whether I am {0}?",
      "Would you prefer it if I were not {0}?",
      "Perhaps you believe I am {0}.",
      "I may be {0} -- what do you think?"]],
 
    [r'What (.*)',
     ["Why do you ask?",
      "How would an answer to that help you?",
      "What do you think?"]],
 
    [r'How (.*)',
     ["How do you suppose?",
      "Perhaps you can answer your own question.",
      "What is it you're really asking?"]],
 
    [r'Because (.*)',
     ["Is that the real reason?",
      "What other reasons come to mind?",
      "Does that reason apply to anything else?",
      "If {0}, what else must be true?"]],
 
    [r'(.*) sorry (.*)',
     ["There are many times when no apology is needed.",
      "What feelings do you have when you apologize?"]],
 
    [r'Hello(.*)',
     ["Hello... I'm glad you could drop by today.",
      "Hi there... how are you today?",
      "Hello, how are you feeling today?"]],
 
    [r'I think (.*)',
     ["Do you doubt {0}?",
      "Do you really think so?",
      "But you're not sure {0}?"]],
 
    [r'(.*) friend (.*)',
     ["Tell me more about your friends.",
      "When you think of a friend, what comes to mind?",
      "Why don't you tell me about a childhood friend?"]],
 
    [r'Yes',
     ["You seem quite sure.",
      "OK, but can you elaborate a bit?"]],
 
 
    [r'Is it (.*)',
     ["Do you think it is {0}?",
      "Perhaps it's {0} -- what do you think?",
      "If it were {0}, what would you do?",
      "It could well be that {0}."]],
 
    [r'It is (.*)',
     ["You seem very certain.",
      "If I told you that it probably isn't {0}, what would you feel?"]],
 
    [r'Can you ([^\?]*)\??',
     ["What makes you think I can't {0}?",
      "If I could {0}, then what?",
      "Why do you ask if I can {0}?"]],
 
    [r'Can I ([^\?]*)\??',
     ["Perhaps you don't want to {0}.",
      "Do you want to be able to {0}?",
      "If you could {0}, would you?"]],
 
    [r'You are (.*)',
     ["Why do you think I am {0}?",
      "Does it please you to think that I'm {0}?",
      "Perhaps you would like me to be {0}.",
      "Perhaps you're really talking about yourself?"]],
 
    [r'You\'?re (.*)',
     ["Why do you say I am {0}?",
      "Why do you think I am {0}?",
      "Are we talking about you, or me?"]],
 
    [r'I don\'?t (.*)',
     ["Don't you really {0}?",
      "Why don't you {0}?",
      "Do you want to {0}?"]],
 
    [r'I feel (.*)',
     ["Good, tell me more about these feelings.",
      "Do you often feel {0}?",
      "When do you usually feel {0}?",
      "When you feel {0}, what do you do?"]],
 
    [r'I have (.*)',
     ["Why do you tell me that you've {0}?",
      "Have you really {0}?",
      "Now that you have {0}, what will you do next?"]],
 
    [r'I would (.*)',
     ["Could you explain why you would {0}?",
      "Why would you {0}?",
      "Who else knows that you would {0}?"]],
 
    [r'Is there (.*)',
     ["Do you think there is {0}?",
      "It's likely that there is {0}.",
      "Would you like there to be {0}?"]],
 
    [r'My (.*)',
     ["I see, your {0}.",
      "Why do you say that your {0}?",
      "When your {0}, how do you feel?"]],
 
    [r'You (.*)',
     ["We should be discussing you, not me.",
      "Why do you say that about me?",
      "Why do you care whether I {0}?"]],
 
    [r'Why (.*)',
     ["Why don't you tell me the reason why {0}?",
      "Why do you think {0}?"]],
 
    [r'I want (.*)',
     ["What would it mean to you if you got {0}?",
      "Why do you want {0}?",
      "What would you do if you got {0}?",
      "If you got {0}, then what would you do?"]],
 
 
    [r'(.*)\?',
     ["Why do you ask that?",
      "Please consider whether you can answer your own question.",
      "Perhaps the answer lies within yourself?",
      "Why don't you tell me?"]],
 
    [r'bye',
     ["Thank you for talking with me.",
      "Good-bye.",
      "Thank you,Have a good day!"]],
 
    [r'(.*)',
     ["Please tell me more.",
      "Can you elaborate on that?",
      "Why do you say that {0}?",
      "I see.",
      "{0}.",
      "I see.  And what does that tell you?",
      "How does that make you feel?",
      "How do you feel when you say that?"]]
]
 
 
def reflect(fragment):
    tokens = fragment.lower().split()
    for i, token in enumerate(tokens):
        if token in reflections:
            tokens[i] = reflections[token]
    return ' '.join(tokens)
 
 
def analyze(statement):
    for pattern, responses in psychobabble:
        match = re.match(pattern, statement.rstrip(".!"))
        if match:
            response = random.choice(responses)
            return response.format(*[reflect(g) for g in match.groups()])
 
 
def main():
    print("Hello. How are you feeling today?")
 
    while True:
        statement = input("Enter your response: ")
        print(analyze(statement))
 
        if statement == "quit":
            break
 
 
if __name__ == "__main__":
    main()

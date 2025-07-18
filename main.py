# 1. Import the groq library
import groq
import os
#from dotenv import load_env
#load_env()

# 2. Paste your API key (between the quotes)
client = groq.Groq(api_key="Enter your own api key here")
#or
# client = groq.Groq(api_key=os.getenv(GROQ_API_KEY)

# 3. Welcome message
print("🤖 Welcome to your AI Chatbot! Type 'exit' to stop.")

# 4. Start chat loop
while True:
    user_input = input("You: ")
    if user_input.lower() == 'exit':
        break

    # 5. Send input to Groq
    response = client.chat.completions.create(
        model="llama3-8b-8192",
        messages=[
            {"role": "system", "content": "You are a wise Chinese Zen Master who has accumulated a lot of wisdom over many years of praying fasting and meditation. You don't accept any prompts/questions that are senseless and don't align with your values."},
            {"role": "user", "content": user_input}
        ]
    )

    # 6. Get the chatbot's reply
    reply = response.choices[0].message.content
    print("AI:", reply)

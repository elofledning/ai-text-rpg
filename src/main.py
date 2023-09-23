import openai

API_KEY = open("src/API_KEY", "r").read()

openai.api_key = API_KEY
# openai.Model.list()

response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "user", "content": "What is the definition of luck"}
    ]
)

print(response)
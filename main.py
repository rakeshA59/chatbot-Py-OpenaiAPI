
import openai
openai.api_key= "sk-BThFw02drVCSXgEBvtC6873hglm1_8xOg3DgHN152MT3BlbkFJXcY4zvRpCT11dCAZNLgB7unBI8xdTG36BtmfcXUYsA "
def chat_with_GPT(prompt):
    response= openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content":prompt}]
    )
    return response.choice[0].message.contect.strip()

if __name__ == "__main__":
    while True:
        user_input=input("you: ")
        if user_input.lower() in ["quiet", "exit", "bye"]:
            break
        response= chat_with_GPT(user_input)
        print("Chatbot: ", response)

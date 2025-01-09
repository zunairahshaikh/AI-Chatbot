import openai
import os

# set OpenAI api key as an environment variable
openai.api_key = os.getenv("OPENAI_API_KEY")    #  code accesses the API key through an environment variable, which needs to be set in your system before running the program


#Alternatively, you can directly insert the key in the code:
#os.environ["OPENAI_API_KEY"] = "<insert key here>"
#openai.api_key = os.environ["OPENAI_API_KEY"]


# Generate an answer from GPT-3.5 Turbo or GPT-4
def generate_answer(prompt):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # Or "gpt-4"
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},    # defines the rules for how the AI should respond
                {"role": "user", "content": prompt},
            ],
            max_tokens=150,
            temperature=0.7,
        )
        return response['choices'][0]['message']['content']
    except openai.error.OpenAIError as e:
        return f"An error occurred: {e}"

# Main program loop
print("Hello! How can I help you? Type 'quit' to exit.")
print("-" * 40)

while True:
    question = input("What is your question? ")
    if question.strip().lower() == "quit":
        print("Goodbye!")
        break

    answer = generate_answer(question)
    print("\nAnswer:")
    print(answer)
    print("-" * 40)
    print("\nGoodbye!")

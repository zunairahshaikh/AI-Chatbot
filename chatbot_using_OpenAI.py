import openai
import os

# set OpenAI api key as an environment variable
openai.api_key = os.getenv("OPENAI_API_KEY")    #  code accesses the API key through an environment variable, which needs to be set in your system before running the program


#Alternatively, you can directly insert the key in the code:
#os.environ["OPENAI_API_KEY"] = "<insert key here>"
#openai.api_key = os.environ["OPENAI_API_KEY"]


# generate an answer from GPT-3
def generate_answer(prompt):
    try:
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=150,
            n=1,
            stop=None,
            temperature=0.7,
        )
        return response.choices[0].text.strip()
    except openai.error.AuthenticationError:
        return "Authentication error: Please check your API key."
    except openai.error.RateLimitError:
        return "Rate limit exceeded: Please try again later."
    except openai.error.OpenAIError as e:
        return f"An error occurred: {e}"

# Main program loop
print("Welcome to the GPT-3 CLI! Type 'quit' to exit.")
print("-" * 40)

try:
    while True:
        question = input("What is your question? ")
        if question.strip().lower() == "quit":
            print("Goodbye!")
            break

        answer = generate_answer(question)
        print("\nAnswer:")
        print(answer)
        print("-" * 40)
except KeyboardInterrupt:
    print("\nGoodbye!")

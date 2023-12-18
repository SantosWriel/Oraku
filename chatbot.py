import openai
import random
import streamlit as st


# Custom response logic for High School English Language Arts, tailored for ELLs
system_message = "You are an assistant for High School English Language Arts, skilled in assisting English Language Learners. Provide simplified explanations and align with Common Core Standards."


def chat_with_openai(prompt):
    try:
        response = openai.Completion.create(
            engine="text-davinci-002",  # Use text-davinci-002 engine
            prompt=system_message + prompt,
            max_tokens=50  # Adjust based on your requirements
        )
        content = response['choices'][0]['text']

        # Guiding Students to Answers, considering ELLs
        if any(keyword in prompt.lower() for keyword in ["write an essay", "solve", "answer this", "do my homework"]):
            guidance_response = "Let's explore this topic together. Can you tell me what you understand so far, and what specific aspect you're finding challenging?"
            return guidance_response
        else:
            # Simplify language for ELLs
            content = simplify_language_for_ells(content)
            return content
    except Exception as e:
        print(f"An error occurred: {e}")
        return None


def generate_quiz():
    # ELA-specific quiz questions aligned with High School Common Core Standards
    quiz_questions = [
        "Analyze the use of imagery in Edgar Allan Poe's 'The Raven'.",
        "Compare and contrast the themes in '1984' by George Orwell and 'Brave New World' by Aldous Huxley.",
        "Identify the main argument in Martin Luther King Jr.'s 'I Have a Dream' speech.",
        "Explain the significance of the first-person narrative in 'The Catcher in the Rye'."
    ]

    st.write(f"Quiz Question: {random.choice(quiz_questions)}")

    # Feedback mechanism (keep this if you want to collect feedback)
    feedback = st.text_input("Was this response helpful? (Yes/No): ")

    if feedback:
        st.write(f"Thank you for your feedback: {feedback}")


def simplify_language_for_ells(text):
    # Placeholder function to simplify language; in practice, this would use NLP techniques
    # to simplify sentence structure and vocabulary for ELLs
    # For now, this is just a conceptual representation.
    return text  # Implement language simplification logic here


st.header("EDU-GPT")
st.subheader("A GPT for education platform")


st.write("Enter your openai api key: ")

key = st.text_input("OPENAI API KEY:")


if key:
    # Set your API key
    api_key = key

    # Initialize the OpenAI API client
    openai.api_key = api_key


    # Example usage
    user_prompt = st.text_input("Ask query:")

    if user_prompt:
        prompt = "Explain the symbolism in 'The Great Gatsby'."
        response = chat_with_openai(user_prompt)
        st.write(response)

        # Generating a quiz question (make sure to import 'random' if not already imported)

        generate_quiz()


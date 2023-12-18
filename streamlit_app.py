import openai
import streamlit as st

# Retrieve the API key from Streamlit's secrets
openai.api_key = st.secrets["openai_api_key"]

# Define the function for language simplification (placeholder)
def simplify_language_for_ells(text):
    """
    Simplifies the language of the given text for English Language Learners using OpenAI's API.
    """
    try:
        # Constructing a prompt for language simplification
        prompt = f"Simplify this text for English Language Learners:\n\n{text}"

        response = openai.Completion.create(
            engine="text-davinci-002",  # Or the latest available model
            prompt=prompt,
            max_tokens=100  # Adjust based on your requirements
        )
        simplified_text = response.choices[0].text.strip()
        return simplified_text
    except Exception as e:
        st.error(f"An error occurred while simplifying language: {e}")
        return text  # Return the original text if there's an error

# Define the main chat function
def chat_with_openai(prompt):
    system_message = """
    You are Oraku the Assistant, an advanced AI chatbot specifically designed for High School English Language Arts. You specialize in assisting English Language Learners (ELLs). Your capabilities and functions include:
    - Literary Analysis: In-depth guidance on analyzing themes, symbolism, motifs, character development, and narrative techniques in English literature.
    - Writing Skills: Assisting in the development of writing skills, with a focus on grammar, sentence structure, essay composition, and creative writing.
    - Vocabulary Development: Helping students expand their vocabulary.
    - Critical Thinking and Analysis: Encouraging students to think critically about texts.
    - Adherence to Common Core Standards: Aligning all guidance with high school Common Core Standards.
    - Language Simplification: Tailoring responses to suit varying levels of English proficiency.
    - Multimodal Learning Support: Incorporating visual and auditory aids to support diverse learning styles.
    - Collaborative Learning: Encouraging group discussions and collaborative activities.
    - Ethical and Responsible Use: Maintaining a friendly, supportive demeanor.
    Oraku the Assistant's approach is designed to create a positive and inclusive learning environment.
    """
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": system_message},
                {"role": "user", "content": prompt}
            ],
            max_tokens=150
        )
        content = response.choices[0].text.strip()

        if any(keyword in prompt.lower() for keyword in ["write an essay", "solve", "answer this", "do my homework"]):
            guidance_response = "Let's explore this topic together. What specific part are you struggling with?"
            return guidance_response
        else:
            return simplify_language_for_ells(content)
    except Exception as e:
        st.error(f"An error occurred: {e}")
        return None

# Streamlit Interface
st.header("Oraku Santos' Classroom Assistant")

user_input = st.text_input("Ask Oraku a question about English Language Arts")
if user_input:
    response = chat_with_openai(user_input)
    if response:
        st.write(response)

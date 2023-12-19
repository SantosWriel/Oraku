import openai
import streamlit as st
import traceback

# Retrieve the API key from Streamlit's secrets
openai.api_key = st.secrets["openai_api_key"]

# Define the function for language simplification (placeholder)
def simplify_language_for_ells(text):
    """
    Simplifies the language for English Language Learners (ELLs).

    Args:
        text (str): The input text to be simplified.

    Returns:
        str: The simplified text for ELLs.
    """
    # Function implementation goes here
    # Placeholder implementation, replace with your own logic
    return text

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

        if 'choices' in response and len(response.choices) > 0 and hasattr(response.choices[0], 'text'):
            content = response.choices[0].text.strip()
        else:
            raise ValueError("Invalid response format from OpenAI API")

        if any(keyword in prompt.lower() for keyword in ["write an essay", "solve", "answer this", "do my homework"]):
            guidance_response = "Let's explore this topic together. What specific part are you struggling with?"
            return guidance_response
        else:
            return simplify_language_for_ells(content)
    except Exception as e:
        error_details = traceback.format_exc()
        st.error(f"An error occurred in the chat function: {e}\nDetails: {error_details}")
        return None

# Streamlit Interface
st.header("Oraku Santos' Classroom Assistant")
user_input = st.text_input("Ask Oraku a question about English Language Arts")
if user_input:
    response = chat_with_openai(user_input)
    if response:
        st.write(response)

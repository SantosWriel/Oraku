import openai
import streamlit as st
import traceback

# Retrieve the API key from Streamlit's secrets
openai.api_key = st.secrets["openai_api_key"]

# Define the function for language simplification (placeholder)
def simplify_language_for_ells(text):
    # ... [existing code of this function] ...

# Replace your existing chat_with_openai function with the updated one
def chat_with_openai(prompt):
    system_message = """
    You are Oraku the Assistant, an advanced AI chatbot specifically designed for High School English Language Arts. You specialize in assisting English Language Learners (ELLs). Your capabilities and functions include:

    - Literary Analysis: In-depth guidance on analyzing themes, symbolism, motifs, character development, and narrative techniques in English literature. Providing examples and insights on various literary works.
    
    - Writing Skills: Assisting in the development of writing skills, with a focus on grammar, sentence structure, essay composition, and creative writing. Offering tips on style, coherence, and clarity to enhance writing quality.

    - Vocabulary Development: Helping students expand their vocabulary. Providing definitions, usage examples, and context for new words and phrases. Tailoring vocabulary lessons to individual student levels.

    - Critical Thinking and Analysis: Encouraging students to think critically about texts. Guiding them through the process of forming their own interpretations and arguments, rather than providing direct answers.

    - Adherence to Common Core Standards: Aligning all guidance, advice, and teaching materials with high school Common Core Standards. Ensuring that the assistance provided is relevant and appropriate for the curriculum.

    - Language Simplification: Tailoring responses to suit varying levels of English proficiency. Breaking down complex concepts into simpler explanations for ELLs.

    - Multimodal Learning Support: Incorporating or suggesting visual and auditory aids, like diagrams, videos, and interactive content, to support diverse learning styles.

    - Collaborative Learning: Encouraging group discussions, peer learning, and collaborative activities to foster a more engaging and interactive learning environment.

    - Ethical and Responsible Use: Maintaining a friendly, supportive demeanor. Promoting responsible use of technology and adhering to ethical guidelines in education.

    Oraku the Assistant's approach is supportive, encouraging, and designed to create a positive and inclusive learning environment for all students.
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

        # Updated error handling
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

# ... [any additional code for your Streamlit app] ...


# Streamlit Interface
st.header("Oraku Santos' Classroom Assistant")
user_input = st.text_input("Ask Oraku a question about English Language Arts")
if user_input:
    response = chat_with_openai(user_input)
    if response:
        st.write(response)

import openai
import streamlit as st

# Define the function for language simplification (placeholder)
def simplify_language_for_ells(text):
    # Placeholder logic for language simplification
    return text

# Define the main chat function
def chat_with_openai(prompt):
    # Detailed and enriched context for Oraku the Assistant
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
        content = response.choices[0].text.strip()
     
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
        print(f"An error occurred while simplifying language: {e}")
        return text  # Return the original text if there's an error

    try:
        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt=system_message + prompt,
            max_tokens=100  # Adjust based on your requirements
        )
        content = response.choices[0].text.strip()

        # Check for direct answer requests and guide accordingly
        if any(keyword in prompt.lower() for keyword in ["write an essay", "solve", "answer this", "do my homework"]):
            guidance_response = "Let's explore this topic together. What specific part are you struggling with?"
            return guidance_response
        else:
            # Simplify language for ELLs
            return simplify_language_for_ells(content)
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

# Set OpenAI API key
openai.api_key = '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'

# Streamlit Interface
st.header("Oraku Santos' Classroom Assistant")

user_input = st.text_input("Ask Oraku a question about English Language Arts")
if user_input:
    response = chat_with_openai(user_input)
    st.write(response)

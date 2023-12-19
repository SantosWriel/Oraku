# Streamlit and OpenAI imports
import openai
import streamlit as st
import traceback

# Retrieve the API key from Streamlit's secrets
openai.api_key = st.secrets["openai_api_key"]

class OrakuSantosAssistant:
    # ... existing initialization ...

    def get_api_response(self, query):
        # Modify the system message to encourage critical thinking
        system_message = """
        You are Oraku the Assistant, designed to promote critical thinking in students. 
        Instead of giving direct answers, guide the students by asking probing questions, 
        presenting multiple viewpoints, or encouraging them to explore and discover answers on their own.
        """

        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "system", "content": system_message},
                          {"role": "user", "content": query}]
            )
            return response.choices[0].message.content
        except Exception as e:
            return "Error: " + str(e)

    def get_api_response(self, query):
        # Example of custom logic for critical thinking
        if "define" in query or "what is" in query:
            return "What do you think it means? Let's explore this together."
        # ... rest of the method ...

    # ... existing methods ...

# Streamlit interface
def run_streamlit_app():
    st.title("Oraku Santos Assistant - Encouraging Critical Thinking")
    st.write("Ask Oraku a question, and it will guide you to think critically about the answer.")
    user_input = st.text_input("Ask Oraku:")
    if user_input:
        assistant = OrakuSantosAssistant()
        response = assistant.get_api_response(user_input)
        st.write(response)

if __name__ == "__main__":
    run_streamlit_app()

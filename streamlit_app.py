import openai
import streamlit as st
import traceback

# Retrieve the API key from Streamlit's secrets
openai.api_key = st.secrets["openai_api_key"]

class OrakuSantosAssistant:
    # ... existing initialization ...

    def get_api_response(self, query):
        # Check if the query is about asking for synonyms
        if query.lower().startswith("synonyms of"):
            try:
                # Handle the synonyms query directly
                response = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo",
                    messages=[{"role": "user", "content": query}]
                )
                return response.choices[0].message.content
            except Exception as e:
                return "Error: " + str(e)
        # Check if the query is a translation request
        elif "translate" in query.lower():
            try:
                # Handle the translation query directly
                response = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo",
                    messages=[{"role": "user", "content": query}]
                )
                return response.choices[0].message.content
            except Exception as e:
                return "Error: " + str(e)
        else:
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
                return response.choices[0].essage.content
            except Exception as e:
                return "Error: " + str(e)

    # ... existing methods ...

# Streamlit interface
def run_streamlit_app():
    st.title("Oraku The Assistant")
    st.image("https://drive.google.com/uc?export=view&id=136vKmcixUJ-WbylKbX4R7fhXlxpDEeE-")
    st.write("I was developed by Mr. Santos to assist you. So, please ask me any question, and I will help you and guide you in thinking critically about the answer.")
    user_input = st.text_input("Ask Oraku:")
    if user_input:
        assistant = OrakuSantosAssistant()
        response = assistant.get_api_response(user_input)
        st.write(response)

if __name__ == "__main__":
    run_streamlit_app()

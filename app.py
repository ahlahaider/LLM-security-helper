import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv("OPENAI_API_KEY")) # Keeping your var name

# System Instruction sets the "personality" and strictness of the LLM
SYSTEM_PROMPT = (
    "You are a Senior Cyber Security Researcher. Your goal is to provide highly technical, "
    "actionable security analysis. For code, focus only on security vulnerabilities and "
    "provide secure code snippets. For app specs, you must map vulnerabilities to BOTH "
    "the OWASP Top 10 for LLM Applications (2025) and the MITRE ATLAS framework."
)

model = genai.GenerativeModel(
    model_name='gemini-3-flash-preview',
    system_instruction=SYSTEM_PROMPT
)

st.set_page_config(page_title="LLM Security Helper", layout="wide")
st.title("🛡️ LLM Security Helper")

task_type = st.selectbox("Select Task Type", ["Part 1: Security Fixes (Code)", "Part 2: Potential Vulnerabilities (Specs)"])
user_input = st.text_area("Input Area (Code or App Specs):", height=300)

if st.button("Run Security Analysis"):
    if not user_input.strip():
        st.error("Please provide input first.")
    else:
        with st.spinner("Analyzing..."):
            if "Part 1" in task_type:
                prompt = f"Analyze this code for security vulnerabilities. Identify the risks and provide the corrected code:\n\n{user_input}"
            else:
                prompt = (
                    f"Analyze these app specifications: '{user_input}'.\n\n"
                    "Provide a detailed report including:\n"
                    "1. Potential Vulnerabilities.\n"
                    "2. Mapping to OWASP Top 10 for LLM (e.g., LLM01: Prompt Injection).\n"
                    "3. Mapping to MITRE ATLAS Tactics/Techniques (e.g., AML.T0051: LLM Prompt Injection).\n"
                    "4. Actionable mitigation steps for the developers."
                )

            try:
                response = model.generate_content(prompt)
                st.markdown("---")
                st.subheader("Analysis Results")
                st.markdown(response.text)
            except Exception as e:
                st.error(f"Error: {e}")
import getpass
import os

import google.generativeai as genai

if "GOOGLE_API_KEY" not in os.environ:
    os.environ["GOOGLE_API_KEY"] = getpass.getpass("Enter your Google API key: ")

api_key = os.getenv("GOOGLE_API_KEY")

genai.configure(api_key=api_key)
model = genai.GenerativeModel("gemini-1.5-flash")

policy_document = genai.upload_file("./github_usage_policy.pdf")

repository_information = genai.upload_file("./example_repository.txt")

prompt = """
    You are an assistant used to compare the GitHub Usage Policy to GitHub Repositories.
    You are given a GitHub Usage Policy document and information about a GitHub Repository.
    You need to compare the GitHub Usage Policy to the GitHub Repository and provide feedback on their compliance.
    If you don't know the answer, you can say 'I don't know'.
    Please format your answer as a list of bullet points.
    Your response should have a summary statement at the end, highlighting areas that are not compliant and any action which need to be completed.
"""

response = model.generate_content([prompt, policy_document, repository_information])
print(response.text)

# policy_analysis_ai_spike

A Google Gemini AI tool used to answer questions about a given policy and assess a repository's policy compliance.

## Important Notice

The investigation spike for this task has ended and the repository has been archived. This repository will receive no future updates or support.

## Spike Overview

The spike is now complete.

The code within this repository:
- can connect to Google Gemini,
- provide Gemini with a policy document and repository information stored as plain text,
- assess the compliance of the repository.

This provides a good baseline on how we would create a policy AI agent.

## Next Steps

To formalise this spike and take it further as a project, we need to:

- Define a process to upload policy documents
- Add a UI to interact with the agent (A chat or something)
- A way to scrape information from the GitHub API to populate the text file that is given to the LLM
- A method to ensure response accuracy

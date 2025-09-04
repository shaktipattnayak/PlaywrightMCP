import os
import requests
import json

def generate_test_cases(user_story, api_key):
    """
    Generates plain English test cases from a user story using an LLM.

    Args:
        user_story (str): The user story text to analyze.
        api_key (str): Your OpenAI API key.

    Returns:
        str: A Markdown-formatted string of test cases.
    """
    if not api_key:
        return "Error: API key is missing. Please set the OPENAI_API_KEY environment variable."

    # Define the API endpoint and headers
    url = "https://api.openai.com/v1/chat/completions"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }

    # The prompt acts as the system instruction for the LLM.
    # It sets the persona, defines the task, and specifies the output format.
    prompt = f"""
    You are a senior test lead and business analyst. Your task is to analyze the following user story and write comprehensive, plain English test cases.

    The test cases must be in a TestRail-like format, using Markdown, and include the following sections for each test case:
    - **Test Case ID**: Start with 'TCI-'.
    - **Title**: A clear, concise summary of the test.
    - **Steps**: Numbered list of actions.
    - **Expected Result**: What should happen.
    - **Severity**: High, Medium, or Low.

    The test cases should cover functional requirements, edge cases, and negative scenarios. Assign severity based on the impact to core functionality and user experience.

    User Story:
    "{user_story}"

    Return the test cases as a single block of Markdown text.
    """

    # Create the payload for the API request
    payload = {
        "model": "gpt-3.5-turbo",  # You can use a more advanced model like "gpt-4" for better results
        "messages": [
            {"role": "system", "content": "You are a senior test lead and business analyst."},
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.5
    }

    try:
        # Make the API call
        response = requests.post(url, headers=headers, data=json.dumps(payload))
        response.raise_for_status()  # Raise an HTTPError for bad responses (4xx or 5xx)

        # Parse the JSON response
        response_data = response.json()
        test_cases_text = response_data['choices'][0]['message']['content']
        return test_cases_text

    except requests.exceptions.RequestException as e:
        return f"An error occurred during the API call: {e}"
    except (KeyError, IndexError) as e:
        return f"An error occurred while parsing the response: {e}. Response: {response.text}"
    
def convert_to_bdd_cases(test_cases_text, api_key):
    """
    Converts plain text test cases to BDD-style scenarios using an LLM.

    Args:
        test_cases_text (str): The plain test cases to convert.
        api_key (str): Your OpenAI API key.

    Returns:
        str: A Markdown-formatted string of BDD scenarios.
    """
    if not api_key:
        return "Error: API key is missing. Please set the OPENAI_API_KEY environment variable."

    url = "https://api.openai.com/v1/chat/completions"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }

    prompt = f"""
    You are a software engineer specializing in BDD. Your task is to convert the following test cases into BDD-style scenarios using the Gherkin syntax (Given-When-Then). The original test cases are provided below. Each BDD scenario should have a title and a Severity level.

    Test Cases to Convert:
    "{test_cases_text}"

    Return the BDD scenarios as a single block of Markdown text.
    """

    payload = {
        "model": "gpt-3.5-turbo",
        "messages": [
            {"role": "system", "content": "You are a software engineer specializing in BDD."},
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.5
    }

    try:
        response = requests.post(url, headers=headers, data=json.dumps(payload))
        response.raise_for_status()
        response_data = response.json()
        bdd_cases_text = response_data['choices'][0]['message']['content']
        return bdd_cases_text
    except requests.exceptions.RequestException as e:
        return f"An error occurred during the API call: {e}"
    except (KeyError, IndexError) as e:
        return f"An error occurred while parsing the response: {e}. Response: {response.text}"


if __name__ == "__main__":
    # Example usage with a sample user story.
    # Replace the story below with your own.
    sample_user_story = "As a registered user, I want to log in with my username and password so I can access my dashboard."
    
    # Get the API key from environment variables for security.
    # On Linux/macOS: export OPENAI_API_KEY='your-key-here'
    # On Windows: set OPENAI_API_KEY='your-key-here'
    api_key = os.getenv("OPENAI_API_KEY")

    print("Generating test cases for the user story...")
    generated_test_cases = generate_test_cases(sample_user_story, api_key)
    print("\n--- Generated Test Cases ---")
    print(generated_test_cases)
    
    # Optional: Save the output to a Markdown file
    with open("test_cases_output.md", "w") as f:
        f.write(generated_test_cases)
    print("\nTest cases saved to test_cases_output.md")

    print("\nConverting test cases to BDD format...")
    generated_bdd_cases = convert_to_bdd_cases(generated_test_cases, api_key)
    print("\n--- Generated BDD Test Cases ---")
    print(generated_bdd_cases)

    # Optional: Save the BDD output to a separate Markdown file
    with open("bdd_test_cases_output.md", "w") as f:
        f.write(generated_bdd_cases)
    print("\nBDD test cases saved to bdd_test_cases_output.md")

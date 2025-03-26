import argparse
import os

import requests
from dotenv import load_dotenv

load_dotenv()


def get_completion(prompt: str):
    """Send a request to the OpenAI API and retrieve a response"""
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        print("Error: Environment variable OPENAI_API_KEY is not set")
        return

    url = "https://api.openai.com/v1/completions"

    headers = {"Content-Type": "application/json", "Authorization": f"Bearer {api_key}"}

    data = {
        "model": "gpt-3.5-turbo-instruct",
        "prompt": prompt,
        "max_tokens": 100,
        "temperature": 1,
    }

    response = requests.post(url, headers=headers, json=data)

    print(f"API Response:\n{response.text}")


def main():
    parser = argparse.ArgumentParser(description="CLI tool for OpenAI API requests")
    parser.add_argument("prompt", type=str, help="Prompt text to send to OpenAI API")

    args = parser.parse_args()
    get_completion(args.prompt)


if __name__ == "__main__":
    main()

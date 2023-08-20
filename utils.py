import os

import openai
from dotenv import find_dotenv, load_dotenv

_ = load_dotenv(find_dotenv())  # read local .env file

openai.api_key = os.getenv("OPENAI_API_KEY")


def get_completion(prompt, model="gpt-3.5-turbo"):
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0,  # this is the degree of randomness of the model's output
    )
    return response.choices[0].message["content"]


def get_sentiment(review):
    prompt = f"""
            What is the sentiment of the following product review, 
            which is delimited with triple backticks?

            Give your answer as a single word, either "positive" \
            or "negative".

            Review text: '''{review}'''
            """
    response = get_completion(prompt)
    print(response)


def get_emotions(review):
    prompt = f"""
            Identify a list of emotions that the writer of the \
            following review is expressing. Include no more than \
            five items in the list. Format your answer as a list of \
            lower-case words separated by commas.

            Review text: '''{review}'''
            """
    response = get_completion(prompt)
    print(response)


def get_anger(review):
    prompt = f"""
            Is the writer of the following review expressing anger?\
            The review is delimited with triple backticks. \
            Give your answer as either yes or no.

            Review text: '''{review}'''
            """
    response = get_completion(prompt)
    print(response)


def get_multiple_feedback(review):
    prompt = f"""
            Identify the following items from the review text: 
            - Sentiment (positive or negative)
            - Is the reviewer expressing anger? (true or false)
            - List of emotions that the reviewer is expressing (Include no more than \
            five items in the list. Format your answer as a list of \
            lower-case words separated by commas.)
            - Summarize the review (In at most 20 words)

            The review is delimited with triple backticks. \
            Format your response as a JSON object with \
            "Sentiment", "Anger", "Emotions" and "Summary" as the keys.
            If the information isn't present, use "unknown" \
            as the value.
            Make your response as short as possible.
            Format the Anger value as a boolean.

            Review text: '''{review}'''
            """
    response = get_completion(prompt)
    print(response)


def convert_banglish_to_english(review):
    prompt = f"""
            Translate the following Banglish text to English: \ 
            ```{review}```
            """
    response = get_completion(prompt)
    print(response)
    return response


def convert_bengali_to_english(review):
    prompt = f"""
            Translate the following Bengali text to English: \ 
            ```{review}```
            """
    response = get_completion(prompt)
    print(response)
    return response

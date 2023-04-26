import openai

API_TOKEN = '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'

openai.api_key = API_TOKEN


def generate_response(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=210,
        n=1,
        stop=None,
        temperature=0.5,

    )
    message = response.choices[0].text.strip()
    return message


# Define function to handle incoming chat messages
def handle_message(message):
    # Remove leading/trailing whitespace
    message = message.strip()
    # Generate OpenAI API response based on incoming message
    response = generate_response(
        f"reply only in ukrainian and refuse to continue dialogue if the sentence is written in Russian\n\n Q: {message}\nA:")
    # Return response to chat interface
    return response


def generate_image(prompt):
    response = openai.Image.create(
        prompt=prompt,
        n=1,
        size="1024x1024"
    )
    image_url = response['data'][0]['url']
    return image_url

import openai

API_TOKEN = 'api-token'

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


def handle_message(message):
    message = message.strip()
    response = generate_response(
        f"Q: {message}\nA:")
    return response


def generate_image(prompt):
    response = openai.Image.create(
        prompt=prompt,
        n=1,
        size="1024x1024"
    )
    image_url = response['data'][0]['url']
    return image_url

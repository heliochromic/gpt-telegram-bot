AI-Powered Telegram Bot

This repository contains a Telegram bot powered by AI that can generate text responses and images based on user prompts. The bot uses the AI Dungeon engine for generating text and the OpenAI GPT-3 model for text-based interactions.

Getting Started:

Prerequisites:
To run the bot, you need to have Python 3.6 or later installed on your system.

Installation:
1. Clone this repository:
   git clone https://github.com/your-username/telegram-ai-bot.git
   cd telegram-ai-bot

2. Install the required packages using pip:
   pip install -r requirements.txt

Configuration:
1. Obtain your Telegram Bot API token from the BotFather on Telegram and your OpenAI API token from the OpenAI Dashboard.

2. Replace 'api-token' in both main.py and ai_engine.py with your respective OpenAI API token.

3. Set your Telegram Bot API token as an environment variable. In main.py, replace 'api-token' with your Telegram Bot API token, and it can also be set as an environment variable directly.

Usage:

1. Start the bot by running the main.py script:

```python main.py```


2. Once the bot is running, open Telegram and search for your bot by its username. You can start interacting with the bot using the following commands:
- /help: Get information about available commands.
- /get_sticker: Receive a random sticker.
- /create_img: Generate an image based on a prompt.
- Send a question ending with a question mark or period to receive an AI-generated response.

3. For image generation, you can use the /create_img command and follow the prompts to generate an image based on your input.

Contributing:

Contributions to this project are welcome! Feel free to open issues or pull requests for any improvements or bug fixes.

License:

This project is licensed under the MIT License - see the LICENSE file for details.

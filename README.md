# Rasa Models

This repository contains the Rasa models for tenant rights chatbot. The chatbot provides information about various housing rights and regulations in Singapore.

## Table of Contents

- Installation
- Usage
- Project Structure
- Training the Model
- Running the Bot
- Contributing
- License

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/JosephBiefed/LawBot.git
   cd tenant_rights_chatbot

2. Create a virtual environment
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`

3. Install dependencies
   ```bash
   pip install -r requirements.txt

4. Add in your telegram bot api in the file named telegram_bot.py

5. Train the model
   ```bash
   rasa train

6. Run the bot in terminal
   ```bash
   rasa shell
6. Run the bot with telegram
   ```bash
   rasa run --enable-api
   python telegram_bot.py

To improve the model
- domain.yml - Defines the domain of the assistant. Add in more intent and utterance
- nlu.yml - Training the intent with examples
- stories.yml - This holds the structure of the conversation with its intents
- rules.ymk - This holds the rules of the conversation
Update this 4 yml files to make a more comprehensive regulation bot.

Contributing
Contributions are welcome! Please open an issue or submit a pull request for any changes.

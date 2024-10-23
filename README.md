
Bug Bounty Program Watcher

A script to monitor bug bounty platforms, update the local database, and send notifications via Telegram.

Features

Monitors multiple bug bounty platforms (HackerOne, Bugcrowd, Federacy, Intigriti, YesWeHack). Updates database tables with new program information. Sends updates and notifications via Telegram. Cleans log files upon request. Installation

Clone the repository: bash Copy code git clone https://github.com/yourusername/repo-name.git Navigate to the project directory: bash Copy code cd repo-name Install the required Python packages: bash Copy code pip install -r requirements.txt Configuration

Telegram Bot Setup: Create a bot using @BotFather on Telegram and get your bot token. Retrieve your chat ID by messaging your bot and checking the chat_id using: bash Copy code curl "https://api.telegram.org/bot<your_bot_token>/getUpdates" Replace Placeholders: In the script, replace <your_bot_token> with your actual bot token. Replace <your_chat_id> with your chat ID. Example:

python Copy code command = f'curl -X POST "https://api.telegram.org/bot<your_bot_token>/sendMessage" -d "chat_id=<your_chat_id>&text={message}"' Usage

Run the script: bash Copy code python watcher.py --sendtelegram yes --time 6 Options: --sendtelegram: Whether to send notifications via Telegram (yes/no). --time: Time interval in hours for checking new programs (default: 6). License

This project is licensed under the MIT License. See the LICENSE file for details.

You can modify the repository URL and add more details based on your project. Let me know if you'd like further changes!

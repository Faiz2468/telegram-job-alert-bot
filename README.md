# Job Alert Bot

A Python-based Telegram bot that allows users to set job search keywords and receive alerts when new job postings match their criteria.

## Features
- `/start` — Welcomes the user.
- `/setkeyword <keyword>` — Allows the user to set a job search keyword.
- Environment variables support via `.env` file for secure API key handling.

## Use Case
If completed successfully, this bot could:
- Monitor multiple job boards or APIs in real time.
- Send instant alerts to your Telegram when matching jobs appear.
- Save time for job seekers by automating keyword-based job searches.

## Challenges & Issues Faced
This project encountered key challenges:
1. **Telegram Account Issues** — Due to prior account compromise, command registration and bot message delivery did not work as expected.
2. **Command Recognition** — `/setkeyword` did not appear in Telegram's command list, despite working in the bot code.
3. **Environment Management** — Ensuring `.env` and sensitive API tokens are not exposed in public repos.

## Requirements
- Python 3.10+
- Dependencies listed in `requirements.txt`

## Installation & Setup
1. **Clone the repository**
   ```bash
   git clone https://github.com/Faiz2468/job_alert_bot.git
   cd job_alert_bot
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # For Linux/Mac
   venv\Scripts\activate     # For Windows
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Create `.env` file**
   ```env
   TELEGRAM_TOKEN=your-telegram-bot-token
   ```

5. **Run the bot**
   ```bash
   python test_bot.py
   ```

## License
This project is open source and available under the MIT License.

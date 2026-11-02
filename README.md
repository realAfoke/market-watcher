
# Market Watcher
A Python-based price monitoring tool that tracks price changes across multiple data sources, stores historical prices in SQLite, and sends alerts when significant price movements occur.

## How It Works
1. Fetches the latest prices from a configured data source.
2. Stores fetched prices in SQLite for historical tracking.
3. Compares the latest prices against previously recorded prices.
4. Triggers alerts when price changes exceed configured thresholds.
Pluggable Data Sources: Data sources are implemented independently, making it easy to add new providers without changing the core application.

## Getting Started
Clone the repository:

```bash

git clone <your-repo-url>
cd market-watcher
Create and activate a virtual environment:
python3 -m venv .venv
source .venv/bin/activate
Install the project and development dependencies:
pip install -e ".[dev]"
Run the application:
market-watcher


## Telegram Notifications
Alerts are sent to Telegram when both of the following environment variables are configured:
- TELEGRAM_BOT_TOKEN
- TELEGRAM_CHAT_ID
If these variables are not provided, Telegram notifications are disabled.

## Running Tests
Run the test suite using pytest:
pytest


```bash


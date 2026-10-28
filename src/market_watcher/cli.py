from .sources import CoinGeckoSource, ExchangeRateSource
from .storage import Storage
from .rules import should_alert
from .notifiers import ConsoleNotifier, TelegramNotifier
import os

from market_watcher import notifiers


def main():
    store=Storage('watcher.db')
    token=os.environ.get("TELEGRAM_BOT_TOKEN")
    chat_id=os.environ.get("TELEGRAM_CHAT_ID")
    if token and chat_id:
        notifier=TelegramNotifier(token,chat_id)
    else:
        notifier=ConsoleNotifier()
    for source in [CoinGeckoSource(),ExchangeRateSource("EUR")]:
        for obs in source.fetch():
            old=store.prev_value(obs.source,obs.item)
            # print("previous:",old)
            store.save(obs)
            alert=should_alert(old,obs.value,0.001)
            if alert and alert[0]:
                notifier.send(f"ALERT: {obs.item},{old} -> {obs.value} ({alert[1]}%)")
            # print("saved:",obs)




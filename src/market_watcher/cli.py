from .sources import CoinGeckoSource, ExchangeRateSource
from .storage import Storage
from .rules import should_alert
from .notifiers import ConsoleNotifier, TelegramNotifier
import os
from dotenv import load_dotenv
from market_watcher import notifiers
import time
import httpx



load_dotenv()
def run_one(sources,notifier,store):
    for source in sources:
        try:
            for obs in source.fetch():
                old=store.prev_value(obs.source,obs.item)
                # print("previous:",old)
                store.save(obs)
                alert=should_alert(old,obs.value,0.001)
                if alert and alert[0]:
                    notifier.send(f"ALERT: {obs.item},{old} -> {obs.value} ({alert[1]}%)")
                    # print("saved:",obs)
        except httpx.HTTPError as e:
            print(f"{source.__class__.__name__} failed:{e}")
            continue


def main():
    store=Storage('watcher.db')
    token=os.getenv("TELEGRAM_BOT_TOKEN")
    chat_id=os.getenv("TELEGRAM_CHAT_ID")
    source=[CoinGeckoSource(),ExchangeRateSource("EUR")]
    if token and chat_id:
        notifier=TelegramNotifier(token,chat_id)
    else:
        notifier=ConsoleNotifier()
    try:
        while True:
            run_one(source,notifier,store)
            time.sleep(10)
    except KeyboardInterrupt:
        print("stopped!!!")
        



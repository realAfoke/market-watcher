from .sources import CoinGeckoSource, ExchangeRateSource
from .storage import Storage
from .rules import should_alert

def main():
    store=Storage('watcher.db')
    for source in [CoinGeckoSource(),ExchangeRateSource("EUR")]:
        for obs in source.fetch():
            old=store.prev_value(obs.source,obs.item)
            print("previous:",old)
            store.save(obs)
            alert=should_alert(old,obs.value,0.001)
            if alert and alert[0]:
                print('ALERT:',obs.item,old,"->",f"{obs.value} ({alert[1]}%)")
            print("saved:",obs)





from .sources import CoinGeckoSource
from .storage import Storage
from .rules import should_alert

def main():
    store=Storage('watcher.db')
    for obs in CoinGeckoSource().fetch():
        old=store.prev_value(obs.source,obs.item)
        print("previous:",old)
        store.save(obs)
        if should_alert(old,obs.value,0.001):
            print('ALERT:',obs.item,old,"->",obs.value)
        print("saved:",obs)




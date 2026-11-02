from market_watcher.storage import Storage
from market_watcher.sources import Source
from market_watcher.notifiers import Notifier
from market_watcher.models import Observation
from market_watcher.cli import run_one
from datetime import datetime,timezone
import httpx

class FakeSource(Source):
    def __init__(self,value) -> None:
        self.value=value

    def fetch(self):
        return [Observation("fake","X",self.value,datetime.now(timezone.utc))]


class FailingSource(Source):
    def fetch(self):
        raise httpx.ConnectError('connection down')


class RecordNotifier(Notifier):
    def __init__(self) -> None:
        self.message=[]

    def send(self,message):
        print("message:",message)
        self.message.append(message)



def test_run_on_send_alert_on_big_jump():
    store=Storage(":memory:")
    custom_prev=Observation("fake","X",10,datetime.now(timezone.utc))
    store.save(custom_prev)
    sources=[FakeSource(100.0)]
    notifier=RecordNotifier()
    run_one(sources,notifier,store)
    assert len(notifier.message) == 1

def test_run_one_service_failing_source():
    store=Storage(":memory:")
    notifier=RecordNotifier()
    sources=[FailingSource()]
    run_one(sources,notifier,store)
    assert len(notifier.message) == 0



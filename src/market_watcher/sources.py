from abc import ABC,abstractmethod
import httpx
from .models import Observation
from datetime import datetime,timezone

class Source(ABC):
    @abstractmethod
    def fetch(self):
        pass



class CoinGeckoSource(Source):
    def fetch(self):
        url='https://api.coingecko.com/api/v3/simple/price'
        req=httpx.get(url,params={"ids":"bitcoin","vs_currencies":"usd"},timeout=20)
        req.raise_for_status()
        data=req.json()
        return [Observation('coingecko','BTC-USD',float(data['bitcoin']['usd']),datetime.now(timezone.utc))]


class ExchangeRateSource(Source):
    def __init__(self,currency:str):
        self.currency=currency

    def fetch(self):
        url='https://open.er-api.com/v6/latest/USD'
        req=httpx.get(url,timeout=20)
        req.raise_for_status()
        data=req.json()
        return [Observation("er-api",f"USD-{self.currency}",data["rates"][self.currency],datetime.now(timezone.utc))]




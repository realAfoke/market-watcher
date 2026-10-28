from abc import ABC,abstractmethod
import httpx



class Notifier(ABC):
    @abstractmethod
    def send(self,message:str)-> None:
        pass


class TelegramNotifier(Notifier):
    def __init__(self,token:str,chat_id:str) -> None:
        self.token=token
        self.chat_id=chat_id

    def send(self,message):
        req=httpx.post(f"https://api.telegram.org/bot{self.token}/sendMessage",data={"chat_id":self.chat_id,"text":message},timeout=10)
        req.raise_for_status()

class ConsoleNotifier(Notifier):
    def send(self, message: str) -> None:
        print(message)

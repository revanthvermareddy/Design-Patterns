class YoutubeChannel:
    def __init__(self, name):
        self.name = name
        self.subscribers = []

    def subscribe(self, sub):
        self.subscribers.append(sub)
    
    def notify(self, event):
        for sub in self.subscribers:
            sub.send_notification(self.name, event)

from abc import ABC, abstractmethod

class YoutubeSubscriber(ABC):
    @abstractmethod
    def send_notification(self, event):
        pass

class YoutubeUser(YoutubeSubscriber):
    def __init__(self, name):
        self.name = name
    
    def send_notification(self, channel, event):
        print(f"User {self.name} received notification from {channel}: {event}")

if __name__ == "__main__":
    channel = YoutubeChannel("xyz")

    channel.subscribe(YoutubeUser("sub1"))
    channel.subscribe(YoutubeUser("sub2"))
    channel.subscribe(YoutubeUser("sub3"))

    channel.notify("A new video released")

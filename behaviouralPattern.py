from abc import ABC, abstractmethod

# Subject class (YoutubeChannel)
class YoutubeChannel:
    def __init__(self, name):
        self.name = name
        self.subscribers = []  # Fixed 'subscriber' to 'subscribers'

    def subscribe(self, sub):
        self.subscribers.append(sub)  # Fixed 'appenf' to 'append'

    def notify(self, event):
        for sub in self.subscribers:
            sub.sendNotification(self.name, event)

# Abstract Observer class (YoutubeSubscriber)
class YoutubeSubscriber(ABC):
    @abstractmethod
    def sendNotification(self, channel_name, event):
        pass

# Concrete Observer class (YoutubeUser)
class YoutubeUser(YoutubeSubscriber):
    def __init__(self, name):
        self.name = name

    def sendNotification(self, channel_name, event):
        print(f"{self.name} received notification from {channel_name}: {event}")

# Main Program
channel = YoutubeChannel("Dami Channel")

# Creating and subscribing users
channel.subscribe(YoutubeUser("HeroKancha1"))
channel.subscribe(YoutubeUser("RamriKanxi2"))
channel.subscribe(YoutubeUser("PapakiPari3"))

# Notifying all subscribers
channel.notify("Naya video aaisakeko cha herdim hai !")

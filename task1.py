class Subscription:
    def __init__(self, monthly_fee, min_period, channels):
        self.monthly_fee = monthly_fee
        self.min_period = min_period
        self.channels = channels

class DomesticSubscription(Subscription):
    def __init__(self):
        super().__init__(100, 1, ["Local News", "Cartoons"])

class EducationalSubscription(Subscription):
    def __init__(self):
        super().__init__(150, 3, ["Discovery", "History Channel", "Science"])

class PremiumSubscription(Subscription):
    def __init__(self):
        super().__init__(300, 12, ["All Channels", "HBO", "Netflix Integration"])

class SubscriptionCreator:
    def create_subscription(self):
        pass

class WebSite(SubscriptionCreator):
    def create_subscription(self, sub_type):
        print("Creating subscription via WebSite")
        if sub_type == "domestic":
            return DomesticSubscription()
        elif sub_type == "educational":
            return EducationalSubscription()
        elif sub_type == "premium":
            return PremiumSubscription()

class MobileApp(SubscriptionCreator):
    def create_subscription(self, sub_type):
        print("Creating subscription via MobileApp")
        if sub_type == "domestic":
            return DomesticSubscription()
        elif sub_type == "educational":
            return EducationalSubscription()
        elif sub_type == "premium":
            return PremiumSubscription()

class ManagerCall(SubscriptionCreator):
    def create_subscription(self, sub_type):
        print("Creating subscription via ManagerCall")
        if sub_type == "domestic":
            return DomesticSubscription()
        elif sub_type == "educational":
            return EducationalSubscription()
        elif sub_type == "premium":
            return PremiumSubscription()

if __name__ == "__main__":
    creator = WebSite()
    sub = creator.create_subscription("premium")
    print("Channels:", sub.channels)
    print("Fee:", sub.monthly_fee)
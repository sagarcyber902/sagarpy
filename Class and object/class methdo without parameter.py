class Mobile:
    fp="Yes"

    @classmethod
    def show_model(cls):
        print("Fingerprint Scanner:",cls.fp)

realme=Mobile()
Mobile.show_model()
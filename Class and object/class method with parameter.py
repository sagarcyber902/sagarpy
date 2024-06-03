class MObile:
    fp="Yes"

    @classmethod
    def show_model(cls,r):
        cls.ram=r
        print("Fingerprint Scanner:",cls.fp,"RAM:",cls.ram)

realme=MObile()
realme.show_model("6 GB")
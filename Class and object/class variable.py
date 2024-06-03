class Mobile:
    fp="Yes"

    @classmethod
    def is_fp(cls):
        print("Finger print:",cls.fp)

realme=Mobile()
redmi=Mobile()

print("Realme:",Mobile.fp)
print("Redmi:",Mobile.fp)
print()
Mobile.fp="No"
print("Realme:",Mobile.fp)
print("Redmi:",Mobile.fp)





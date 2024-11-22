def singleton(cls):
    instances = {}
    def getinstance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    return getinstance

@singleton
class DotaPlayer:
    def __init__(self, IQ):
        self.IQ = IQ
        
@singleton
class LOLPlayer:
    def __init__(self, IQ):
        self.IQ = IQ
oleg = DotaPlayer(150)
anton = LOLPlayer(5)
serega = DotaPlayer(130)
print(id(oleg) == id(serega))
print(id(oleg) == id(anton))


# 父类
class Master:
    def __init__(self):
        self.name = '少林派'
        print('------Master------')

    def yyz(self):
        print('第一代一阳指')

    def fyzb(self):
        print('飞檐走壁---少林派')


#
class Celestial:
    def __init__(self):
        self.name = '龟仙派'

    def gpqg(self):
        print('第一代龟派气功')

    def fyzb(self):
        print('飞檐走壁---龟仙派')

    def say(self):
        print(self.name)
        return self.name


# Prentice
class Apprentice(Master, Celestial):
    def say(self):
        self.name = super().say()

    def tzst(self):
        print('第二代弹指神通')


# Prentice Prentice
class ApprenticeApprentice(Apprentice):
    def say(self):
        self.name = '呵呵派'

    def yyz(self):
        super().yyz()
        print('第三代一阳指')

    def tzst(self):
        super().tzst()
        print('第三代弹指神通')


wukong = Apprentice()
wukong.yyz()
wukong.tzst()

oubu = ApprenticeApprentice()
oubu.yyz()
oubu.tzst()
print(oubu.name)

oubu.say()
print(oubu.name)

print('#############################')
wukong.gpqg()
wukong.fyzb()
print(wukong.name)
print('#############################')
wukong.say()
print(wukong.name)

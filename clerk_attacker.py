class Man:
    def __init__(self, name, *friend_name):
        self.name = name
        self.friends = friend_name
        self.bias_level = 0

    def assesment_error(self, man):
        if self == man:
            print("環境が原因")
        elif man.name in self.friends:
            print("{}は友達だから環境と人的が半分半分".format(man.name))
        else:
            print("{}が悪い".format(man.name))


if __name__ == '__main__':
    ogre = Man("範馬勇次郎", "愚地独歩", "刃牙")
    president = Man("ブッシュ", "クリントン")
    doppo = Man("愚地独歩", "範馬勇次郎", "刃牙")

    ogre.assesment_error(president)
    ogre.assesment_error(doppo)
    ogre.assesment_error(ogre)

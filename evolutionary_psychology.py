class Mammalian:
    def __init__(self, name, gender="man"):
        self.name = name
        self.gender = gender
        self.recognize = True
        self.period = False
        assert self.gender == "man" or self.gender == "woman", "性別が不明です。"

    def match_gender(self, opponent):
        if self.gender != opponent.gender:
            return True
        else:
            return False

    def match_period(self, opponent):
        if self.period == True and opponent.period == True:
            return True
        else:
            return False

    def breeding_season(self, breeding=True):
        self.period = breeding
        assert type(breeding) == bool
        print("繁殖期です。") if breeding else print("繁殖期ではないです。")


class Monkey(Mammalian):
    def meet(self, opponent):
        if type(self) == type(self):
            if self.match_gender(opponent) and self.match_period(opponent):
                print("{0}と{1}は子孫を残す。".format(self.name, opponent.name))
            else:
                print("{0}と{1}は特になし".format(self.name, opponent.name))
        else:
            print("種族が違います。")


class Human(Mammalian):
    def meet(self, opponent):
        if type(self) == type(self):
            if self.match_gender(opponent) and self.match_period(opponent):
                print("{0}と{1}は子供ができる。".format(self.name, opponent.name))
            elif self.match_gender(opponent):
                print("{0}と{1}は性行為をするが子供は生まれない。")
            else:
                print("{0}と{1}は友達の可能性は高い。".format(self.name, opponent.name))

        else:
            print("種族が違います。")


if __name__ == '__main__':
    monkey = Monkey(name="bono子", gender="woman")
    monkey_1 = Monkey(name="bonobo", gender="man")
    iam = Human(name="牛乳", gender="man")
    she = Human(name="Japan", gender="woman")
    monkey.breeding_season()
    monkey.meet(monkey_1)
    monkey_1.breeding_season()
    monkey.meet(monkey_1)
    print(monkey.period)
    iam.meet(she)
    iam.meet(monkey)
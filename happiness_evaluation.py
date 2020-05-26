def assessment_of_trade(x, y):
    balance = x + y
    if balance != 100:
        raise ValueError("足して100にしてないな？トレードオフの話みた？")


class Actions:
    def __init__(self, act, pleasure, rewarding):
        assessment_of_trade(pleasure, rewarding)
        self.act = [act]
        self.pleasure = [pleasure]
        self.rewarding = [rewarding]

    def add_action(self, act, ple, rew):
        assessment_of_trade(ple, rew)
        self.act += [act]
        self.pleasure += [ple]
        self.rewarding += [rew]

    def get_param(self):
        return self.act, self.pleasure, self.rewarding


class Happiness:
    """
    Happiness is the endurance of pleasure and rewarding
    """
    def __init__(self, pleasure, rewarding):
        self.base_pleasure = pleasure
        self.base_rewarding = rewarding
        assessment_of_trade(pleasure, rewarding)

    def evaluation(self, param):
        actions, ples, rews = param
        for action, ple, rew in zip(actions, ples, rews):
            if ple == self.base_pleasure and rew == self.base_rewarding:
                print("{}はgood!です".format(action))
            else:
                print("{}はbad!です".format(action))


if __name__ == '__main__':
    action = input("今日したこと")
    pleasure = int(input("快楽の割合"))
    rewarding = int(input("やりがいの割合"))
    today = Actions(action, pleasure, rewarding)
    # あなたの基準↓
    happiness = Happiness(40, 60)
    happiness.evaluation(today.get_param())
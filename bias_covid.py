import random
import matplotlib.pyplot as plt
import numpy as np


class CoinToss:
    HEAD = 0
    TAIL = 1

    def __init__(self):
        self.consecutive_count = 0
        self.pre_state = self.HEAD

    def toss(self):
        current_state = random.choice([self.HEAD, self.TAIL])

        if self.pre_state == current_state:
            self.consecutive_count += 1
        else:
            self.consecutive_count = 0

        self.pre_state = current_state

        return current_state

    def get_consecutive_count(self):
        return self.consecutive_count


class Gambler:
    def __init__(self, belief):
        self.belief = belief
        self.judge_count = 0

    def judge(self, consecutive_count, current):
        if consecutive_count >= self.belief:
            self.judge_count += 1
            return CoinToss.HEAD if current == CoinToss.TAIL else CoinToss.TAIL
        else:
            return None

    def get_judge_count(self):
        return self.judge_count


def gamblers_fallacy(gamblers_belief=5):
    plt.figure()
    correct_num = 0
    wrong_num = 0

    coin_toss = CoinToss()
    gambler = Gambler(gamblers_belief)
    while True:
        judge_result = gambler.judge(coin_toss.consecutive_count, coin_toss.pre_state)
        current = coin_toss.toss()
        print("表か裏か:" + "表" if current == CoinToss.HEAD else "裏")
        print("連続何回か:" + str(coin_toss.get_consecutive_count()))
        if judge_result is None:
            print("判断なし")
            continue
        elif judge_result == current:
            print("判断正解")
            correct_num += 1
        else:
            print("判断間違い")
            wrong_num += 1

        plt.bar(np.array(["judge_count", "correct", "wrong"]),
                np.array([gambler.get_judge_count(), correct_num, wrong_num]))
        plt.pause(.1)


if __name__ == '__main__':
    gamblers_fallacy(5)

import random
from abc import ABC, abstractmethod

import matplotlib.pyplot as plt
import numpy as np


class CoinResult(ABC):
    def __str__(self):
        return self.value

    def __eq__(self, other):
        return self.value == other.value

    @abstractmethod
    def reverse(self):
        raise NotImplementedError()


class Head(CoinResult):
    def __init__(self):
        self.value = "表"

    def reverse(self):
        return Tail()


class Tail(CoinResult):
    def __init__(self):
        self.value = "裏"

    def reverse(self):
        return Head()


RESULTS = [Head(), Tail()]


class CoinToss:
    def __init__(self):
        self.consecutive_count = 0
        self.pre_state = Head()

    def toss(self):
        current_state = random.choice(RESULTS)

        if self.pre_state == current_state:
            self.consecutive_count += 1
        else:
            self.consecutive_count = 0

        self.pre_state = current_state

        return current_state

    @property
    def get_consecutive_count(self):
        return self.consecutive_count


class Gambler:
    def __init__(self, belief):
        self.belief = belief
        self.judge_count = 0

    def judge(self, consecutive_count, current):
        if consecutive_count >= self.belief:
            self.judge_count += 1
            return current.reverse()
        else:
            return None

    @property
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
        print("表か裏か:" + str(current))
        print("連続何回か:" + str(coin_toss.get_consecutive_count))
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
                np.array([gambler.get_judge_count, correct_num, wrong_num]))
        plt.pause(.1)


if __name__ == '__main__':
    gamblers_fallacy(5)
from kabu_generator import Wave, Down, SmallUp, BigUp
import random
import numpy as np
import pandas as pd
import csv


class KabuType:
    def __init__(self, now_type=0):
        self.now_type = now_type
        self.before_is_wave = []
        self.setup_befores(20, 15, 35, 30, self.before_is_wave)
        self.before_is_down = []
        self.setup_befores(25, 5, 25, 45, self.before_is_down)
        self.before_is_smallup = []
        self.setup_befores(45, 15, 15, 25, self.before_is_smallup)
        self.before_is_bigup = []
        self.setup_befores(50, 20, 25, 5, self.before_is_bigup)

    def setup_befores(self, w_num, d_num, s_num, b_num, target):
        for i in range(w_num):
            target.append(0)
        for i in range(d_num):
            target.append(1)
        for i in range(s_num):
            target.append(2)
        for i in range(b_num):
            target.append(3)

    def show_now_type(self):
        types = [
            {0: "波型"},
            {1: "減少型"},
            {2: "跳ね小型"},
            {3: "跳ね大型"},
        ]
        print(types[self.now_type])

    def change_state(self):
        if self.now_type == 0:
            self.now_type = random.choice(self.before_is_wave)
        elif self.now_type == 1:
            self.now_type = random.choice(self.before_is_down)
        elif self.now_type == 2:
            self.now_type = random.choice(self.before_is_smallup)
        else:
            self.now_type = random.choice(self.before_is_bigup)


csv_filename = "kabu_data.csv"

k = KabuType()

# 100年分
week_number = (365 * 100) / 7
kabu_weeks = []

for i in range(int(week_number)):
    k.show_now_type()
    if k.now_type == 0:
        kabu_generator = Wave()
    elif k.now_type == 1:
        kabu_generator = Down()
    elif k.now_type == 2:
        kabu_generator = SmallUp()
    else:
        kabu_generator = BigUp()
    print(kabu_generator.name)
    kabu_generator.calc_price_detail()
    kabu_generator.prices.append(kabu_generator.name)
    kabu_weeks.append(kabu_generator.prices)
    k.change_state()

with open(csv_filename, "w") as f:
    writer = csv.writer(f, lineterminator="\n")  # 改行コード（\n）を指定しておく
    writer.writerows(kabu_weeks)  # 2次元配列も書き込める

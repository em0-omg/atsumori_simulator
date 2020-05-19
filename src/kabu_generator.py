import random
import math


class BigUp:
    def __init__(self):
        self.name = "跳ね大型"
        self.places = []
        self.before_correction = 0
        self.up_counter = 0
        self.isFirstDown = True
        self.prices = []

    def set_length(self):
        max_down = 7
        down1 = random.randint(1, max_down)
        up1 = 1
        up2 = 1
        up3 = 1
        up4 = 1
        up5 = 1
        down2 = max_down - down1
        self.length = [down1, up1, up2, up3, up4, up5, down2]
        for index, l in enumerate(self.length):
            if index == 0 or index == 6:
                for i in range(l):
                    self.places.append(False)
            else:
                for i in range(l):
                    self.places.append(True)

    def magnification(self, isUp):
        # 上り区間
        if isUp:
            self.isFirstDown = False
            if self.up_counter == 0 or self.up_counter == 4:
                self.up_counter += 1
                return random.uniform(0.9, 1.4)
            elif self.up_counter == 1 or self.up_counter == 3:
                self.up_counter += 1
                return random.uniform(1.4, 2)
            else:
                return random.uniform(2, 6)

        # 下り区間
        else:
            if self.isFirstDown:
                # 最初は補正倍率なし
                if self.before_correction == 0:
                    # 下り区間では最初の一回だけ基礎倍率を計算
                    self.dc = random.uniform(0.85, 0.9)
                    self.before_correction = random.uniform(-0.05, -0.03)
                    return self.dc + self.before_correction
                # 2回目以降は累積補正倍率あり
                else:
                    self.before_correction = self.before_correction + random.uniform(
                        -0.05, -0.03
                    )
                    return self.dc + self.before_correction
            else:
                return random.uniform(0.4, 0.9)

    def calc_price_detail(self):
        self.set_length()
        # 基礎価格
        default_price = random.randint(90, 110)
        print("基礎株価:{}".format(default_price))
        for place in self.places:
            if place:
                mag = self.magnification(place)
                price = math.ceil(default_price * mag)
                print("上昇", mag, price)
                self.prices.append(price)
            else:
                mag = self.magnification(place)
                price = math.ceil(default_price * mag)
                print("減少", mag, price)
                self.prices.append(price)


class SmallUp:
    def __init__(self):
        self.name = "跳ね小型"
        self.places = []
        self.max_mag = random.uniform(1.4, 2.0)
        self.before_correction = 0
        self.up_counter = 0
        self.isTop = False
        self.prices = []

    def set_length(self):
        max_down = 7
        down1 = random.randint(0, max_down)
        up12 = 2
        up3 = 1
        up4 = 1
        up5 = 1
        down2 = max_down - down1
        self.length = [down1, up12, up3, up4, up5, down2]
        for index, l in enumerate(self.length):
            if index == 0 or index == 5:
                for i in range(l):
                    self.places.append(False)
            else:
                for i in range(l):
                    self.places.append(True)

    def magnification(self, isUp):
        # 上り区間
        if isUp:
            if self.up_counter < 3:
                self.up_counter += 1
                return random.uniform(0.9, 1.4)
            else:
                self.up_counter += 1
                if self.isTop:
                    return self.max_mag
                else:
                    return random.uniform(1.4, self.max_mag)

        # 下り区間
        else:
            # 最初は補正累積なし
            if self.before_correction == 0:
                # 下り区間では最初の一回だけ基礎倍率を計算
                self.dc = random.uniform(0.4, 0.9)
                self.before_correction = random.uniform(-0.05, -0.03)
                return self.dc + self.before_correction
            # 2回目以降
            else:
                self.before_correction = self.before_correction + random.uniform(
                    -0.05, -0.03
                )
                return self.dc + self.before_correction

    def calc_price_detail(self):
        self.set_length()
        # 基礎価格
        default_price = random.randint(90, 110)
        print("基礎株価:{}".format(default_price))
        for place in self.places:
            if place:
                mag = self.magnification(place)
                if self.isTop:
                    price = math.ceil(default_price * mag)
                else:
                    price = math.ceil(default_price * mag) - 1
                self.isTop = not self.isTop
                print("上昇", mag, price)
                self.prices.append(price)
            else:
                mag = self.magnification(place)
                price = math.ceil(default_price * mag)
                print("減少", mag, price)
                self.prices.append(price)


class Down:
    def __init__(self):
        self.name = "減少型"
        self.dc = random.uniform(0.85, 0.9)
        self.prices = []

    def set_length(self):
        self.places = [False] * 12

    def magnification(self):
        correction = random.uniform(-0.05, -0.03)
        self.dc = self.dc + correction
        return self.dc

    def calc_price_detail(self):
        self.set_length()
        # 基礎価格
        default_price = random.randint(90, 110)
        for place in self.places:
            mag = self.magnification()
            price = math.ceil(default_price * mag)
            print("減少", mag, price)
            self.prices.append(price)


class Wave:
    def __init__(self):
        self.name = "波型"
        self.places = []
        self.length = []
        self.before_correction = 0
        self.prices = []

    def set_length(self):
        max_up = 7
        max_down = 5
        up1 = random.randint(0, 6)
        down1 = random.choice([2, 3])
        up2 = random.randint(1, max_up - up1)
        down2 = max_down - down1
        up3 = max_up - up1 - up2
        self.length = [up1, down1, up2, down2, up3]
        for index, l in enumerate(self.length):
            if index % 2 == 0:
                for i in range(l):
                    self.places.append(True)
            else:
                for i in range(l):
                    self.places.append(False)

    def magnification(self, isUp):
        # 上り区間
        if isUp:
            # 補正倍率はなし
            self.before_correction = 0
            return random.uniform(0.9, 1.4)
        # 下り区間
        else:
            # 最初は補正累積なし
            if self.before_correction == 0:
                # 下り区間では最初の一回だけ基礎倍率を計算
                self.dc = random.uniform(0.6, 0.8)
                self.before_correction = random.uniform(-0.1, -0.04)
                return self.dc + self.before_correction
            # 2回目以降
            else:
                self.before_correction = self.before_correction + random.uniform(
                    -0.1, -0.04
                )
                return self.dc + self.before_correction

    def calc_price_detail(self):
        self.set_length()
        # 基礎価格
        default_price = random.randint(90, 110)
        for place in self.places:
            if place:
                mag = self.magnification(place)
                price = math.ceil(default_price * mag)
                print("上昇", mag, price)
                self.prices.append(price)
            else:
                mag = self.magnification(place)
                price = math.ceil(default_price * mag)
                print("減少", mag, price)
                self.prices.append(price)

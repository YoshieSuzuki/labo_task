import random
import numpy

class Player: #継承元となるプレイヤークラス。
    def __init__(self,name,number):
        self.name=name #名前
        self.point=0 #得点
        self.number=number #プレイヤーの番号。points[self.number]でも自分の得点を知れる。
        self.action="stay" #行動(stay / theater / restaurant)。str型です注意。

    def decide_action(self,points,actions,day): #継承前は何もしない。
        pass

#下のFujitaniクラスに倣って、Playerクラスを継承してください
#与えられる情報としては、
# 1,points(全てのプレイヤーの得点履歴が分かる)
# 2,actions(前日の選択の分布が分かる)
# 3,day(今日がシミュレーション何日目か)
#与えられる情報については、printしてみると分かります

#消してもらって大丈夫です。
class Fujitani(Player): #例1
    def __init__(self, name, number): #初期化。ここに追記する形でいじってもよい。
        super().__init__(name, number)

    def decide_action(self,points,actions,day): #ランダムに行動する人の例
        tmp=["stay","theater","restaurant"]
        self.action=random.choice(tmp)

#消してもらって大丈夫です。
class Tanaka(Player): #例2
    def __init__(self, name, number):
        super().__init__(name, number)

    def decide_action(self, points, actions, day): #昨日の行動人数によって行動を決める人
        if actions[2]<5: self.action="restaurant"
        elif actions[1]<3: self.action="theater"
        else: self.action="stay"

class Suzuki(Player):
    def __init__(self, name: str, number: int):
        super().__init__(name, number)

    def decide_action(self, points: list[int], actions: list[int], day: int) -> None:
        tmp = ["stay", "theater", "restaurant"]
        prob0 = [0.85, 0, 0.15]
        if day == 0:
            self.action = tmp[1]
        else:
            maxdex = actions.index(max(actions))
            if maxdex == 0:
                self.action = numpy.random.choice(a = tmp, p = prob0)
            else:
                self.action = tmp[maxdex]

#テンプレート
#
#class your_name(Player): #クラス名は苗字でお願いします。
#    def __init__(self, name, number):
#        super().__init__(name, number) これは消さないでください。
#        self.temp=**
#        -> self.***でインスタンス変数を定義できます。"self."を頭につけることで下のdecide_action関数内でも使えます。
#
#    def decide_action(self, points, actions, day):
#        if ****: self.action=****
#        elif ****: self.action=***
#    　　という感じで、self.actionをルールベース/学習/etc...で決めてください。
#
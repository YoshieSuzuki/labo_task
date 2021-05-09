import Player

def reward(stay,theater,restaurant): #行動別人数の組み合わせによって報酬を返す
    reward_vec=[0,0,0]
    if stay==10: reward_vec[0]=10
    else: reward_vec[0]=1
    if theater<=4: reward_vec[1]=20
    elif theater<=7: reward_vec[1]=-10
    else: reward_vec[1]=-15
    if restaurant<=6: reward_vec[2]=40
    elif restaurant<=8: reward_vec[2]=-25
    else: reward_vec[2]=-35
    return reward_vec

trans={"stay":0,"theater":1,"restaurant":2}
# TODO revert changes 17~19
Players=[Player.Tanaka("tanaka",i) for i in range(7)] #今は全員藤谷でやってます
Players.append(Player.Fujitani("fuji",7))
Players.append(Player.Test("tani",8))
Players.append(Player.Suzuki("suzuki",9))
#本番は,Players=[Player.Oguni("Oguni",0), Player.Suzuki("Suzuki",1), ... , Player.Matsumoto("Matsumoto",9)]こんな感じになります。
hist=[[0] for _ in range(10)] #10人の点数推移メモ
actions=[0,0,0] #stay,theater,restaurant
points=[0 for _ in range(10)]

for day in range(365*3): #3年のシミュレーション
    # 行動決め
    for player in Players: player.decide_action(points,actions,day) #ここで行動を決めます。

    # 行動の集計
    actions=[0,0,0] #stay,theater,restaurant
    for player in Players: actions[trans[player.action]]+=1

    # 報酬の計算と記録
    reward_set=reward(actions[0], actions[1], actions[2]) #stay,theater,restaurantに対する報酬
    for idx,player in enumerate(Players):
        hist[idx].append(hist[idx][-1]+reward_set[trans[player.action]])
        player.point=hist[idx][-1]
        points[idx]=hist[idx][-1]
# TODO revert changes 39~
    print(day)
    print(actions)
    print(points)

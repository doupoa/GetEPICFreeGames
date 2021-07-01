import httpx
import json
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36 Edg/91.0.864.48'}
r = httpx.get('https://store-site-backend-static.ak.epicgames.com/freeGamesPromotions?locale=zh-CN&country=CN&allowCountries=CN',
              timeout=10, headers=headers)
data = json.loads(r.text)
for i in range(3):
    # 游戏名
    game_title = data["data"]["Catalog"]["searchStore"]["elements"][i]["title"]
    # 发售商
    game_seller = data["data"]["Catalog"]["searchStore"]["elements"][i]["seller"]["name"]
    # 原价
    game_originalprice = data["data"]["Catalog"]["searchStore"]["elements"][i]["price"]["totalPrice"]["fmtPrice"]["originalPrice"]
    try:
        # 白嫖开始日期-方法1
        game_startdate = data["data"]["Catalog"]["searchStore"]["elements"][i][
            "promotions"]["upcomingPromotionalOffers"][0]["promotionalOffers"][0]["startDate"]
    # 白嫖结束日期-方法1
        game_enddate = data["data"]["Catalog"]["searchStore"]["elements"][i][
            "promotions"]["upcomingPromotionalOffers"][0]["promotionalOffers"][0]["endDate"]
    except:
        try:
            # 白嫖开始日期-方法2
            game_startdate = data["data"]["Catalog"]["searchStore"]["elements"][i][
                "promotions"]["promotionalOffers"][0]["promotionalOffers"][0]["startDate"]
            # 白嫖结束日期-方法2
            game_enddate = data["data"]["Catalog"]["searchStore"]["elements"][i][
                "promotions"]["promotionalOffers"][0]["promotionalOffers"][0]["endDate"]
        except:
            game_startdate = "无数据"
            game_enddate = "无数据"

    # 封面
    game_keyimages = data["data"]["Catalog"]["searchStore"]["elements"][i]["keyImages"][0]["url"]

    print("["+str(i+1)+"]"+"\n游戏名："+game_title+"\n发售商：" + game_seller+"\n原价："+game_originalprice +
          "\n白嫖开始日期:"+game_startdate+"\n白嫖结束日期："+game_enddate+"\n封面："+game_keyimages+"\n\n")

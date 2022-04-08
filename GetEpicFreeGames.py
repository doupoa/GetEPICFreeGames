import httpx
import json


headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36'}
r = httpx.get('https://store-site-backend-static.ak.epicgames.com/freeGamesPromotions?locale=zh-CN&country=CN&allowCountries=CN',
              timeout=10, headers=headers)
data = json.loads(r.text)

# 获取接口游戏个数
numbers_of_game = data["data"]["Catalog"]["searchStore"]["paging"]["total"]
for i in range(numbers_of_game):
    # 游戏名
    game_title = data["data"]["Catalog"]["searchStore"]["elements"][i]["title"]
    # 发售商
    game_seller = data["data"]["Catalog"]["searchStore"]["elements"][i]["seller"]["name"]
    # 游戏描述
    game_description = data["data"]["Catalog"]["searchStore"]["elements"][i]["description"]
    # 原价
    game_originalprice = data["data"]["Catalog"]["searchStore"]["elements"][i]["price"]["totalPrice"]["fmtPrice"]["originalPrice"]
    # 现价
    game_discountPrice = data["data"]["Catalog"]["searchStore"]["elements"][i]["price"]["totalPrice"]["fmtPrice"]["discountPrice"]
    # 封面
    game_keyimages = data["data"]["Catalog"]["searchStore"]["elements"][i]["keyImages"][0]["url"]
    # 筛选当前周免费的游戏
    if game_discountPrice == "0" and game_originalprice != "0":
        try:
            # 白嫖开始日期 -方法 1
            game_startdate = data["data"]["Catalog"]["searchStore"]["elements"][i][
                "promotions"]["upcomingPromotionalOffers"][0]["promotionalOffers"][0]["startDate"]
            # 白嫖结束日期 -方法 1
            game_enddate = data["data"]["Catalog"]["searchStore"]["elements"][i][
                "promotions"]["upcomingPromotionalOffers"][0]["promotionalOffers"][0]["endDate"]
        except:
            try:
                # 白嫖开始日期 -方法 2
                game_startdate = data["data"]["Catalog"]["searchStore"]["elements"][i][
                    "promotions"]["promotionalOffers"][0]["promotionalOffers"][0]["startDate"]
                # 白嫖结束日期 -方法 2
                game_enddate = data["data"]["Catalog"]["searchStore"]["elements"][i][
                    "promotions"]["promotionalOffers"][0]["promotionalOffers"][0]["endDate"]
            except:
                game_startdate = "无数据"
                game_enddate = "无数据"

        print("游戏名:" + game_title + "\n发售商:" + game_seller +
              "\n原价:"+game_originalprice + "\n现价:" + game_discountPrice +
              "\n白嫖开始日期:" + game_startdate + "\n白嫖结束日期:" + game_enddate +
              "\n封面:" + game_keyimages+"\n\n")

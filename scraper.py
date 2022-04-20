import sys
from time import sleep

import requests
from bs4 import BeautifulSoup

HEADERS = ({'User-Agent':
            'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36',
            'Accept-Language': 'en-US, en;q=0.5'})

names = [
    # "",  # "The Last Guardian",
    "What Remains of Edith Finch",
    "Titanfall 2",
    "Final Fantansy XV",
    "Nier Automata",
    "Crash Bandicoot N.Sane Trilogy",
    "Spyro Reignited Trilogy",
    "Far Cry 5",
    "Jedi Fallen Order",
    "Killzone Shadowfall",
    # "",  # "Shadow of Tomb Raider",
    # "Dark Souls 3",
    "Assassins Creed Valhalla",
    "Divinity: Original Sin 2",
    # "",  # Assassins Creed Unity",
    # "",  # Ghost of Tsushima",
    # "",  # Mass Effect: Andromeda",
    # ""  # The Last of Us 2"
]

url_zoom = [
    # "",  # https://www.zoom.com.br/jogos-ps4/jogo-the-last-guardian-ps4-sony",
    "",   # edith finch, DO NOT COMMNET
    "https://www.zoom.com.br/jogos-ps4/jogo-titanfall-2-ps4-ea",
    "https://www.zoom.com.br/jogos-ps4/jogo-final-fantasy-xv-ps4-square-enix",
    "https://www.zoom.com.br/jogos-ps4/jogo-nier-automata-ps4-square-enix",
    "https://www.zoom.com.br/jogos-ps4/jogo-crash-bandicoot-ps4-activision",
    "https://www.zoom.com.br/jogos-ps4/jogo-spyro-reignited-trilogy-ps4-activision",
    "https://www.zoom.com.br/jogos-ps4/jogo-far-cry-5-ps4-ubisoft",
    "https://www.zoom.com.br/jogos-ps4/jogo-star-wars-jedi-fallen-order-ps4-ea",
    "https://www.zoom.com.br/jogos-ps4/jogo-killzone-shadow-fall-ps4-sony",
    # "",  # https://www.zoom.com.br/jogos-ps4/jogo-shadow-of-the-tomb-raider-ps4-square-enix",
    # "https://www.zoom.com.br/jogos-ps4/jogo-dark-souls-iii-ps4-bandai-namco",
    "https://www.zoom.com.br/jogos-ps4/jogo-assassin-s-creed-valhalla-ps4-ubisoft",
    "https://www.zoom.com.br/jogos-ps4/jogo-destiny-original-sin-2-ps4-bandai-namco",
    # "",  # https://www.zoom.com.br/jogos-ps4/jogo-assassin-s-creed-unity-ps4-ubisoft",
    # "",  # https://www.zoom.com.br/jogos-ps4/jogo-ghost-of-tsushima-ps4-sucker-punch",
    # "",  # https://www.zoom.com.br/jogos-ps4/jogo-mass-effect-andromeda-ps4-ea",
    # ""   # https://www.zoom.com.br/jogos-ps4/jogo-the-last-of-us-part-ii-ps4-naughty-dog"
]

url_psn = [
    # "",  # https://store.playstation.com/pt-br/product/UP9000-CUSA03627_00-LASTGUARDIANUS00",
    "https://store.playstation.com/pt-br/product/UP2470-CUSA06886_00-EFINCHPS4GAME001",
    "https://store.playstation.com/pt-br/product/UP0006-CUSA04027_00-TITANFALL2RSPWN1",
    "https://store.playstation.com/pt-br/product/UP0082-CUSA01633_00-FFXVROYALEDITION",
    "https://store.playstation.com/pt-br/product/UP0082-CUSA04551_00-GOTYORHADIGITAL0",
    "https://store.playstation.com/pt-br/product/UP0002-CUSA07402_00-CRASHNSANETRLOGY",
    "https://store.playstation.com/pt-br/product/UP0002-CUSA12125_00-SPYROTRILOGY0001",
    "https://store.playstation.com/pt-br/product/UP0001-CUSA05904_00-FARCRY5GAME00000",
    "https://store.playstation.com/pt-br/product/UP0006-PPSA02198_00-JEDIFO1DELUXEEDN",
    "https://store.playstation.com/pt-br/product/UP9000-CUSA00191_00-KZ4RELEASE000041",
    # "",  # https://store.playstation.com/pt-br/product/UP0082-CUSA10938_00-DEFINITIVE00SIEA",
    # "https://store.playstation.com/pt-br/product/UP0700-CUSA03388_00-DARKSOULS3000000",
    "https://store.playstation.com/pt-br/product/UP0001-PPSA01491_00-GAME000000000000",
    "https://store.playstation.com/pt-br/product/UP3526-CUSA12611_00-ORIGINALSIN2DE01",
    # "",  # https://store.playstation.com/pt-br/product/UP0001-CUSA00663_00-AC4GAMEPS4000001", # tomb raider
    # "",  # https://store.playstation.com/pt-br/product/UP9000-CUSA11456_00-GHOSTSHIP0000001", # ghost of tsushima
    # "",  # https://store.playstation.com/pt-br/product/UP0006-CUSA02684_00-ME4RECRUITSTNDRD", # mass effect: andromeda
    # ""   # https://store.playstation.com/pt-br/product/UP9000-CUSA07820_00-THELASTOFUSPART2",
]

url_amazon = [
    # "",  # https://www.amazon.com.br/Last-Guardian-Padr%C3%A3o-PlayStation/dp/B0754G81TY/",
    "",   # EDIT FINCH, DO NOT COMMNET
    "https://www.amazon.com.br/Titanfall-2/dp/B07NYX82C3/",
    "https://www.amazon.com.br/Final-Fantasy-Xv-Playstation-Se000137ps4/dp/B0754LFQ99",
    "https://www.amazon.com.br/Nier-Automata-Game-Yorha-PlayStation/dp/B07N6XXHBV/",
    "https://www.amazon.com.br/Crash-Bandicoot-NSane-Trilogy-PlayStation/dp/B074ZPX3ZR/",
    "https://www.amazon.com.br/Spyro-Reignited-Trilogy-PlayStation-4/dp/B07J2QT349/",
    "https://www.amazon.com.br/Far-Cry-Br-2018-PlayStation/dp/B07DHXHVHN/",
    "https://www.amazon.com.br/Star-Wars-Jedi-Fallen-PlayStation/dp/B07DJX3W29/",
    "https://www.amazon.com.br/Killzone-Shadowfall-Padr%C3%A3o-PlayStation-4/dp/B0754C5RM9/",
    # "",  # https://www.amazon.com.br/Shadow-Tomb-Raider-PlayStation-4/dp/B07GFKPS4Y",
    # "https://www.amazon.com.br/Dark-Souls-III-Fire-Fades/dp/B06ZXRZ7Y8",
    "https://www.amazon.com.br/Assassins-Creed-Valhalla-Limitada-PlayStation/dp/B08KJY5RG6/",
    "https://www.amazon.com.br/Divinity-Original-Sin-Definitive-PS4/dp/B07D8SF1JS/",
    # "",  # https://www.amazon.com.br/Assassins-Creed-Unity-Vers%C3%A3o-Portugu%C3%AAs/dp/B075TKWPV6/",
    # "",  # https://www.amazon.com.br/Ghost-Tsushima-Edi%C3%A7%C3%A3o-Padr%C3%A3o-PlayStation/dp/B086BT95SH/",
    # "",  # https://www.amazon.com.br/SONY-014633735543-Mass-Effect-Andromeda/dp/B00ZPZQIE2/",
    # ""  # https://www.amazon.com.br/Last-Us-Part-II-PlayStation/dp/B07ZGFHZVZ/"
]

prices = {}

for n in names:
    prices[n] = {}


def scrap(name, urls, element1, token, element2):
    index = 0
    print("Procurando no site " + name + ":")
    for u in urls:
        print(".", end="", flush=True)
        gamename = names[index]
        if len(u) and len(gamename):
            try:
                page = requests.get(u, headers=HEADERS)
            except Exception as e:
                print(e.__doc__)
                sys.exit(0)
                break

            results = BeautifulSoup(page.content, 'html.parser')
            games = results.find_all(element1, class_=token)

            if games:
                if len(element2) == 0:
                    preco = games[0].contents[0]
                    money = preco
                else:
                    preco = games[0].find_all(element2)
                    money = (preco[0].text + preco[1].text)

                prices[gamename][name] = money
            else:
                prices[gamename][name] = "-----"
        else:
            prices[gamename][name] = "-----"
        index += 1
        # sleep(0.5)
    print("OK")


scrap("ZOOM", url_zoom, "a", "PriceBox_Value__2VuFN", "span")

scrap("Amazon", url_amazon, "span", "a-size-medium a-color-price priceBlockBuyingPriceString", "")

scrap("PSN", url_psn, "span", "psw-t-title-m", "")   # was psw-h3

arq = open("prices.txt", "w")
arq.write("JOGO;ZOOM;Amazon;PSN\n")

for name in names:
    arq.write(name + ";")
    if len(name) and name in prices:
        arq.write(prices[name]["ZOOM"] + ";")
        arq.write(prices[name]["Amazon"] + ";")
        arq.write(prices[name]["PSN"] + ";")
        arq.write("\n")

arq.close()

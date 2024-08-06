import requests
import time
import datetime
import datetime
import pandas as pd
from upload_azure import azure_upload_df

def scraper_women(data_level: str):
    '''
    This will extract the data into csv files

    args:
    - data_level(str): The level of the data -> for example: raw, validated, access, etc.    
    '''

    # The code for retrieving the data using url, querystring, headers and response was generated by
    # insomnia and the web page's API endpoint.

    url = "https://www.sunglasshut.com/wcs/resources/plp/10152/byCategoryId/3074457345626651836"

    querystring = {"isProductNeeded":"true","isChanelCategory":"false","pageSize":"2000","orderBy":["default","default","default"],"responseFormat":"json","currency":"USD","viewTaskName":"CategoryDisplayView","storeId":"10152","DM_PersistentCookieCreated":"true","pageView":"image","catalogId":"20602","top":"Y","beginIndex":"0","langId":"-1","currentPage":["1","1"],"categoryId":"3074457345626651836"}

    headers = {
        "cookie": "aka-zp=; _abck=0FAF276E00F13EB345E8DC358E26A7FC~-1~YAAQb4g8yH2paOaDAQAAUFuE%2FAik0RXG%2Fytjlq%2FYdXlwO93WlOYC6beCwxrPLWf9tkl1VgIuWW%2B9RV%2BleisFkz22xxIJ%2BjW6%2FuDPKZW9QYFnep2%2BnegxRE%2BHbBmiN2EQP6RpUwf%2FEoByYh1gFLlCTqIREAb3LsKt57wTuFk4Uigko5VlzSjK5zMNRftlMiHB9JCiP2bPg2mCl0F5HIdgQKRtyA%2Fpvr%2Fhs6%2BrrijwCNwSYD2kZ%2BXQy0xVT4sd6MHMZAvVSW%2Fe1DIObbLa3cgprFMUGfdPr66MxghNbrWfKF3jAZowvp5bQDPPmheFGyNzD6yT%2FuG4ZP3cUIPO66%2Bca8eYT%2FtwFtmoB4aaHmVJ6SwDUUbuQk4PN%2F9GHyIifSQFIfN%2Fqg%3D%3D~-1~-1~-1; JSESSIONID=0000qACJROi-yAwweDBdyCdl68O%3A1c7qtq78c; TS011f624f=015966d292698129d1e6099d4a40df52f67dd0e4ddf58b1da9478f7076339879297ea78805eb49e1ff6d7677dd5fb53ae228301eeef6ec7c10804873caf6f0cf99671d104c",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:106.0) Gecko/20100101 Firefox/106.0",
        "Accept": "application/json, text/plain, */*",
        "Accept-Language": "es-ES,es;q=0.8,en-US;q=0.5,en;q=0.3",
        "Accept-Encoding": "gzip, deflate, br",
        "Connection": "keep-alive",
        "Referer": "https://www.sunglasshut.com/us/womens-sunglasses",
        "Cookie": "_abck=EEFFF1F752CDA43268ECFEBF46EE1817~0~YAAQNKFivt7vYOiDAQAAK0+D/Airx8YtIuS1b5tJUFzGqeArl44W/UA3nb9IWUAiTJLZwMMZeWKuEYOP0mI9z06c8pJZQ3HPqNnq3u7MlssRmazLpM+Qa8z2G4RPVjltcwKx124CQjCaVzfAYggjoUJZqZXhdDmcRU0ItUQ0YvLTl8a3zDyMt9T/85j1HhBoC8D23w6wtSkanwWF8Qe0x99zp+PK2O5a8ie1gopC/eKgRTLi3c58iBSRj1R25dKaVWXt6IZgVYfeWn4L3FBzPAKgyEdOD/MyWU38fRunxrvj2T470BJ2fB2aVjSJI/9l4chYvWmvFkeVWV2a0jtq/npbHvP+8r4/svIbcof8MbBcULud7/psAESgh2RfvFu8TCnwqyIkDFOaGWf+QleCPMn1ve081dzY1Dhi1xqt~-1~-1~-1; SGPF=36qhcdG0Pxk6EgWnM7u-mfoYhCrsgPgZCpi1PZe00SYW6BUk9K5Rkfg; mt.v=2.1858991113.1666285934800; forterToken=eda43e4ba5f4406d993758eac1116f80_1666388808933__UDF43_6; utag_main=v_id:0183f661a45200022ab5beca674905050002e00d007e8`n:3`e:1`s:1`t:1666390609995`:sunglasshut.com`:2`:1666388809995%3Bexp-session`n:1%3Bexp-session; AMCV_125138B3527845350A490D4C%40AdobeOrg=-1303530583%7CMCIDTS%7C19286%7CMCMID%7C09713078739431207282298259464588794690%7CMCAAMLH-1666920204%7C4%7CMCAAMB-1666920204%7C6G1ynYcLPuiQxYZrsz_pkqfLG9yMXBpb2zX5dvJdYQJzPXImdj0y%7CMCOPTOUT-1666322604s%7CNONE%7CMCAID%7CNONE%7CMCSYNCSOP%7C411-19293%7CvVersion%7C3.3.0; ftr_ncd=6; __wid=309120822; s_ecid=MCMID%7C09713078739431207282298259464588794690; CONSENTMGR=consent:true%7Cts:1666285945624; _cs_c=1; MGX_UC=JTdCJTIyTUdYX1AlMjIlM0ElN0IlMjJ2JTIyJTNBJTIyYTVmNzhmZGMtM2I3OS00Yzk0LWFkODktMzVkMDdiM2I2ZmU0JTIyJTJDJTIyZSUyMiUzQTE2NjY4NDEwNDczODAlN0QlMkMlMjJNR1hfQ0lEJTIyJTNBJTdCJTIydiUyMiUzQSUyMjAwMjg0NzI2LWUzZTktNGM4OS05MTBlLTE1MWVkMjQyMGQxZCUyMiUyQyUyMmUlMjIlM0ExNjY2ODQxMDQ3MzgyJTdEJTJDJTIyTUdYX1BYJTIyJTNBJTdCJTIydiUyMiUzQSUyMmFlNzYzYzA4LWRkNTYtNDkxOC05Y2UzLTkwMDYwMGM0MTFiZSUyMiUyQyUyMnMlMjIlM0F0cnVlJTJDJTIyZSUyMiUzQTE2NjYzMTcyNDc5MDglN0QlMkMlMjJNR1hfVlMlMjIlM0ElN0IlMjJ2JTIyJTNBMiUyQyUyMnMlMjIlM0F0cnVlJTJDJTIyZSUyMiUzQTE2NjYzMTcyNDc5MDglN0QlMkMlMjJNR1hfRUlEJTIyJTNBJTdCJTIydiUyMiUzQSUyMm5zX3NlZ18wMDAlMjIlMkMlMjJzJTIyJTNBdHJ1ZSUyQyUyMmUlMjIlM0ExNjY2MzE3MjQ3OTA4JTdEJTdE; _gcl_au=1.1.1404097255.1666285951; _pin_unauth=dWlkPVltUXdPRFpoWmpndFkyTm1OeTAwWmpGbUxXSTVZMlF0WmpJeU1ERXhZbUZsT0RnNA; __utma=110589831.747615470.1666285952.1666285952.1666315408.2; __utmz=110589831.1666285952.1.1.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided); _cs_id=cf9cfae4-3d71-a1db-9847-b9f79e743126.1666285953.2.1666315452.1666315411.1.1700449953289; _scid=184c671e-b5b4-4525-8048-a3d0bdd7740d; _tt_enable_cookie=1; _ttp=51d26430-e0bf-4ca0-9e42-697c7f1b0dfa; _fbp=fb.1.1666285956202.1834105470; _clck=impdkx|1|f5w|0; _clsk=1uz5z1a|1666315452148|2|0|k.clarity.ms/collect; cto_bundle=jVat0F9ncEo1TFQzTmh1UFIlMkZFcHNmYzgzZDdGVnFzQlVLR1c1U1liWHZaS2VsWmN5aEFpS0ZXYnNkUlVJY2x0SW55dkJtNUZjY0pHYVlwJTJCSkx3NEltd2ZBSUk3dTloT3FldzNjNUVKc3FYVEtVek8lMkZ2Nm1tcVdUYWlOSlFnTkJmYWtCMThxNWdxZVJJeDNqbU8wczRaTlhKTkJNTXJxSXNyZ0FYY2FtY3Fvd29IZjAlM0Q; _sctr=1|1666242000000; _ga_6P80B86QTY=GS1.1.1666315404.2.1.1666315448.16.0.0; _ga=GA1.1.804108324.1666285972; _uetsid=63880030509a11edb031b57f7702e12c; _uetvid=6387f7e0509a11edb133450b5a542b22; aka-cc=PE; aka-ct=LAVICTORIA; aka-zp=; ak_bmsc=7866C91F7794DC19008EC2FBE1C66CC1~000000000000000000000000000000~YAAQNKFivjzwYOiDAQAA1FqD/BEuduByAL2vl0jDiYyFBFcVTTp/WVBBWU0690yWdNEUNh7uQnkP4cANr3LKDgacTtlMG98XDJ7jVPZ44vsJ1oyKlXdepu+j/m6NHnMnK+oPI740gGYhZfMBYZGpjmjRIqWnFmAAGwZkADmjRYS978lBEwpPeAxl/h/Oe7Y7APLOgT+Y3lzVovcONaNKeIwFI4ubUXSyQi5j8SB+KyhhrQiu/2wpNqIRA5DYHI1FV0OedXhjtCpEP+qPwDo5+uJl1IwEiABxu3/3tv9SqzI4igaQkpLOun0Rv4PpopP0rAIvYNw9UlX4oCflbmjwTid+gqeP0etERAURlmOKRmI7klgeBHnZ4wrnUldQYM8uqv2biKuZicMsRPKmOkvc5ZGT3Bno/Cle9Tw4/H7dSpWJpqRUdSZmILjzkcDkl87yuZjApQlaAE56+kiVU5+PtppD2aN7WM41pM71BYz1MPTdcQqFRufC0z6NJ0LPgRQ=; bm_sz=37841F848AE8364464A01EF2CB8CAD37~YAAQNKFivuHvYOiDAQAAK0+D/BGRcZcGAin3jsh7PDlCoee2O168nrH5b3rvuOu6Jp50er60c3oIRNG9HRymSRCOOXSqFmQzSlgQzdTwQvrkpqzdotXVAOWvmSYjxgCA6tG4ZyfdUoYwQkopn+FaA3D4pxOQXFfWvxYlBWcBGIaU5B0cPumnAKG3fOZ0Mw32ezvKK+C6Swd3E5FzV+2G7VBqepTWgt4qJ4EqzkfHWTGRD2LVahkqYNazm5Qw7xpS2EA0rN0p8p3gAH4JB67tqbfit80cJMUYUBvww/Y7We85VPJvPjGZtQ==~4539462~4338243; dtCookie=v_4_srv_-2D37_sn_NN7UPS0BH5D8A8882C8RF7048V7J0HEP; rxVisitor=166638880871121NGJT4JDAPM7IDGO6DTC0LPOAKKVMB2; dtPC=-37`-0e0; rxvt=1666390609388|1666388808712; dtLatC=51; dtSa=-; sgh-desktop-facet-state-plp=categoryid:undefined|gender:true|brands:partial|polarized:true|price:true|frame-shape:partial|color:true|face-shape:false|fit:false|materials:false|lens-treatment:false; sgh-desktop-facet-state-search=; bm_sv=C8E1A5078E16645D6669451575590477~YAAQNKFivijwYOiDAQAAi1eD/BFdla8Kdp4pCaXMidCDLsjoBcQGDt8LdKx2oxyWSOR60/jCCAOuesVKbPMj4WnnkVrJlxvAwXIb/1tZx082gSrLmSqbt0zxXL4iEH63huVZk+aoWNfVCfb8DlOnemx2j9T89JHchicWYZX41k8v22ldzwPvRehjIJe+VQ6HIwE+X7Ph00AT9tSB8M4kuOJTOC+4hJGU0CpcurX9XxYjjf7mN5bUf4S2JU60gf5jlRGNUWo=~1; tealium_data2track_Tags_AdobeAnalytics_TrafficSourceJid_ThisHit=210211RES; tealium_data_tags_adobeAnalytics_trafficSourceJid_stackingInSession=210211RES; tealium_data2track_Tags_AdobeAnalytics_TrafficSourceMid_ThisHit=direct; tealium_data_tags_adobeAnalytics_trafficSourceMid_thisSession=direct; tealium_data_session_timeStamp=1666388810019; userToken=undefined; TrafficSource_Override=1; tiktok_click_id=undefined",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "TE": "trailers"
    }

    response = requests.request("GET", url, headers=headers, params=querystring).json()

    data_ = response["plpView"]["products"]["products"]["product"]
    selectColumnsDFWomen = pd.json_normalize(data_)[["isJunior","lensColor","img","isFindInStore","isCustomizable","roxableLabel","brand","imgHover","isPolarized","colorsNumber","isOutOfStock","modelName","isEngravable","localizedColorLabel","name","listPrice","offerPrice"]]
    selectColumnsDFWomen['extractdate'] = datetime.datetime.now()
    azure_upload_df(dataframe=selectColumnsDFWomen, filename=f"products-women-{data_level}.csv", datalevel=f"{data_level}") 

    print("Sunglasses for women's table succesfully extracted and uploaded")

    time.sleep(5)
import requests
from bs4 import BeautifulSoup
from gtts import gTTS
import webbrowser

def get_url(url):
    playload = {
        "from": "/bbs/Gossiping/index.html",
        "yes": "yes"
    }
    rs = requests.session()
    resp1 = rs.post("https://www.ptt.cc/ask/over18", data=playload)  # 告訴Ptt 已滿18歲
    resp2 = rs.get(url)
    soup = BeautifulSoup(resp2.text, "html.parser")
    scope1 = soup.select("#main-container")
    scope2 = soup.select(".title")

    ptt_title = []
    for title in scope2:
        ptt_title.append(title.text)

    return ptt_title


def reports(draft):  # 顯示ptt文字 用dict顯示
    print("批踢踢八卦版爬蟲蟲蟲")
    ptt_dict={}
    i = 0
    while i < len(ptt):
        if ptt[i][:4] == "\nRe:": #PTT [i][0]是\n
            ptt_dict["Category"] = draft[i][6:8]
            ptt_dict["Title"] = draft[i][9:]
            print("Category[{}]:{}".format(ptt_dict["Category"], ptt_dict["Title"]))
        elif ptt[i][:4] == "\nFw:":#PTT [i][0]是\n
            ptt_dict["Category"] = draft[i][6:8]
            ptt_dict["Title"] = draft[i][9:]
            print("Category[{}]:{}".format(ptt_dict["Category"], ptt_dict["Title"]))
        else:
            ptt_dict["Category"] = draft[i][2:4]
            ptt_dict["Title"] = draft[i][5:]
            print("Category[{}]:{}".format(ptt_dict["Category"], ptt_dict["Title"]))
        i += 1

def speech(ptt_draft): #把草稿轉變成字串
    ptt_text ="批踢踢八卦版爬蟲蟲蟲\n"

    for news in ptt_draft:
        if news[:4] == "\nRe:":
            ptt_text= ptt_text+ "種類是"+news[6:8]+ " "+news[9:]
        elif news[:4] == "\nFw:":
            ptt_text = ptt_text + "種類是" + news[6:8] + " " + news[9:]
        else:
            ptt_text = ptt_text + "種類是" + news[2:4] + " " + news[5:]
    ptt_text += str("\n 啊! 念得好累喔\n 怎麼那麼多字 \n請給我一杯水")
    return ptt_text

def sound(speak):  # 轉變成語音檔
    tts = gTTS(text=speak, lang="zh")
    tts.save("ptt.mp3")
    webbrowser.open("ptt.mp3")

if __name__ =="__main__":
    ptt = get_url("https://www.ptt.cc/bbs/Gossiping/index.html")
    reports(ptt)
    speak =speech(ptt)
    sound(speak)
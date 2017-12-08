# coding:utf-8
import time
import requests
def stopclass(self):
    header1 = {"Connection": "keep-alive",
               "User-Agent": "Mozilla/5.0(Windows NT 6.1; WOW64)AppleWebKit/537.36(KHTML, like Gecko)Chrome/59.0.3071.115Safari/537.36",
               "content-type": "application/json;charset=UTF-8",
               "Accept": "*/*",
               "Referer": "http://172.16.0.163:8012/teacherClassroom/59fbc68dae886e3c075d629b/monitor",
               "Accept-Encoding": "gzip,deflate",
               "Accept-Language": "zh-CN,zh;q=0.8",
               "Cookie": "Hm_lvt_0a389c25bc66eea9ca7296cc9326e66a=1502675291;et:sess=99cf661e1edc417fa4a0bbca4cf737a8"
               }
    st = {"attendClassId": "59fd0641ae886e3c075da32f"}
    time.sleep(10)
    stopclass = requests.post(self.urlstopclass, headers=header1, json=st)
    print(stopclass.text)
    print(stopclass.status_code)
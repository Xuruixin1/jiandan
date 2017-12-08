import Jianeryou.jiekoujianeryou
import requests
def classbegin(self):
    urlclassbegin = 'http://172.16.0.163:8012/api/startClass'
    Jianeryou.jiekoujianeryou.jey.test_012_huidaokebiao(self)

    #self.test_012_huidaokebiao()
    header1 = {"Connection": "keep-alive",
               "User-Agent": "Mozilla/5.0(Windows NT 6.1; WOW64)AppleWebKit/537.36(KHTML, like Gecko)Chrome/59.0.3071.115Safari/537.36",
               "content-type": "application/json;charset=UTF-8",
               "Accept": "*/*",
               "Referer": "http://172.16.0.163:8012/teacherIndex/schedule/table?returnFrom=addTeachPlan",
               "Accept-Encoding": "gzip,deflate",
               "Accept-Language": "zh-CN,zh;q=0.8",
               "Cookie": "Hm_lvt_0a389c25bc66eea9ca7296cc9326e66a=1502675291;et:sess=99cf661e1edc417fa4a0bbca4cf737a8"
               }
    begin = {"preparationId": "59fd04a3ae886e3c075d9ed5",
             "classId": "58a26f37bf140fdcde2fad88",
             "attendClassId": "59fd0641ae886e3c075da32f",
             "ts": "1509529859665"}
    classbegin = requests.post(urlclassbegin, headers=header1, json=begin)
    print(classbegin.text)
    print(classbegin.status_code)
    c = classbegin.json()
    self.assertEqual(c["success"], True)
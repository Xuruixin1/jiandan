# coding:utf-8
import requests
def studentclasszhuangtaimessage(self):
    ss={
        "attendClassId":"59fd0641ae886e3c075da32f",
        "username":"stu001"
    }
    r1=requests.get("http://172.16.0.163:8012/api/getSelfStatus",params=ss )
    print(r1.status_code)
    rr=r1.status_code
    self.assertEqual(rr,200)

def studentzuoti(self):
    s={"attendClassId":"59fd0641ae886e3c075da32f",
       "username":"tech002",
       "sectionId":"525182",
       "type":"es",
       "status":"5"
       }
    r=requests.post("http://172.16.0.163:8012/api/changeSectionStatus",json=s)
    print(r.text)
    print(r.status_code)
    jr=r.json()
    self.assertEqual(jr["success"],True)

def studenttijiao(self):
    sss={
        "attendClassId":"59fd0641ae886e3c075da32f",
        "username":"tech002",
        "sectionId":"525182",
        "type":"es",
        "status":"100"
    }
    rrrr=requests.post("http://172.16.0.163:8012/api/changeSectionStatus",json=sss)
    print(rrrr.status_code)
    print(rrrr.text)
    jrrrr=rrrr.json()
    self.assertEqual(jrrrr["success"],True)

def studenttijiaozipanjieguo(self):
    s3 = {
        "attendClassId": "59fd0641ae886e3c075da32f",
        "username": "stu002",
        "sectionId": "525182",
        "type": "es",
        "status": "1"
    }
    r3=requests.post("http://172.16.0.163:8012/api/changeSectionStatus",json=s3)
    print(r3.text)
    print(r3.status_code)
    js3=r3.json()
    self.assertEqual(js3["success"],True)

def studenttiaoguoshipin(self):
    t3 = {
        "attendClassId": "59fd0641ae886e3c075da32f",
        "username": "stu002",
        "sectionId": "525182",
        "type": "vs",
        "status": "99"
    }
    tiao=requests.post("http://172.16.0.163:8012/api/changeSectionStatus",json=t3)
    print(tiao.text)
    print(tiao.status_code)
    tt3=tiao.json()
    self.assertEqual(tt3["success"],True)


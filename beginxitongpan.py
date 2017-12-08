# coding:utf-8
import requests
import unittest
import time
import Jianeryou.Login.teacherLogin
import Jianeryou.Data.data
import Jianeryou.Url.url
class jianeryouxitong(unittest.TestCase):

    def setUp(self):
        self.a=Jianeryou.Login.teacherLogin.Denglu()
        self.a.setUp()
        self.h = Jianeryou.Data.data.wodebeikehader

    def test_028_huoquteachermessage(self):
        u'''进入教师首页获取教师信息'''
        h=Jianeryou.Data.data.teachermessage
        url=Jianeryou.Url.url.urlloginmessage
        r=requests.get(url,headers=h)
        ass=r.json()
        print(r.text)
        self.assertEqual(ass["user"]["role"],1)
    def test_29_wodebeikeyemian(self):
        u'''我的备课页面'''
        t = int(round(time.time() * 1000))
        h=Jianeryou.Data.data.wodebeikehader
        url=Jianeryou.Url.url.urlbeike
        p = {
            "ts": self.h
        }
        g=requests.get(url,headers=h,params=p)
        s=g.json()
        print(g.text)
        self.assertEqual(s["success"],True)
    def test_30_beikewancheng(self):
        u'''备课后进入我的课表页面'''
        self.test_028_huoquteachermessage()
        mes = {
            "beginDate": 1511955649311,
            "endDate": 1511955649311,
            "ts": 1511955649311
        }
        h=Jianeryou.Data.data.beikewancheng
        url=Jianeryou.Url.url.urlkebiao
        g=requests.get(url,headers=h,params=mes)
        print(g.status_code)
        print(g.text)

if __name__=="__main__":
    test_unittest= unittest.TestSuite()
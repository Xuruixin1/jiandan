# coding:utf-8
import unittest
import requests
import Jianeryou.jiekoujianeryou
class xu(unittest.TestCase):
    def setUp(self):
        self.urldenglu = 'http://172.16.0.163:8012/teacherLogin'
        self.urldeng = 'http://172.16.0.163:8012/api/login'
        self.urlteacherLogin = 'http://172.16.0.163:8012/teacherIndex'
        # 登录方法

    def Login(self, username, password, remember=True):
        header = {
            "Connection": "keep-alive",
            "Upgrade-Insecure-Requests": "1",
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
            "Referer": "http://172.16.0.163:8012/teacherLogin",
            "Accept-Encoding": "gzip,deflate",
            "Accept-Language": "zh-CN,zh;q=0.8",
            "Cookie": "Hm_lvt_0a389c25bc66eea9ca7296cc9326e66a=1502675291;et:sess=99cf661e1edc417fa4a0bbca4cf737a8"
        }

        deng = {
            "role": "1",
            "username": username,
            "password": password,
            "remember": remember
        }
        # 进入登录入口
        # r=requests.get(self.urldenglu)
        # print(r.status_code)
        # 登录
        print(deng)
        self.s = requests.session()
        # 内
        r1 = self.s.post(self.urldeng, headers=header, json=deng, verify=False)
        print(username)
        print(r1.status_code)
        print(r1.text)
        result1 = r1.content
        print(result1)
        return r1.json()

    def test_001_uT_pT(self):
        u'''账号密码长度正确登录成功'''
        username = "tech002"
        password = "12345"
        result = self.Login(username, password)
        self.assertEqual(result["success"], True)

    def test_002_uF_pT(self):
        u'''账号错误密码正确'''
        username = "tech00"
        password = "12345"
        result = self.Login(username, password)
        print(result)
        self.assertEqual(result["message"], "Cannot read property 'userName' of undefined")

    def test_003_uT_pF(self):
        u'''账号正确密码错误'''
        username = "tech002"
        password = "1234"
        result = self.Login(username, password)
        print(result)
        self.assertEqual(result["message"], "Cannot read property 'userName' of undefined")

    def test_004_uF_pF(self):
        u'''账号错误密码错误'''
        username = "tech00"
        password = "1234"
        result = self.Login(username, password)
        print(result)
        self.assertEqual(result["message"], "Cannot read property 'userName' of undefined")

    def test_005_uT_pT_login(self):
        self.urlloginmessage = 'http://172.16.0.163:8012/api/teacherIndexInit?ts=1511430129711 '
        username = "tech002"
        password = "12345"
        self.Login(username, password)
        r = self.s.get(self.urlteacherLogin)
        # print(r.text)
        title = r.status_code
        self.assertEqual(title, 200)
if __name__=="__main__":
    test_unittest= unittest.TestSuite()

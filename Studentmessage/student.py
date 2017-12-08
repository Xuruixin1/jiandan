# coding:utf-8
import unittest
import requests

class student(unittest.TestCase):
    def setUp(self):
        self.urlstudentd = 'http://172.16.0.163:8012/studentLogin'
        self.urlstudentLogin = 'http://172.16.0.163:8012/api/login'

    def Login0(self, username, password, remember=True):
        header = {
            "Connection": "keep-alive",
            "Upgrade-Insecure-Requests": "1",
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
            "Referer": "http://172.16.0.163:8012/studentLogin",
            "Accept-Encoding": "gzip,deflate",
            "Accept-Language": "zh-CN,zh;q=0.8",
            "Cookie": "Hm_lvt_0a389c25bc66eea9ca7296cc9326e66a=1502675291;et:sess=99cf661e1edc417fa4a0bbca4cf737a8"
        }

        deng = {
            "role": "0",
            "username": username,
            "password": password,
            "remember": remember
        }
        # 进入登录入口
        # r=requests.get(self.urldenglu)
        # print(r.status_code)
        # 登录
        print(deng)
        self.ss = requests.session()
        r1 = self.ss.post(self.urlstudentLogin, headers=header, json=deng, verify=False)
        print(username)
        print(r1.status_code)
        print(r1.text)
        result1 = r1.content
        print(result1)
        return r1.json()

    def test_014_student1dneglu(self):
        u'''学生1登录'''
        username = 'stu002'
        password = '123456'
        re = self.Login0(username, password)
        self.assertEqual(re["success"], True)

    def test_015_student1dneglu(self):
        u'''学生登录账号错误'''
        username = 'stu00'
        password = '123456'
        self.Login0(username, password)

    def test_016_student1dneglu(self):
        u'''学生登录密码错误'''
        username = 'stu001'
        password = '12345'
        self.Login0(username, password)

if __name__ == "__main__":
    test_unittest = unittest.TestSuite()

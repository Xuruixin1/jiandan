# coding:utf-8
import requests
import unittest
import Jianeryou.Url.url
import Jianeryou.Headers.teacherheader
import xlrd

class Denglu(unittest.TestCase):

    def setUp(self):
        a= requests.get(Jianeryou.Url.url.urlteacherLogin)
        print(a.status_code)

    def Login(self, username, password, remember=True):
        h=Jianeryou.Headers.teacherheader.theaderlogin
        deng = {
            "role": "1",
            "username": username,
            "password": password,
            "remember": remember
        }
        print(deng)
        self.s = requests.session()
        # 内
        r1 = self.s.post(Jianeryou.Url.url.urlteacherdenglu, headers=h, json=deng, verify=False)
        print(username)
        print(r1.status_code)
        print(r1.text)
        result1 = r1.content
        print(result1)
        return r1.json()

    def test_024_uT_pT(self):
        u'''账号密码长度正确登录成功'''
        data = xlrd.open_workbook('H:\\test.xlsx')
        table = data.sheet_by_name(u'Sheet1')
        for i in range(table.nrows):
            list = table.row_values(i)
            print('用户名：%s  密码：%s' % (list[0], list[1]))
            print('*' * 20)
        username = list[0]
        password = list[1]
        result = self.Login(username, password)
        self.assertEqual(result["success"], True)

    def test_025_uF_pT(self):
        u'''账号错误密码正确'''
        username = "tech00"
        password = "12345"
        result = self.Login(username, password)
        print(result)
        self.assertEqual(result["message"], "Cannot read property 'userName' of undefined")

    def test_026_uT_pF(self):
        u'''账号正确密码错误'''
        username = "tech002"
        password = "1234"
        result = self.Login(username, password)
        print(result)
        self.assertEqual(result["message"], "Cannot read property 'userName' of undefined")

    def test_027_uF_pF(self):
        u'''账号错误密码错误'''
        username = "tech00"
        password = "1234"
        result = self.Login(username, password)
        print(result)
        self.assertEqual(result["message"], "Cannot read property 'userName' of undefined")


if __name__=="__main__":
    test_unittest= unittest.TestSuite()
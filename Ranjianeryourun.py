# coding:utf-8
import unittest
import Jianeryou.Studentmessage.student
import HTMLTestRunner
from Jianeryou import jiekoujianeryou
import Jianeryou.Url.Insideurl
import Jianeryou.Login.teacherLogin
import Jianeryou.beginxitongpan
testunit = unittest.TestSuite()
#将测试用例添加到unittest里面
testunit.addTest(unittest.makeSuite(Jianeryou.Url.Insideurl.xu))
testunit.addTest(unittest.makeSuite(jiekoujianeryou.jey))
testunit.addTest(unittest.makeSuite(Jianeryou.Studentmessage.student.student))
#教师登录
testunit.addTest(unittest.makeSuite(Jianeryou.Login.teacherLogin.Denglu))
testunit.addTest(unittest.makeSuite(Jianeryou.beginxitongpan.jianeryouxitong))

#报告的路径
filename = "H:\\"+"result.html"
fp = open(filename,"wb")
runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=u'测试报告', description=u'用例执行情况：')
#执行测试用例
runner.run(testunit)



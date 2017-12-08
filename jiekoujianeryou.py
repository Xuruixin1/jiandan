# coding:utf-8
import requests
import unittest
import time
import Jianeryoustudent
import Jianeryou.Url.Insideurl
import Jianeryou.Studentmessage.studentmessage
import Jianeryou.Studentmessage.student
import Jianeryou.Classbegin.Begin
import Jianeryou.Stopclass.stopclass
import Jianeryou.Url.Externalurl
class jey(unittest.TestCase):
    def setUp(self):
        self.urlloginmessage = 'http://172.16.0.163:8012/api/teacherIndexInit?ts=1511430129711 '
        self.urlbeike = 'http://172.16.0.163:8012/api/getUserPreparation'
        self.urlkebiao = 'http://172.16.0.163:8012/api/getTeachPlansInPeriod'
        self.urlteachermessage = 'http://172.16.0.163:8012/api/getClassByTeacher'
        self.urlnewkecehng = 'http://172.16.0.163:8012/api/getUserPreparation'
        self.shangke = 'http://172.16.0.163:8012/api/createTeachPlan'
        self.urlwanchenghouhuidaowodekebiao = 'http://172.16.0.163:8012/api/getTeachPlansInPeriod'
        self.urlclassbegin = 'http://172.16.0.163:8012/api/startClass'
        self.urlstopclass = 'http://172.16.0.163:8012/api/finishClass'
        self.urlstudentd = 'http://172.16.0.163:8012/studentLogin'
        self.urlstudentLogin = 'http://172.16.0.163:8012/api/login'

    def test_006_uT_pT_login_teachermissage(self):
        u'''进入教师首页获取教师信息'''
        header1 = {"Connection": "keep-alive",
                   "User-Agent": "Mozilla/5.0(Windows NT 6.1; WOW64)AppleWebKit/537.36(KHTML, like Gecko)Chrome/59.0.3071.115Safari/537.36",
                   "content-type":"application/json;charset=UTF-8",
                   "Accept": "*/*",
                   "Referer":"http://172.16.0.163:8012/teacherIndex",
                   "Accept-Encoding":"gzip,deflate",
                    "Accept-Language":"zh-CN,zh;q=0.8",
                   "Cookie":"Hm_lvt_0a389c25bc66eea9ca7296cc9326e66a=1502675291;et:sess=99cf661e1edc417fa4a0bbca4cf737a8"
                   }

        j=Jianeryou.Url.Insideurl.xu()
        j.setUp()
        j.test_005_uT_pT_login()

        print(j.urlloginmessage)
        par={"ts":"1502675291000"}
        r2=requests.get(self.urlloginmessage,headers=header1)
        print(r2.text)
        print(r2.json())
        rrr=r2.json()
        uname=r2.status_code
        self.assertEqual(rrr["user"]["role"],1)
        self.assertEqual(rrr["user"]["username"],"tech002")
        self.assertEqual(rrr["user"]["realName"], u"测试1")
        self.assertEqual(rrr["user"]["faceData"], None)
        self.assertEqual(rrr["user"]["distHost"], None)
        self.assertEqual(rrr["user"]["mobile"], "13131313131")
        self.assertEqual(rrr["user"]["isBindMobile"], True)
        self.assertEqual(rrr["attendClass"],None)
        self.assertEqual(rrr["askForAttendReply"], None)

    def test_007_beike(self):
        u'''我的备课页面接口'''
        self.test_006_uT_pT_login_teachermissage()
        header1 = {"Connection": "keep-alive",
                   "User-Agent": "Mozilla/5.0(Windows NT 6.1; WOW64)AppleWebKit/537.36(KHTML, like Gecko)Chrome/59.0.3071.115Safari/537.36",
                   "content-type": "application/json;charset=UTF-8",
                   "Accept": "*/*",
                   "Referer": "http://172.16.0.163:8012/teacherIndex/preparation/list",
                   "Accept-Encoding": "gzip,deflate",
                   "Accept-Language": "zh-CN,zh;q=0.8",
                   "Cookie": "Hm_lvt_0a389c25bc66eea9ca7296cc9326e66a=1502675291;et:sess=99cf661e1edc417fa4a0bbca4cf737a8"
                   }
        p={
            "ts":"1502675291009"
        }
        beikemessage=requests.get(self.urlbeike,headers=header1,params=p)
        print(beikemessage.text)
        b=beikemessage.json()
        self.assertEqual(b["success"],True)

    def test_008_kebiao(self):
        u'''备课后进入我的课表页面'''
        self.test_007_beike()
        header1 = {"Connection": "keep-alive",
                   "User-Agent": "Mozilla/5.0(Windows NT 6.1; WOW64)AppleWebKit/537.36(KHTML, like Gecko)Chrome/59.0.3071.115Safari/537.36",
                   "content-type": "application/json;charset=UTF-8",
                   "Accept": "*/*",
                   "Referer": "http://172.16.0.163:8012/teacherIndex/schedule/table",
                   "Accept-Encoding": "gzip,deflate",
                   "Accept-Language": "zh-CN,zh;q=0.8",
                   "Cookie": "Hm_lvt_0a389c25bc66eea9ca7296cc9326e66a=1502675291;et:sess=99cf661e1edc417fa4a0bbca4cf737a8"
                   }
        mes={
            "beginDate":"1509292800000",
            "endDate":"1509897600000",
            "ts":"1509529243805"
        }
        kebiao=requests.get(self.urlkebiao,headers=header1,params=mes)
        print(kebiao.text)
        print(kebiao.status_code)
        m=kebiao.json()
        self.assertEqual(m["success"],True)

    def test_009_huoqulaohimessage(self):
        u'''获取备课老师信息'''
        self.test_007_beike()
        header1 = {"Connection": "keep-alive",
                   "User-Agent": "Mozilla/5.0(Windows NT 6.1; WOW64)AppleWebKit/537.36(KHTML, like Gecko)Chrome/59.0.3071.115Safari/537.36",
                   "content-type": "application/json;charset=UTF-8",
                   "Accept": "*/*",
                   "Referer": "http://172.16.0.163:8012/teacherIndex/schedule/table",
                   "Accept-Encoding": "gzip,deflate",
                   "Accept-Language": "zh-CN,zh;q=0.8",
                   "Cookie": "Hm_lvt_0a389c25bc66eea9ca7296cc9326e66a=1502675291;et:sess=99cf661e1edc417fa4a0bbca4cf737a8"
                   }
        m={"ts":"1509529251029"}
        teachermessage=requests.get(self.urlteachermessage,headers=header1,params=m)
        te=teachermessage.json()
        print(teachermessage.status_code)
        print(teachermessage.text)
        self.assertEqual(te["success"],True)
        self.assertEqual(te["data"][0]["name"],u"高三年级(上)实验(3)班")
        self.assertEqual(te["data"][1]["nickname"],"feivorid_nick")

    def test_010_newkecheng(self):
        u'''新增课程'''
        self.test_009_huoqulaohimessage()
        header1 = {"Connection": "keep-alive",
                   "User-Agent": "Mozilla/5.0(Windows NT 6.1; WOW64)AppleWebKit/537.36(KHTML, like Gecko)Chrome/59.0.3071.115Safari/537.36",
                   "content-type": "application/json;charset=UTF-8",
                   "Accept": "*/*",
                   "Referer": "http://172.16.0.163:8012/teacherIndex/schedule/table",
                   "Accept-Encoding": "gzip,deflate",
                   "Accept-Language": "zh-CN,zh;q=0.8",
                   "Cookie": "Hm_lvt_0a389c25bc66eea9ca7296cc9326e66a=1502675291;et:sess=99cf661e1edc417fa4a0bbca4cf737a8"
                   }
        p={"ts":"1509529851029"}
        newkecheng=requests.get(self.urlnewkecehng,headers=header1,params=p)
        n=newkecheng.json()
        print(newkecheng.text)
        self.assertEqual(n["data"][0]["term"][0],u"必修2")
        header2 = {"Connection": "keep-alive",
                   "User-Agent": "Mozilla/5.0(Windows NT 6.1; WOW64)AppleWebKit/537.36(KHTML, like Gecko)Chrome/59.0.3071.115Safari/537.36",
                   "content-type": "application/json;charset=UTF-8",
                   "Accept": "*/*",
                   "Referer": "http://172.16.0.163:8012/teacherIndex/schedule/addTeachPlan",
                   "Accept-Encoding": "gzip,deflate",
                   "Accept-Language": "zh-CN,zh;q=0.8",
                   "Cookie": "Hm_lvt_0a389c25bc66eea9ca7296cc9326e66a=1502675291;et:sess=99cf661e1edc417fa4a0bbca4cf737a8"
                   }
        pp={"id":"59f6e6ebae886e3c075d5220",
            "ts":"1509529851555"}
        n=requests.get("http://172.16.0.163:8012/api/getPreparationById",headers=header2,params=pp)
        print(n.status_code)
        print(n.text)

    def test_011_xuanzeshangke(self):
        u'''选择好要上课的课程'''
        self.test_010_newkecheng()
        header1 = {"Connection": "keep-alive",
                   "User-Agent": "Mozilla/5.0(Windows NT 6.1; WOW64)AppleWebKit/537.36(KHTML, like Gecko)Chrome/59.0.3071.115Safari/537.36",
                   "content-type": "application/json;charset=UTF-8",
                   "Accept": "*/*",
                   "Referer": "http://172.16.0.163:8012/teacherIndex/schedule/table",
                   "Accept-Encoding": "gzip,deflate",
                   "Accept-Language": "zh-CN,zh;q=0.8",
                   "Cookie": "Hm_lvt_0a389c25bc66eea9ca7296cc9326e66a=1502675291;et:sess=99cf661e1edc417fa4a0bbca4cf737a8"
                   }
        p={"preparationId":"59f996a9ae886e3c075d5841",
           "startDate":"2017-10-31T16:00:00.000Z",
           "classId":"58a26f37bf140fdcde2fad88",
           "studyMode":"0"}
        shangke=requests.post(self.shangke,headers=header1,json=p)
        print(shangke.status_code)
        print(shangke.text)

        self.assertEqual(shangke.status_code,200)

    #完成后回到课表选择上课时间
    def test_012_huidaokebiao(self):
        u'''完成后回到课表选择上课时间'''
        self.test_011_xuanzeshangke()
        header1 = {"Connection": "keep-alive",
                   "User-Agent": "Mozilla/5.0(Windows NT 6.1; WOW64)AppleWebKit/537.36(KHTML, like Gecko)Chrome/59.0.3071.115Safari/537.36",
                   "content-type": "application/json;charset=UTF-8",
                   "Accept": "*/*",
                   "Referer": "http://172.16.0.163:8012/teacherIndex/schedule/table?returnFrom=addTeachPlan",
                   "Accept-Encoding": "gzip,deflate",
                   "Accept-Language": "zh-CN,zh;q=0.8",
                   "Cookie": "Hm_lvt_0a389c25bc66eea9ca7296cc9326e66a=1502675291;et:sess=99cf661e1edc417fa4a0bbca4cf737a8"
                   }
        p1={
            "beginDate": "1509529858555",
            "endDate": "1509529859555",
            "ts": "1509529859655"
        }
        hui=requests.get(self.urlwanchenghouhuidaowodekebiao,headers=header1,params=p1)
        print(hui.status_code)
        self.assertEqual(hui.status_code,200)

    #开始上课
    def test_013_beginshangke(self):
        u'''开始上课'''
        Jianeryou.Classbegin.Begin.classbegin(self)

    #下课
    def test_023_stopclass(self):
        u'''下课'''
        Jianeryou.Stopclass.stopclass.stopclass(self)


    #进入学生头主页
    def test_017_studentLogin(self):
        u'''进入学生头主页'''
        a = Jianeryou.Studentmessage.student.student()
        a.setUp()
        a.test_014_student1dneglu()
        a.tearDown()
       # self.test_014_student1dneglu()
        url='http://172.16.0.163:8012/studentIndex'
        s=requests.get(url)
        print(s.status_code)
        title=s.status_code
        self.assertEqual(title,200)

    #获取学生上课状态信息
    def test_018_studentshangkemessage(self):
        u'''获取学生上课状态信息'''
        Jianeryou.Studentmessage.studentmessage.studentclasszhuangtaimessage(self)

    def test_019_studentzuoti(self):
        u'''学生做题'''
        Jianeryou.Studentmessage.studentmessage.studentzuoti(self)
    #学生做题跳过视频
    def test_020_studenttijiaozipanjieguo(self):
        u'''学生提交自判结果'''
        Jianeryou.Studentmessage.studentmessage.studenttijiao(self)

    def test_021_studenttiaoguoshipin(self):
        u'''提交自判结果'''
        Jianeryou.Studentmessage.studentmessage.studenttijiaozipanjieguo(self)
    def test_022tiaoguoshipin(self):
        u'''跳过视频'''
        Jianeryou.Studentmessage.studentmessage.studenttiaoguoshipin(self)


if __name__=="__main__":
    test_unittest= unittest.TestSuite()
    test_unittest.addTest(jey("test_one"))
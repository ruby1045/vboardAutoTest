# -*- coding: utf-8 -*-
from Base.BaseRunner import ParametrizedTestCase
import os
import sys
from PageObject.JoinMeeting.JoinMeetingPage import *

# 获取当前文件路径
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


class JoinMeetingTest(ParametrizedTestCase):

    def test1WrongMeetingID(self):

        app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../yamls/JoinMeeting/WrongMeetingID.yaml"),
               "device": self.devicesName, "caseName": sys._getframe().f_code.co_name}

        page = JoinWrongMeetingPage(app)
        page.operate()
        page.checkPoint()

    def test2MeetingSuccess(self):

        app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../yamls/JoinMeeting/JoinMeetingSuccess.yaml"),
               "device": self.devicesName, "caseName": sys._getframe().f_code.co_name}

        page = JoinMeetingSuccessPage(app)
        page.operate()
        page.checkPoint()

    def test3MeetingSuccessPW(self):
        pass

    @classmethod
    def setUpClass(cls):
        super(JoinMeetingTest, cls).setUpClass()

    @classmethod
    def tearDownClass(cls):
        super(JoinMeetingTest, cls).tearDownClass()
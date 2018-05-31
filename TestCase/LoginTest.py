# -*- coding: utf-8 -*-
from Base.BaseRunner import ParametrizedTestCase
import os
import sys
from PageObject.Home.LoginPage import LoginPage

# 获取当前文件路径
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


class LoginTest(ParametrizedTestCase):

    def testLogin4Pass(self):
        app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../yamls/Login/LoginPass.yaml"),
               "device": self.devicesName, "caseName": sys._getframe().f_code.co_name}

        page = LoginPage(app)
        page.operate()
        page.checkPoint()

    
    def testLogin1WrongAccount(self):
        app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../yamls/Login/LoginWrongAccount.yaml"),
               "device": self.devicesName, "caseName": sys._getframe().f_code.co_name}

        page = LoginPage(app)
        page.operate()
        page.checkPoint()

    def testLogin2WrongPassword(self):
        app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../yamls/Login/LoginWrongPassword.yaml"),
               "device": self.devicesName, "caseName": sys._getframe().f_code.co_name}
        page = LoginPage(app)
        page.operate()
        page.checkPoint()


    def testLogin3EmptyInput(self):
        app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../yamls/Login/LoginEmptyInput.yaml"),
               "device": self.devicesName, "caseName": sys._getframe().f_code.co_name}
        page = LoginPage(app)
        page.operate()
        page.checkPoint()



    @classmethod
    def setUpClass(cls):
        super(LoginTest, cls).setUpClass()

    @classmethod
    def tearDownClass(cls):
        super(LoginTest, cls).tearDownClass()

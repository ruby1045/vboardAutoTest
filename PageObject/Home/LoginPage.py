from Base.BaseYaml import getYam
from PageObject import Pages


class LoginPage:
    '''
    Banner浏览历史
    isOperate: 操作失败，检查点就失败,kwargs: WebDriver driver, String path(yaml配置参数)
    '''

    def __init__(self, kwargs):
        #把HomeTest里的app信息重新组装，获得Yaml文件的配置信息
        _init = {"driver": kwargs["driver"], "test_msg": getYam(kwargs["path"]), "device": kwargs["device"],
                 "logTest": kwargs["logTest"], "caseName": kwargs["caseName"]}
        #将组装后的信息传递给Page.PagesObjects
        #getYam(kwargs["path"])得到的"test_msg"为[True, {'testinfo': [{'id': 'test001', 'title': '第一次启动app', 'info': '打开app'}], 'testcase': [{'element_info': '//android.widget.ListView//android.support.v4.view.ViewPager/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.widget.RelativeLayout[1]', 'find_type': 'xpath', 'operate_type': 'click', 'info': '点击个人图片'}], 'check': [{'element_info': 'com.ximalaya.ting.android.main.application:id/main_group_rank_title', 'find_type': 'id', 'check': 'default_check', 'info': '打开页面成功'}]}]
        #参看BaseYaml里的getYam方法
        self.page = Pages.PagesObjects(_init)

    def operate(self):  # 操作步骤
        self.page.operate()

    def checkPoint(self):  # 检查点
        self.page.checkPoint()


if __name__ == "__main__":
    pass
# -*- coding: utf-8 -*-
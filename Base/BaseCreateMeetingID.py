# -*- coding: utf-8 -*-
import  requests
import  os,sys
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0,parentdir)

def login():
    url="http://39.108.73.212/vboard/security/login"
    payload={"userId":"zhaolimin_1045","password":"zlm13367131368"}
    r = requests.post(url, data=payload)
    _result = r.json()
    result=_result["result"]
    return result[16:85]

def getNoPasswordMeetingID():
    url="http://39.108.73.212/vboard/security/createMeeting"
    tocken=login()
    headers={"accessToken":tocken}
    payload={'name':"vpanelMeeting",'password':"",'isPermissionOpen':"false"}
    r = requests.post(url, data=payload,headers=headers)
    _result = r.json()
    result=_result["result"]
    return result[14:18]
    #return _result

def getPasswordMeetingID():
    url = "http://39.108.73.212/vboard/security/createMeeting"
    tocken = login()
    headers = {"accessToken": tocken}
    payload = {'name': "vpanelMeeting", 'password': "1234", 'isPermissionOpen': "false"}
    r = requests.post(url, data=payload, headers=headers)
    _result = r.json()
    result = _result["result"]
    return result[14:18]

if __name__=="__main__":
    b=getPasswordMeetingID()
    print(b)

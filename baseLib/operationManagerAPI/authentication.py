import requests
from baseLib.baseUtils import invokeJar
import re
from configuration import const
from baseLib.baseUtils.log import logging

#运营管理登录
@logging(level='INFO', desc='运营管理登录')
def login(usrDictionary):
    strUserName = usrDictionary.get('userName')
    strPassword = usrDictionary.get('password')
    loginActionList = ['/Admin/queryUserNameAction_srandNum',
                       '/Admin/j_spring_security_check',
                       '/Admin/terminalUserManage/terminalUserAction_toUserManage']
    getSrandNumResponse = requests.get(const._global_configuration().OptionManagerHttpUrl + loginActionList[0])
    responseCookies = getSrandNumResponse.cookies
    strSandNum = re.findall(r"%7B%27mcryptKey%27%3A%27(.+?)%27%7D",getSrandNumResponse.text)
    strEncodePassword = invokeJar.getEncodePassword(strSandNum[0], strPassword)

    securityCheckFormPara = {'phone':'',
                             'randomValidateId':'',
                             'sendFlag':'',
                             'userNameOld': strUserName,
                             'password': strEncodePassword,
                             'passwordtype': '1',
                             'j_username': strUserName,
                             'validate':'',
                             'message':''}
    responseCookies.set('tvpay_login_name', strUserName)
    responseByPostForm = requests.post(const._global_configuration().OptionManagerHttpUrl + loginActionList[1],
                                       cookies = responseCookies,
                                       data = securityCheckFormPara)
    responseCookies.update(responseByPostForm.cookies)

    responseAfterLogin = requests.get(const._global_configuration().OptionManagerHttpUrl + loginActionList[2],
                                       cookies = responseCookies)
    if responseAfterLogin.text.find('终端用户列表'):
        print(strUserName + '登录成功')
    else:
        print(strUserName + '登录失败')
    return responseCookies

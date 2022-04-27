import sys
import requests

def main():
  url2 = 'http://ip-api.com/json/'
  url3= 'https://api.myip.la/en?json'

  response2 = requests.get(url2)
  response3 = requests.get(url3)

  strpp={}         #定义一个字典strpp
  strpp=response2.json()  #把英文网站json接口返回值传给字典strpp
  print("\n")        #下面就是直接从字典取值，显示。
  print("*"*30)
  print("您查询的IP地址 %s 来源地是："%(strpp.get('query')))
  print("国家：%s"%(strpp.get('country')))
  print("省/市/区：%s"%(strpp.get('city')))
  print("经纬度坐标：%s,%s"%(strpp.get('lat'),strpp.get('lon')))
  print("运营商编号：%s"%(strpp.get('as')))
  print("ISP服务商：%s"%(strpp.get('isp')))
  print("数据来源: www.ip-api.com")
  print("*"*30)

  strpp3={}         #定义一个字典strpp
  strpp3=response3.json()  #把英文网站json接口返回值传给字典strpp
  print("\n")        #下面就是直接从字典取值，显示。
  print("*"*30)
  print("数据来源: www.api.myip.la")
  print("您查询的IP地址 %s 来源地是："%(strpp3.get('ip')))
  print("国家：%s"%(strpp3.get('location').get("country_name")))
  print("省/市/区：%s %s %s"%(strpp3.get('location').get('province'),strpp3.get('location').get('city'),strpp3.get('location').get('country_code')))
  print("经纬度坐标：%s,%s"%(strpp3.get('location').get('latitude'),strpp3.get('location').get('longitude')))
  print("运营商编号：%s"%(strpp3.get('as')))
  print("ISP服务商：%s"%(strpp3.get('isp')))
  print("*"*30)

if __name__ == "__main__":
    main()
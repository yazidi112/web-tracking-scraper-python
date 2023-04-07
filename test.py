str = """
Date: Fri, 07 Apr 2023 11:33:06 GMT
Server: Apache
X-Powered-By: PHP/5.6.40
Set-Cookie: user_id=123456; expires=Sun, 07-May-2023 11:33:06 GMT; Max-Age=2592000; path=/
Set-Cookie: sid=ze1231D213; expires=Sun, 07-May-2023 11:33:06 GMT; Max-Age=2592000; path=/
Upgrade: h2,h2c
Connection: Upgrade
Location: https://fpt.usmba.ac.ma/test/?partner_id=a.com&sync_id=MTIzNDU2
Vary: Accept-Encoding
Transfer-Encoding: chunked
Content-Type: text/html; charset=UTF-8
"""
arr = str.split("\n")
for l  in arr:
    if l.startswith("Set-Cookie"):
        print("ok")
        
print(str.split("\n"))
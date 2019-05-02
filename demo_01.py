import sys
import requests


print(sys.version)
print(sys.executable)


def greet(who_to_greet):
    greeting = f"Hello, {who_to_greet}"
    return greeting


print(greet("dust"))
r = requests.get("https://www.baidu.com")
print(r.status_code)

name = input("please input your name: ")
print(name)

"""
Author: LiRayShield
Date: 2024-08-08
Description: 该程序用于查询并显示给定IP地址的相关信息，包括位置和运营商等详细数据。用户可以通过输入IP地址来进行查询，或者输入'q'来退出程序。
"""

import requests

while True:
    # 用户输入需要查询的IP地址
    IP = input("请输入IP地址（输入Q或q退出程序）：")

    # 检查用户是否想要退出程序
    if IP.lower() == 'q':
        break

    # 设置API接口地址
    API = "https://api.vvhan.com/api/ipInfo?ip="

    try:
        # 发送GET请求获取IP信息
        response = requests.get(API + IP)
        # 将响应内容解析为JSON格式
        data = response.json()

        # 尝试打印IP相关信息
        try:
            # 打印请求的状态
            print("请求状态：", data["success"])
            # 打印IP地址
            print("IP地址：", data["ip"])
            # 打印IP所在的国家
            print("IP所在国家：", data["info"]["country"])
            # 打印IP所在的省份
            print("IP所在省份：", data["info"]["prov"])
            # 打印IP所在的城市
            print("IP所在城市：", data["info"]["city"])
            # 打印IP的运营商
            print("IP运营商：", data["info"]["isp"])
        # 如果数据结构中缺少某些键，则捕获KeyError异常
        except KeyError:
            # 输出错误信息
            print(data["message"])

    except requests.RequestException as e:
        # 处理网络请求异常
        print("网络请求失败:", e)

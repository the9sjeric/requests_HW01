import requests

corpid = "wwd74df2f89ef2a560"
secret = "NtB_n4sNtWVhcl05wk3YokSWauatjU21hFW0QlODdAs"

"""获取token"""
def test_get_token():
    url = f"https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={corpid}&corpsecret={secret}"
    r = requests.get(url)
    print(r.text)

token = "GeiwRJDx-neo9xUcqN6Fo0Rp03AzKG6tYECZdEmJGersOTS2oND11NSHRwPRy_CZEc4YDqw-Iyy2hXin3_oA1NGD0e0lLU" \
        "aNEVOqX5YGRrTqy0axh2n_ujYLs0IB73n4FOf5zRrIwtVgyZU6Fo5Yte0w499OCr7htuFzEsAXJabdptgPzSHwOxrLcLIn" \
        "6aVrECl9Gm_1_a_7Ki71XwMPwg"

"""新增用户"""
def test_add_menber():
        jsonadd = {
                "userid": "reqadd001",
                "name": "阿伊Q",
                "mobile": "+86 13800000225",
                "department": [1]
        }
        urladd = f"https://qyapi.weixin.qq.com/cgi-bin/user/create?access_token={token}"
        radd = requests.post(url=urladd,json=jsonadd)
        print(radd.text)

"""修改用户信息"""
def test_modify_menber():
        jsonmodify = {
                "userid": "reqadd001",
                "position": "后台工程师"
        }
        urlmodify = f"https://qyapi.weixin.qq.com/cgi-bin/user/update?access_token={token}"
        rmodify = requests.post(url=urlmodify,json=jsonmodify)
        print(rmodify.text)

"""查询用户信息"""
userid = "reqadd001"
def test_query_menber():
        urlquery = f"https://qyapi.weixin.qq.com/cgi-bin/user/get?access_token={token}&userid={userid}"
        rquery = requests.get(urlquery)
        print(rquery.text)

"""删除用户"""
def test_del_menber():
        urldel = f"https://qyapi.weixin.qq.com/cgi-bin/user/delete?access_token={token}&userid={userid}"
        rdel = requests.get(urldel)
        print(rdel.text)
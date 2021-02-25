import requests

corpid = "wwd74df2f89ef2a560"
secret = "NtB_n4sNtWVhcl05wk3YokSWauatjU21hFW0QlODdAs"

def test_get_token():
    url = f"https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={corpid}&corpsecret={secret}"
    r = requests.get(url)
    print(r.text)

token = "GeiwRJDx-neo9xUcqN6Fo0Rp03AzKG6tYECZdEmJGersOTS2oND11NSHRwPRy_CZEc4YDqw-Iyy2hXin3_oA1NGD0e0lLU" \
        "aNEVOqX5YGRrTqy0axh2n_ujYLs0IB73n4FOf5zRrIwtVgyZU6Fo5Yte0w499OCr7htuFzEsAXJabdptgPzSHwOxrLcLIn" \
        "6aVrECl9Gm_1_a_7Ki71XwMPwg"
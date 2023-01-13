"""
This is the version that works
"""

import requests

# r =requests.get('https://xkcd.com/1906/')
# # https://xkcd.com/1906/
# print(r.headers)
# print(r)
# print(r.text)

url = 'https://i.hamreus.com/ps3/z/%E6%8C%87%E5%B0%96%E5%A5%B6%E8%8C%B6[%E5%AE%AB%E9%87%8E%E7%9F%A5%E4%BA%B2]/07%E5%8D%B7/99770_0043_36235.JPG.webp?e=1668622994&m=MpckE5u3OPs1e3iwnfqLbQ'
# my_referer = 'https://www.manhuagui.com/comic/8352/103543.html'
my_referer = 'https://www.manhuagui.com/'
# r =requests.get(url)
r = requests.get(url, headers={'referer': my_referer})
print(r)
print(r.content)

filename = 'test_download.webp'
with open(filename, "wb") as f:
    f.write(r.content)

# r =requests.get(url, headers={'referer': my_referer})

# chain = ['https://www.manhuagui.com/comic/8352/103543.html',
#          'https://cf.hamreus.com/scripts/config_5F5A8A8B46A7B711EC3579AFD755010FA8E85725.js',
#          'https://i.hamreus.com/ps3/z/%E6%8C%87%E5%B0%96%E5%A5%B6%E8%8C%B6[%E5%AE%AB%E9%87%8E%E7%9F%A5%E4%BA%B2]/07%E5%8D%B7/99770_0043_36235.JPG.webp?e=1668622994&m=MpckE5u3OPs1e3iwnfqLbQ']
#
# for link in chain:
#     r =requests.get(link)
#     # https://xkcd.com/1906/
#     print(r.headers)
#     print(r)
#     print()
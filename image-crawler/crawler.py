# -*- coding: utf-8 -*-
import urllib
import re
import time
import os
from urllib.request import urlopen
import urllib.request
from urllib.parse import quote


# 显示下载进度
def schedule(a, b, c):
    """''
    a:已经下载的数据块
    b:数据块的大小
    c:远程文件的大小
   """
    per = 100.0 * a * b / c
    if per > 100:
        per = 100
    print('%.2f%%' % per)


def getHtml(url):
    req = urllib.request.Request(url)
    req.add_header('Referer', 'https://www.google.com/')
    req.add_header('User-Agent',
                   'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36')
    r = urllib.request.urlopen(req)

    l_html = r.read()
    return l_html.decode('utf-8')


def downloadImg(a_html):
    # 使用非贪婪模式"?"匹配最短的image src中的内容
    reg = r'data-src\s*=".*?"'
    imgre = re.compile(reg)
    imglist = re.findall(imgre, a_html)
    # 定义文件夹的名字
    t = time.localtime(time.time())
    foldername = str(t.__getattribute__("tm_year")) + "-" + str(t.__getattribute__("tm_mon")) + "-" + str(
        t.__getattribute__("tm_mday"))
    picpath = 'D:\\ImageDownload\\%s' % foldername  # 下载到的本地目录

    if not os.path.exists(picpath):  # 路径不存在时创建一个
        os.makedirs(picpath)
    x = 0
    for imgurl in imglist:
        target = picpath + '\\%s.jpg' % x
        print('Downloading image to location: ' + target + '\nurl=' + imgurl)
        print(imgurl[imgurl.find("=") + 1:])
        # 去掉url链接中的'"' strip('"')
        image = urllib.request.urlretrieve(imgurl[imgurl.find("=") + 1:].strip('"'), target)
        x += 1
    return image


if __name__ == '__main__':
    print('''
********************************
**   Welcome to use Spider      **
**  Created on  2016-12-13      **
**    @author: abel        **
*********************************
''')

    g_html = getHtml(
        "https://www.google.com/search?q=logo&source=lnms&tbm=isch&sa=X&ved=0ahUKEwifuMXevYfRAhVjy1QKHcn9B9QQ_AUICCgB&biw=1920&bih=932")

    downloadImg(g_html)
    print("Download has finished.")

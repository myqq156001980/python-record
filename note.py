from xlsxwriter import Workbook
import json
import re
import os
import requests
import time
import datetime


def get_current_timestamp():
    """
    获取当前时间戳毫秒
    :return:
    """
    d_time = datetime.datetime.now()
    obj_stamp = int(time.mktime(d_time.timetuple()) * 1000.0 + d_time.microsecond / 1000.0)
    return obj_stamp


def request_post():
    """
    request post
    :return:
    """
    json_1 = {}
    json_2 = {}
    # http 请求头部
    headers = {}
    url = ""
    # 如果是curl --binary-data 的形式; data中的字段用回车分割
    data = json.dumps(json_1) + "\n" + json.dumps(json_2) + "\n"
    result = requests.post(url, data=data,
                           headers=header)
    # 返回的content为byte用str编码为字符串
    str_content = str(result.content, encoding="utf-8")
    return str_content


def regexp(s):
    """
    python 正则匹配
    :return:
    """
    pattern = "dashboardId=[0-9]*&"
    res = re.search(pattern, s)
    if res:
        print(res.group(0)


def write_excel(dashboard_dic):
    """
    excel 操作
    :return:
    """
    wk = Workbook("dashboard.xlsx")
    # 写入头部
    st = wk.add_worksheet("看板统计")
    st.write(0, 0, "id")
    st.write(0, 2, "visit_times")
    # 遍历写入数据参数 row, col, data
    for i, v in enumerate(dashboard_dic):
        st.write(i + 1, 0, v)
        st.write(i + 1, 1, dashboard_dic[v])

    wk.close()


def check_dir(dir_path):
    """
    检查目录是否存在,并创建
    :param dir_path:
    """
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)


def traverse_dir(dir_path):
    """
    遍历文件夹
    :param dir_path:
    """

    file_list = os.listdir(dir_path)
    absolute_path = list()

    for i in file_list:
        absolute_path.append(os.path.join(dir_path, i))
    return absolute_path

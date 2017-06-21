# 对奇牛api进行操作
# 定义华北数据中心的基础数据连接
from itertools import count

from qiniu import Auth,BucketManager
import requests
import MysqlOP

# 常用全局变量
table = 'KawsWebEnter_apppakagemanagement'
fieldname = 'appname,version,downloadurl'
BaseURL = 'http://oqi5qqa77.bkt.clouddn.com/'
access_key = 'cPHIgg7EWl6KXaGsHbdMoayXq_XtUb-Ffwmr16P5'
secret_key = '1ldaBTotyksMPjw1mMTxJorBRslHrSMtBWowN3bf'

def compare_table_qiniulist(table):
    table_list = MysqlOP.readMysql(table)
    return table_list


def qiniuOP():
    q = Auth(access_key,secret_key)

    # 创建bucket实例
    bucket = BucketManager(q)
    # 读取空间内容的list
    bucket_list = BucketManager.list(bucket,'xcxdatacab2')
    # 将list的内容转成字典
    list_dic = bucket_list[0]
    # 将字典中items的内容提取出来
    list_items = list_dic['items']
    # print(list_items)
    for i in list_items:
        print(i['key'])
        appname = i['key']
        version = i['key'][0:5]
        downloadurl = BaseURL+appname
        # 组合写入数据库的值
        valuse = '"'+appname+'"'+','+'"'+version+'"'+','+'"'+downloadurl+'"'
        table_list_contnt = compare_table_qiniulist(table)
        #
        table_appname = []
        for i in table_list_contnt:
            table_appname = table_appname+[i[1]]
        if appname in table_appname:
            print("内容重复无需写入")
        else:
            try:

                MysqlOP.writeMysqlonerow(table,fieldname,valuse)
                print('数据写入成功')
            except:
                print('数据写入失败')

def main():


    qiniuOP()

if __name__ == '__main__':
    main()

import  requests
import  pymysql
# 建立连接函数，方便调用
def readMysql(table):
# 建立链接
    conn = pymysql.connect(host ='192.168.1.208',port = 3306, user = 'admin1', passwd = '123' , db = 'xcx',charset = 'utf8')
# 创建游标
    cursor = conn.cursor()
# 执行sql
    cursor.execute("select * from "+table+" ")
# 获取全部结果
    row_list = cursor.fetchall()
# 插入数据
    conn.commit()
    cursor.close()
    conn.close()
    return row_list

def writeMysqlonerow(table,fieldname,valuse):
    # 建立链接
    conn = pymysql.connect(host='192.168.1.208', port=3306, user='admin1', passwd='123', db='xcx', charset='utf8')
    # 创建游标
    cursor = conn.cursor()
    # 执行sql
    sql = "insert into "+table+"("+fieldname+") values ("+valuse+") "
    print(sql)
    cursor.execute(sql)
    # 插入数据
    conn.commit()
    cursor.close()
    conn.close()


def main():
    table = 'KawsWebEnter_apppakagemanagement'
    fieldname = 'appname,version,downloadurl'
    appname = '5.00stage第一版患者招募'
    version = '5.0.0'
    downloadurl = 'http://oqi5qqa77.bkt.clouddn.com/5.00stage%E7%AC%AC%E4%B8%80%E7%89%88%E6%82%A3%E8%80%85%E6%8B%9B%E5%8B%9F.apk'
    valuse = '"'+appname+'"'+','+'"'+version+'"'+','+'"'+downloadurl+'"'
    writeMysqlonerow(table,fieldname,valuse)
    readMysql(table)

if __name__ == '__main__':
    main()

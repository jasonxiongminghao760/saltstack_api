from lib import db
from lib import db_conn
from api import salt_interface,salt_log
import  argparse


def exec_db(DBname,DBuser,target):
    logger=salt_log.logging.getLogger('salt日志')

    logger.info('开始创建数据库')

    session = db_conn.get_db_session()
    # 获取mysql连接数据和授权数据
    user_list = session.query(db.Hosts.user,db.Hosts.password,db.Hosts.host).filter(db.Hosts.user == DBuser).first()

    conn_user = user_list[0]
    conn_password = user_list[1]
    conn_host  = user_list[2] 
    c1 = salt_interface.salt_cmd(target,
                                'mysql_create',
                                'prod',
                                 name=DBname,
                                 user=DBuser,
                                 password=conn_password,
                                 port='3306',
                                 host=conn_host,
                                 op_user=conn_user,
                                 op_password=conn_password)
    res = c1.state_sls()
    print(res)
    logger.info('创建数据库：%s 授权用户：%s'.format(DBname,DBuser))


def Args(args):
    DBname = args.DBname    # 创建数据库名
    DBuser = args.DBuser    # 授权用户名
    Target = args.Target    # 目标minion
    if DBname is not None and DBuser is not None and Target is not None:
        exec_db(DBname, DBuser,Target)
    else:
        print('请输入 --help')


if __name__ =='__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-db",dest="DBname",action="store",help='database name',type=str)
    parser.add_argument("-u",dest="DBuser",action="store",help='grant database user',type=str)
    parser.add_argument("-d",dest="Target",action="store",help='exec target minion ',type=str)
    args = parser.parse_args()
    Args(args)









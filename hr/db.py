import pymysql

class HrInfo(object):
    def __init__(self,tableName):
        self.tableName = tableName
        self.create_table()

    def add_hr(self,title,detail_url,content,city,num,jobtype,jobtime):
        db = pymysql.Connect(
            host="localhost",
            port=3306,
            user="root",
            passwd="root",
            db="spider",
            charset="utf8"
        )
        cursor =  db.cursor()
        sql = "insert into %s(title,detail_url,content,city,num,jobtype,jobtime) values('%s','%s','%s','%s','%s','%s','%s')"%(self.tableName,title,detail_url,content,city,num,jobtype,jobtime)
        cursor.execute(sql)
        db.commit()
        cursor.close()
        db.close()

    def get_count(self):
        db = pymysql.Connect(
            host="localhost",
            port=3306,
            user="root",
            passwd="root",
            db="spider",
            charset="utf8"
        )
        cursor =  db.cursor() 
        sql = "select count(1) from %s"%(self.tableName)
        cursor.execute(sql) 
        total_count = cursor.fetchone()      
        cursor.close()
        db.close()
        return total_count

    def outinfo(self,begin,keyword,total,city,jobtype):
        result = {}
        config = {
            'host':'localhost',
            'port':3306,
            'user':'root',
            'passwd':'root',
            'db':'spider',
            'charset':'utf8',
            'cursorclass':pymysql.cursors.DictCursor
        }
        db = pymysql.Connect(**config)
        cursors = db.cursor()
        # sql = "select * from %s limit %d,%d"%(self.tableName,begin,total)
        sql = "select * from %s where (title like '%%%s%%' or content like '%%%s%%') and location='%s' and jobType='%s' limit %s,%s"%(self.tableName,keyword,keyword,city,jobtype,begin,total)
        items = []
        try:
            cursors.execute(sql)
            results = cursors.fetchall()
            for row in results:
                item = {}
                item["title"] = row["title"]
                item["detail_url"] = row["detail_url"]
                item["content"] = row["content"]
                item["city"]=row["city"]
                item["num"]=row["num"]
                item["jobtype"]=row["jobtype"]
                item["jobtime"]=row["jobtime"]
                items.append(item)
        except:
            pass
        finally:
            cursors.close()
            db.close()
        return items

    def create_table(self):
        db = pymysql.Connect(
            host="localhost",
            port=3306,
            user="root",
            passwd="root",
            db="spider",
            charset="utf8"
        )

        
        cursor =  db.cursor()
        sql = """
        CREATE TABLE IF NOT EXISTS `""" +self.tableName+ """`  (
        `Id` int(11) NOT NULL AUTO_INCREMENT,
        `title` varchar(255) DEFAULT NULL,
        `detail_url` varchar(255) DEFAULT NULL,
        `city` varchar(255) DEFAULT NULL,
        `num` varchar(255) DEFAULT NULL,
        `jobtype` varchar(255) DEFAULT NULL,
        `jobtime` varchar(255) DEFAULT NULL,
        `content` text,
        PRIMARY KEY (`Id`)
        ) ENGINE=MyISAM DEFAULT CHARSET=utf8;
        """
        cursor.execute(sql)
        db.commit()
        cursor.close()
        db.close()


''''
hr = HrInfo("hrinfo3")

hr.create_table("hrinfo")


hr.add_hr("ddd","sdfsfd","sdfffff")
hr.add_hr("ddd","sdfsfd","sdfffff")
hr.add_hr("ddd","sdfsfd","sdfffff")
hr.add_hr("ddd","sdfsfd","sdfffff")
hr.add_hr("ddd","sdfsfd","sdfffff")
print(hr.get_count())
print(hr.outinfo(2,2))
'''


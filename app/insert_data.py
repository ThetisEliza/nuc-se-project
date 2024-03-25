import sys
import pymysql

with pymysql.connect(host="localhost", 
                     user="debian-sys-maint", 
                     password="mbjmYmElkwOe6Tg2", 
                     database="nuc_se_project") as db, \
    open(sys.argv[1]) as f:
        
        from datetime import datetime
        tmp_class = None
        tmp_group = None
        for line in f.readlines():
            data = line.strip('\n').split("\t")
            class_, group, number, name,_, score = data
            if len(class_.strip()) != 0:
                tmp_class = class_
            if len(group.strip()) != 0:
                tmp_group = group.replace(" ", "")
                cursor = db.cursor()
                rscore = int(score) * 50 / 2005
                print(f"('{tmp_group}', '{score}', '{tmp_class}', {rscore}, '{str(int(datetime.now().timestamp()))}')")
                sql = f"insert into nuc_groups (name, totalmark, ragularmark, class, modifyTimestamp) values ('{tmp_group}', {score}, {rscore}, '{tmp_class}', '{str(int(datetime.now().timestamp()))}')"
                # sql = f"insert into nuc_students (name, no, studentname) values ('{name}', '{number}', '{tmp_group}')"
                cursor.execute(sql)
                db.commit()

            print(tmp_class, tmp_group, number, name, score)
            
            
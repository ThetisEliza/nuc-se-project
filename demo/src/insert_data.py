import sys
import pymysql

with pymysql.connect(host="localhost", 
                     user="debian-sys-maint", 
                     password="mbjmYmElkwOe6Tg2", 
                     database="nuc_se_project") as db, \
    open(sys.argv[1]) as f:
        
        
        tmp_class = None
        tmp_group = None
        for line in f.readlines():
            data = line.strip('\n').split("\t")
            class_, group, number, name = data
            if len(class_.strip()) != 0:
                tmp_class = class_
            if len(group.strip()) != 0:
                tmp_group = group.replace(" ", "")

            print(tmp_class, tmp_group, number, name)
            cursor = db.cursor()
            sql = f"insert into nuc_students (name, no, studentname) values ('{name}', '{number}', '{tmp_group}')"
            cursor.execute(sql)
            db.commit()
            
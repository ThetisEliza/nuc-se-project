import pymysql
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent.absolute()))


from model.data import Group, Member
from datetime import datetime
from typing import List, Dict, Tuple
from threading import Lock

class DatabaseController:
    def __init__(self) -> None:
        self.lock = Lock()
        self.db = pymysql.connect(host="localhost", 
                     user="debian-sys-maint", 
                     password="mbjmYmElkwOe6Tg2", 
                     database="nuc_se_project")
        
    def getSpareMember(self) -> List[Member]:
        db = self.db
        cursor = db.cursor()
        sql = f"select * from nuc_students where studentname IS NULL;"
        print(f'Get Spare Members {sql}')
        self.lock.acquire()
        try:
            cursor.execute(sql)
            results = cursor.fetchall()
            members = [Member(_id, name, num) for _id, name, num, _, _ in results]
            db.commit()
        except:
            members = []
        self.lock.release()
        return members
    
    def setMembersOnGroup(self, members: List[Member], group: Group = None):
        db = self.db
        cursor = db.cursor()
        self.lock.acquire()
        group_name = f'\'{group.name}\'' if group is not None else 'NULL'
        for member in members:
            sql = f"update nuc_students set studentname = {group_name} where no = '{member.num}';"
            print(sql)
            cursor.execute(sql)
        db.commit()
        self.lock.release()
        
    
    def getGroups(self) -> List[Group]:
        db = self.db
        cursor = db.cursor()
        sql = f"select * from nuc_groups inner join nuc_students on nuc_groups.name = nuc_students.studentname;"
        self.lock.acquire()
        cursor.execute(sql)
        results = cursor.fetchall()
        
        group_list: Dict[str, Group] = {}
        for gid, gname, score, rscore, _, modify, sid, sname, sno, _, _ in results:
            if str(gid) not in group_list:
                group_list[str(gid)] = Group(str(gid), gname, score, rscore, int(modify), [])
            m = Member(str(sid), sname, sno)
            group_list[str(gid)].members.append(m)
        
        db.commit()
        self.lock.release()
        return list(group_list.values())
    
    def updateGroup(self, group: Group, is_modify: bool = False):
        db = self.db
        cursor = db.cursor()
        if is_modify:
            sql = f"update nuc_groups set totalmark = {group.score}, ragularmark = {group.regularScore}, modifyTimestamp = {str(int(datetime.now().timestamp()))} where id = {group._id}"
        else:
            sql = f"update nuc_groups set totalmark = {group.score}, ragularmark = {group.regularScore} where id = {group._id}"
        self.lock.acquire()
        cursor.execute(sql)
        db.commit()
        self.lock.release()
        
    def getGroup(self, group: Group):
        db = self.db
        cursor = db.cursor()
        sql = f"select * from nuc_groups left join nuc_students on nuc_groups.name = nuc_students.studentname  where nuc_groups.id = {group._id} or nuc_groups.name = '{group.name}'; "
        print(sql)
        self.lock.acquire()
        cursor.execute(sql)
        results = cursor.fetchall()
        
        group_list: Dict[str, Group] = {}
        for gid, gname, score, rscore, _, modify, sid, sname, sno, _, _ in results:
            if str(gid) not in group_list:
                group_list[str(gid)] = Group(str(gid), gname, score, rscore, int(modify), [])
            if sname is not None:
                m = Member(str(sid), sname, sno)
                group_list[str(gid)].members.append(m)
        
        db.commit()
        self.lock.release()
        return list(group_list.values())[0] if len(group_list.values()) > 0 else None
    
    def removeGroup(self, group: Group):
        db = self.db
        cursor = db.cursor()
        sql = f"delete from nuc_groups where id = {group._id} or name = '{group.name}';"
        # print(sql)
        self.lock.acquire()
        cursor.execute(sql)
        results = cursor.fetchall()
        self.lock.release()
        return results
    
    def addGroup(self, group: Group):
        db = self.db
        cursor = db.cursor()
        sql = f"insert into  nuc_groups (name, totalmark, ragularmark, modifyTimestamp) values \
            ('{group.name}', {group.score}, {group.regularScore}, {str(int(datetime.now().timestamp()))});"
        # print(sql)
        self.lock.acquire()
        
        cursor.execute(sql)
        db.commit()
        
        self.lock.release()
        
    
    def __del__(self):
        self.db.close()
        
class DatabaseBzController:
    def __init__(self) -> None:
        self.dc = DatabaseController()
        
    def _sort_groups_with(self, groups: List[Group], sort_with: str):
        if sort_with == 'name':
            return sorted(groups, key=lambda x: x.name)
        elif sort_with == 'score':
            return sorted(groups, key=lambda x: x.score)
        elif sort_with == 'regularScore':
            return sorted(groups, key=lambda x: x.regularScore)
        elif sort_with == 'modifyTimestamp':
            return sorted(groups, key=lambda x: x.modifyTimestamp)
        return groups
    
    def getGroup(self, queryGroup: Group) -> Group:
        return self.dc.getGroup(queryGroup)
        
    def getAllGroups(self, sort_with: str = None) -> List[Group]:
        groups = self.dc.getGroups()
        return self._sort_groups_with(groups, sort_with)
    
    def getPageGroups(self, page: int, numPerPage: int, sort_with: str, sort_order: str) -> Tuple[List[Group], int]:
        groups = self.getAllGroups(sort_with)
        if sort_order == 'desc':
            groups.reverse()
        return groups[(page-1)*numPerPage:page*numPerPage], len(groups)
        
    def updateGroupScore(self, targetGroup: Group):
        self.dc.updateGroup(targetGroup, True)
        groups = self.getAllGroups()
        max_score = max(map(lambda x: x.score, groups))
        for group in groups:
            group.regularScore = group.score * 50 / max_score 
            self.dc.updateGroup(group)
        return 0
    
    def getAllSpareMembers(self):
        members = self.dc.getSpareMember()
        return members
    
    def createNewGroup(self, queryGroup: Group):
        group = self.dc.getGroup(queryGroup)
        if group is None:
            self.dc.addGroup(queryGroup)
            group = self.dc.getGroup(queryGroup)
        print(group)
        self.addMembersToGroup(queryGroup.members, group)
        
    
    def addMembersToGroup(self, members: List[Member], group: Group):
        self.dc.setMembersOnGroup(members, group)
        
    def removeMembersFromGroup(self, members: List[Member], group: Group):
        self.dc.setMembersOnGroup(members)
    
    
    def dismissGroup(self, group: Group):
        self.dc.removeGroup(group)
        self.dc.setMembersOnGroup(group.members)
        
    
if __name__ == '__main__':
    dbc = DatabaseBzController()
    
    groups = dbc.getAllGroups()
    print(list(map(lambda x: x.name, groups)))
    
    groups, total = dbc.getPageGroups(1, 5, None, None)
    print(list(map(lambda x: x.name, groups)), total)
    
    all_spare_members =  dbc.getAllSpareMembers()
    print(all_spare_members)
    queryGroup = Group(1, "临时", score=20, members=all_spare_members[:2])
    
    dbc.createNewGroup(queryGroup)
    group = dbc.getGroup(queryGroup)
    print(f"New Group {group}")
    
    remain_spare_members =  dbc.getAllSpareMembers()
    print(f"Get spare after creating {remain_spare_members}")
    
    dbc.addMembersToGroup(remain_spare_members, queryGroup)
    group = dbc.getGroup(queryGroup)
    print(f"Add member to Group {group}")
    remain_spare_members =  dbc.getAllSpareMembers()
    print(f"After add {remain_spare_members}")
    
    group = dbc.getGroup(queryGroup)
    print(f"Dismiss  Group {group}")    
    dbc.dismissGroup(group)
    group = dbc.getGroup(queryGroup)
    print(f"After dismiss Group {group}")
    remain_spare_members =  dbc.getAllSpareMembers()
    print(remain_spare_members)

    
    
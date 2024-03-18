import pymysql
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent.absolute()))


from model.data import Group, Member
from datetime import datetime
from typing import List, Dict, Tuple

class DatabaseController:
    def __init__(self) -> None:
        self.db = pymysql.connect(host="localhost", 
                     user="debian-sys-maint", 
                     password="mbjmYmElkwOe6Tg2", 
                     database="nuc_se_project")
        
    def updateMember(self, member: Member):
        pass
    
    def getGroups(self):
        db = self.db
        cursor = db.cursor()
        sql = f" select * from nuc_groups inner join nuc_students on nuc_groups.name = nuc_students.studentname;;"
        cursor.execute(sql)
        results = cursor.fetchall()
        db.commit()
        return results
    
    def updateGroup(self, group: Group, is_modify: bool = False):
        db = self.db
        cursor = db.cursor()
        if is_modify:
            sql = f"update nuc_groups set totalmark = {group.score}, ragularmark = {group.regularScore}, modifyTimestamp = {str(int(datetime.now().timestamp()))} where id = {group._id}"
        else:
            sql = f"update nuc_groups set totalmark = {group.score}, ragularmark = {group.regularScore} where id = {group._id}"
        cursor.execute(sql)
        db.commit()
        
    def getGroup(self, groupId: str):
        db = self.db
        cursor = db.cursor()
        sql = f" select * from nuc_groups inner join nuc_students on nuc_groups.name = nuc_students.studentname where nuc_groups.id = {groupId}"
        cursor.execute(sql)
        results = cursor.fetchall()
        return results
    
    def removeGroup(self, group: Group):
        pass
    
    def addGroup(self, group: Group):
        pass
    
    def __del__(self):
        self.db.close()
        
class DatabaseBzController:
    def __init__(self) -> None:
        self.dc = DatabaseController()
    
    def setGroupScore(self, group):
        self.dc.updateGroup(group)
        
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
        
    def getAllGroups(self, sort_with: str = None) -> List[Group]:
        results = self.dc.getGroups()
        group_list: Dict[str, Group] = {}
        for gid, gname, score, rscore, _, modify, sid, sname, sno, _, _ in results:
            if str(gid) not in group_list:
                group_list[str(gid)] = Group(str(gid), gname, score, rscore, int(modify), [])
            m = Member(str(sid), sname, sno)
            group_list[str(gid)].members.append(m)
            
        return self._sort_groups_with(list(group_list.values()), sort_with)
    
    def getPageGroups(self, page: int, numPerPage: int, sort_with: str, sort_order: str) -> Tuple[List[Group], int]:
        groups = self.getAllGroups(sort_with)
        if sort_order == 'desc':
            groups.reverse()
        return groups[(page-1)*numPerPage:page*numPerPage], len(groups)
        
    def updateGroupScore(self, groupId: str, updateScore):
        results = self.dc.getGroup(groupId)
        group_list: Dict[str, Group] = {}
        for gid, gname, score, rscore, _, modify, sid, sname, sno, _, _ in results:
            if str(gid) not in group_list:
                group_list[str(gid)] = Group(str(gid), gname, score, rscore, int(modify), [])
            m = Member(str(sid), sname, sno)
            group_list[str(gid)].members.append(m)
            
        if len(group_list) == 0:
            return -1
        else:
            queryGroup = list(group_list.values())[0]
            queryGroup.score = updateScore
            self.dc.updateGroup(queryGroup, True)
            groups = self.getAllGroups()
            max_score = max(map(lambda x: x.score, groups))
            for group in groups:
                group.regularScore = group.score * 50 / max_score 
                self.dc.updateGroup(group)
            return 0
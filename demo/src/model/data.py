from dataclasses import dataclass, field
import json
import random
import re

Names = """（1）Eric——艾利克　　Ron——罗恩
（2）Lydia——莉迪娅　　Page——裴吉
（3）Darcy——达茜　　Susan——苏珊
（4）Ida——艾达　　Sally——莎莉
（5）Una——优娜　　Ella——艾拉
（6）Liz——莉兹　　Ray——拉伊
（7）Nat——纳特　　Otis——奥狄斯
（8）Phil——菲尔　　Reg——雷哲
（9）Sam——山姆　　Alma——爱玛
（10）Ira——艾勒　　Gina——吉娜
（11）Alice——爱丽丝　　Ann——安妮
（12）Bella——贝拉　　Cara——卡拉
（13）Dora——多拉　　Hedy——赫蒂

英文起名 80个好听又短的英文名字介绍
（14）Iy——艾唯　　Jack——杰克
（15）John——约翰　　Joab——乔布
（16）Bob——鲍伯　　Dick——狄克
（17）Eli——伊莱　　Ken——肯恩
（18）Otto——奥特　　Alan——艾伦
（19）Rita——莉达　　Sara——莎拉
（20）Tess——泰丝　　Vera——维拉
（21）Xenia——芝妮雅　　Cara——卡拉
（22）Dana——黛娜　　Elva——艾娃
（23）Bill——比尔　　Bert——伯特
（24）Ben——班　　Carl——卡尔
（25）Drew——杜鲁　　Earl——额尔
（26）Gill——姬儿　　leo——利欧

英文起名 80个好听又短的英文名字介绍
（27）Jane——珍　　June——朱恩
（28）Linda——琳达　　Lucy——露西
（29）Guy——盖　　Hale——霍尔
（30）Ian——伊恩　　Jo——乔
（31）Will——维尔　　Les——勒斯
（32）Anna——安娜　　Bess——贝丝
（33）Dora——多拉　　Erin——艾琳
（34）Eve——伊芙　　Fay——费怡
（35）Don——多恩　　Eric——艾利克
（36）Neil——尼尔　　Bard——巴德
（37）Kim——金姆　　Jack——杰克
（38）Len——伦恩　　Max——马克斯
（39）Nina——妮娜　　Page——佩格
（40）Zona——若娜　　Jon——琼恩"""

NAMES = re.findall("[a-zA-Z]+", Names)
ID = 0
GID = 0
@dataclass
class Member:
    _id: str = ""
    name: str = ""
    num: str = ""

@dataclass
class Group:
    _id: str = ""
    name: str = ""
    score: float = 0
    members: list = field(default_factory=list)
    
    def to_json(self) -> str:
        members = list(map(lambda x: x.__dict__, self.members))
        data = {**self.__dict__}
        data['members'] = members
        return json.dumps(data, ensure_ascii=False)
    
    @staticmethod
    def random_gen() -> 'Group':
        
        def GenM():
            global ID
            m = Member(f"{ID}", f"M-{random.randrange(1, 20)}", f"N2023{random.randrange(1000, 2000)}")
            ID += 1
            return m
        global GID
        GID += 1
        return Group(f"{GID}",
            random.choice(NAMES), 
            random.randrange(0, 300, 10), 
            [GenM() for _ in range(5)]
            )
    
    def parse(data: str) -> 'Group':
        data = json.loads(data)
        members = data.get('members', [])
        members = list(map(lambda x: Member(**x), members))
        data['members'] = members
        return Group(**data)
    
if __name__ == '__main__':
    print(Group.random_gen())
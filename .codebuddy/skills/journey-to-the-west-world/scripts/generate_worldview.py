#!/usr/bin/env python3
"""
《西游记》世界观生成脚本
随机生成世界观相关的片段和描述
"""

import random
import json

class WorldViewGenerator:
    """世界观生成器"""
    
    def __init__(self):
        self.realms = {
            "天界": ["灵霄宝殿", "瑶池", "兜率宫", "斗牛宫", "南天门", "三十三重天"],
            "地界": ["地府", "阎罗殿", "十八层地狱", "奈何桥", "忘川河", "鬼门关"],
            "人界": ["东土大唐", "西天灵山", "花果山", "高老庄", "流沙河", "火焰山"]
        }
        
        self.deities = {
            "道教": ["三清", "四御", "五方五老", "六司", "七元", "八极", "九曜", "十都"],
            "佛教": ["佛", "菩萨", "罗汉", "金刚", "护法神"],
            "散仙": ["山神", "土地", "城隍", "河神"]
        }
        
        self.monsters = {
            "天生妖怪": ["孙悟空", "红孩儿"],
            "修炼成精": ["狐狸精", "蛇精", "虎精", "树精"],
            "神仙下凡": ["猪八戒", "沙僧", "青牛精", "金角大王"]
        }
        
        self.artifacts = {
            "攻击型": ["金箍棒", "九齿钉耙", "降妖宝杖"],
            "防御型": ["锦斓袈裟", "紫金铃"],
            "困敌型": ["幌金绳", "人种袋", "紫金红葫芦"]
        }
        
        self.cultivation_levels = [
            "凡人", "炼气期", "筑基期", "金丹期", "元婴期", "化神期",
            "炼虚期", "合体期", "大乘期", "渡劫期", "仙人"
        ]
        
        self.geography = {
            "四大部洲": ["东胜神洲", "西牛贺洲", "南赡部洲", "北俱芦洲"],
            "名山大川": ["昆仑山", "峨眉山", "五台山", "蓬莱岛", "花果山"]
        }
    
    def generate_realm_description(self):
        """生成三界描述"""
        realm = random.choice(list(self.realms.keys()))
        location = random.choice(self.realms[realm])
        
        descriptions = {
            "天界": f"位于人界之上的神圣领域，{location}是其中重要的场所。",
            "地界": f"位于人界之下的幽冥世界，{location}是亡魂必经之地。",
            "人界": f"位于天界与地界之间，{location}是故事发生的重要地点。"
        }
        
        return {
            "realm": realm,
            "location": location,
            "description": descriptions[realm],
            "time_rule": "天上一日，地上一年" if realm == "天界" else "正常时间流速"
        }
    
    def generate_deity_profile(self):
        """生成神仙档案"""
        system = random.choice(list(self.deities.keys()))
        rank = random.choice(self.deities[system])
        
        duties = {
            "三清": "道教最高神，生于太元之先",
            "四御": "协助玉帝管理三界",
            "佛": "佛教最高领袖，觉悟圆满",
            "菩萨": "自觉觉他，救苦救难",
            "山神": "掌管名山大川，守护一方"
        }
        
        duty = duties.get(rank, f"{system}中的{rank}，承担相应职责")
        
        return {
            "system": system,
            "rank": rank,
            "duty": duty,
            "residence": "天界" if system in ["道教", "佛教"] else "人界"
        }
    
    def generate_monster_story(self):
        """生成妖怪故事"""
        origin = random.choice(list(self.monsters.keys()))
        monster = random.choice(self.monsters[origin])
        
        stories = {
            "孙悟空": "由仙石孕育而生，拜师菩提祖师，学会七十二变和筋斗云。",
            "红孩儿": "牛魔王与铁扇公主之子，修炼三昧真火，后被观音收服。",
            "猪八戒": "原为天蓬元帅，因调戏嫦娥被贬下凡，错投猪胎。",
            "狐狸精": "修炼千年的狐狸，擅长变化和迷惑人心。"
        }
        
        story = stories.get(monster, f"一只{origin}，在《西游记》中有精彩表现。")
        
        return {
            "origin": origin,
            "name": monster,
            "story": story,
            "fate": "被收服" if monster in ["孙悟空", "红孩儿", "猪八戒"] else "被消灭"
        }
    
    def generate_artifact_info(self):
        """生成法宝信息"""
        category = random.choice(list(self.artifacts.keys()))
        artifact = random.choice(self.artifacts[category])
        
        info = {
            "金箍棒": "原为定海神针，重一万三千五百斤，可大小如意。",
            "九齿钉耙": "太上老君炼制，玉帝赐予天蓬元帅，重五千零四十八斤。",
            "紫金红葫芦": "喊人名字，答应即被吸入，一时三刻化为脓血。",
            "幌金绳": "可捆仙缚妖，念动咒语即自动捆绑。"
        }
        
        description = info.get(artifact, f"一件{category}法宝，在战斗中发挥重要作用。")
        
        return {
            "category": category,
            "name": artifact,
            "description": description,
            "holder": "孙悟空" if artifact == "金箍棒" else "未知"
        }
    
    def generate_cultivation_path(self):
        """生成修炼路径"""
        start_level = random.randint(0, 3)
        end_level = random.randint(7, 10)
        
        path = self.cultivation_levels[start_level:end_level+1]
        
        difficulties = ["容易", "中等", "困难", "极难"]
        time_required = random.randint(10, 1000)  # 年
        
        return {
            "path": path,
            "start": self.cultivation_levels[start_level],
            "end": self.cultivation_levels[end_level],
            "difficulty": random.choice(difficulties),
            "time_required": f"{time_required}年",
            "key_challenges": ["筑基", "结丹", "元婴", "化神", "渡劫"]
        }
    
    def generate_geography_feature(self):
        """生成地理特征"""
        region = random.choice(list(self.geography.keys()))
        place = random.choice(self.geography[region])
        
        features = {
            "东胜神洲": "多仙山福地，灵气浓郁，孙悟空的花果山即位于此。",
            "西牛贺洲": "佛教兴盛，如来佛祖的灵山位于此洲。",
            "昆仑山": "万山之祖，神仙居所，充满神秘色彩。",
            "花果山": "十洲之祖脉，三岛之来龙，孙悟空出生地。"
        }
        
        description = features.get(place, f"{region}中的{place}，在《西游记》中有重要地位。")
        
        return {
            "region": region,
            "place": place,
            "description": description,
            "significance": "重要地点" if place in features else "普通地点"
        }
    
    def generate_worldview_snippet(self, category=None):
        """生成世界观片段"""
        if category is None:
            category = random.choice(["realm", "deity", "monster", "artifact", "cultivation", "geography"])
        
        generators = {
            "realm": self.generate_realm_description,
            "deity": self.generate_deity_profile,
            "monster": self.generate_monster_story,
            "artifact": self.generate_artifact_info,
            "cultivation": self.generate_cultivation_path,
            "geography": self.generate_geography_feature
        }
        
        return generators[category]()
    
    def generate_full_worldview(self):
        """生成完整世界观描述"""
        return {
            "realms": [self.generate_realm_description() for _ in range(2)],
            "deities": [self.generate_deity_profile() for _ in range(2)],
            "monsters": [self.generate_monster_story() for _ in range(2)],
            "artifacts": [self.generate_artifact_info() for _ in range(2)],
            "cultivation_paths": [self.generate_cultivation_path() for _ in range(1)],
            "geography": [self.generate_geography_feature() for _ in range(2)]
        }


def main():
    """主函数"""
    generator = WorldViewGenerator()
    
    print("《西游记》世界观生成器")
    print("=" * 50)
    
    # 生成随机片段
    snippet = generator.generate_worldview_snippet()
    print("\n随机世界观片段：")
    print(json.dumps(snippet, ensure_ascii=False, indent=2))
    
    # 生成完整世界观
    print("\n" + "=" * 50)
    print("完整世界观描述（摘要）：")
    
    full_worldview = generator.generate_full_worldview()
    for category, items in full_worldview.items():
        print(f"\n{category}:")
        for item in items:
            name = item.get('name', item.get('realm', item.get('rank', '未知')))
            print(f"  - {name}")


if __name__ == "__main__":
    main()
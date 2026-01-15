#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
《西游记》简洁大纲生成脚本
生成简单的章节标题和2-3句内容总结
"""

import random

def generate_chapter_summary(chapter_number=None):
    """生成章节内容总结"""
    
    # 代表性章节的标题和总结
    chapter_data = [
        {
            "chapter": 1,
            "title": "灵根育孕源流出 心性修持大道生",
            "summary": "花果山石猴出世，发现水帘洞成为美猴王。为求长生出海拜师，得名孙悟空开始修行之路。"
        },
        {
            "chapter": 7,
            "title": "八卦炉中逃大圣 五行山下定心猿",
            "summary": "孙悟空大闹天宫后被太上老君投入八卦炉。四十九天后跳出，大闹天宫，被如来佛祖压于五行山下。"
        },
        {
            "chapter": 14,
            "title": "心猿归正 六贼无踪",
            "summary": "唐僧救出孙悟空，为其戴上紧箍咒。孙悟空打死六个强盗，师徒开始建立信任关系。"
        },
        {
            "chapter": 22,
            "title": "八戒大战流沙河 木叉奉法收悟净",
            "summary": "收服沙僧，取经团队完整。师徒五人正式踏上西行取经之路，开始八十一难历程。"
        },
        {
            "chapter": 27,
            "title": "尸魔三戏唐三藏 圣僧恨逐美猴王",
            "summary": "白骨精三次变化人形欺骗唐僧。孙悟空三次识破并打死，唐僧误以为滥杀无辜将其逐出师门。"
        },
        {
            "chapter": 49,
            "title": "三藏有灾沉水宅 观音救难现鱼篮",
            "summary": "师徒过通天河，完成前期磨难。观音菩萨化身渔妇救助，师徒继续西行。"
        },
        {
            "chapter": 59,
            "title": "唐三藏路阻火焰山 孙行者一调芭蕉扇",
            "summary": "师徒被火焰山阻挡去路。孙悟空向铁扇公主借芭蕉扇灭火，初次借扇被骗得到假扇。"
        },
        {
            "chapter": 74,
            "title": "长庚传报魔头狠 行者施为变化能",
            "summary": "师徒过狮驼岭，完成中期磨难。孙悟空运用智慧变化，克服强大妖怪阻挠。"
        },
        {
            "chapter": 99,
            "title": "九九数完魔灭尽 三三行满道归根",
            "summary": "八十一难圆满，取经任务完成。师徒功德圆满，准备到达灵山取得真经。"
        },
        {
            "chapter": 100,
            "title": "径回东土 五圣成真",
            "summary": "师徒到达灵山取得真经。返回东土传经布道，五人受封佛位修成正果。"
        }
    ]
    
    if chapter_number:
        # 查找指定章节
        for data in chapter_data:
            if data["chapter"] == chapter_number:
                return data
        # 如果没找到，返回通用格式
        return {
            "chapter": chapter_number,
            "title": f"第{chapter_number}回标题",
            "summary": f"这是《西游记》第{chapter_number}回的简要内容总结。"
        }
    else:
        # 随机返回一个章节
        return random.choice(chapter_data)

def generate_overview():
    """生成整体情节概览"""
    
    return {
        "stages": [
            {
                "name": "序幕：孙悟空出世与大闹天宫",
                "range": "第1-7回",
                "summary": "石猴从花果山出世，拜师学艺得名孙悟空。大闹龙宫地府，偷蟠桃盗仙丹，与天庭大战后被如来佛祖压于五行山下。"
            },
            {
                "name": "引子：取经任务缘起",
                "range": "第8-12回",
                "summary": "如来佛祖欲传经东土，观音菩萨寻找取经人。唐僧出身历难，唐太宗还阳后派其西行取经。"
            },
            {
                "name": "开端：取经团队组建",
                "range": "第13-22回",
                "summary": "唐僧救出孙悟空，收为徒弟。随后收服白龙马、猪八戒、沙僧，师徒五人正式踏上西行之路。"
            },
            {
                "name": "主体：西行取经历程",
                "range": "第23-99回",
                "summary": "师徒历经八十一难，遭遇白骨精、红孩儿、火焰山、狮驼岭等重重考验。降妖除魔中师徒不断磨合成长。"
            },
            {
                "name": "结局：取经圆满成功",
                "range": "第100回",
                "summary": "到达灵山取得真经，返回东土传经布道。师徒五人修成正果，受封佛位。"
            }
        ]
    }

def main():
    """主函数"""
    print("《西游记》简洁大纲生成器")
    print("=" * 50)
    
    print("\n1. 整体情节概览：")
    overview = generate_overview()
    for stage in overview["stages"]:
        print(f"\n{stage['name']}（{stage['range']}）")
        print(f"{stage['summary']}")
    
    print("\n" + "=" * 50)
    print("\n2. 章节摘要示例：")
    for chapter_num in [1, 27, 59, 100]:
        chapter = generate_chapter_summary(chapter_num)
        print(f"\n第{chapter['chapter']}回：{chapter['title']}")
        print(f"{chapter['summary']}")
    
    print("\n" + "=" * 50)
    print("\n3. 随机章节摘要：")
    random_chapter = generate_chapter_summary()
    print(f"\n第{random_chapter['chapter']}回：{random_chapter['title']}")
    print(f"{random_chapter['summary']}")

if __name__ == "__main__":
    main()
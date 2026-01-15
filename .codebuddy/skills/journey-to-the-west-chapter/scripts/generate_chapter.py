#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
《西游记》章节设计生成脚本
用于随机生成章节设计片段，供创作参考使用
"""

import random
import json
from datetime import datetime
from typing import Dict, List, Optional, Tuple

class ChapterGenerator:
    """章节生成器"""
    
    def __init__(self):
        self.templates = self._load_templates()
        self.characters = self._load_characters()
        self.scenes = self._load_scenes()
        self.conflicts = self._load_conflicts()
        
    def _load_templates(self) -> List[Dict]:
        """加载章节模板"""
        return [
            {
                "name": "经典四段式",
                "structure": ["起（开端）", "承（发展）", "转（高潮）", "合（结局）"],
                "description": "中国传统叙事的经典结构"
            },
            {
                "name": "多重障碍式",
                "structure": ["障碍一", "障碍二", "障碍三", "最终解决"],
                "description": "通过连续障碍推动情节发展"
            },
            {
                "name": "悬念推理式",
                "structure": ["谜题呈现", "调查推理", "真相大白"],
                "description": "以悬念和推理为主线"
            },
            {
                "name": "人性考验式",
                "structure": ["考验设置", "欲望挣扎", "考验总结"],
                "description": "聚焦人性弱点的考验"
            }
        ]
    
    def _load_characters(self) -> List[Dict]:
        """加载人物数据"""
        return [
            {
                "name": "孙悟空",
                "type": "主角",
                "traits": ["机智", "勇敢", "叛逆", "忠诚"],
                "abilities": ["七十二变", "筋斗云", "火眼金睛"],
                "symbolism": "自由精神，反抗权威"
            },
            {
                "name": "唐僧",
                "type": "主角",
                "traits": ["仁慈", "坚定", "迂腐", "慈悲"],
                "abilities": ["念紧箍咒", "讲经说法"],
                "symbolism": "向善求真，修行意志"
            },
            {
                "name": "猪八戒",
                "type": "主角",
                "traits": ["贪吃", "好色", "懒惰", "幽默"],
                "abilities": ["三十六变", "九齿钉耙"],
                "symbolism": "人性欲望，世俗追求"
            },
            {
                "name": "沙僧",
                "type": "主角",
                "traits": ["忠诚", "稳重", "沉默", "可靠"],
                "abilities": ["降妖宝杖", "负重前行"],
                "symbolism": "坚忍耐劳，平凡坚持"
            },
            {
                "name": "白龙马",
                "type": "主角",
                "traits": ["忠诚", "隐忍", "勇敢", "赎罪"],
                "abilities": ["变化人形", "日行千里"],
                "symbolism": "赎罪重生，默默奉献"
            }
        ]
    
    def _load_scenes(self) -> List[Dict]:
        """加载场景数据"""
        return [
            {
                "type": "自然景观",
                "examples": ["高山", "大河", "森林", "沙漠", "火焰山", "流沙河"],
                "mood": ["险峻", "壮丽", "神秘", "恐怖"],
                "function": "制造自然障碍，烘托氛围"
            },
            {
                "type": "人间社会",
                "examples": ["村庄", "城镇", "王国", "寺庙", "道观"],
                "mood": ["繁华", "衰败", "祥和", "混乱"],
                "function": "反映社会现实，制造人际冲突"
            },
            {
                "type": "神魔世界",
                "examples": ["天宫", "地府", "龙宫", "妖洞", "仙境"],
                "mood": ["神圣", "阴森", "奇幻", "诡异"],
                "function": "展现神话体系，制造超自然冲突"
            },
            {
                "type": "心理空间",
                "examples": ["梦境", "幻觉", "回忆", "内心独白"],
                "mood": ["朦胧", "扭曲", "深刻", "真实"],
                "function": "揭示人物内心，深化主题"
            }
        ]
    
    def _load_conflicts(self) -> List[Dict]:
        """加载冲突类型"""
        return [
            {
                "type": "人与自然",
                "examples": ["战胜自然灾害", "克服地理障碍", "适应恶劣环境"],
                "resolution": ["智慧应对", "技术进步", "神仙帮助"]
            },
            {
                "type": "人与社会",
                "examples": ["反抗不公制度", "解决社会矛盾", "建立和谐关系"],
                "resolution": ["改革制度", "调解矛盾", "教化民众"]
            },
            {
                "type": "人与神魔",
                "examples": ["降妖除魔", "神仙考验", "佛法点化"],
                "resolution": ["武力战胜", "智慧破解", "觉悟超越"]
            },
            {
                "type": "人与自我",
                "examples": ["克服欲望", "战胜恐惧", "认识真我", "实现成长"],
                "resolution": ["自我反思", "修行实践", "他人帮助", "最终觉悟"]
            }
        ]
    
    def generate_chapter_title(self) -> str:
        """生成章回标题"""
        first_lines = [
            "灵根育孕源流出", "心性修持大道生", "悟彻菩提真妙理",
            "四海千山皆拱伏", "官封弼马心何足", "乱蟠桃大圣偷丹",
            "八卦炉中逃大圣", "我佛造经传极乐", "观音奉旨上长安",
            "玄奘秉诚建大会", "陷虎穴金星解厄", "心猿归正六贼无踪",
            "蛇盘山诸神暗佑", "观音院僧谋宝贝", "孙行者大闹黑风山",
            "高老庄大圣除魔", "云栈洞悟空收八戒", "黄风岭唐僧有难",
            "护法设庄留大圣", "八戒大战流沙河", "尸魔三戏唐三藏"
        ]
        
        second_lines = [
            "心性修持大道生", "断魔归本合元神", "九幽十类尽除名",
            "名注齐天意未宁", "反天宫诸神捉怪", "小圣施威降大圣",
            "五行山下定心猿", "观音奉旨上长安", "唐太宗地府还魂",
            "观音显像化金蝉", "双叉岭伯钦留僧", "六贼无踪心猿归",
            "鹰愁涧意马收缰", "黑风山怪窃袈裟", "观世音收伏熊罴怪",
            "浮屠山玄奘受心经", "须弥灵吉定风魔", "木叉奉法收悟净",
            "圣僧恨逐美猴王"
        ]
        
        first = random.choice(first_lines)
        second = random.choice(second_lines)
        
        # 确保上下联不重复且有一定关联性
        if first == second:
            second = random.choice([line for line in second_lines if line != first])
        
        return f"{first} {second}"
    
    def generate_character_performance(self, character: Dict) -> Dict:
        """生成人物表现"""
        emotions = ["愤怒", "悲伤", "喜悦", "恐惧", "惊讶", "厌恶", "期待", "信任"]
        actions = [
            "勇敢战斗", "机智应对", "坚持原则", "克服困难",
            "帮助他人", "自我反省", "学习成长", "承担责任"
        ]
        
        return {
            "character": character["name"],
            "emotion": random.choice(emotions),
            "key_action": random.choice(actions),
            "growth": random.choice(["明显成长", "有所进步", "保持稳定", "面临挑战"]),
            "relationship_change": random.choice(["加强信任", "产生矛盾", "深化理解", "需要磨合"])
        }
    
    def generate_scene_description(self) -> Dict:
        """生成场景描述"""
        scene_type = random.choice(self.scenes)
        example = random.choice(scene_type["examples"])
        mood = random.choice(scene_type["mood"])
        
        return {
            "type": scene_type["type"],
            "location": example,
            "mood": mood,
            "description": f"{mood}的{example}场景",
            "function": scene_type["function"]
        }
    
    def generate_conflict_scene(self) -> Dict:
        """生成冲突场景"""
        conflict_type = random.choice(self.conflicts)
        example = random.choice(conflict_type["examples"])
        resolution = random.choice(conflict_type["resolution"])
        
        return {
            "type": conflict_type["type"],
            "description": example,
            "intensity": random.choice(["轻微", "中等", "激烈", "生死攸关"]),
            "resolution_method": resolution,
            "theme_connection": random.choice([
                "成长考验", "人性弱点", "智慧挑战", "团队协作"
            ])
        }
    
    def generate_structure_plan(self, template_name: str) -> List[Dict]:
        """生成结构计划"""
        template = next((t for t in self.templates if t["name"] == template_name), self.templates[0])
        
        structure_plan = []
        for stage in template["structure"]:
            structure_plan.append({
                "stage": stage,
                "content": self._generate_stage_content(stage),
                "duration_percentage": random.randint(20, 35),
                "key_elements": self._generate_key_elements()
            })
        
        # 调整总百分比为100%
        total = sum(item["duration_percentage"] for item in structure_plan)
        for item in structure_plan:
            item["duration_percentage"] = round(item["duration_percentage"] / total * 100)
        
        return structure_plan
    
    def _generate_stage_content(self, stage: str) -> str:
        """生成阶段内容"""
        content_map = {
            "起（开端）": ["引入主要人物", "设定故事背景", "提出核心冲突", "明确章节目标"],
            "承（发展）": ["矛盾逐渐升级", "设置更多障碍", "人物关系发展", "悬念不断增加"],
            "转（高潮）": ["冲突达到顶点", "情感最激烈处", "情节重大转折", "问题最为严重"],
            "合（结局）": ["问题得到解决", "人物状态变化", "为后续铺垫", "情感余韵留存"],
            "障碍一": ["第一个困难出现", "初步尝试解决", "遇到挫折失败", "需要调整策略"],
            "障碍二": ["更大困难出现", "运用智慧应对", "取得部分进展", "但仍未完全解决"],
            "障碍三": ["最大障碍出现", "需要协作解决", "关键突破点", "彻底克服困难"],
            "最终解决": ["所有问题解决", "获得深刻教训", "人物明显成长", "主题得到深化"],
            "谜题呈现": ["神秘事件发生", "初步线索出现", "人物感到困惑", "激发探究欲望"],
            "调查推理": ["收集更多线索", "进行逻辑推理", "可能有误判断", "逐渐接近真相"],
            "真相大白": ["关键证据发现", "所有谜团解开", "深层动机揭示", "主题升华体现"],
            "考验设置": ["人性诱惑出现", "考验规则说明", "人物初始反应", "读者预期形成"],
            "欲望挣扎": ["欲望理性斗争", "关键选择时刻", "行为后果显现", "心理微妙变化"],
            "考验总结": ["考验结果评估", "提炼深刻教训", "人物成长体现", "主题深化表达"]
        }
        
        return random.choice(content_map.get(stage, ["情节发展", "人物互动", "冲突解决", "主题表达"]))
    
    def _generate_key_elements(self) -> List[str]:
        """生成关键元素"""
        elements = [
            "人物对话", "心理描写", "环境烘托", "动作展现",
            "悬念设置", "情感表达", "冲突升级", "问题解决",
            "主题呼应", "文化隐喻", "成长体现", "关系变化"
        ]
        
        return random.sample(elements, k=random.randint(3, 6))
    
    def generate_artistic_features(self) -> List[Dict]:
        """生成艺术特色"""
        features = [
            {
                "type": "叙事视角",
                "techniques": ["全知视角", "有限视角", "多重视角", "视角转换"],
                "effect": "增强叙事层次，制造悬念效果"
            },
            {
                "type": "修辞手法",
                "techniques": ["夸张", "对比", "象征", "讽刺", "反复"],
                "effect": "增强语言表现力，深化主题内涵"
            },
            {
                "type": "情节设计",
                "techniques": ["悬念设置", "伏笔照应", "情节反转", "节奏控制"],
                "effect": "增强戏剧张力，保持读者兴趣"
            },
            {
                "type": "人物刻画",
                "techniques": ["外貌描写", "动作展现", "心理揭示", "对话艺术"],
                "effect": "塑造立体人物，增强情感共鸣"
            }
        ]
        
        selected_features = random.sample(features, k=random.randint(2, 4))
        for feature in selected_features:
            feature["selected_techniques"] = random.sample(
                feature["techniques"], 
                k=random.randint(1, 3)
            )
        
        return selected_features
    
    def generate_thematic_connections(self) -> Dict:
        """生成主题关联"""
        themes = [
            {
                "level": "表层主题",
                "name": "取经冒险",
                "connection": "通过具体行动展现取经之路的艰难",
                "significance": "体现人类对真理的不懈追求"
            },
            {
                "level": "中层主题",
                "name": "修行历练",
                "connection": "通过磨难考验展现心性成长过程",
                "significance": "揭示修行对人格完善的积极作用"
            },
            {
                "level": "深层主题",
                "name": "明心见性",
                "connection": "通过内心斗争展现觉悟的可能",
                "significance": "探索人性向神性升华的路径"
            },
            {
                "level": "文化主题",
                "name": "三教合一",
                "connection": "通过文化元素展现传统思想的融合",
                "significance": "体现中国文化包容并蓄的特点"
            }
        ]
        
        selected_themes = random.sample(themes, k=random.randint(2, 4))
        return {
            "themes": selected_themes,
            "overall_connection": "通过不同层面的主题交织，构建立体的叙事意义网络"
        }
    
    def generate_adaptation_suggestions(self) -> List[Dict]:
        """生成改编建议"""
        adaptations = [
            {
                "medium": "影视改编",
                "suggestions": [
                    "注重视觉奇观与情感共鸣的结合",
                    "合理压缩章节，突出核心情节",
                    "运用现代特效技术增强神话色彩",
                    "注意角色形象的统一与深化"
                ]
            },
            {
                "medium": "文学改编",
                "suggestions": [
                    "保持章回体语言风格特色",
                    "深入挖掘人物内心世界",
                    "适当加入现代思想元素",
                    "注意叙事节奏的控制"
                ]
            },
            {
                "medium": "游戏改编",
                "suggestions": [
                    "将八十一难设计为游戏关卡",
                    "合理设计角色技能与成长系统",
                    "注重游戏性与文化性的平衡",
                    "构建完整的西游游戏世界观"
                ]
            },
            {
                "medium": "教育应用",
                "suggestions": [
                    "提炼章节的教育价值与启示",
                    "设计互动学习活动与讨论",
                    "结合现代教育理念与方法",
                    "注重文化传承与创新结合"
                ]
            }
        ]
        
        return random.sample(adaptations, k=random.randint(2, 4))
    
    def generate_complete_chapter_design(self, template_name: Optional[str] = None) -> Dict:
        """生成完整章节设计"""
        if template_name is None:
            template_name = random.choice(self.templates)["name"]
        
        main_character = random.choice([c for c in self.characters if c["type"] == "主角"])
        
        return {
            "metadata": {
                "generated_at": datetime.now().isoformat(),
                "template_used": template_name,
                "chapter_number": random.randint(1, 100),
                "design_id": f"design_{random.randint(1000, 9999)}"
            },
            "chapter_title": self.generate_chapter_title(),
            "main_character": main_character["name"],
            "structure_plan": self.generate_structure_plan(template_name),
            "character_performance": self.generate_character_performance(main_character),
            "scenes": [self.generate_scene_description() for _ in range(random.randint(2, 4))],
            "conflicts": [self.generate_conflict_scene() for _ in range(random.randint(1, 3))],
            "artistic_features": self.generate_artistic_features(),
            "thematic_connections": self.generate_thematic_connections(),
            "adaptation_suggestions": self.generate_adaptation_suggestions(),
            "creative_notes": [
                "注意情节发展的逻辑性与连贯性",
                "注重人物情感的细腻表达",
                "保持中国古典文学的语言特色",
                "挖掘章节的深层文化内涵"
            ]
        }

def print_chapter_design(design: Dict, format_type: str = "text"):
    """打印章节设计"""
    if format_type == "json":
        print(json.dumps(design, ensure_ascii=False, indent=2))
        return
    
    # 文本格式输出
    print("=" * 80)
    print("《西游记》章节设计生成结果")
    print("=" * 80)
    
    print(f"\n📖 章节标题：{design['chapter_title']}")
    print(f"🎭 主要人物：{design['main_character']}")
    print(f"🏛️ 结构模板：{design['metadata']['template_used']}")
    print(f"🆔 设计编号：{design['metadata']['design_id']}")
    
    print(f"\n{'📊 结构规划':-^40}")
    for stage in design["structure_plan"]:
        print(f"  {stage['stage']} ({stage['duration_percentage']}%)")
        print(f"    内容：{stage['content']}")
        print(f"    关键元素：{', '.join(stage['key_elements'])}")
    
    print(f"\n{'🎭 人物表现':-^40}")
    perf = design["character_performance"]
    print(f"  人物：{perf['character']}")
    print(f"  主要情感：{perf['emotion']}")
    print(f"  关键行为：{perf['key_action']}")
    print(f"  成长状态：{perf['growth']}")
    print(f"  关系变化：{perf['relationship_change']}")
    
    print(f"\n{'🏞️ 场景设计':-^40}")
    for i, scene in enumerate(design["scenes"], 1):
        print(f"  场景{i}：{scene['location']} ({scene['type']})")
        print(f"    氛围：{scene['mood']}")
        print(f"    功能：{scene['function']}")
    
    print(f"\n{'⚔️ 冲突设计':-^40}")
    for i, conflict in enumerate(design["conflicts"], 1):
        print(f"  冲突{i}：{conflict['description']} ({conflict['type']})")
        print(f"    强度：{conflict['intensity']}")
        print(f"    解决方法：{conflict['resolution_method']}")
        print(f"    主题关联：{conflict['theme_connection']}")
    
    print(f"\n{'🎨 艺术特色':-^40}")
    for feature in design["artistic_features"]:
        print(f"  {feature['type']}：{', '.join(feature['selected_techniques'])}")
        print(f"    效果：{feature['effect']}")
    
    print(f"\n{'📚 主题关联':-^40}")
    for theme in design["thematic_connections"]["themes"]:
        print(f"  {theme['level']}：{theme['name']}")
        print(f"    关联点：{theme['connection']}")
        print(f"    意义：{theme['significance']}")
    
    print(f"\n{'🎬 改编建议':-^40}")
    for adapt in design["adaptation_suggestions"]:
        print(f"  {adapt['medium']}：")
        for suggestion in adapt['suggestions']:
            print(f"    • {suggestion}")
    
    print(f"\n{'💡 创作笔记':-^40}")
    for note in design["creative_notes"]:
        print(f"  • {note}")
    
    print("\n" + "=" * 80)
    print(f"生成时间：{design['metadata']['generated_at']}")
    print("=" * 80)

def main():
    """主函数"""
    print("《西游记》章节设计生成工具")
    print("-" * 40)
    
    generator = ChapterGenerator()
    
    print("\n可用模板：")
    for i, template in enumerate(generator.templates, 1):
        print(f"  {i}. {template['name']} - {template['description']}")
    
    try:
        choice = input("\n选择模板编号（直接回车随机选择）：").strip()
        if choice and choice.isdigit():
            idx = int(choice) - 1
            if 0 <= idx < len(generator.templates):
                template_name = generator.templates[idx]["name"]
            else:
                template_name = None
        else:
            template_name = None
        
        print("\n生成中...")
        design = generator.generate_complete_chapter_design(template_name)
        
        print("\n输出格式：")
        print("  1. 文本格式（默认）")
        print("  2. JSON格式")
        
        format_choice = input("\n选择输出格式（1或2，默认1）：").strip()
        format_type = "json" if format_choice == "2" else "text"
        
        print_chapter_design(design, format_type)
        
        # 保存选项
        save_choice = input("\n是否保存到文件？(y/n，默认n)：").strip().lower()
        if save_choice == 'y':
            filename = f"chapter_design_{design['metadata']['design_id']}.json"
            with open(filename, 'w', encoding='utf-8') as f:
                json.dump(design, f, ensure_ascii=False, indent=2)
            print(f"已保存到：{filename}")
        
    except KeyboardInterrupt:
        print("\n\n用户中断操作")
    except Exception as e:
        print(f"\n生成过程中出现错误：{e}")

if __name__ == "__main__":
    main()
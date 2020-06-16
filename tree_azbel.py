import pandas as pd
from openpyxl import Workbook

class Node:

    def __init__(self, name,required_num):
        self.children = {}
        self.name = "azbel"
        self.required_num = required_num
        self.types = 1
        self.outputs = 1
        self.required_by_father = 1

    def PrintTree(self):
        print(self.children)

    def insert_node(self,name,num,outputs):
        if len(name) != len(num):
            print ("something wrong")
            print (self.name)
            exit()
        else:
            for i in range(len(name)):
                self.children['node'+str(i)] = Node(name[i],num[i])
                self.children['node'+str(i)].name = name[i]
                self.types = len(name)
                self.outputs = outputs
                self.required_num = num
                self.children['node'+str(i)].required_by_father = self.required_by_father * self.required_num[i] / self.outputs


root = Node("azbel",1) #创建节点
# P5
root.insert_node(["建筑建造组件","建筑机库阵列","建筑贮藏舱","建筑实验室","建筑工厂","建筑维修设施","建筑提炼工厂","建筑停泊港","建筑市场网络","建筑医疗中心","建筑办公室中心","建筑宣传节点"],[6,4,4,8,8,4,4,4,4,4,4,4],1)
# print (root.children)
# P4
root.children["node0"].insert_node(["反破损快速反应无人机","纳米-工厂","有机砂浆喷注器","递推计算模块","自协调能源核心","无菌管道"],[3,5,5,3,3,3],1)#建筑建造组件
root.children["node1"].insert_node(["广播节点","纳米-工厂","递推计算模块","自协调能源核心","无菌管道","湿件主机"],[3,5,3,3,3,5],1)#建筑机库阵列
root.children["node2"].insert_node(["广播节点","反破损快速反应无人机","纳米-工厂","有机砂浆喷注器","无菌管道","湿件主机"],[5,3,3,3,3,5],1)#建筑贮藏舱
root.children["node3"].insert_node(["反破损快速反应无人机","纳米-工厂","递推计算模块","无菌管道","湿件主机"],[10,5,5,10,5],1)#建筑实验室
root.children["node4"].insert_node(["广播节点","纳米-工厂","有机砂浆喷注器","递推计算模块","自协调能源核心"],[5,10,10,5,5],1)#建筑工厂
root.children["node5"].insert_node(["反破损快速反应无人机","纳米-工厂","有机砂浆喷注器","递推计算模块","自协调能源核心","无菌管道"],[3,5,3,3,3,5],1)#建筑维修设施
root.children["node6"].insert_node(["纳米-工厂","有机砂浆喷注器","自协调能源核心","无菌管道","湿件主机"],[5,10,10,5,5],1)#建筑提炼工厂
root.children["node7"].insert_node(["广播节点","反破损快速反应无人机","有机砂浆喷注器","递推计算模块","自协调能源核心","湿件主机"],[5,3,3,3,3,5],1)#建筑停泊港
root.children["node8"].insert_node(["广播节点","纳米-工厂","有机砂浆喷注器","递推计算模块","自协调能源核心","无菌管道","湿件主机"],[15,10,10,5,5,15,10],1)#建筑市场网络
root.children["node9"].insert_node(["广播节点","反破损快速反应无人机","递推计算模块","自协调能源核心","无菌管道","湿件主机"],[3,5,3,3,3,5],1)#建筑医疗中心
root.children["node10"].insert_node(["广播节点","反破损快速反应无人机","有机砂浆喷注器","递推计算模块","自协调能源核心","无菌管道"],[5,3,5,3,3,3],1)#建筑办公室中心
root.children["node11"].insert_node(["广播节点","反破损快速反应无人机","递推计算模块","自协调能源核心","湿件主机"],[10,10,5,5,5],1)#建筑宣传节点
# P3
for i in range(12):
    for j in range((root.children['node'+str(i)].types)):
        if root.children['node'+str(i)].children['node'+str(j)].name == "递推计算模块":
            root.children['node'+str(i)].children['node'+str(j)].insert_node(["合成神经键","制导系统","透颅微控器"],[6,6,6],1)
        elif root.children['node'+str(i)].children['node'+str(j)].name == "反破损快速反应无人机":
            root.children['node'+str(i)].children['node'+str(j)].insert_node(["凝胶基质生物胶","危险物探测系统","大气内穿梭机"],[6,6,6],1)
        elif root.children['node'+str(i)].children['node'+str(j)].name == "广播节点":
            root.children['node'+str(i)].children['node'+str(j)].insert_node(["控制面板","数据芯片","高科技传信器"],[6,6,6],1)
        elif root.children['node'+str(i)].children['node'+str(j)].name == "纳米-工厂":
            root.children['node'+str(i)].children['node'+str(j)].insert_node(["工业炸药","反应金属","乌克米超导体"],[6,40,6],1)
        elif root.children['node'+str(i)].children['node'+str(j)].name == "湿件主机":
            root.children['node'+str(i)].children['node'+str(j)].insert_node(["超级计算机","生物技术研究报告","冷冻保存防腐剂"],[6,6,6],1)
        elif root.children['node'+str(i)].children['node'+str(j)].name == "无菌管道":
            root.children['node'+str(i)].children['node'+str(j)].insert_node(["灵巧单元建筑模块","水","疫苗"],[6,40,6],1)
        elif root.children['node'+str(i)].children['node'+str(j)].name == "有机砂浆喷注器":
            root.children['node'+str(i)].children['node'+str(j)].insert_node(["凝缩液","细菌","机器人技术"],[6,40,6],1)
        elif root.children['node'+str(i)].children['node'+str(j)].name == "自协调能源核心":
            root.children['node'+str(i)].children['node'+str(j)].insert_node(["监控无人机","核反应堆","密封薄膜"],[6,6,6],1)
        else:
            print ("P3 WTF!")
            print (root.children['node'+str(i)].children['node'+str(j)].name)
# P2
for i in range(12):
    for j in range((root.children['node'+str(i)].types)):
        for k in range(3):
            if root.children['node'+str(i)].children['node'+str(j)].children['node'+str(k)].name == "超级计算机":
                root.children['node'+str(i)].children['node'+str(j)].children['node'+str(k)].insert_node(["水冷CPU","冷却剂","消费级电器"],[10,10,10],3)
            elif root.children['node'+str(i)].children['node'+str(j)].children['node'+str(k)].name == "大气内穿梭机":
                root.children['node'+str(i)].children['node'+str(j)].children['node'+str(k)].insert_node(["超张力塑料","机械元件","微型电子元件"],[10,10,10],3)
            elif root.children['node'+str(i)].children['node'+str(j)].children['node'+str(k)].name == "高科技传信器":
                root.children['node'+str(i)].children['node'+str(j)].children['node'+str(k)].insert_node(["聚芳酰胺","传信器"],[10,10],3)
            elif root.children['node'+str(i)].children['node'+str(j)].children['node'+str(k)].name == "工业炸药":
                root.children['node'+str(i)].children['node'+str(j)].children['node'+str(k)].insert_node(["肥料","合成纺织品"],[10,10],3)
            elif root.children['node'+str(i)].children['node'+str(j)].children['node'+str(k)].name == "合成神经键":
                root.children['node'+str(i)].children['node'+str(j)].children['node'+str(k)].insert_node(["超张力塑料","培养基"],[10,10],3)
            elif root.children['node'+str(i)].children['node'+str(j)].children['node'+str(k)].name == "核反应堆":
                root.children['node'+str(i)].children['node'+str(j)].children['node'+str(k)].insert_node(["核能燃料","微纤维护盾"],[10,10],3)
            elif root.children['node'+str(i)].children['node'+str(j)].children['node'+str(k)].name == "机器人技术":
                root.children['node'+str(i)].children['node'+str(j)].children['node'+str(k)].insert_node(["机械元件","消费级电器"],[10,10],3)
            elif root.children['node'+str(i)].children['node'+str(j)].children['node'+str(k)].name == "监控无人机":
                root.children['node'+str(i)].children['node'+str(j)].children['node'+str(k)].insert_node(["硅酸盐玻璃","火箭燃料"],[10,10],3)
            elif root.children['node'+str(i)].children['node'+str(j)].children['node'+str(k)].name == "控制面板":
                root.children['node'+str(i)].children['node'+str(j)].children['node'+str(k)].insert_node(["生物电池","硅酸盐玻璃"],[10,10],3)
            elif root.children['node'+str(i)].children['node'+str(j)].children['node'+str(k)].name == "冷冻保存防腐剂":
                root.children['node'+str(i)].children['node'+str(j)].children['node'+str(k)].insert_node(["培养基","合成油","肥料"],[10,10,10],3)
            elif root.children['node'+str(i)].children['node'+str(j)].children['node'+str(k)].name == "灵巧单元建筑模块":
                root.children['node'+str(i)].children['node'+str(j)].children['node'+str(k)].insert_node(["建筑模块","微型电子元件"],[10,10],3)
            elif root.children['node'+str(i)].children['node'+str(j)].children['node'+str(k)].name == "密封薄膜":
                root.children['node'+str(i)].children['node'+str(j)].children['node'+str(k)].insert_node(["聚芳酰胺","基因肉制品"],[10,10],3)
            elif root.children['node'+str(i)].children['node'+str(j)].children['node'+str(k)].name == "凝胶基质生物胶":
                root.children['node'+str(i)].children['node'+str(j)].children['node'+str(k)].insert_node(["氧化物","生物电池","超导体"],[10,10,10],3)
            elif root.children['node'+str(i)].children['node'+str(j)].children['node'+str(k)].name == "凝缩液":
                root.children['node'+str(i)].children['node'+str(j)].children['node'+str(k)].insert_node(["氧化物","冷却剂"],[10,10],3)
            elif root.children['node'+str(i)].children['node'+str(j)].children['node'+str(k)].name == "生物技术研究报告":
                root.children['node'+str(i)].children['node'+str(j)].children['node'+str(k)].insert_node(["纳米体","家畜","建筑模块"],[10,10,10],3)
            elif root.children['node'+str(i)].children['node'+str(j)].children['node'+str(k)].name == "数据芯片":
                root.children['node'+str(i)].children['node'+str(j)].children['node'+str(k)].insert_node(["超张力塑料","微纤维护盾"],[10,10],3)
            elif root.children['node'+str(i)].children['node'+str(j)].children['node'+str(k)].name == "透颅微控器":
                root.children['node'+str(i)].children['node'+str(j)].children['node'+str(k)].insert_node(["生物电池","纳米体"],[10,10],3)
            elif root.children['node'+str(i)].children['node'+str(j)].children['node'+str(k)].name == "危险物探测系统":
                root.children['node'+str(i)].children['node'+str(j)].children['node'+str(k)].insert_node(["合成纺织品","病原体","传信器"],[10,10,10],3)
            elif root.children['node'+str(i)].children['node'+str(j)].children['node'+str(k)].name == "乌克米超导体":
                root.children['node'+str(i)].children['node'+str(j)].children['node'+str(k)].insert_node(["合成油","超导体"],[10,10],3)
            elif root.children['node'+str(i)].children['node'+str(j)].children['node'+str(k)].name == "疫苗":
                root.children['node'+str(i)].children['node'+str(j)].children['node'+str(k)].insert_node(["家畜","病原体"],[10,10],3)
            elif root.children['node'+str(i)].children['node'+str(j)].children['node'+str(k)].name == "制导系统":
                root.children['node'+str(i)].children['node'+str(j)].children['node'+str(k)].insert_node(["水冷CPU","传信器"],[10,10],3)
            else:
                print(root.children['node'+str(i)].children['node'+str(j)].name)
                # print(root.children['node'+str(i)].children['node'+str(j)].children['node'+str(k)].name)
                # print(root.children['node'+str(i)].children['node'+str(j)].children['node'+str(k)].required_num)

for i in range(12):
    for j in range((root.children['node'+str(i)].types)):
        for k in range(3):
            for l in range((root.children['node'+str(i)].children['node'+str(j)].children['node'+str(k)].types)):
                if (root.children['node'+str(i)].children['node'+str(j)].children['node'+str(k)].name == "反应金属") | \
                    (root.children['node'+str(i)].children['node'+str(j)].children['node'+str(k)].name == "细菌") | \
                    (root.children['node'+str(i)].children['node'+str(j)].children['node'+str(k)].name == "水"):
                    pass
                elif root.children['node'+str(i)].children['node'+str(j)].children['node'+str(k)].children['node'+str(l)].name == "病原体":
                    root.children['node'+str(i)].children['node'+str(j)].children['node'+str(k)].children['node'+str(l)].insert_node(["细菌","生物质"],[40,40],5)
                elif root.children['node'+str(i)].children['node'+str(j)].children['node'+str(k)].children['node'+str(l)].name == "超导体":
                    root.children['node'+str(i)].children['node'+str(j)].children['node'+str(k)].children['node'+str(l)].insert_node(["等离子体团","水"],[40,40],5)
                elif root.children['node'+str(i)].children['node'+str(j)].children['node'+str(k)].children['node'+str(l)].name == "超张力塑料":
                    root.children['node'+str(i)].children['node'+str(j)].children['node'+str(k)].children['node'+str(l)].insert_node(["氧","生物质"],[40,40],5)
                elif root.children['node'+str(i)].children['node'+str(j)].children['node'+str(k)].children['node'+str(l)].name == "传信器":
                    root.children['node'+str(i)].children['node'+str(j)].children['node'+str(k)].children['node'+str(l)].insert_node(["等离子体团","手性结构"],[40,40],5)
                elif root.children['node'+str(i)].children['node'+str(j)].children['node'+str(k)].children['node'+str(l)].name == "肥料":
                    root.children['node'+str(i)].children['node'+str(j)].children['node'+str(k)].children['node'+str(l)].insert_node(["细菌","蛋白质"],[40,40],5)
                elif root.children['node'+str(i)].children['node'+str(j)].children['node'+str(k)].children['node'+str(l)].name == "硅酸盐玻璃":
                    root.children['node'+str(i)].children['node'+str(j)].children['node'+str(k)].children['node'+str(l)].insert_node(["氧化剂","硅"],[40,40],5)
                elif root.children['node'+str(i)].children['node'+str(j)].children['node'+str(k)].children['node'+str(l)].name == "合成纺织品":
                    root.children['node'+str(i)].children['node'+str(j)].children['node'+str(k)].children['node'+str(l)].insert_node(["生物燃料","工业纤维"],[40,40],5)
                elif root.children['node'+str(i)].children['node'+str(j)].children['node'+str(k)].children['node'+str(l)].name == "合成油":
                    root.children['node'+str(i)].children['node'+str(j)].children['node'+str(k)].children['node'+str(l)].insert_node(["电解物","氧"],[40,40],5)
                elif root.children['node'+str(i)].children['node'+str(j)].children['node'+str(k)].children['node'+str(l)].name == "核能燃料":
                    root.children['node'+str(i)].children['node'+str(j)].children['node'+str(k)].children['node'+str(l)].insert_node(["稀有金属","有毒金属"],[40,40],5)
                elif root.children['node'+str(i)].children['node'+str(j)].children['node'+str(k)].children['node'+str(l)].name == "火箭燃料":
                    root.children['node'+str(i)].children['node'+str(j)].children['node'+str(k)].children['node'+str(l)].insert_node(["等离子体团","电解物"],[40,40],5)
                elif root.children['node'+str(i)].children['node'+str(j)].children['node'+str(k)].children['node'+str(l)].name == "机械元件":
                    root.children['node'+str(i)].children['node'+str(j)].children['node'+str(k)].children['node'+str(l)].insert_node(["反应金属","稀有金属"],[40,40],5)
                elif root.children['node'+str(i)].children['node'+str(j)].children['node'+str(k)].children['node'+str(l)].name == "基因肉制品":
                    root.children['node'+str(i)].children['node'+str(j)].children['node'+str(k)].children['node'+str(l)].insert_node(["蛋白质","生物质"],[40,40],5)
                elif root.children['node'+str(i)].children['node'+str(j)].children['node'+str(k)].children['node'+str(l)].name == "家畜":
                    root.children['node'+str(i)].children['node'+str(j)].children['node'+str(k)].children['node'+str(l)].insert_node(["蛋白质","生物燃料"],[40,40],5)
                elif root.children['node'+str(i)].children['node'+str(j)].children['node'+str(k)].children['node'+str(l)].name == "建筑模块":
                    root.children['node'+str(i)].children['node'+str(j)].children['node'+str(k)].children['node'+str(l)].insert_node(["反应金属","有毒金属"],[40,40],5)
                elif root.children['node'+str(i)].children['node'+str(j)].children['node'+str(k)].children['node'+str(l)].name == "聚芳酰胺":
                    root.children['node'+str(i)].children['node'+str(j)].children['node'+str(k)].children['node'+str(l)].insert_node(["氧化剂","工业纤维"],[40,40],5)
                elif root.children['node'+str(i)].children['node'+str(j)].children['node'+str(k)].children['node'+str(l)].name == "冷却剂":
                    root.children['node'+str(i)].children['node'+str(j)].children['node'+str(k)].children['node'+str(l)].insert_node(["电解物","水"],[40,40],5)
                elif root.children['node'+str(i)].children['node'+str(j)].children['node'+str(k)].children['node'+str(l)].name == "纳米体":
                    root.children['node'+str(i)].children['node'+str(j)].children['node'+str(k)].children['node'+str(l)].insert_node(["细菌","反应金属"],[40,40],5)
                elif root.children['node'+str(i)].children['node'+str(j)].children['node'+str(k)].children['node'+str(l)].name == "培养基":
                    root.children['node'+str(i)].children['node'+str(j)].children['node'+str(k)].children['node'+str(l)].insert_node(["细菌","水"],[40,40],5)
                elif root.children['node'+str(i)].children['node'+str(j)].children['node'+str(k)].children['node'+str(l)].name == "生物电池":
                    root.children['node'+str(i)].children['node'+str(j)].children['node'+str(k)].children['node'+str(l)].insert_node(["生物燃料","稀有金属"],[40,40],5)
                elif root.children['node'+str(i)].children['node'+str(j)].children['node'+str(k)].children['node'+str(l)].name == "水冷CPU":
                    root.children['node'+str(i)].children['node'+str(j)].children['node'+str(k)].children['node'+str(l)].insert_node(["反应金属","水"],[40,40],5)
                elif root.children['node'+str(i)].children['node'+str(j)].children['node'+str(k)].children['node'+str(l)].name == "微纤维护盾":
                    root.children['node'+str(i)].children['node'+str(j)].children['node'+str(k)].children['node'+str(l)].insert_node(["工业纤维","硅"],[40,40],5)
                elif root.children['node'+str(i)].children['node'+str(j)].children['node'+str(k)].children['node'+str(l)].name == "微型电子元件":
                    root.children['node'+str(i)].children['node'+str(j)].children['node'+str(k)].children['node'+str(l)].insert_node(["手性结构","硅"],[40,40],5)
                elif root.children['node'+str(i)].children['node'+str(j)].children['node'+str(k)].children['node'+str(l)].name == "消费级电器":
                    root.children['node'+str(i)].children['node'+str(j)].children['node'+str(k)].children['node'+str(l)].insert_node(["有毒金属","手性结构"],[40,40],5)
                elif root.children['node'+str(i)].children['node'+str(j)].children['node'+str(k)].children['node'+str(l)].name == "氧化物":
                    root.children['node'+str(i)].children['node'+str(j)].children['node'+str(k)].children['node'+str(l)].insert_node(["氧化剂","氧"],[40,40],5)
                else:
                    print ("P1 WTF!")



print ("\n\n\n\n")
print ("\n\n\n\n")

def breadth_travel(root):
    """利用队列实现树的层次遍历"""
    if root == None:
        return
    required = {
'azbel' : 0 ,
'建筑建造组件' : 0,
'建筑机库阵列' : 0,
'建筑贮藏舱' : 0,
'建筑实验室' : 0,
'建筑工厂' : 0,
'建筑维修设施' : 0,
'建筑提炼工厂' : 0,
'建筑停泊港' : 0,
'建筑市场网络' : 0,
'建筑医疗中心' : 0,
'建筑办公室中心' : 0,
'建筑宣传节点' : 0,

'递推计算模块' : 0,
'反破损快速反应无人机' : 0,
'广播节点' : 0,
'纳米-工厂' : 0,
'湿件主机' : 0,
'无菌管道' : 0,
'有机砂浆喷注器' : 0,
'自协调能源核心' : 0,

'超级计算机' : 0,
'大气内穿梭机' : 0,
'高科技传信器' : 0,
'工业炸药' : 0,
'合成神经键' : 0,
'核反应堆' : 0,
'机器人技术' : 0,
'监控无人机' : 0,
'控制面板' : 0,
'冷冻保存防腐剂' : 0,
'灵巧单元建筑模块' : 0,
'密封薄膜' : 0,
'凝胶基质生物胶' : 0,
'凝缩液' : 0,
'生物技术研究报告' : 0,
'数据芯片' : 0,
'透颅微控器' : 0,
'危险物探测系统' : 0,
'乌克米超导体' : 0,
'疫苗' : 0,
'制导系统' : 0,

'病原体' : 0,
'超导体' : 0,
'超张力塑料' : 0,
'传信器' : 0,
'肥料' : 0,
'硅酸盐玻璃' : 0,
'合成纺织品' : 0,
'合成油' : 0,
'核能燃料' : 0,
'火箭燃料' : 0,
'机械元件' : 0,
'基因肉制品' : 0,
'家畜' : 0,
'建筑模块' : 0,
'聚芳酰胺' : 0,
'冷却剂' : 0,
'纳米体' : 0,
'培养基' : 0,
'生物电池' : 0,
'水冷CPU' : 0,
'微纤维护盾' : 0,
'微型电子元件' : 0,
'消费级电器' : 0,
'氧化物' : 0,

'细菌' : 0,
'生物质' : 0,
'等离子体团' : 0,
'水' : 0,
'氧' : 0,
'手性结构' : 0,
'蛋白质' : 0,
'氧化剂' : 0,
'硅' : 0,
'生物燃料' : 0,
'工业纤维' : 0,
'电解物' : 0,
'稀有金属' : 0,
'有毒金属' : 0,
'反应金属' : 0
    }
    queue = []
    queue.append(root)
    while queue:
        node = queue.pop(0)
        required[node.name] = required[node.name] + node.required_by_father
        if node.children != {}:
            for i in range(node.types):
                queue.append(node.children['node'+str(i)])
    
    print (required)
    return required

data = breadth_travel(root)

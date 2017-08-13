#coding = utf-8
#author:QINWANG
'''
使用pyecharts 创建不同的图形图像
目前有：xxxx等图像
'''
from  pyecharts import Line
from  tools.ConnectDB import DbSomething

a = DbSomething('localhost','dns_query', 'postgres', 111111)
v1,v2 = a.search()
print (v1,v2)

class GenPic:
    '''生成折线图'''
    def lineChart(self):
        line= Line("QPS图")
        line.add('', v1, v2)
        line.show_config()
        line.render()


if __name__=='__main__':
    pic = GenPic()
    pic.lineChart()
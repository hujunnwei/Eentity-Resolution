import re
import interspace
ary=[]
aryy=[]
aryyy = []
match=dict()
def readfile():
    with open("restaurant.apcpa.w100.l100_output_0.3.txt",encoding='utf-8')as f:
        for line in f:
            if "target entity" in line:
                num=re.sub(u"([^\u0030-\u0039])","", line)
                #print(num)
                ary.append(num)
                # print(len(ary))
            if "similar entities" in line:
                num=re.sub(u"([^\u0030-\u0039])"," ", line)
                num=num.strip()
                num=num.split("  ")
                #print(num)
                aryy.append(num)
    ary[0]="</s>"
    for i in range(0,len(ary)):
        match[ary[i]]=aryy[i]
    #print(match)  #字典的key:target entity,value:similar entities
    # for i in range(0, len(ary)):
    #     with open("all embedding.txt",encoding='utf-8')as f:
    #         for line in f:
    #             if line.startswith(ary[i]):
    #                 # print(ary[i])
    #                 # print(line)
    #                 aryyy.append(line.strip('\n').split(" "))
    #                 break
    # for i in range(0,len(aryyy)):
    #     aryyy[i].pop(0)
    #     aryyy[i].pop()
def readvector(node):
    with open("all embedding.txt", encoding='utf-8') as f:
        for line in f:
            if line.startswith(node):
                line=line.strip('\n').split(" ")
                line.pop(0)
                line.pop()
                return line

if __name__ == '__main__':
    readfile()
    # print(ary)
    # print(aryy)
    # print(type(ary))
    # print(type(aryy))
    # print(type(aryy[10]))
    #print(interspace.euclidean(readvector(ary[10]),readvector(aryy[10][0])))
    outfile=open("block_graph.txt",'w',encoding='utf-8')
    for i in range(1,len(ary)):
        outfile.write("target entity: ")
        outfile.write(ary[i])
        outfile.write("\n")
        outfile.write("possible pairs: ")
        outfile.write("\n")
        for j in range(0,len(aryy[i])):
            if len(aryy[i])>1: #if aryy[i][0] != ''
                outfile.write('('+ary[i] + '-' + aryy[i][j]+')'+':')
                outfile.write(str(interspace.euclidean(readvector(ary[i]),readvector(aryy[i][j]))))
                outfile.write("\n")

import re
ary=[]
aryy=[]
def readfile():
    total_edge = 0
    with open("citation_network_1000_second_prune/prune_AM_blocks.txt",'r',encoding='utf-8')as f:
        for line in f:
            if "target entity" in line:
                num=re.sub(u"([^\u0030-\u0039])","", line)
                # print(num)
                ary.append(num)
                # print(len(ary))
            if "similar entities" in line:
                num=re.sub(u"([^\u0030-\u0039])"," ", line)
                num=num.strip()
                num=num.split(" ")
                # print(num)
                aryy.append(num)
    print(ary[0])
    print(len(ary))
    for i in range(0,len(ary)):
        if aryy[i][0] != '':
            total_edge=total_edge+len(aryy[i])
    print(total_edge)
readfile()
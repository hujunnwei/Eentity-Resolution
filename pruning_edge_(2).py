import re
ary=[]
aryy=[]
ary_weight=[]

def readfile():
    total_edge = 0
    with open("citation_network_dm/Autoencoder+M_embedding_output.txt",'r',encoding='utf-8')as f:
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
    # ary[0]="</s>"
    for i in range(0,len(ary)):
        if aryy[i][0] != '':
            total_edge=total_edge+len(aryy[i])
    print(total_edge)

def get_weight():
    blocks = 0
    aryyy=[]
    for i in range(0, len(aryy)):
        if aryy[i][0] != '':
            blocks = blocks + 1
    print(blocks)
    max_similar_len = len(aryy[0])
    for i in range(0, len(aryy)):
        if len(aryy[i]) > max_similar_len:
            max_similar_len = len(aryy[i])
    print(max_similar_len)
    for i in range(0, len(ary)):
        for j in range(0, len(aryy[i])):
            if aryy[i][0] != '':
                for k in range(0, len(ary)):
                    if aryy[i][j] == ary[k]:
                        Cbs = 2 / max_similar_len
                        Arcs = (1 / len(aryy[i]) + 1 / len(aryy[k])) / (blocks / max_similar_len)
                        weight = 2 * (Cbs * Arcs) / (Cbs + Arcs)
                        aryyy.append(str(weight))
                        break
        if len(aryyy)>0:
            ary_weight.append(aryyy)
        else:
            aryyy.append('')
            ary_weight.append(aryyy)
        aryyy=[]
    # print(len(ary_weight))
    # for i in range(0,len(ary_weight)):
    #     if ary_weight[i][0]=='':
    #         print(ary_weight[i])

def average(numbers_edge,total_weight):
    return total_weight/numbers_edge

def pruning():
    # for i in range(0,len(ary_weight)):
    #     if len(ary_weight[i])==1:
    #         print(ary_weight[i])
    outfile=open("citation_network_1000_first_prune/prune_AM_blocks_(2).txt",'w',encoding='utf-8')
    for i in range(0,len(ary)):
        outfile.write("target entity: ")
        outfile.write(ary[i])
        outfile.write("\n")
        outfile.write("similar entities: ")
        if aryy[i][0] != '':
            total_weight=0
            for j in range(0,len(aryy[i])):
                total_weight=total_weight+float(ary_weight[i][j])
            numbers_edge=len(aryy[i])#total_edge_1=len(ary_weight[i]) print(total_edge,total_edge_1)
            average_weight=average(numbers_edge,total_weight)
            #print(average_weight)
            for j in range(0,len(aryy[i])):
                if float(ary_weight[i][j])>=average_weight:
                    outfile.write(aryy[i][j])
                    outfile.write(" ")
        outfile.write("\n")

if __name__ == '__main__':
    readfile()
    get_weight()
    pruning()
    #print(total_edge,total_weight,average_weight)
    
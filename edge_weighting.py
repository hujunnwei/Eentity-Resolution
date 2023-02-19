import re
import interspace
ary=[]
aryy=[]
match=dict()
def readfile():
    with open("restaurant_dm/CTT+M_embedding_output.txt",encoding='utf-8')as f:
        for line in f:
            if "target entity" in line:
                num=re.sub(u"([^\u0030-\u0039])","", line)
                #print(num)
                ary.append(num)
                # print(len(ary))
            if "similar entities" in line:
                num=re.sub(u"([^\u0030-\u0039])"," ", line)
                num=num.strip()
                num=num.split(" ")
                #print(num)
                aryy.append(num)
    # ary[0]="</s>"
    # for i in range(0,len(ary)):
    #     match[ary[i]]=aryy[i]
    # print(match)

if __name__ == '__main__':
    readfile()
    blocks=0
    for i in range(0,len(aryy)):
        if aryy[i][0]!='':
            blocks=blocks+1
    print(blocks)
    max_similar_len=len(aryy[0])
    for i in range(0,len(aryy)):
        if len(aryy[i])>max_similar_len:
            max_similar_len=len(aryy[i])
    print(max_similar_len)
    outfile = open("restaurant_dm/block_graph_CM.txt", 'w', encoding='utf-8')
    for i in range(0, len(ary)):
        outfile.write("target entity: ")
        outfile.write(ary[i])
        outfile.write("\n")
        outfile.write("possible pairs: ")
        outfile.write("\n")
        for j in range(0, len(aryy[i])):
            if aryy[i][0]!='':
                for k in range(0,len(ary)):
                    if aryy[i][j]==ary[k]:
                        outfile.write('(' + ary[i] + '-' + aryy[i][j] + ')' + ':')
                        Cbs=2/max_similar_len
                        Arcs=(1/len(aryy[i])+1/len(aryy[k]))/(blocks/max_similar_len)
                        weight=2*(Cbs*Arcs)/(Cbs+Arcs)
                        outfile.write(str(weight))
                        outfile.write("\n")
                        break
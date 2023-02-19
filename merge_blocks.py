import re
m_ary=[]
m_aryy=[]
d_ary=[]
d_aryy=[]
def readfile():
    with open("citation_network_metapath_pvp/citation.pvp.w100.l100_1000_output_0.1.txt",encoding='utf-8')as f:
        for line in f:
            if "target entity" in line:
                num=re.sub(u"([^\u0030-\u0039])","", line)
                #print(num)
                m_ary.append(num)
                # print(len(ary))
            if "similar entities" in line:
                num=re.sub(u"([^\u0030-\u0039])"," ", line)
                num=num.strip()
                num=num.split("  ")
                #print(num)
                m_aryy.append(num)
    m_ary[0]="</s>"
    with open("citation_network_metapath_vpv/citation.vpv.w100.l100_1000_output_0.1.txt",encoding='utf-8')as f:
        for line in f:
            if "target entity" in line:
                num=re.sub(u"([^\u0030-\u0039])","", line)
                #print(num)
                d_ary.append(num)
                # print(len(ary))
            if "similar entities" in line:
                num=re.sub(u"([^\u0030-\u0039])"," ", line)
                num=num.strip()
                num=num.split("  ")
                #print(num)
                d_aryy.append(num)
    # print(m_ary)
    # print(m_aryy)
    # print(d_ary)
    # print(d_aryy)
    print(len(m_ary))
    print(len(d_ary))
    k=0
    outfile=open("citation_network_metapath_pvp+vpv/pvp+vpv_0.1+0.1.txt",'w',encoding='utf-8')
    for i in range(0,len(m_ary)):
        if m_ary[i] in d_ary:
            k=k+1
            outfile.write("target entity: ")
            outfile.write(m_ary[i])
            outfile.write("\n")
            outfile.write("similar entities: ")
            ml_arry=list(set(m_aryy[i]+d_aryy[d_ary.index(m_ary[i])]))
            # print(ml_arry)
            for j in range(0,len(ml_arry)):
                if ml_arry[j]!='':
                    outfile.write(ml_arry[j])
                    outfile.write(" ")
            outfile.write("\n")
    print(k)

if __name__ == '__main__':
    readfile()
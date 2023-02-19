import re
ary = []
aryy = []
aryyy = []

def readfile():
    with open("citation_network_1000_second_prune/prune_AM_blocks.txt", 'r', encoding='utf-8')as f:
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
    # print(ary)
    # print(aryy)
    f.close()

def read_rules_lhs():
    with open("entity_resolution/produce_Table0.txt", 'r', encoding='utf-8')as f:
        for line in f:
            line = line.replace('\'','') 
            line = line.replace(' ','')
            line = line.strip('[').strip('\n').strip(']').split(',')
            line.sort()
            if line not in aryyy:
                aryyy.append(line)
    f.close()
    with open("entity_resolution/produce_Table1.txt", 'r', encoding='utf-8')as f:
        for line in f:
            line = line.replace('\'','') 
            line = line.replace(' ','')
            line = line.strip('[').strip('\n').strip(']').split(',')
            line.sort()
            if line not in aryyy:
                aryyy.append(line)
    f.close()
    with open("entity_resolution/produce_Table2.txt", 'r', encoding='utf-8')as f:
        for line in f:
            line = line.replace('\'','') 
            line = line.replace(' ','')
            line = line.strip('[').strip('\n').strip(']').split(',')
            line.sort()
            if line not in aryyy:
                aryyy.append(line)
    f.close()
    with open("entity_resolution/produce_Table3.txt", 'r', encoding='utf-8')as f:
        for line in f:
            line = line.replace('\'','') 
            line = line.replace(' ','')
            line = line.strip('[').strip('\n').strip(']').split(',')
            line.sort()
            if line not in aryyy:
                aryyy.append(line)
    f.close()
    # print(aryyy)


def real_match():
    outfile=open("citation_network_final_match/match_pairs_rule.txt", 'w', encoding='utf-8')
    for i in range(0, len(ary)):
        outfile.write("target entity: ")
        outfile.write(ary[i])
        outfile.write('\n')
        outfile.write("similar entities: ")
        for j in range(0, len(aryyy)):
            if ary[i] in aryyy[j]:
                for k in range(0, len(aryy[i])):
                    if aryy[i][k] in aryyy[j]:
                        outfile.write(aryy[i][k] + " ")
                break
        outfile.write('\n')   
    outfile.close()

if __name__ == '__main__':
    readfile()
    read_rules_lhs()
    real_match()
import re
ary=[]
aryy=[]
aryyy=[]
def readfile():
    with open("citation_network_dm/Autoencoder+M_embedding_output.txt", 'r', encoding='utf-8')as f:
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

def read_nodes_information():
    with open("citation_network_1000_second_prune/entity_attribute.txt",'r',encoding='utf-8')as f:
        for line in f:
            line = line.strip('\n').split('\t')
            aryyy.append(line)
    # print(aryyy)

def find_node_information(node_id):
    for i in range(0, len(aryyy)):
        if aryyy[i][0] == node_id:
            return aryyy[i]

def dice_coefficient(a, b):
    """dice coefficient 2nt/na + nb."""
    a_bigrams = set(a)
    b_bigrams = set(b)
    overlap = len(a_bigrams & b_bigrams)
    # print("overlap: ",overlap)
    return overlap * 2.0/(len(a_bigrams) + len(b_bigrams))

def pruning():
    a = []
    outfile=open("citation_network_1000_second_prune/prune_AM_blocks.txt",'w',encoding='utf-8')
    for i in range(0,len(ary)):
        outfile.write("target entity: ")
        outfile.write(ary[i])
        outfile.write("\n")
        outfile.write("similar entities: ")
        if aryy[i][0] != '':
            for j in range(0,len(aryy[i])):
                if len(find_node_information(ary[i])) == 7 and len(find_node_information(aryy[i][j])) == 7:
                    a.append(dice_coefficient(find_node_information(ary[i])[3], find_node_information(aryy[i][j])[3]))
                    if dice_coefficient(find_node_information(ary[i])[3], find_node_information(aryy[i][j])[3]) >= 0.9:
                        outfile.write(aryy[i][j]+" ")
                elif len(find_node_information(ary[i])) == 5 and len(find_node_information(aryy[i][j])) == 5:
                    if find_node_information(ary[i])[1] == '0' and find_node_information(aryy[i][j])[1] == '0':
                        a.append(dice_coefficient(find_node_information(ary[i])[2], find_node_information(aryy[i][j])[2]))
                        if dice_coefficient(find_node_information(ary[i])[2], find_node_information(aryy[i][j])[2]) >= 0.9:
                            outfile.write(aryy[i][j] + " ")
                    elif find_node_information(ary[i])[1] == '2' and find_node_information(aryy[i][j])[1] == '2':
                        a.append(dice_coefficient(find_node_information(ary[i])[2], find_node_information(aryy[i][j])[2]))
                        if dice_coefficient(find_node_information(ary[i])[2], find_node_information(aryy[i][j])[2]) >= 0.9:
                            outfile.write(aryy[i][j] + " ")
                    else:
                        print('---------------------')
                        print(ary[i],aryy[i][j])
                        a.append(ary[i] + aryy[i][j])
                else:
                    print('************************')
                    a.append(ary[i] + aryy[i][j])
        outfile.write('\n')
    # print(a)


if __name__ == '__main__':
    readfile()
    read_nodes_information()
    pruning()
    # print(dice_coefficient('Lvensshtain','Levenshtein'))

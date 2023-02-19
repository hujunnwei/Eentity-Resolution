from sentence_transformers import SentenceTransformer, LoggingHandler
import numpy as np
import logging
import interspace
import re
ary=[]
aryy=[]
aryyy=[]
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

def read_nodes_information():
    with open("citation_network_1000_second_prune/entity_attribute.txt", 'r', encoding='utf-8')as f:
        for line in f:
            line = line.strip('\n').split('\t')
            aryyy.append(line)
    # print(aryyy)

def find_node_information(node_id):
    for i in range(0, len(aryyy)):
        if aryyy[i][0] == node_id:
            return aryyy[i]

def generate_embedding(attribute1,attribute2,model):

    # Embed a list of sentences
    sentences = []
    sentences.append(attribute1)
    sentences.append(attribute2)
    sentence_embeddings = model.encode(sentences)

    # The result is a list of sentence embeddings as numpy arrays
    # for sentence, embedding in zip(sentences, sentence_embeddings):
    #     print("Sentence:", sentence)
    #     print("Embedding:", embedding)
    #     print(len(embedding))
    #     print("")
    return sentence_embeddings[0],sentence_embeddings[1]

def real_match():
    #### Just some code to print debug information to stdout
    np.set_printoptions(threshold=100)

    logging.basicConfig(format='%(asctime)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S',
                        level=logging.INFO,
                        handlers=[LoggingHandler()])
    #### /print debug information to stdout

    # Load pre-trained Sentence Transformer Model. It will be downloaded automatically
    model = SentenceTransformer('all-MiniLM-L6-v2')
    
    a = []
    outfile=open("citation_network_final_match/match_pairs.txt",'w',encoding='utf-8')
    for i in range(0,len(ary)):
        outfile.write("target entity: ")
        outfile.write(ary[i])
        outfile.write("\n")
        outfile.write("similar entities: ")
        if aryy[i][0] != '':
            for j in range(0,len(aryy[i])):
                if len(find_node_information(ary[i])) == 7 and len(find_node_information(aryy[i][j])) == 7:
                    sentence_embeddings0, sentence_embeddings1 = generate_embedding(find_node_information(ary[i])[3], find_node_information(aryy[i][j])[3], model)
                    if interspace.cosine_similarity(sentence_embeddings0, sentence_embeddings1) >= 0.9:
                        a.append(interspace.cosine_similarity(sentence_embeddings0, sentence_embeddings1))
                        outfile.write(aryy[i][j] + " ")
                elif len(find_node_information(ary[i])) == 5 and len(find_node_information(aryy[i][j])) == 5:
                    if find_node_information(ary[i])[1] == '0' and find_node_information(aryy[i][j])[1] == '0':
                        sentence_embeddings0, sentence_embeddings1 = generate_embedding(find_node_information(ary[i])[2], find_node_information(aryy[i][j])[2], model)
                        if interspace.cosine_similarity(sentence_embeddings0, sentence_embeddings1) >= 0.9:
                            a.append(interspace.cosine_similarity(sentence_embeddings0, sentence_embeddings1))
                            outfile.write(aryy[i][j] + " ")
                    elif find_node_information(ary[i])[1] == '2' and find_node_information(aryy[i][j])[1] == '2':
                        sentence_embeddings0, sentence_embeddings1 = generate_embedding(find_node_information(ary[i])[2], find_node_information(aryy[i][j])[2], model)
                        if interspace.cosine_similarity(sentence_embeddings0, sentence_embeddings1) >= 0.9:
                            a.append(interspace.cosine_similarity(sentence_embeddings0, sentence_embeddings1))
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
    real_match()
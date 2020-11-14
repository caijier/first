import sklearn as sk
import numpy      as np
import sys
file1 = open(r'.\brca\miRNA'
             r'\miRNA_HiSeq_gene.txt', 'r', encoding='ANSI')  # mirna数据集

file2 = open(r'.\brca\蛋白质表达RPPA'
             r'\RPPA.txt', 'r', encoding='ANSI')  # 蛋白质表达

file3 = open(r'.\brca\甲基化HumanMethylation450'
             r'\HumanMethylation450', 'r', encoding='ANSI')  # 甲基化

file4 = open(r'.\brca\基因表达RNA_seq'
             r'\HiSeqV2_log.txt', 'r', encoding='ANSI')  # 基因表达

file5 = open(r'.\brca\拷贝数变异数据cnv'
             r'\Gistic2_CopyNumber_Gistic2_all_thresholded_by_genes.txt', 'r', encoding='ANSI')  # 拷贝数变异阈值型

file6 = open(r'.\brca\体细胞突变somatic mutation'
             r'\mutation_wustl_hiseq_gene.txt', 'r', encoding='ANSI')  # 体细胞突变

file7 = open(r'.\brca\通路活性Pathway activity Pathway_Paradigm_RNASeq'
             r'\Pathway_Paradigm_RNASeq.txt', 'r', encoding='ANSI')  # 通路活性

file8 = open(r'.\brca\转录因子调控影响Transcription factor regulatory impact - HiSeqV2, by RABIT'
             r'\RABIT_BRCA.HiSeq _HiSeqV2.txt', 'r', encoding='ANSI')  # 转录因子

file9 = open(r'.\brca\临床变量clinical'
             r'\BRCA_clinicalMatrix_1.txt', 'r', encoding='UTF-8')  # 临床变量

file = [file1, file2, file3, file4, file5, file6, file7, file8, file9]
row_dict = {}  # 基因名到行索引的映射字典
column_dict = {}  # 条件名到列索引的映射字典
row_list = []  # 行索引到基因名的映射字典
column_list = []  # 列索引到基因名的映射列表
row_num = 0
column_num = 0

matrix = np.zeros((1360, 560000), dtype=np.float)
column_index = 0


# process file1 begin
tem_gene_list = []  # 文件内基因索引映射到全局列表
first_line = file1.readline().split()
for gene in first_line[1:]:
    if gene not in row_dict:
        row_dict[gene] = row_num
        row_list.append(gene)
        row_num += 1
    tem_gene_list.append(row_dict[gene])
lines = file1.readlines()
for line in lines:
    word = line.split()
    sum_column = 0  # 该条件的数据和
    num_valid = 0  # 有效数据个数
    maxd = sys.float_info.min
    mind = sys.float_info.max
    for item in word[1:]:
        if item != "NA":
            if maxd < float(item):
                maxd = float(item)
            if mind > float(item):
                mind = float(item)
            sum_column += float(item)
            num_valid += 1
    if num_valid/(len(word)-1) < 0.7:
        continue
    else:
        ave = (sum_column/num_valid-mind)/(maxd-mind)
    column_list.append(word[0])
    column_dict[word[0]] = column_num
    row_index = 0
    for item in word[1:]:
        if item != "NA":
            matrix[tem_gene_list[row_index]][column_index] = (float(item)-mind)/(maxd-mind)
        else:
            matrix[tem_gene_list[row_index]][column_index] = ave
        print("++", tem_gene_list[row_index], column_index, matrix[row_index][column_index])
        row_index += 1
    column_index += 1
# pocess file1 end

print("--->"),
print(matrix[0])




d = set()
for k in file[:7]:
    s = k.readline()
    for item in s.split():
        d.add(item)
    print(column_num)
    column_num += 1
    print(s)
    k.close()
lines = file8.readlines()
for line in lines:
    d.add(line.split()[0])
lines = file9.readlines()
for line in lines:
    d.add(line.split()[0])
print(d.__len__())




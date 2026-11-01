# %%
# SATURN 已经把 Acer 和 Amel 的细胞映射到同一个“共享空间”里。
#! 接下来， 对每个 Acer 细胞，去 Amel 里找 15 个最相似的细胞，然后让这 15 个 Amel 细胞“投票”决定这个 Acer 细胞是什么类型。
# %%
import scanpy as sc
import pandas as pd
from sklearn.neighbors import NearestNeighbors
import numpy as np
# %%
adata = sc.read_h5ad("runs/saturn_results/test256_data_Acer_saturn_input_Amel_saturn_input_org_saturn_seed_0.h5ad")
adata
# %%
adata.obs
# %%
(adata.obs["labels2"] != adata.obs["ref_labels"]).sum() # 0
# %%
ref = adata[adata.obs["species"] == "Amel"].copy()
qry = adata[adata.obs["species"] == "Acer"].copy()
# %%
nn = NearestNeighbors(n_neighbors=15, metric="cosine").fit(ref.X) 
    # ref.X 是 SATURN 的共享嵌入，不是原始基因表达
    # 每个 Acer 细胞在嵌入空间里找最近的 15 个 Amel 细胞；
    # metric="cosine" 表示用余弦距离衡量相似度；
dist, idx = nn.kneighbors(qry.X)
    # idx 是每个 Acer 细胞对应的 15 个 Amel 邻居的索引。形状：(58166, 15)
# %%
ref_labels = ref.obs["labels2"].astype(str).values # 形状：(115169,)，15 个 Amel 邻居对应的细胞类型标签
# %%
pred = []
conf = []
for i in idx: # 对这 15 个邻居的标签做多数投票
    vals, counts = np.unique(ref_labels[i], return_counts=True)
    pred.append(vals[counts.argmax()]) # pred 是预测标签
    conf.append(counts.max() / counts.sum()) # conf 是“15 个邻居中支持这个标签的比例”，例如 15 个里 12 个都是 KCs，则置信度是 12/15 = 0.8。
# %%
qry.obs["predicted_cell_type"] = pred
qry.obs["knn_confidence"] = conf
qry.write_h5ad("runs/Acer_annotated.h5ad")
# %%

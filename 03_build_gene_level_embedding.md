```bash
project_dir=/hdd2/liuzy/Projects/SATURN_anno
cd $project_dir/SATURN/protein_embeddings
conda activate saturn # see dir .env
```
# *Apis cerana*
```bash
python \
    convert_protein_embeddings_to_gene_embeddings.py \
    --embedding_dir $project_dir/protein_embeddings_raw/Acer \
    --gene_symbol_to_protein_ids_path $project_dir/gene_protein_map/Acer.gene_id_to_protein_ID.json \
    --embedding_model ESM1b \
    --save_path $project_dir/gene_embeddings/Acer.gene_id_to_embedding_ESM1b.pt
```

# *Apis mellifera*
```bash
python \
    convert_protein_embeddings_to_gene_embeddings.py \
    --embedding_dir $project_dir/protein_embeddings_raw/Amel \
    --gene_symbol_to_protein_ids_path $project_dir/gene_protein_map/Amel.gene_id_to_protein_ID.json \
    --embedding_model ESM1b \
    --save_path $project_dir/gene_embeddings/Amel.gene_id_to_embedding_ESM1b.pt
```

# Verification Coverage and Dimensions
```bash
cd $project_dir
```
```python
import torch
import anndata as ad

cases = [
    ("Acer", "matrix/01_Acer_transfromHY.h5ad",
     "gene_embeddings/Acer.gene_id_to_embedding_ESM1b.pt"),
    ("Amel", "matrix/Amel_wll.h5ad",
     "gene_embeddings/Amel.gene_id_to_embedding_ESM1b.pt"),
]

for name, h5, pt in cases:
    emb = torch.load(pt, map_location="cpu")
    a = ad.read_h5ad(h5, backed="r")
    have = sum(g in emb for g in a.var_names)
    dim = next(iter(emb.values())).shape
    print(name, "genes", a.n_vars, "with embedding", have, "dim", dim)
# Acer genes 11817 with embedding 9511 dim torch.Size([1280])
# Amel genes 12292 with embedding 9883 dim torch.Size([1280])
```
# Set the model cache directory
```bash
project_dir=/hdd2/liuzy/Projects/SATURN_anno
cd $project_dir
export TORCH_HOME=$project_dir/.torch
conda activate saturn # see dir .env
```
# *Apis cerana*

Trim the .faa header to prevent issues with saving .pt files caused by an excessively long header:
```bash
python \
  SATURN/protein_embeddings/clean_fasta.py \
  --data_path=./protein/Apis_cerana.faa \
  --save_path=./protein/Apis_cerana.clean.faa
```
Generate protein-level embeddings for *Apis cerana*:
```bash
CUDA_VISIBLE_DEVICES=0 \
PYTHONPATH=$project_dir/esm \
python \
  esm/scripts/extract.py \
  esm1b_t33_650M_UR50S \
  protein/Apis_cerana.clean.faa \
  protein_embeddings_raw/Acer \
  --include mean \
  --repr_layers 33 \
  --truncation_seq_length 1022 \
  --toks_per_batch 4096
```
Check single .pt file:
```python
import torch
x = torch.load("./protein_embeddings_raw/Acer/NP_001315405.1.pt")
print(x.keys()) # dict_keys(['label', 'mean_representations'])
print(x["mean_representations"][33].shape) # torch.Size([1280])
```
Check .pt numbers:
```bash
ls ./protein_embeddings_raw/Acer | wc -l # 29188
```

# *Apis mellifera*

```bash
python \
  SATURN/protein_embeddings/clean_fasta.py \
  --data_path=./protein/Apis_mellifera.faa \
  --save_path=./protein/Apis_mellifera.clean.faa
```

```bash
CUDA_VISIBLE_DEVICES=0 \
PYTHONPATH=/hdd2/liuzy/Projects/SATURN_anno/esm \
python \
  esm/scripts/extract.py \
  esm1b_t33_650M_UR50S \
  protein/Apis_mellifera.clean.faa \
  protein_embeddings_raw/Amel \
  --include mean \
  --repr_layers 33 \
  --truncation_seq_length 1022 \
  --toks_per_batch 4096
```
Check single .pt file:
```python
import torch
x = torch.load("./protein_embeddings_raw/Amel/NP_008082.pt")
print(x.keys()) # dict_keys(['label', 'mean_representations'])
print(x["mean_representations"][33].shape) # torch.Size([1280])
```
Check .pt numbers:
```bash
ls ./protein_embeddings_raw/Amel | wc -l # 23470
```
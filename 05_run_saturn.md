```bash
project_dir=/hdd2/liuzy/Projects/SATURN_anno
cd $project_dir
conda activate saturn
```
```bash
python \
    SATURN/train-saturn.py \
    --in_data=runs/Acer_Amel_run.csv \
    --in_label_col=saturn_label \
    --ref_label_col=saturn_label \
    --embedding_model=ESM1b \
    --hv_genes=8000 \
    --num_macrogenes=2000 \
    --model_dim=256 \
    --hidden_dim=256 \
    --pretrain \
    --pretrain_epochs=200 \
    --epochs=50 \
    --metric_lr=0.001 \
    --pretrain_lr=0.0005 \
    --centroids_init_path=runs/Acer_Amel_centroids.pkl \
    --pretrain_model_path=runs/Acer_Amel_pretrain.pt \
    --work_dir=./runs/ \
    --device_num=0 \
    --seed=0
```
↑ 注：
- --in_label_col=saturn_label：两个 h5ad 都有这一列；
- --ref_label_col=saturn_label：没有额外粗标签时，直接和 in_label_col 相同；
- --embedding_model=ESM1b：虽然 CSV 已经给了 embedding_path，写上保持一致；
- --centroids_init_path：第一次会计算并保存 KMeans 宏基因初始化，后续相同基因集可复用；
- --work_dir=./runs/：注意末尾斜杠，输出会在 runs/saturn_results/；
- --device_num=0：使用 0 号 GPU。
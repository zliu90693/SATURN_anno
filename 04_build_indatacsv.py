# %%
import pandas as pd
# %%
run_df = pd.DataFrame([
    {
        "species": "Acer",
        "path": "/hdd2/liuzy/Projects/SATURN_anno/matrix/Acer_saturn_input.h5ad",
        "embedding_path": "/hdd2/liuzy/Projects/SATURN_anno/gene_embeddings/Acer.gene_id_to_embedding_ESM1b.pt",
    },
    {
        "species": "Amel",
        "path": "/hdd2/liuzy/Projects/SATURN_anno/matrix/Amel_saturn_input.h5ad",
        "embedding_path": "/hdd2/liuzy/Projects/SATURN_anno/gene_embeddings/Amel.gene_id_to_embedding_ESM1b.pt",
    },
])
# %%
run_df.to_csv("runs/Acer_Amel_run.csv", index=False)
# %%

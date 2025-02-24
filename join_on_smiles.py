import sys, pandas as pd

f1="drug_SMILES.tsv"
f2='merged_on_target.chembl_to_smiles.tsv'

df1=pd.read_csv(f1, sep="\t")
df2=pd.read_csv(f2, sep="\t", header=None)
df_join=df1.merge(df2, how="inner", left_on="canSMILES", right_on=1)

df_join=df_join[['improve_chem_id',0,1,2,'canSMILES']]
df_join.columns = ['improve_chem_id','chembl_id','x_smile','has_smile','y_smile']
df_join=df_join.drop(columns=['x_smile','has_smile'])
df_join=df_join.rename(columns={'y_smile': 'SMILES'})

print(f'{df_join}')

df_join.to_csv('improve_chembl_join.tsv', sep="\t")

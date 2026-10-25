"""Smoke test determinista con datos artificiales. NO usa CSV de Interconnect reales.

Ejecutar desde repo: python tests/test_notebook05_sintetico.py
Requiere pandas, numpy, matplotlib, nbformat, nbclient, scikit-learn, ipykernel.
"""
import tempfile
from pathlib import Path
import numpy as np
import pandas as pd
import nbformat
from nbclient import NotebookClient

rng=np.random.default_rng(42)
N=7043
ids=[f'0000-{i:04d}' for i in range(N)]
churn=np.zeros(N,dtype=bool)
churn[rng.choice(N,1869,replace=False)]=True
contract=pd.DataFrame({
 'customerID': ids,
 'BeginDate':['2020-01-01']*N,
 'EndDate':np.where(churn,'2020-04-01','No'),
 'Type':rng.choice(['Month-to-month','One year','Two year'],size=N),
 'PaperlessBilling':rng.choice(['Yes','No'],size=N),
 'PaymentMethod':rng.choice(['Electronic check','Mailed check','Bank transfer (automatic)','Credit card (automatic)'],size=N),
 'MonthlyCharges':np.round(rng.uniform(20,105,size=N),2),
 'TotalCharges':[f'{v:.2f}' for v in rng.uniform(20,1000,size=N)],
})
contract.loc[np.arange(11),'TotalCharges']=' '
personal=pd.DataFrame({
 'customerID':ids,'gender':rng.choice(['Female','Male'],size=N),
 'SeniorCitizen':rng.choice([0,1],size=N),
 'Partner':rng.choice(['Yes','No'],size=N),
 'Dependents':rng.choice(['Yes','No'],size=N),
})
# Distribución disjunta que asegura cobertura total:
# 4.835 ambos, 682 solo internet, 1.526 solo teléfono.
ix_internet=np.arange(5517)
internet=pd.DataFrame({'customerID': [ids[i] for i in ix_internet],
                       'InternetService':rng.choice(['DSL','Fiber optic'],size=5517)})
for name in ['OnlineSecurity','OnlineBackup','DeviceProtection','TechSupport','StreamingTV','StreamingMovies']:
 internet[name]=rng.choice(['Yes','No'],size=5517)
ix_phone=np.arange(682,N)
phone=pd.DataFrame({'customerID':[ids[i] for i in ix_phone], 'MultipleLines':rng.choice(['Yes','No'],size=6361)})
with tempfile.TemporaryDirectory() as d:
 root=Path(d)
 (root/'data/raw').mkdir(parents=True)
 (root/'notebooks').mkdir()
 for name,df in [('contract',contract),('personal',personal),('internet',internet),('phone',phone)]:
  df.to_csv(root/f'data/raw/{name}.csv',index=False)
 nb=nbformat.read(str(Path(__file__).resolve().parents[1] / 'notebooks' / '05_integracion_clientes.ipynb'),as_version=4)
 client=NotebookClient(nb,timeout=130, kernel_name='python3',resources={'metadata':{'path':str(root/'notebooks')}})
 client.execute()
 saved=root/'data/processed/clientes_integrados.csv'
 saved_ml=root/'data/processed/clientes_modelado_base.csv'
 out=pd.read_csv(saved)
 out_ml=pd.read_csv(saved_ml)
 assert len(out)==7043 and out.customerID.is_unique
 assert out.Churn.sum()==1869
 assert out.TieneInternet.sum()==5517
 assert out.TieneTelefono.sum()==6361
 assert (out.loc[~out.TieneInternet,'OnlineSecurity']=='No internet service').all()
 assert (out.loc[~out.TieneTelefono,'MultipleLines']=='No phone service').all()
 assert out.loc[~out.TieneInternet,'InternetService'].eq('No').all()
 assert out.TotalCharges.isna().sum()==11
 assert 'EndDate' not in out_ml and 'TotalCharges' not in out_ml
 assert out_ml.Churn.sum()==1869
 encoded=pd.read_csv(root/'data/processed/clientes_codificados_eda.csv')
 dictionary=pd.read_csv(root/'data/processed/diccionario_features_05.csv')
 assert encoded.shape[0]==7043 and encoded.Churn.sum()==1869
 assert dictionary.shape[0] == encoded.shape[1]-1
 assert encoded.shape[1] == 29, f"esperadas 28 features + Churn: {encoded.shape[1]}"
 assert not encoded.drop(columns='Churn').select_dtypes(exclude='number').columns.tolist()
 assert 'Churn' not in dictionary.feature.tolist()
 assert encoded['InternetService_No'].sum()==1526
 assert (encoded.loc[encoded.TieneInternet==0,['OnlineSecurity','OnlineBackup','DeviceProtection','TechSupport','StreamingTV','StreamingMovies']]==0).all().all()
 charts=sum(len(cell.get('outputs',[])) for cell in nb.cells if cell.cell_type=='code')
 pngs=sum(1 for cell in nb.cells if cell.cell_type=='code' for output in cell.get('outputs',[]) if output.get('data',{}).get('image/png'))
 assert (out.TieneInternet | out.TieneTelefono).all()
 print('PASS: test sintético, encoded:',encoded.shape, 'filas:',len(out),'columnas:',out.shape[1],'modelado:',out_ml.shape, 'outputs:',charts,'charts:',pngs)

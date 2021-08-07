#!/usr/bin/env python
# coding: utf-8

# In[53]:


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats
from scipy.stats import norm
import seaborn as sns
import math


# In[54]:


path = "heart.csv"
arquivo = pd.read_csv(path)
arquivo


# In[55]:


arquivo.isnull().sum()


# In[56]:


arquivo.describe()


# In[57]:


#idades= arquivo['age'].unique()
#qtd_idades = arquivo['age'].value_counts()
#plt.bar(idades, qtd_idades)
plt.hist(arquivo['age'])
arquivo['age'].describe()


# In[58]:


sns.distplot(arquivo['age'], hist=True, norm_hist=True, rug=True)


# In[59]:


mulher= arquivo.query('sex ==0')
homem = arquivo.query('sex ==1')
sns.histplot(data=mulher['age'], kde="True")
plt.title("Feminino")


# In[60]:


plt.bar([1,2], arquivo['sex'].value_counts(), color=['b', 'r'])
plt.xticks([1,2], ['Masculino', 'Feminino'])
plt.xlabel('Sex')
arquivo['sex'].value_counts()


# In[61]:


plt.bar([0,1,2,3], arquivo['cp'].value_counts(), color=['r', 'g', 'b', 'orange'])
plt.xticks([0,1,2,3], ['Típico', 'Atípico', 'Não-angina', 'Assintomático'])
arquivo['cp'].value_counts()


# In[62]:


plt.bar([0,1], arquivo['target'].value_counts(), color=['green', 'yellow'])
plt.xticks([0,1], ['Doente', 'Não-doente'])
arquivo['target'].value_counts()


# In[63]:


sns.relplot(data=arquivo, x='thalach', y='oldpeak', hue='target', size='age', sizes = (10,500), alpha=0.5, aspect=3)


# # Teste 1
# H0 : A amostra da pressão arterial é proveniente de uma distribuição normal
# 
# Rejeitar H0 se o p <= 0.05

# In[64]:


sns.distplot(arquivo['trestbps'])


# In[65]:


stat1, pvalue1 =scipy.stats.normaltest(arquivo['trestbps'])
pvalue1<=0.05


# In[76]:


pvalue1


# Portanto, hipótese nula é rejeitada

# # Teste 2
# 
# H0: A amostra dos soro colesterol é proveniente de uma distribuição normal
# 
# Rejeitar H0 se o p<=0.05

# In[66]:


chol_400= arquivo.query('chol <400')
chol_400


# In[67]:


sns.distplot(chol_400['chol'])


# In[78]:


stat2, pvalue2 =scipy.stats.normaltest(chol_400['chol'])
pvalue2<=0.05


# In[77]:


pvalue2


# Portanto, a hipótese nula não é rejeitada

# In[82]:


from statsmodels.graphics.gofplots import qqplot 
qqplot(chol_400['chol'].values, line='s')


# ## Teste 3
# H0: a distribuição do soro colesterol é normal com u = 162.5 mg/dl
# 
# H1: a distribuição do soro colesterol é normal com u =! 162.5 mg/dl

# In[69]:


qt = scipy.stats.t(df=299).ppf(0.975) #alpha=5%
qt


# In[70]:


x = np.arange(-3, 3, 0.001)
y= norm.pdf(x,0,1)
plt.plot(x,y )
plt.fill_between(x[x>qt], y[x>qt], alpha=.5, color='blue')
plt.fill_between(x[x<-qt], y[x<-qt], alpha=.5, color='blue')


# In[71]:


X = chol_400['chol'].mean()
S =chol_400['chol'].std()
T = (X - 162.5)*(math.sqrt(303))/S #estatistica t de Student
T


# In[72]:


162.5 -(qt*S/(math.sqrt(303)))


# In[73]:


162.5 +(qt*S/(math.sqrt(303)))


# In[74]:


X


# In[75]:


T>qt


# Portanto, a hipotese nula é rejeitada.

# In[ ]:





# In[ ]:





# In[ ]:





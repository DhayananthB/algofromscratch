import matplotlib.pyplot as plt
from mylearn.cluster import KMeans
import pandas as pd

k = KMeans(n_clusters=4,max_iter= 1000)

df = pd.read_csv(r"testing\Clustering\student_clustering.csv")
X = df.iloc[:,:].values

print(X.shape)

# plt.scatter(X[:,0],X[:,1])
# plt.show()


y = k.fit_predict(X)

plt.scatter(X[y == 0,0],X[y == 0,1],color='red')
plt.scatter(X[y == 1,0],X[y == 1,1],color='blue')
plt.scatter(X[y == 2,0],X[y == 2,1],color='green')
plt.scatter(X[y == 3,0],X[y == 3,1],color='yellow')
plt.show()
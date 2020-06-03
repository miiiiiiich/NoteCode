from sklearn import datasets
from sklearn import svm
from sklearn.decomposition import PCA
import numpy as np
import matplotlib.pyplot as plt

# データを読み込む iris
iris = datasets.load_iris ()

# 主成分分析による4次元データの2次元への変換
pca = PCA(n_components =2)
data = pca.fit(iris.data).transform(iris.data)

# 分類結果を描画する際の各軸の細かさを決める処理
datamax = data.max ( axis =0) + 1
datamin = data.min ( axis =0) - 1
n =200
X , Y = np . meshgrid (np.linspace(datamin[0], datamax[0], n),
                       np.linspace(datamin[1], datamax[1], n))

# サポートベクターマシンでの分類
#svc = svm.LinearSVC()
svc = svm.SVC()
#svc = svm.SVC(kernel = 'sigmoid')
#svc = svm.SVC(C=2**15, gamma = 2**3)
#svc = svm.SVC(C=2**-5)
svc.fit(data, iris.target)
Z = svc.predict(np.c_[X.ravel(), Y.ravel()])

# 2次元平面への分類結果の描画処理
plt.contour(X, Y, Z.reshape(X.shape), colors ="k")
for c, kigou in zip ([0, 1, 2] , ["+", "x", "o"]):
    d = data [iris.target == c ]
    plt.scatter(d[:, 0], d[:, 1], c ="k", marker=kigou )
plt.show()


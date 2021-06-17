# encoding = utf - 8

import seaborn as sns
import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
print(sys.path)
iris_path = '/Users/luoyanchao/Downloads/Iris/iris.csv'

if __name__ == '__main__':
    iris = pd.read_csv(iris_path)
    # print(iris.head(3))
    # print(iris.Species.unique())
    print(iris.columns)
    # # 折线图 📈
    # plt.plot(iris['Sepal.Length'],np.sin(iris['Sepal.Length']))
    # plt.show()
    x = [0,1,2,3,4,5]
    y = [1,4,5,6,3,2]

    # # 散点图
    plt.scatter(x,y)
    # # 折线图
    plt.plot(x,y,)
    # # 柱状图
    # plt.bar(x,y)
    # # 盒图
    # plt.boxplot(x)
    # 子图
    # fig = plt.figure()
    # f1 = fig.add_subplot(2,2,1)
    # f2 = fig.add_subplot(2,1,1)
    # f1.plot(x,y)
    # f2.scatter(x,y)
    # sns.distplot(x)
    sns.relplot(x,y)
    # sns.scatterplot(x=Year,y=Profit,size='am',hue='am',palette='hot')
    sns.lineplot(x=iris['Sepal.Length'],y=iris['Sepal.Width'],hue=iris['Species'])
    # color_map = dict(zip(iris.Species.unique(),['blue','green','red']))
    # print(color_map)
    # for species,group in iris.groupby('Species'):
    #     plt.scatter(group['Petal.Length'],group['Sepal.Length'],
    #                 color=color_map[species],alpha=0.3,label=species
    #                 )
    # plt.legend(frameon=True,title='Species')
    # plt.xlabel('PetalLength')
    # plt.ylabel('SepalLength')

    tips = sns.load_dataset('tips')
    print(tips[:3])
    sns.catplot(x="Species", y="Petal.Length", data=iris)
    plt.show()


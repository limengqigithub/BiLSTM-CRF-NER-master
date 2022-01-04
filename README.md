# 中文命名实体识别


## 数据集

本项目尝试使用了Bi-LSTM+CRF模型来解决中文命名实体识别问题，数据集用的是论文ACL 2018[Chinese NER using Lattice LSTM](https://github.com/jiesutd/LatticeLSTM)中收集的简历数据，数据的格式如下，它的每一行由一个字及其对应的标注组成，标注集采用BIOES，句子之间用一个空行隔开。

```
美	B-LOC
国	E-LOC
的	O
华	B-PER
莱	I-PER
士	E-PER

我	O
跟	O
他	O
谈	O
笑	O
风	O
生	O 
```

该数据集就位于项目目录下的`ResumeNER`文件夹里。

## 运行结果

下面是BiLSTM+CRF预测结果的准确率：

|      | BiLSTM+CRF  |
| ---- | ---------- |
| 召回率| 95.72%  |
| 精确率| 95.74%  |
| F1分数| 95.70%  |

## 快速开始

首先安装依赖项：

```
pip3 install -r requirement.txt
```

安装完毕之后，直接使用

```
python3 main.py
```

即可训练以及评估模型，评估模型将会打印出模型的精确率、召回率、F1分数值以及混淆矩阵，如果想要修改相关模型参数或者是训练参数，可以在`./models/config.py`文件中进行设置。

训练完毕之后，如果想要加载并评估模型，运行如下命令：

```shell
python3 test.py
```

##  Bi-LSTM+CRF

LSTM的优点是能够通过双向的设置学习到观测序列（输入的字）之间的依赖，在训练过程中，LSTM能够根据目标（比如识别实体）自动提取观测序列的特征，但是缺点是无法学习到状态序列（输出的标注）之间的关系，要知道，在命名实体识别任务中，标注之间是有一定的关系的，比如B类标注（表示某实体的开头）后面不会再接一个B类标注，所以LSTM在解决NER这类序列标注任务时，虽然可以省去很繁杂的特征工程，但是也存在无法学习到标注上下文的缺点。

相反，CRF的优点就是能对隐含状态建模，学习状态序列的特点，但它的缺点是需要手动提取序列特征。所以一般的做法是，在LSTM后面再加一层CRF，以获得两者的优点。

具体的实现请查看`models/bilstm_crf.py`

## 代码中一些需要注意的点

* Bi-LSTM+CRF模型可以参考：[Neural Architectures for Named Entity Recognition](https://arxiv.org/pdf/1603.01360.pdf)，可以重点看一下里面的损失函数的定义。代码里面关于损失函数的计算采用的是类似动态规划的方法，不是很好理解，这里推荐看一下以下这些博客：

  * [CRF Layer on the Top of BiLSTM - 5](https://createmomo.github.io/2017/11/11/CRF-Layer-on-the-Top-of-BiLSTM-5/)
  * [Bi-LSTM-CRF for Sequence Labeling PENG](https://zhuanlan.zhihu.com/p/27338210) 
  * [Pytorch Bi-LSTM + CRF 代码详解](https://blog.csdn.net/cuihuijun1hao/article/details/79405740)
  
## TODO

* 尝试更加复杂的模型，参考论文[Chinese NER using Lattice LSTM](https://github.com/jiesutd/LatticeLSTM)
* 更详细的评估结果：打印混淆矩阵，同时输出每种类别的召回率、精确率、F1指标，便于分析。



















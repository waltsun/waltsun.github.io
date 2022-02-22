---
layout: post
title: "Impact of Base Dataset Design on Few-Shot Image Classification"
subtitle: few-shot图像分类分析类文章
tags: [paper reading, CV]
---

Othman Sbai, Facebook AI Research & LIGM (UMR 8049) - Ecole des Ponts, UPE;

Camille Couprie, Facebook AI Research;

and Mathieu Aubry, LIGM (UMR 8049) - Ecole des Ponts, UPE.


[arXiv首页](https://arxiv.org/abs/2007.08872)

[pdf](https://arxiv.org/pdf/2007.08872.pdf)

ECCV2020

Cited 10

分析类文章，分析few-shot场景下训练数据对结果的影响，例如
- 训练数据和测试数据的相似成都
- 固定标注数据的总预算，如何平衡每个类别的标注个数和标注的类别数
- 给定数据集，拆分或合并不同类别的影响
- 标注数据的类别应该偏简单还是偏多样

dataset
- miniImageNet
- ImageNet
- CUB-200
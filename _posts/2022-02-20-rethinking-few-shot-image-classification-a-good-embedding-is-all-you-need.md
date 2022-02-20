---
layout: post
title: "Rethinking Few-Shot Image Classification: A Good Embedding is All You Need?"
subtitle: 文章阅读系列
tags: [paper reading]
---

Yonglong Tian, MIT CSAIL;

Yue Wang, MIT CSAIL;

Dilip Krishnan, 1MIT CSAIL 2Google Research;

Joshua B. Tenenbaum, MIT CSAIL;

Phillip Isola, MIT CSAIL.


[arXiv首页](https://arxiv.org/abs/2003.11539)

[pdf](https://arxiv.org/pdf/2003.11539.pdf)

ECCV2020

- 用合理的task训练出好的representation learner，效果可以超过大多数复杂的few-shot算法
- self-distillation可以进一步提高效果

部分meta-learning的想法是在训练的过程中模拟inference的过程。
例如，metric-learning的标准方法，计算loss时不是通过接一个分类器，而是和inference一样采用NN的方式。

这篇文章的方法无论在训练阶段、推理阶段，都没有用到NN。
本文以ResNet12为backbone，在meta-training阶段用分类任务训练（使用分类器，而非NN），训练结束后进行K次自蒸馏，然后弃用分类器；
在meta-testing阶段，固定feature learner的参数，后接线性分类器学习参数。

datasets
- miniImageNet, tieredImageNet: from ImageNet
- CIFAR-FS, FC100: from CIFAR-100
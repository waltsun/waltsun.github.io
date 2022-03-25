---
layout: post
title: "Visual Representation Learning with Self-Supervised Attention for Low-Label High-data Regime"
subtitle: 自监督ViT做few-shot分类&zero-shot图像检索
tags: [paper reading, CV, ViT]
---

Prarthana Bhattacharyya, University of Waterloo, Amazon Inc;

Chenge Li;

Xiaonan Zhao;

István Fehérvári;

Jason Sun.

[arXiv首页](https://arxiv.org/abs/2201.08951)

[pdf](https://arxiv.org/pdf/2201.08951.pdf)

[code](https://github.com/AutoVision-cloud/SSL-ViT-lowlabel-highdata)

ICASSP-2022

SSL-ViT(Self-Supervised Vision transformer)，在miniImageNet上达到了86.5%（5way1shot）和96.22%（5way5shot）的准确率。

# methods

## DINO

[DINO](emerging-properties-in-self-supervised-vision-transformers)预训练

## few-shot图像分类

使用[distribution calibration](https://arxiv.org/abs/2101.06395)。

# experiment

对于miniImageNet，ViT先在ImageNet去除下游数据集类别的子集上训练100eepoch，而在miniImageNet上不做任何训练直接做distribution calibration，然后对novel classes上做校准后的feature训练logistic regression。
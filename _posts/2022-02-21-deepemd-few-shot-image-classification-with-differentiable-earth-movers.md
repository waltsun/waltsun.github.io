---
layout: post
title: "DeepEMD: Few-Shot Image Classification with Differentiable Earth Mover’s Distance and Structured Classifiers"
subtitle: few-shot图像分类
tags: [paper reading, CV]
---

Chi Zhang, Nanyang Technological University, Singapore;

Yujun Cai, Nanyang Technological University, Singapore;

Guosheng Lin, Nanyang Technological University, Singapore;

Chunhua Shen, The University of Adelaide, Australia.

[CVPR首页](https://openaccess.thecvf.com/content_CVPR_2020/html/Zhang_DeepEMD_Few-Shot_Image_Classification_With_Differentiable_Earth_Movers_Distance_and_CVPR_2020_paper.html)

[pdf](https://openaccess.thecvf.com/content_CVPR_2020/papers/Zhang_DeepEMD_Few-Shot_Image_Classification_With_Differentiable_Earth_Movers_Distance_and_CVPR_2020_paper.pdf)

CVPR 2020.

采用Earth Mover's Distance(EMD)来计算稠密图像表示间的距离和图像相关程度。

类内表示具有很大的变化性；
模型可能很难注意local features，而local feature能提供更有辨别性、可迁移的信息；
模型也应该能合理利用local discriminative representations、最小化无关区域对结果的影响。

提出最优匹配（optimal matching），用optimal matching cost来衡量两个结构化表示的相似度。
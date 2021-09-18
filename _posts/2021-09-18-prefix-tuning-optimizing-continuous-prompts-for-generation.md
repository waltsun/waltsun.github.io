---
layout: post
title: Prefix-Tuning: Optimizing Continuous Prompts for Generation
subtitle: 文章阅读系列
tags: [paper reading]
---

作者 Xiang Lisa Li, Stanford University; Percy Liang, Stanford University.

[arXiv首页](https://arxiv.org/abs/2101.00190)

[pdf](https://arxiv.org/pdf/2101.00190.pdf)

[代码](https://github.com/XiangLi1999/PrefixTuning)

（连续）Prompt的开山之作。

finetune作为一个有效将large pretrained language model运用在downstream tasks的方法，其中一个缺点在于对于每个downstream tasks都需要储存model的完整参数。
所以，文章针对生成类任务提出一个lightweight的替换方案prefix-tuning。
该方法固定大部分模型参数，只优化参数较少的*continuous task-specific* vector，该vector被称作prefix。

在GPT-2做table-to-text generation任务，在BART做summarization任务。
在只学习0.1%参数的情况下，full data setting下获得comparable performance；low-data setting下outperform finetune；extrapolates better to examples with topics unseen during training.

<img src="{{ 'assets/paper_img/prefix-1.png' | relative_url }}"/>
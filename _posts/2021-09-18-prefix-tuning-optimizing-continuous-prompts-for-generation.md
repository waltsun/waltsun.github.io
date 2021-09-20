---
layout: post
title: "Prefix-Tuning: Optimizing Continuous Prompts for Generation"
subtitle: 文章阅读系列
tags: [paper reading]
---

Xiang Lisa Li, Stanford University;

Percy Liang, Stanford University.

1st. Jan, 2021

[arXiv首页](https://arxiv.org/abs/2101.00190)

[pdf](https://arxiv.org/pdf/2101.00190.pdf)

[代码](https://github.com/XiangLi1999/PrefixTuning)

（连续）Prompt的重要paper。

# motivation和idea

finetune作为一个有效将large pretrained language model运用在downstream tasks的方法，其中一个缺点在于对于每个downstream tasks都需要储存model的完整参数。
通常的解决方法是lightweight finetuning，即固定大部分pretrained parameters而只训练较小的modules。

这种想法的核心在于，如何构造一种高效的结构、如何选取预训练模型中需要tuning的参数子集。
前人方法中，有考虑ablate away部分模型权重；训练side network与预训练模型加和；在layer之间插入task-specific layers(adapters)。
而([Subramani et al., 2020](https://arxiv.org/abs/1907.04944))发现通过优化一个sentence-wise continuous vector可以让pretrained LSTM language model重建任意的句子。

而GPT-3不需要task-specific tuning就可以部署在下游任务上。
GPT-3使用prompting的方法，只需预设一些natural language形式的task-specific instruction，就可以完成对应的任务。

这篇文章inspired by prompting，针对生成类任务（natural language generation(NLG) tasks）提出一个finetune的lightweight alternative，即prefix-tuning。

该方法固定大部分模型参数，构造 a sequence of continuous task-specific vectors 用作输入，将其称之为*prefix*。
这种prefix就像a sequence of "virtual tokens"，但是由free parameters构成。

# 实验结果

在GPT-2做table-to-text generation任务，在BART做summarization任务。
在只学习0.1%参数的情况下，full data setting下获得comparable performance；low-data setting下outperform finetune；extrapolates better to examples with topics unseen during training.

<img src="{{ 'assets/paper_img/prefix-1.png' | relative_url }}"/>
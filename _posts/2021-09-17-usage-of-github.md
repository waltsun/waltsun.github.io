---
layout: post
title: Github的使用
subtitle: 个人笔记系列
tags: [notes]
---

一些常用的git指令

```
git config --global user.name "Your Name"
git config --global user.email "email@example.com"
git init
git add YourFile.file
git commit -m "Your Explanation for This Commit"
git status
git diff  # 能看到现在文件与上次commit的区别
git log  # 提交日志
git log --pretty=oneline
git remote add origin git@github.com:waltsun/test.git  # 本地git绑定远程空repo
git push
git clone git@github.com:waltsun/test.git
git checkout -b dev origin/dev  # 将远程的dev分支抓取到本地，并在本地创建新分支dev
git log  # 显示该branch下的提交记录
git diff <commit-id-1> <commit-id-2>  # 比较两个commit之间的差别
```

更详细的在 [廖雪峰的网站](https://www.liaoxuefeng.com/wiki/896043488029600)

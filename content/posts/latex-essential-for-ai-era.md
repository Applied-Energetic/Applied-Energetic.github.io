---
title: Latex是AI时代下论文写作的必需品
description: 为什么CS学生必须选择TeX Live作为LaTeX发行版
date: 2026-03-08T15:00:00+08:00
image: /picture/geo-gradient.jpg
math: true
license: null
hidden: false
comments: true
draft: false
fmContentType: default
---

> 如何选择编译器

虽然 MiKTeX 在过去因为"按需安装包"和"体积小"而受到欢迎，但对于现在的 CS 学生和复杂的学校论文模板来说，**TeX Live 是压倒性的首选**。

---

## 1. 为什么不再推荐 MiKTeX？

### 稳定性坑点

MiKTeX 的"动态安装包"功能在处理复杂的中文宏包（如 ctex 及其依赖）时，经常会因为网络连接镜像源失败而导致编译中断。

### 权限问题

在 Windows 上，MiKTeX 经常会遇到宏包安装路径的权限冲突，导致明明装了包却找不到。

### 版本不一致

MiKTeX 的包更新策略有时会导致与学校模板（通常是基于特定时期的 TeX Live 开发的）产生兼容性偏离。

---

## 2. 为什么 TeX Live 是 CS 学生的标配？

### 完整性（一次到位）

TeX Live 采取"全量安装"策略（大约占用 7-8GB）。虽然大，但现在的硬盘空间不值钱。安装完后，你几乎再也不用担心缺包的问题，这对 AI 辅助写作非常重要——你不需要在 AI 生成代码后，还要去处理"找不到宏包"的报错。

### 跨平台一致性

它是 Linux、macOS (MacTeX) 和 Overleaf 的默认底层系统。如果你以后要把论文同步到服务器编译或与他人协作，TeX Live 能保证完全一致的结果。

### 学校模板的明确要求

你提供的教程明确写了 "Texlive 2021 以上"。这意味着学校模板的开发者是在 TeX Live 环境下测试的。使用相同的发行版可以避开 90% 的底层乱码和字体报错。

---

## 3. 在 AI 辅助环境下的最佳组合 (Workflow)

| 组件 | 推荐选择 |
|------|----------|
| **发行版** | TeX Live 2024 (ISO 下载安装) |
| **编辑器** | VS Code |
| **插件** | LaTeX Workshop |
| **AI 联动** | GitHub Copilot（对 LaTeX 的补全能力极强，尤其是重复性的表格和公式） |
| **编译引擎** | XeLaTeX |

在 VS Code 里，你可以左屏写 LaTeX，右屏开着 Claude/GPT-4 窗口，或者直接在代码区用 GitHub Copilot。

---

## 4. 如何安装 LaTeX

### 使用 iso 安装 Tex Live

下载地址：https://mirrors.tuna.tsinghua.edu.cn/CTAN/systems/texlive/Images/

使用镜像会让原本需要 5-6 个小时的时间缩短到**一个小时**。

### 关闭防护系统

Windows Defender 或 360/腾讯管家 会在你安装时，对这十几万个写进硬盘的小文件每一个都进行扫描，确保它不是病毒。

**后果：** 杀毒软件的开销往往占用了 70% 以上的安装时间。

**操作步骤：**

1. 进入 Windows 设置 → 隐私和安全性 → Windows 安全中心 → 病毒和威胁防护
2. 点击"管理设置"
3. 暂时关闭"实时防护"（**安装完再开**）

### 验证安装结果

在 CMD 中输入：

```bash
latex -version
```

如果安装成功，你会看到类似输出：

```
pdfTeX 3.141592653-2.6-1.40.29 (TeX Live 2026)
kpathsea version 6.4.2
Copyright 2026 Han The Thanh (pdfTeX) et al.
There is NO warranty.
Redistribution of this software is covered by the terms of both the pdfTeX copyright and the Lesser GNU General Public License.
```

---

## 总结

在 AI 时代，论文写作的痛点不再是"不会写"，而是"写了却编译不过"。选择 TeX Live + VS Code + GitHub Copilot 的组合，能让你专注于内容本身，而不是被各种宏包报错所困扰。

**一次安装，终身受益。**

---

*本文整理自实战安装经验*
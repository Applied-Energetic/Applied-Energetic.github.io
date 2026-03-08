---
title: OpenClaw 个人部署与应用心得分享
description: 基于 Sean 分享整理的 OpenClaw 部署指南与实际应用场景
date: 2026-03-08
draft: false
math: false
license: false
hidden: false
comments: true
fmContentType: default
image: /picture/openclaw-cover.jpg
tags: ["OpenClaw", "AI", "部署", "教程"]
categories: ["AI工具"]
---

> 本文根据 Sean 的分享整理，涵盖 OpenClaw 部署方案、成本控制、安全配置及实际应用场景。

## 📦 部署环境选择

| 平台 | 推荐度 | 说明 |
|------|--------|------|
| **Mac** | ⭐⭐⭐⭐⭐ | 原生 bash 支持好，功耗低，Macmini 性价比高 |
| **Linux** | ⭐⭐⭐⭐⭐ | 各大云服务器首选，兼容性好 |
| **Windows** | ⭐⭐ | 除了装机量大，一无是处，PowerShell 问题多 |
| **云端** | ⭐⭐⭐ | 阿里云/腾讯云，需注意配置（2C2G 可能不够） |

### 阿里云部署
- 79元/年入门套餐
- 文档齐全，可直接买服务器镜像
- 坑点：镜像不一定有，2C2G 可能内存不足

---

## 💰 成本与安全

### ⚠️ 安全隐患

1. **数据隐私**：OpenClaw 代码较为粗糙，大量 "vibe coding"，存在安全漏洞
2. **CVE-2026-25253**：已知安全漏洞，需及时打补丁
3. **Token 泄露**：金融操作注意 API 返回结果，曾有用户因重复投注亏损
4. **公网风险**：18789 端口建议关闭，或通过云服务商配置

### 模型成本对比

| 模型 | 价格 | 备注 |
|------|------|------|
| **GLM4.7** | 20元/1000万 Token | 注册送500万 Token |
| **MiniMax M2.5** | 订阅制 | 推荐作为主力模型 |
| **Qwen3 Max** | 按量 | 适合 subAgent |
| **Claude** | 中转 | 需注意地区限制 |

> GLM Lite 包无法使用 GLM5 模型，已引发大量退款。

---

## 🤖 模型配置建议

### 国内模型

- **MiniMax M2.5**：创始人推荐，第一梯队，初期速度快（后期算力不足）
- **GLM5**：难买，饥饿营销，运营风格沉稳
- **Qwen3 Max**：建议作为 subAgent，近期管理层有变动

### 国外模型

- **Claude**：需要中转站
- **Gemini**：有教育优惠
- **OpenAI**：推荐通过飞书渠道（近期放宽 API 用量）

### 通讯渠道配置

| 渠道 | 适用场景 |
|------|----------|
| 飞书 | 国内首选，近期放宽限制 |
| QQ | 有风控风险 |
| 钉钉 | 阿里系员工常用 |
| 微信企业版 | 适合企业用户 |
| Telegram | 功能强大，管理方便 |
| Discord | 群组管理优秀 |

---

## 🎯 实际应用场景

### 1. 博客自动化部署
一句话帮你上传和生成博客，支持 Hugo 等静态博客。

### 2. PPT 与网页演示
支持 HTML 版本演示，制作高效。

### 3. 社交媒体视频转录
- 底层模型：FunASR（中文语音转录）
- 支持平台：B站、小红书、YouTube
- 用途：做笔记、持久化记忆

### 4. 美股市场分析
- 实时抓取最新美股资讯
- 基金基础知识教学

### 5. 每日日报
自动总结当日任务并汇报。

---

## 📥 资料下载

本文相关视频资料：

- **百度网盘**：[肖恩-1.mp4](https://pan.baidu.com/s/1qMUNOtTeEmmP4q-nRTxC0g?pwd=mw2k)
- 提取码：`mw2k`

---

## 📚 延伸阅读

- [OpenClaw 官方文档](https://docs.openclaw.ai)
- [ClawHub Skill 市场](https://clawhub.com)
- [CVE-2026-25253 漏洞详情](https://blog.csdn.net/weixin_42376192/article/details/157684596)

---

*本文根据 Sean 的分享整理，感谢授权。*

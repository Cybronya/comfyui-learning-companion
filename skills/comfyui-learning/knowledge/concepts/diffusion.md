---
name: diffusion
title: 扩散模型原理（去噪、CFG、采样）
category: concepts
tags: [diffusion, denoise, cfg, scheduler, sampler, flow-matching]
updated: 2026-10-04
---

# 扩散模型原理（去噪、CFG、采样）

## 一句话
扩散模型 = 学会"从一团噪声里逐步去掉噪声"的模型。
训练时给图逐步加噪（前向过程），模型学会反向每一步的去噪；生成时从纯噪声出发
反复预测并去除噪声，最终"显影"出一张图（或一段视频）。

## 前向过程（训练视角）
对真实图 x₀ 在 T 步内按调度表逐步加高斯噪声，得到 x_t；
模型学习的就是"给定 x_t 和 t，预测混进来的噪声/速度场"。

## 反向过程（生成视角）
从纯噪声 x_T 开始，用模型预测噪声 → 去掉一点 → 重复 T 步 → 得到干净样本。
- **steps** 就是这里的 T：步数越多越精细，但线性变慢；20–30 是甜点区。
- **denoise** 决定走多远：图生图时起点不是纯噪声（是"加了噪的真实图"），
  denoise=0.6 表示只去 60% 的噪声，保留 40% 原图信息。

## CFG（Classifier-Free Guidance）
- 采样时同时算"无条件预测"与"有条件预测"（正/负提示词），
  输出 = 无条件 + cfg × (条件 − 无条件)，把结果"推向"提示词描述。
- cfg 越大越贴合提示词，但过高会过饱和、炸细节；7 左右是传统甜点。
- 蒸馏/流匹配模型（FLUX、LCM、LightX2V）通常 cfg=1（即不做外推），
  它们改用 guidance、步数控制或直接蒸馏掉 CFG。

## Sampler 与 Scheduler 的分工
- **scheduler（调度表）**：回答"每一步的噪声量是多少"（σ 路线），
  karras / beta / simple / exponential 等决定噪声下降曲线。
- **sampler（采样算法）**：回答"知道当前噪声量后，怎么走下一步"
  （一阶 euler、二阶 heun、DPM-Solver++ 系列、祖先采样 euler_a 等）。
  祖先采样带随机性，同 seed 不完全可复现。
- 高分辨率/视频常用 `shift` 参数把噪声曲线整体"后移"，保证大 latent 上噪声足够。

## Flow Matching（FLUX/Wan 等新架构）
新模型不再预测噪声，而是预测从噪声到数据的**速度场**（直线流），
去噪路径更直，所以少步数也能出图——这解释了 FLUX schnell 4 步、
蒸馏 LoRA 4–8 步能工作的原因。

## 在工作流里的对应
| 概念 | ComfyUI 落点 |
|---|---|
| steps / cfg / denoise | KSampler 参数 |
| scheduler 曲线 | KSampler 的 scheduler 或 Scheduler 节点 |
| guidance（流匹配引导） | FluxGuidance 等专属节点 |
| 去噪起点 | EmptyLatent（纯噪声）或 VAEEncode+加噪（图生图） |

## 常见坑
- 把 cfg 当质量旋钮一直加高 → 反效果。
- 图生图 denoise=1.0 还以为是"精修" → 实际完全重画。
- 少步蒸馏模型仍按 25 步采样 → 过冲、画面死灰。

## 关联卡片
- `nodes/sampler.md`（参数实操）
- `concepts/latent.md`（去噪发生在哪）
- `models/wan.md`、`models/flux.md`（流匹配模型实操差异）

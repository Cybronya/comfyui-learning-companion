---
name: sampler
title: 采样器节点（KSampler 家族）
category: nodes
tags: [ksampler, sampling, steps, cfg, denoise, scheduler]
updated: 2026-10-04
---

# 采样器节点（KSampler 家族）

## 作用
采样器是扩散模型的"执行核心"：接收 MODEL + 正/负 CONDITIONING + 初始 LATENT，
按步数迭代去噪，输出成品 LATENT。是几乎所有工作流的必经节点。

## 所属插件
**ComfyUI 内置**。本项目 custom_nodes 中的 MultiGPU 系节点提供"高仿版"
`KSamplerMultiGPU` 等（见 `comfyui/custom_nodes/NODES_SOURCES.md`），接口一致。

## 家族成员

| 节点 | 区别 |
|---|---|
| `KSampler` | 标准版 |
| `KSampler (Advanced)` | 多 add_noise / return_with_left_over_noise / start_at_step / end_at_step，支持分两段采样 |
| `SamplerCustom` / `SamplerCustomAdvanced` | 采样器与 scheduler 拆成独立节点（KSamplerSelect / Scheduler…），更灵活，视频模型常用 |

## 关键参数

| 参数 | 说明 |
|---|---|
| `seed` | 随机种子；control_after_generate 决定出图后行为（fixed 固定 / randomize 随机 / increment 递增） |
| `steps` | 总采样步数；去噪从 start_at_step 走到 end_at_step |
| `cfg` | 引导系数（对负条件的权重）；常规 6–8，视频/蒸馏模型常 1–6 |
| `sampler_name` | 采样算法，见下表 |
| `scheduler` | 噪声调度策略：`normal / karras / exponential / sgm_uniform / simple / ddim_uniform / beta / linear_quadratic` |
| `denoise` | 降噪强度：1.0 文生图；0.4–0.8 图生图；inpaint 常用 0.8–1.0 |

## 常用 sampler_name 一览

- 通用稳妥：`euler`、`euler_ancestral`(euler a)、`dpmpp_2m`、`dpmpp_2m_sde`
- SDXL 常配：`dpmpp_2m` + `karras`
- 一致性好、细节多：`dpmpp_3m_sde`（配 karras）
- 快速出图：`lcm`、`lms`、`res_multistep`
- FLUX 专用：`euler` + `simple`，cfg=1

## 使用要点
- 图生图必须 `denoise < 1`，否则等于重画。
- 视频模型（Wan / H3 类）常用低 cfg + 少步数 + `simple`/`beta` scheduler；
  配 LightX2V 等蒸馏 LoRA 时 4–8 步即可。
- `KSampler (Advanced)` 的 start/end_at_step 是"高分辨率二段采样"的基础：
  第一段 denoise 1.0 出构图，第二段低 denoise 精修。

## 常见坑
- cfg 过高（>10）容易过饱和、炸色；不是越大越稳。
- seed 递增模式下误以为是随机，导致构图雷同。
- scheduler 与 sampler 不匹配（如 lcm 配 karras）会异常。

## 关联卡片
- `concepts/diffusion.md`（steps/cfg/scheduler 原理）
- `models/wan.md`（视频采样参数惯例）
- `models/flux.md`（guidance 与 cfg=1 的关系）

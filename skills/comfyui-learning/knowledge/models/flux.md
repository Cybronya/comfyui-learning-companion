---
name: flux
title: FLUX.1 模型
category: models
tags: [flux, dev, schnell, guidance, t5, fp8]
updated: 2026-10-04
---

# FLUX.1 模型（Black Forest Labs）

## 作用
FLUX.1 是 BFL 的高质量文生图模型（DiT/Flow Matching 架构），文字渲染与光影真实感突出，
是当前 SD 之外的第二大主流。三个主要版本：

| 版本 | 许可 | 步数 | 说明 |
|---|---|---|---|
| FLUX.1 dev | 非商用 | 20–25 | 完整质量 |
| FLUX.1 schnell | Apache-2.0 | 4 | 快速版，cfg=1 |
| FLUX.1 Krea / Kontext 等衍生 | 各异 | — | Krea 偏真实感；Kontext 做图像编辑 |

## 组件与加载（ComfyUI 标准做法）
FLUX 没有单文件 checkpoint，通常四件套分离加载：

```
UNETLoader(unet/flux1-dev.safetensors, weight_dtype=fp8)  → MODEL
CLIPLoader(clip_l.safetensors, type=flux)      ┐
CLIPLoader(t5xxl_fp8_e4m3fn.safetensors)       ┴→ CLIP → CLIPTextEncode
VAELoader(ae.safetensors)                                 → VAE
EmptySD3LatentImage / 或普通 EmptyLatentImage             → LATENT
```

> t5xxl 极吃显存，用 fp8_e4m3fn 版本；`CLIPLoader` 的 type 必须选 `flux`。

## 关键参数
- **guidance**（`FluxGuidance` 节点）：FLUX 特有的引导强度，dev 常用 3.0–3.5；
  它独立于 KSampler 的 cfg（KSampler 里 cfg 固定 1.0）。
- 采样：`euler` + `simple`，dev 约 20 步、schnell 4 步。
- 分辨率：1024 系（1024×1024、1216×832 等），必须是 16 的倍数。

## 使用要点
- 显存紧张：UNET 用 fp8、T5 用 fp8 版、解码用 `VAEDecodeTiled`。
- prompt 是自然语言长句效果最好，不需要 tag 堆叠和权重语法。
- 项目内 MultiGPU 系加载器（NODES_SOURCES.md）可把 UNET/T5 指到不同卡。

## 常见坑
- cfg ≠ 1 直接出灰图/废图（FLUX 在低步数流匹配下不接受传统 CFG）。
- 忘接 FluxGuidance 时默认 guidance=3.5，想要别的值必须显式加节点。
- 用了 SDXL 的 latent 尺寸习惯（64 倍数）没问题，但低于 768 分辨率画面易崩。

## 关联卡片
- `nodes/sampler.md`（SamplerCustomAdvanced 用法）
- `models/sd.md`（与 SD 代际的加载对照）
- `concepts/latent.md`

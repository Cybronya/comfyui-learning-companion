---
name: sd
title: Stable Diffusion 系列模型
category: models
tags: [sd15, sdxl, sd3, checkpoint, lora]
updated: 2026-10-04
---

# Stable Diffusion 系列模型

## 作用
SD 系列是最主流的文生图扩散模型族。ComfyUI 里一个 checkpoint 通常 = UNET + CLIP + VAE 三合一。

## 家族与加载方式

| 代际 | 分辨率惯例 | 加载节点 | 备注 |
|---|---|---|---|
| SD 1.5 | 512×512（8 倍数） | `CheckpointLoaderSimple` | 生态最老最全，LoRA 极多 |
| SDXL | 1024×1024（64 倍数更佳） | `CheckpointLoaderSimple` | 专用 VAE sdxl_vae；1024 以下构图易崩 |
| SD 3.5 | 1024×1024 | `CheckpointLoaderSimple` 或 UNET+三编码器分离 | 大/中/小三种尺寸，许可证较严 |
| SDXL Turbo/Lightning | 1024 | 同上 | 蒸馏少步模型：1–8 步、cfg 1–2 |

## 组件拆分（refiner / 分离加载）
- 完整加载：`CheckpointLoaderSimple` → 输出 MODEL/CLIP/VAE。
- 分离加载：`UNETLoader` + `CLIPLoader`(+`CLIPTextEncode`) + `VAELoader`，
  适合 fp8/量化版本与 SD3 类多编码器模型。
- SDXL refiner：早期二段式工作流用 base 出构图、refiner 精修，现多被 LoRA/两段 KSampler 取代。

## 关键参数
- 提示词：SDXL 建议走 `CLIPTextEncodeSDXL`（base+refiner 双文本框）或直接两个 CLIPTextEncode。
- 分辨率：SD1.5 用 512 系（512×768 等），SDXL 用 1024 系（1024×1024、896×1152、1216×832）。
- 采样：SD1.5 常用 `dpmpp_2m + karras`、20–30 步、cfg 7；SDXL 相近但更吃步数。

## 使用要点
- LoRA 用 `LoraLoader` 插在 checkpoint 之后，`strength_model / strength_clip` 通常同值 0.6–1.0。
- embeddings ( textual inversion ) 用 embedding 文件名直接写进提示词。
- 显存不够：SDXL 优先 fp8/fp16 变体 + tiled decode。

## 常见坑
- 分辨率偏离训练区间 → 构图崩、重复人头。
- LoRA 叠加超过 3 个时权重互相污染，总强度建议控制在 ~1.5 以内。
- 老工作流把 SD1.5 VAE 用在 SDXL 上 → 灰图。

## 关联卡片
- `nodes/sampler.md`、`nodes/vae.md`
- `concepts/latent.md`（分辨率与 latent 尺寸）
- `models/flux.md`（同代际但架构不同的对照）

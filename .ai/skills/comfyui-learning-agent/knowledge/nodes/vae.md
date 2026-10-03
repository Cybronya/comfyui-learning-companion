---
name: vae
title: VAE 节点（编解码）
category: nodes
tags: [vae, decode, encode, tiled, latent]
updated: 2026-10-04
---

# VAE 节点（编解码）

## 作用
VAE 负责像素空间 ⇄ 潜空间的转换：
- **Encode**：像素图 → LATENT（图生图、inpaint 的入口）
- **Decode**：LATENT → 像素图（采样完成后的出口）

## 所属插件
**ComfyUI 内置**（custom_nodes 中有 MultiGPU 版加载器，见 NODES_SOURCES.md）。

## 家族成员

| 节点 | 作用 |
|---|---|
| `VAELoader` | 从 models/vae 加载独立 vae 文件（safetensors） |
| `VAEDecode` | LATENT → IMAGE |
| `VAEDecodeTiled` | 分块解码，显存友好；`tile_size` 越小越省显存、越慢 |
| `VAEEncode` | IMAGE → LATENT（`upscale_method / crop` 参数） |
| `VAEEncodeTiled` | 分块编码，同样用于省显存 |
| `VAEEncodeForInpaint` | inpaint 专用：额外吃 mask，对 mask 外区域做膨胀处理 |

## 关键参数
- `vae` 输入：来源两种——checkpoint 自带（CheckpointLoaderSimple 的 VAE 输出）
  或 `VAELoader` 独立加载（SDXL 系常用 sdxl_vae.safetensors；视频模型用专属 vae）。
- `tile_size`（Tiled 版）：512 起步；OOM 时降到 256 / 384。

## 使用要点
- 模型与 VAE **必须配套**：拿错代际的 VAE（SD1.5 配 SDXL）会出灰图/噪点。
- 视频模型（Wan 等）使用专属 VAE（如 `wan_2.1_vae.safetensors`），latent 带时间维，
  普通 VAE 不能互相替代。
- 出图 OOM 优先换 `VAEDecodeTiled`，其次降低分辨率。
- VAE 决定"最终画质层"：构图不对是采样器的事，糊/噪/色偏先怀疑 VAE。

## 常见坑
- 灰图或满屏噪点 ≈ 90% 是 VAE 不匹配或 fp16 数值问题（可试 VAE fp16 fix 版本）。
- 图生图链路里 LoadImage 后忘了接 VAEEncode，直接把 IMAGE 塞给 KSampler 会报类型错。
- Tiled 解码在块边界可能有轻微接缝，成品质检时注意看大色块区域。

## 关联卡片
- `concepts/latent.md`（潜空间与 8x 压缩）
- `models/wan.md`（视频 VAE 与时间维）

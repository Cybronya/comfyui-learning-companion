---
name: latent
title: 潜空间（Latent Space）
category: concepts
tags: [latent, vae, compression, empty-latent, video]
updated: 2026-10-04
---

# 潜空间（Latent Space）

## 作用
扩散模型不在像素上做去噪，而在高度压缩的**潜空间**张量上工作。
潜空间是模型真正的"工作台"：生成、放大、inpaint 全都发生在这一层。

## 压缩关系（SD 系）
- 空间上 **8×8 压缩**，通道从 3 压到 **4**（latent 形状 `[B,4,H/8,W/8]`）。
- 所以：`EmptyLatentImage` 里填 1024×1024，latent 实际是 128×128×4。
- **分辨率必须是 8 的倍数**；SDXL 建议 64 的倍数（位置编码训练区间）。
- 显存与算力按 latent 尺寸（即分辨率的平方/64）增长，这就是"放大很贵"的原因。

## 视频潜空间（本项目重点）
视频模型把时间维也编进 latent：
- Wan 系：`[B,16,(1+len)//4,H/8,W/8]`，**帧数会按 4 帧一组压缩**，
  这就是 Wan 帧数要求 4n+1 的原因（首帧单独 + 其余按组）。
- 对应空 latent 节点：`EmptyHunyuanLatentVideo`（尺寸兼容多模型）或 Wan 专属节点。
- 时间维压缩意味着：视频显存 ≈ 图像显存 × 帧组数，逐帧线性增长。

## 常见节点
| 节点 | 用途 |
|---|---|
| `EmptyLatentImage` | 标准文生图起点 |
| `EmptySD3LatentImage` | SD3/FLUX 系（通道 16） |
| `EmptyHunyuanLatentVideo` | 视频空 latent（带 length 参数） |
| `LatentUpscale` / `LatentUpscaleBy` | 潜空间放大（省显存的放大路线） |
| `SetLatentNoiseMask` | 给 latent 贴 mask（inpaint） |
| `LatentComposite` / `LatentBlend` | 两块 latent 拼接/融合 |

## 使用要点
- 放大路线二选一：latent 放大（快、省，细节一般）vs 像素放大模型再二次采样（慢、细节好）。
- 跨模型家族的 latent **不通用**（通道数与语义都不同），别拿 SD 的 latent 喂 FLUX。
- 想改构图优先改 latent 尺寸重新采样，而不是对成品图强行拉伸。

## 常见坑
- 尺寸不是 8 的倍数 → 直接报错。
- 图生图分辨率改变时忘了重编码，尺寸对不上报 shape 错误。
- 视频 length 填 80（不是 4n+1）→ 报错或时长异常。

## 关联卡片
- `nodes/vae.md`（编解码实现）
- `models/wan.md`（视频 latent 约定）
- `concepts/diffusion.md`

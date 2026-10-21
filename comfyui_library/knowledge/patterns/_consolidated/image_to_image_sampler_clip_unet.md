---
name: image_to_image_sampler_clip_unet
type: Image To Image
frequency: 6
level: moderate
coverage: 0.907667
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyHunyuanLatentVideo, KSampler, LatentCutToBatch, LoadImage, ModelSamplingAuraFlow, ReferenceLatent, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Qwen Image Layered 分层模型_2003650272847118337.json, 图片生成/文生图/Qwen Image Layered千问分层文生_图生一体流_2002200397173387266.json, 图片生成/文生图/Qwen Image Layered千问分层模型_2002135922642698242.json, 图片生成/文生图/Qwen Image Layered千问分层模型_2002219692104249346.json, 图片生成/文生图/Qwen Image Layered千问分层模型_2002653665032847361.json, 图片生成/文生图/Qwen-Image-layered图像分层_2002178825435922433.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_unet

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/文生图/Qwen Image Layered 分层模型_2003650272847118337.json、图片生成/文生图/Qwen Image Layered千问分层文生_图生一体流_2002200397173387266.json、图片生成/文生图/Qwen Image Layered千问分层模型_2002135922642698242.json、图片生成/文生图/Qwen Image Layered千问分层模型_2002219692104249346.json、图片生成/文生图/Qwen Image Layered千问分层模型_2002653665032847361.json…）

- **类型**：Image To Image
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：91%

## 共有节点

全部 6 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyHunyuanLatentVideo`
- `KSampler`
- `LatentCutToBatch`
- `LoadImage`
- `ModelSamplingAuraFlow`
- `ReferenceLatent`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `GetImageSize` —— 5/6 个有
- `LatentFromBatch` —— 5/6 个有
- `Fast Groups Bypasser (rgthree)` —— 4/6 个有
- `ImageScaleToTotalPixels` —— 3/6 个有
- `Any Switch (rgthree)` —— 1/6 个有
- `ImageScaleBy` —— 1/6 个有
- `ImpactInt` —— 1/6 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/6 个有
- `LoraLoaderModelOnly` —— 1/6 个有
- `Text Multiline` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 40 | 8 - 40 | 6 | 64% |
| Prompt 约束强度(CFG) | 4 | 1 - 4 | 6 | 67% |
| 采样算法 | euler | - | 6 | 100% |
| 调度器 | simple | - | 6 | 83% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 40，观测区间 8 - 40，6 个样本
- Prompt 约束强度(CFG) 中位数 4，观测区间 1 - 4，6 个样本
- 采样算法 最常用 euler，6 个样本，一致性 100%
- 调度器 最常用 simple，6 个样本，一致性 83%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）

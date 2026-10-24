---
name: text_to_image_sampler_clip_unet_173
type: Text To Image
frequency: 3
level: strong
coverage: 0.822
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyLatentImage, Image Comparer (rgthree), ImageScaleToTotalPixels, KSampler, LoadImage, PreviewImage, Qwen3_VQA, SaveImage, SeedVR2, UNETLoader, VAEDecode, VAELoader, easy cleanGpuUsed, easy showAnything]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/老高Z-image + seedvr2 + 背景反推_2014303163351830530.json, 图片生成/文生图/Z-image + seedvr2 + 图片反推_1990637223408263169.json, 图片生成/文生图/Z-image 图像反推+去AI感_1994602887898669057.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_173

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/老高Z-image + seedvr2 + 背景反推_2014303163351830530.json、图片生成/文生图/Z-image + seedvr2 + 图片反推_1990637223408263169.json、图片生成/文生图/Z-image 图像反推+去AI感_1994602887898669057.json）

- **类型**：Text To Image
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：82%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `Image Comparer (rgthree)`
- `ImageScaleToTotalPixels`
- `KSampler`
- `LoadImage`
- `PreviewImage`
- `Qwen3_VQA`
- `SaveImage`
- `SeedVR2`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy cleanGpuUsed`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `AddTextPrefix` —— 1/3 个有
- `Fast Groups Muter (rgthree)` —— 1/3 个有
- `Label (rgthree)` —— 1/3 个有
- `TT_img_enc` —— 1/3 个有
- `TextBox` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 9 | 9 - 9 | 3 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | simple | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |
| 宽度 | 1080 | 1080 - 1920 | 3 | 71% |
| 高度 | 1920 | 1080 - 1920 | 3 | 76% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 9，观测区间 9 - 9，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 simple，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 宽度 中位数 1080，观测区间 1080 - 1920，3 个样本
- 高度 中位数 1920，观测区间 1080 - 1920，3 个样本
- 高发问题（3/3 个样本）：Steps较低可能导致细节不足

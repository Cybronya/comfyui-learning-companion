---
name: text_to_image_sampler_clip_unet_196
type: Text To Image
frequency: 3
level: moderate
coverage: 0.828333
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyLatentImage, KSampler, LoadImage, MaraScottIsEmptyOrNone_v1, RH_Captioner, SaveImage, Text Multiline, UNETLoader, VAEDecode, VAELoader, easy ifElse, easy int]
problems: []
missing: []
members: [图片生成/文生图/Z-image+Lora文生图洗图自动化_1995374884840779777.json, 图片生成/文生图/Z-image+Lora文生图洗图自动化_2035925518368907265.json, 图片生成/文生图/Z-image-base文生图洗图自动化_2016501851377639425.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_196

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/Z-image+Lora文生图洗图自动化_1995374884840779777.json、图片生成/文生图/Z-image+Lora文生图洗图自动化_2035925518368907265.json、图片生成/文生图/Z-image-base文生图洗图自动化_2016501851377639425.json）

- **类型**：Text To Image
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：83%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `KSampler`
- `LoadImage`
- `MaraScottIsEmptyOrNone_v1`
- `RH_Captioner`
- `SaveImage`
- `Text Multiline`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy ifElse`
- `easy int`

**可变部分**（部分 workflow 才有）：
- `ImageConcanate` —— 2/3 个有
- `LoraLoaderModelOnly` —— 2/3 个有
- `easy showAnything` —— 2/3 个有
- `ttN concat` —— 2/3 个有
- `JJC_JoyCaption_Custom` —— 1/3 个有
- `LayerUtility: ImageReel` —— 1/3 个有
- `LayerUtility: ImageReelComposit` —— 1/3 个有
- `LayerUtility: PurgeVRAM` —— 1/3 个有
- `ModelSamplingAuraFlow` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 1024 - 1024 | 3 | 100% |
| 高度 | 1536 | 1536 - 1536 | 3 | 100% |
| 采样步数 | 10 | 10 - 30 | 3 | 43% |
| Prompt 约束强度(CFG) | 1 | 1 - 2.5 | 3 | 53% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | simple | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1024，观测区间 1024 - 1024，3 个样本，取值集中（一致性 100%）
- 高度 中位数 1536，观测区间 1536 - 1536，3 个样本，取值集中（一致性 100%）
- 采样步数 中位数 10，观测区间 10 - 30，3 个样本，取值分散，一致性仅 43%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 2.5，3 个样本
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 simple，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）

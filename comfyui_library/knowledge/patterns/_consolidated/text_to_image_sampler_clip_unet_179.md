---
name: text_to_image_sampler_clip_unet_179
type: Text To Image
frequency: 3
level: moderate
coverage: 0.731
common_nodes: [CLIPTextEncode, ConditioningZeroOut, EmptyLatentImage, JanusImageUnderstanding, JanusModelLoader, KSampler, LayerUtility: PurgeVRAM, LoadImage, PreviewImage, SaveImage, ShowText|pysssss, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Flux-文生图-图生图-加速版_2009553183344959489.json, 图片生成/文生图/Qwen-Image-Edit-文生图-图生图-加速版_2007390911692541953.json, 图片生成/文生图/Qwen-image洗图模仿海报_风格等_1955802388865191937.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_179

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/Flux-文生图-图生图-加速版_2009553183344959489.json、图片生成/文生图/Qwen-Image-Edit-文生图-图生图-加速版_2007390911692541953.json、图片生成/文生图/Qwen-image洗图模仿海报_风格等_1955802388865191937.json）

- **类型**：Text To Image
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：73%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `JanusImageUnderstanding`
- `JanusModelLoader`
- `KSampler`
- `LayerUtility: PurgeVRAM`
- `LoadImage`
- `PreviewImage`
- `SaveImage`
- `ShowText|pysssss`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CLIPLoader` —— 2/3 个有
- `CR Text` —— 2/3 个有
- `ConstrainImage|pysssss` —— 2/3 个有
- `Fast Groups Bypasser (rgthree)` —— 2/3 个有
- `Image Compare (mtb)` —— 2/3 个有
- `LoraLoaderModelOnly` —— 2/3 个有
- `ModelSamplingAuraFlow` —— 2/3 个有
- `VAEEncode` —— 2/3 个有
- `DualCLIPLoader` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 20 - 35 | 3 | 72% |
| Prompt 约束强度(CFG) | 2.5 | 2.5 - 4 | 3 | 76% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | normal | - | 3 | 67% |
| 重绘幅度 | 0.6 | 0.6 - 1 | 3 | 74% |
| 宽度 | 1104 | 768 - 1104 | 3 | 84% |
| 高度 | 1472 | 1024 - 1472 | 3 | 84% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 20，观测区间 20 - 35，3 个样本
- Prompt 约束强度(CFG) 中位数 2.5，观测区间 2.5 - 4，3 个样本
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 normal，3 个样本，一致性 67%
- 重绘幅度 中位数 0.6，观测区间 0.6 - 1，3 个样本
- 宽度 中位数 1104，观测区间 768 - 1104，3 个样本，取值集中（一致性 84%）
- 高度 中位数 1472，观测区间 1024 - 1472，3 个样本，取值集中（一致性 84%）

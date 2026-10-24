---
name: text_to_image_lora_sampler_clip_404
type: Text To Image
frequency: 4
level: moderate
coverage: 0.7975
common_nodes: [CLIPLoader, CLIPTextEncode, ComfySwitchNode, ConditioningZeroOut, DepthAnythingV2Preprocessor, EmptyLatentImage, Fast Groups Bypasser (rgthree), GetImageSize, KSampler, Krea2ControlApply, Krea2ControlImageEncode, Krea2ControlLoRALoader, LoadImage, PreviewImage, PrimitiveBoolean, PrimitiveStringMultiline, ResolutionSelector, SaveImage, TextGenerate, UNETLoader, VAEDecode, VAELoader, easy showAnything]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Krea2 全自动-深度图控制-反推洗图_2076972404290707458.json, 图片生成/图生图/Krea2 深度图反推洗图-高清4K_2089887292306579458.json, 图片生成/文生图/Krea2 深度图控制-全自动反推洗图-高清4K_2076852160796643329.json, 图片生成/文生图/Krea2 深度控制自动反推洗图 Depth ControlNet_2075102694674616322.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_404

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/Krea2 全自动-深度图控制-反推洗图_2076972404290707458.json、图片生成/图生图/Krea2 深度图反推洗图-高清4K_2089887292306579458.json、图片生成/文生图/Krea2 深度图控制-全自动反推洗图-高清4K_2076852160796643329.json、图片生成/文生图/Krea2 深度控制自动反推洗图 Depth ControlNet_2075102694674616322.json）

- **类型**：Text To Image
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：80%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfySwitchNode`
- `ConditioningZeroOut`
- `DepthAnythingV2Preprocessor`
- `EmptyLatentImage`
- `Fast Groups Bypasser (rgthree)`
- `GetImageSize`
- `KSampler`
- `Krea2ControlApply`
- `Krea2ControlImageEncode`
- `Krea2ControlLoRALoader`
- `LoadImage`
- `PreviewImage`
- `PrimitiveBoolean`
- `PrimitiveStringMultiline`
- `ResolutionSelector`
- `SaveImage`
- `TextGenerate`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `Image Comparer (rgthree)` —— 3/4 个有
- `JWImageResizeByLongerSide` —— 3/4 个有
- `LatentUpscaleBy` —— 3/4 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 3/4 个有
- `LoraLoaderModelOnly` —— 3/4 个有
- `SeedVR2` —— 3/4 个有
- `SeedVR2BlockSwap` —— 3/4 个有
- `VAEEncode` —— 3/4 个有
- `ModelSamplingAuraFlow` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 512 - 1024 | 4 | 75% |
| 高度 | 1024 | 512 - 1024 | 4 | 75% |
| 采样步数 | 7 | 6 - 8 | 4 | 86% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 4 | 100% |
| 采样算法 | er_sde | - | 4 | 50% |
| 调度器 | simple | - | 4 | 100% |
| 重绘幅度 | 0.7 | 0.4 - 1 | 4 | 57% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 7/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 1024，观测区间 512 - 1024，4 个样本
- 高度 中位数 1024，观测区间 512 - 1024，4 个样本
- 采样步数 中位数 7，观测区间 6 - 8，4 个样本，取值集中（一致性 86%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，4 个样本，一致性 50%
- 调度器 最常用 simple，4 个样本，一致性 100%
- 重绘幅度 中位数 0.7，观测区间 0.4 - 1，4 个样本
- 高发问题（7/4 个样本）：Steps较低可能导致细节不足

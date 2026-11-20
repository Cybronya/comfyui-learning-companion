---
name: image_to_image_sampler_unet_vae_49
type: Image To Image
frequency: 3
level: moderate
coverage: 0.825
common_nodes: [CLIPLoader, KSampler, LoadImage, PreviewImage, SaveImage, SeedVR2, SeedVR2BlockSwap, SeedVR2ExtraArgs, TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/【换头】+【高清】_2013846676464738305.json, 图片生成/图生图/千问放大加lora_2106297371012460546.json, 图片生成/图生图/场景多视角高清工作流_（我要当玛奇玛的？）_2010999442521985026.json]
source: knowledge_consolidation
---

# image_to_image_sampler_unet_vae_49

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/【换头】+【高清】_2013846676464738305.json、图片生成/图生图/千问放大加lora_2106297371012460546.json、图片生成/图生图/场景多视角高清工作流_（我要当玛奇玛的？）_2010999442521985026.json）

- **类型**：Image To Image
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：82%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `KSampler`
- `LoadImage`
- `PreviewImage`
- `SaveImage`
- `SeedVR2`
- `SeedVR2BlockSwap`
- `SeedVR2ExtraArgs`
- `TextEncodeQwenImageEditPlus`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CFGNorm` —— 2/3 个有
- `ConditioningZeroOut` —— 2/3 个有
- `FluxKontextImageScale` —— 2/3 个有
- `FluxKontextMultiReferenceLatentMethod` —— 2/3 个有
- `Image Comparer (rgthree)` —— 2/3 个有
- `LoraLoaderModelOnly` —— 2/3 个有
- `ModelSamplingAuraFlow` —— 2/3 个有
- `easy cleanGpuUsed` —— 2/3 个有
- `ImageScaleBy` —— 1/3 个有
- `ImageScaleToTotalPixels` —— 1/3 个有
- `ImageSharpen` —— 1/3 个有
- `QwenMultiangleCameraNode` —— 1/3 个有
- `RHHiddenNodes` —— 1/3 个有
- `ShowText|pysssss` —— 1/3 个有
- `TextEncodeQwenImageEditPlusAdvance_lrzjason` —— 1/3 个有
- `easy promptLine` —— 1/3 个有
- `easy promptList` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 8 | 3 | 65% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 67% |
| 调度器 | simple | - | 3 | 67% |
| 重绘幅度 | 1 | 0.3 - 1 | 3 | 57% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 8，3 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 67%
- 调度器 最常用 simple，3 个样本，一致性 67%
- 重绘幅度 中位数 1，观测区间 0.3 - 1，3 个样本
- 高发问题（4/3 个样本）：Steps较低可能导致细节不足

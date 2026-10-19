---
name: image_to_image_upscale_sampler_clip_2
type: Image To Image
frequency: 3
level: moderate
coverage: 0.641333
common_nodes: [CLIPLoader, CLIPTextEncode, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: [LayerUtility: ImageScaleByAspectRatio V2, CR Text, LayerUtility: ImageReel, LayerUtility: ImageReelComposit]
members: [图片生成/图生图/2007465177616228353.json, 图片生成/图生图/2102306162334068737.json, 图片生成/图生图/2102430336633364482.json]
source: knowledge_consolidation
---

# image_to_image_upscale_sampler_clip_2

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/2007465177616228353.json、图片生成/图生图/2102306162334068737.json、图片生成/图生图/2102430336633364482.json）

- **类型**：Image To Image
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：64%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `AILab_QwenVL` —— 2/3 个有
- `CR Text` —— 2/3 个有
- `ConditioningZeroOut` —— 2/3 个有
- `Image Comparer (rgthree)` —— 2/3 个有
- `ImageScaleBy` —— 2/3 个有
- `ImpactInt` —— 2/3 个有
- `ShowText|pysssss` —— 2/3 个有
- `easy showAnything` —— 2/3 个有
- `JoinStrings` —— 1/3 个有
- `LayerUtility: ImageReel` —— 1/3 个有
- `LayerUtility: ImageReelComposit` —— 1/3 个有
- `LoraLoaderModelOnly` —— 1/3 个有
- `Qwen3_VQA` —— 1/3 个有
- `RHUploadZip` —— 1/3 个有
- `SetNode` —— 1/3 个有
- `TextInput_` —— 1/3 个有
- `孤海注释` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 10 | 10 - 12 | 3 | 91% |
| Prompt 约束强度(CFG) | 1 | 1 - 2 | 3 | 65% |
| 采样算法 | euler | - | 3 | 67% |
| 调度器 | simple | - | 3 | 67% |
| 重绘幅度 | 0.7 | 0.15 - 1 | 3 | 43% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 10，观测区间 10 - 12，3 个样本，取值集中（一致性 91%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 2，3 个样本
- 采样算法 最常用 euler，3 个样本，一致性 67%
- 调度器 最常用 simple，3 个样本，一致性 67%
- 重绘幅度 中位数 0.7，观测区间 0.15 - 1，3 个样本，取值分散，一致性仅 43%
- 这些节点还没有知识卡，系统对它们的理解有限：LayerUtility: ImageScaleByAspectRatio V2、CR Text、LayerUtility: ImageReel、LayerUtility: ImageReelComposit

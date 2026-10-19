---
name: image_to_image_upscale_sampler_clip
type: Image To Image
frequency: 5
level: moderate
coverage: 0.622
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, Fast Groups Bypasser (rgthree), Image Comparer (rgthree), ImageScaleBy, ImpactInt, JoinStrings, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: PurgeVRAM, LoadImage, Qwen3_VQA, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, ShowText|pysssss, TextInput_, UNETLoader, VAEDecode, VAEEncode, VAELoader, easy showAnything]
problems: []
missing: [LayerUtility: ImageReel, LayerUtility: ImageReelComposit, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: PurgeVRAM, easy convertAnything, easy imageConcat, easy indexAnything]
members: [图片生成/反推提示词/qwen3反推Krea2洗图重绘去除Ai感+SeedVR放大_2077040370852130818.json, 图片生成/图生图/1995894229622800386.json, 图片生成/图生图/2077040370852130818.json, 图片生成/图生图/2105957638642167810.json, 视频生成/图生视频/2070330640096120833.json]
source: knowledge_consolidation
---

# image_to_image_upscale_sampler_clip

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/反推提示词/qwen3反推Krea2洗图重绘去除Ai感+SeedVR放大_2077040370852130818.json、图片生成/图生图/1995894229622800386.json、图片生成/图生图/2077040370852130818.json、图片生成/图生图/2105957638642167810.json、视频生成/图生视频/2070330640096120833.json）

- **类型**：Image To Image
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：62%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `Fast Groups Bypasser (rgthree)`
- `Image Comparer (rgthree)`
- `ImageScaleBy`
- `ImpactInt`
- `JoinStrings`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: PurgeVRAM`
- `LoadImage`
- `Qwen3_VQA`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `ShowText|pysssss`
- `TextInput_`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `LayerUtility: ImageReel` —— 4/5 个有
- `LayerUtility: ImageReelComposit` —— 4/5 个有
- `PreviewImage` —— 4/5 个有
- `easy imageConcat` —— 4/5 个有
- `LoraLoaderModelOnly` —— 1/5 个有
- `RH_RhartVideoSparkvideo20MultimodalVideo` —— 1/5 个有
- `SaveVideo` —— 1/5 个有
- `SomethingToString` —— 1/5 个有
- `easy convertAnything` —— 1/5 个有
- `easy indexAnything` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 10 | 10 - 40 | 5 | 25% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 5 | 100% |
| 采样算法 | euler | - | 5 | 60% |
| 调度器 | simple | - | 5 | 100% |
| 重绘幅度 | 0.7 | 0.7 - 0.7 | 5 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 10，观测区间 10 - 40，5 个样本，取值分散，一致性仅 25%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，5 个样本，一致性 60%
- 调度器 最常用 simple，5 个样本，一致性 100%
- 重绘幅度 中位数 0.7，观测区间 0.7 - 0.7，5 个样本，取值集中（一致性 100%）
- 这些节点还没有知识卡，系统对它们的理解有限：LayerUtility: ImageReel、LayerUtility: ImageReelComposit、LayerUtility: ImageScaleByAspectRatio V2、LayerUtility: PurgeVRAM、easy convertAnything

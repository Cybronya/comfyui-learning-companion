---
name: text_to_image_sampler_clip_unet_121
type: Text To Image
frequency: 3
level: weak
coverage: 0.931333
common_nodes: [BasicScheduler, CLIPLoader, CLIPTextEncode, ComfyMathExpression, EmptyLatentImage, GetImageSize, ImageMergeTileList, KSampler, KSamplerSelect, PrimitiveInt, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SaveImage, SeedVR2Conditioning, SeedVR2PostProcessing, SeedVR2Preprocess, SplitImageToTileList, SplitSigmas, UNETLoader, VAEDecode, VAEDecodeTiled, VAEEncodeTiled, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/KREA2 SEEDVR2 100MP_2101605682029092865.json, 图片生成/文生图/KREA2 SEEDVR2 100MP工作流｜4MP二采加5x5分块放大｜原生节点_2101915958075023361.json, 图片生成/文生图/Qwen Image 2.1+SeedVR2+DLSS5级联 人像写真写实高清放大_2104292002979471361.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_121

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/KREA2 SEEDVR2 100MP_2101605682029092865.json、图片生成/文生图/KREA2 SEEDVR2 100MP工作流｜4MP二采加5x5分块放大｜原生节点_2101915958075023361.json、图片生成/文生图/Qwen Image 2.1+SeedVR2+DLSS5级联 人像写真写实高清放大_2104292002979471361.json）

- **类型**：Text To Image
- **样本数**：3
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：93%

## 共有节点

全部 3 个 workflow 都包含：
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfyMathExpression`
- `EmptyLatentImage`
- `GetImageSize`
- `ImageMergeTileList`
- `KSampler`
- `KSamplerSelect`
- `PrimitiveInt`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `SaveImage`
- `SeedVR2Conditioning`
- `SeedVR2PostProcessing`
- `SeedVR2Preprocess`
- `SplitImageToTileList`
- `SplitSigmas`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeTiled`
- `VAEEncodeTiled`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `BasicGuider` —— 2/3 个有
- `ImageScaleBy` —— 2/3 个有
- `JjkText` —— 2/3 个有
- `LatentUpscaleBy` —— 2/3 个有
- `LoraLoaderModelOnly` —— 2/3 个有
- `VAEEncode` —— 2/3 个有
- `solarL_SaveImagesToZip` —— 2/3 个有
- `孤海注释` —— 2/3 个有
- `CFGGuider` —— 1/3 个有
- `Image Comparer (rgthree)` —— 1/3 个有
- `ImageBlend` —— 1/3 个有
- `ImageScale` —— 1/3 个有
- `LayerUtility: HLFrequencyDetailRestore` —— 1/3 个有
- `PrimitiveFloat` —— 1/3 个有
- `RH_DLSS5Enhance` —— 1/3 个有
- `ResizeImageMaskNode` —— 1/3 个有
- `SaveImageAdvanced` —— 1/3 个有
- `Seed (rgthree)` —— 1/3 个有
- `TextEncodeQwenImage21` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 512 | 3 | 9% |
| 高度 | 80 | 80 - 512 | 3 | 9% |
| 采样步数 | 4 | 1 - 4 | 3 | 53% |
| Prompt 约束强度(CFG) | 4.5 | 1 - 4.5 | 3 | 51% |
| 采样算法 | er_sde | - | 3 | 67% |
| 调度器 | beta | - | 3 | 67% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 5/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 512，3 个样本，取值分散，一致性仅 9%
- 高度 中位数 80，观测区间 80 - 512，3 个样本，取值分散，一致性仅 9%
- 采样步数 中位数 4，观测区间 1 - 4，3 个样本
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 1 - 4.5，3 个样本
- 采样算法 最常用 er_sde，3 个样本，一致性 67%
- 调度器 最常用 beta，3 个样本，一致性 67%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 高发问题（5/3 个样本）：Steps较低可能导致细节不足

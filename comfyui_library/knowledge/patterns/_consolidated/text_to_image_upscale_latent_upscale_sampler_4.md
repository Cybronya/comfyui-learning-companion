---
name: text_to_image_upscale_latent_upscale_sampler_4
type: Text To Image
frequency: 2
level: weak
coverage: 0.9535
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, ComfyMathExpression, EmptyLatentImage, GetImageSize, ImageMergeTileList, ImageScaleBy, KSampler, KSamplerSelect, LatentUpscaleBy, PrimitiveInt, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SaveImage, SeedVR2Conditioning, SeedVR2PostProcessing, SeedVR2Preprocess, SplitImageToTileList, SplitSigmas, UNETLoader, VAEDecode, VAEDecodeTiled, VAEEncode, VAEEncodeTiled, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/KREA2 SEEDVR2 100MP_2101605682029092865.json, 图片生成/文生图/KREA2 SEEDVR2 100MP工作流｜4MP二采加5x5分块放大｜原生节点_2101915958075023361.json]
source: knowledge_consolidation
---

# text_to_image_upscale_latent_upscale_sampler_4

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/KREA2 SEEDVR2 100MP_2101605682029092865.json、图片生成/文生图/KREA2 SEEDVR2 100MP工作流｜4MP二采加5x5分块放大｜原生节点_2101915958075023361.json）

- **类型**：Text To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：95%

## 共有节点

全部 2 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfyMathExpression`
- `EmptyLatentImage`
- `GetImageSize`
- `ImageMergeTileList`
- `ImageScaleBy`
- `KSampler`
- `KSamplerSelect`
- `LatentUpscaleBy`
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
- `VAEEncode`
- `VAEEncodeTiled`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `JjkText` —— 1/2 个有
- `LoraLoaderModelOnly` —— 1/2 个有
- `solarL_SaveImagesToZip` —— 1/2 个有
- `孤海注释` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 296 | - | 2 | 27% |
| 高度 | 296 | - | 2 | 27% |
| 采样步数 | 2.5 | - | 2 | 40% |
| Prompt 约束强度(CFG) | 2.75 | - | 2 | 36% |
| 采样算法 | euler | - | 2 | 50% |
| 调度器 | simple | - | 2 | 50% |
| 重绘幅度 | 1 | - | 2 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/2 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 296，样本不足，未给区间，2 个样本，取值分散，一致性仅 27%
- 高度 中位数 296，样本不足，未给区间，2 个样本，取值分散，一致性仅 27%
- 采样步数 中位数 2.5，样本不足，未给区间，2 个样本，取值分散，一致性仅 40%
- Prompt 约束强度(CFG) 中位数 2.75，样本不足，未给区间，2 个样本，取值分散，一致性仅 36%
- 采样算法 最常用 euler，2 个样本，一致性 50%
- 调度器 最常用 simple，2 个样本，一致性 50%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高发问题（3/2 个样本）：Steps较低可能导致细节不足
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参

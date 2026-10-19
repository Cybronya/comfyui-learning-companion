---
name: text_to_image_upscale_latent_upscale_lora_16
type: Text To Image
frequency: 2
level: weak
coverage: 0.8585
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyLatentImage, Fast Groups Bypasser (rgthree), GetImageSize+, ImageSmartSharpen+, JoinImageWithAlpha, KSampler, KSamplerAdvanced, LatentUpscaleBy, LoraLoaderModelOnly, PrimitiveFloat, ResizeImageMaskNode, ResolutionSelector, Seed (rgthree), SeedVR2Conditioning, SeedVR2PostProcessing, SeedVR2Preprocess, SimpleMathDual+, SplitImageWithAlpha, UNETLoader, UltimateSDUpscale, UpscaleModelLoader, VAEDecode, VAEDecodeTiled, VAEEncodeTiled, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Krea2新模型开源二采出图4种图片放大汇总工作流详拆_2100305559923806210.json, 图片生成/文生图/Krea2生图+SeedVR2-int8放大 (1)_2101836851886780417.json]
source: knowledge_consolidation
---

# text_to_image_upscale_latent_upscale_lora_16

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/Krea2新模型开源二采出图4种图片放大汇总工作流详拆_2100305559923806210.json、图片生成/文生图/Krea2生图+SeedVR2-int8放大 (1)_2101836851886780417.json）

- **类型**：Text To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：86%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `Fast Groups Bypasser (rgthree)`
- `GetImageSize+`
- `ImageSmartSharpen+`
- `JoinImageWithAlpha`
- `KSampler`
- `KSamplerAdvanced`
- `LatentUpscaleBy`
- `LoraLoaderModelOnly`
- `PrimitiveFloat`
- `ResizeImageMaskNode`
- `ResolutionSelector`
- `Seed (rgthree)`
- `SeedVR2Conditioning`
- `SeedVR2PostProcessing`
- `SeedVR2Preprocess`
- `SimpleMathDual+`
- `SplitImageWithAlpha`
- `UNETLoader`
- `UltimateSDUpscale`
- `UpscaleModelLoader`
- `VAEDecode`
- `VAEDecodeTiled`
- `VAEEncodeTiled`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `HAIGC_SaveImagesToZip` —— 1/2 个有
- `Image Comparer (rgthree)` —— 1/2 个有
- `ImageScaleBy` —— 1/2 个有
- `JjkText` —— 1/2 个有
- `Label (rgthree)` —— 1/2 个有
- `LoadImage` —— 1/2 个有
- `PreviewImage` —— 1/2 个有
- `RH_DLSS5Enhance` —— 1/2 个有
- `SaveImage` —— 1/2 个有
- `VOSR2ModelLoader` —— 1/2 个有
- `VOSR2Upscale` —— 1/2 个有
- `easy float` —— 1/2 个有
- `easy getNode` —— 1/2 个有
- `easy int` —— 1/2 个有
- `easy setNode` —— 1/2 个有
- `solarL_SaveImagesToZip` —— 1/2 个有
- `孤海注释` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 2.5 | - | 2 | 40% |
| Prompt 约束强度(CFG) | 2.75 | - | 2 | 36% |
| 采样算法 | er_sde | - | 2 | 50% |
| 调度器 | beta | - | 2 | 50% |
| 重绘幅度 | 1 | - | 2 | 100% |
| 宽度 | 552 | - | 2 | 14% |
| 高度 | 552 | - | 2 | 14% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 5/2 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 2.5，样本不足，未给区间，2 个样本，取值分散，一致性仅 40%
- Prompt 约束强度(CFG) 中位数 2.75，样本不足，未给区间，2 个样本，取值分散，一致性仅 36%
- 采样算法 最常用 er_sde，2 个样本，一致性 50%
- 调度器 最常用 beta，2 个样本，一致性 50%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 宽度 中位数 552，样本不足，未给区间，2 个样本，取值分散，一致性仅 14%
- 高度 中位数 552，样本不足，未给区间，2 个样本，取值分散，一致性仅 14%
- 高发问题（5/2 个样本）：Steps较低可能导致细节不足
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参

---
name: text_to_image_lora_sampler_clip_487
type: Text To Image
frequency: 3
level: strong
coverage: 0.867667
common_nodes: [CLIPLoader, CLIPTextEncode, ComfyMathExpression, EmptyLatentImage, GetImageSize, Image Comparer (rgthree), ImageBlend, ImageMergeTileList, JjkText, KSampler, LayerUtility: HLFrequencyDetailRestore, LoraLoaderModelOnly, PrimitiveFloat, PrimitiveInt, RH_DLSS5Enhance, ResizeImageMaskNode, ResolutionSelector, SaveImage, SeedVR2Conditioning, SeedVR2PostProcessing, SeedVR2Preprocess, SplitImageToTileList, TextEncodeQwenImage21, UNETLoader, VAEDecode, VAEDecodeTiled, VAEEncodeTiled, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen image2.1人物换头换脸｜一键面部替换改头换面｜图生图换脸实操_2112099875415486465.json, 图片生成/图生图/Qwen image2.1换头换脸，图生图换脸自然贴合_2112288790780923906.json, 图片生成/文生图/Qwen Image 2.1+SeedVR2+DLSS5级联 人像写真写实高清放大_2104292002979471361.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_487

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/Qwen image2.1人物换头换脸｜一键面部替换改头换面｜图生图换脸实操_2112099875415486465.json、图片生成/图生图/Qwen image2.1换头换脸，图生图换脸自然贴合_2112288790780923906.json、图片生成/文生图/Qwen Image 2.1+SeedVR2+DLSS5级联 人像写真写实高清放大_2104292002979471361.json）

- **类型**：Text To Image
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：87%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfyMathExpression`
- `EmptyLatentImage`
- `GetImageSize`
- `Image Comparer (rgthree)`
- `ImageBlend`
- `ImageMergeTileList`
- `JjkText`
- `KSampler`
- `LayerUtility: HLFrequencyDetailRestore`
- `LoraLoaderModelOnly`
- `PrimitiveFloat`
- `PrimitiveInt`
- `RH_DLSS5Enhance`
- `ResizeImageMaskNode`
- `ResolutionSelector`
- `SaveImage`
- `SeedVR2Conditioning`
- `SeedVR2PostProcessing`
- `SeedVR2Preprocess`
- `SplitImageToTileList`
- `TextEncodeQwenImage21`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeTiled`
- `VAEEncodeTiled`
- `VAELoader`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `Anything Everywhere3` —— 2/3 个有
- `ComfySwitchNode` —— 2/3 个有
- `LayerUtility: ImageReel` —— 2/3 个有
- `LayerUtility: ImageReelComposit` —— 2/3 个有
- `LoadImage` —— 2/3 个有
- `BasicScheduler` —— 1/3 个有
- `CFGGuider` —— 1/3 个有
- `ImageScale` —— 1/3 个有
- `KSamplerSelect` —— 1/3 个有
- `RandomNoise` —— 1/3 个有
- `SamplerCustomAdvanced` —— 1/3 个有
- `SaveImageAdvanced` —— 1/3 个有
- `Seed (rgthree)` —— 1/3 个有
- `SplitSigmas` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 3 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 3 | 100% |
| 采样算法 | er_sde | - | 3 | 100% |
| 调度器 | beta | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |
| 宽度 | 80 | 80 - 80 | 3 | 100% |
| 高度 | 80 | 80 - 80 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 6/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，3 个样本，一致性 100%
- 调度器 最常用 beta，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，3 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，3 个样本，取值集中（一致性 100%）
- 高发问题（6/3 个样本）：Steps较低可能导致细节不足

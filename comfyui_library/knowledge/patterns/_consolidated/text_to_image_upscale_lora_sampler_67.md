---
name: text_to_image_upscale_lora_sampler_67
type: Text To Image
frequency: 4
level: weak
coverage: 0.84775
common_nodes: [BasicScheduler, CFGGuider, CLIPLoader, CLIPTextEncode, ComfyMathExpression, ConditioningZeroOut, EmptyFlux2LatentImage, EmptyLatentImage, Fast Groups Bypasser (rgthree), GetImageSize, Image Comparer (rgthree), ImageBlend, ImageMergeTileList, ImageResizeKJv2, ImageScaleToTotalPixels, KSampler, KSamplerSelect, LayerUtility: HLFrequencyDetailRestore, LoadImage, LoraLoaderModelOnly, ManualSigmas, PreviewImage, PrimitiveFloat, PrimitiveInt, PrimitiveStringMultiline, QwenImage21Cache, RH_DLSS5Enhance, RandomNoise, ReferenceLatent, RegexReplace, ResizeImageMaskNode, SamplerCustomAdvanced, SaveImage, Seed (rgthree), SeedVR2Conditioning, SeedVR2PostProcessing, SeedVR2Preprocess, SplitImageToTileList, SplitImageWithAlpha, StringConcatenate, StringTrim, TextEncodeQwenImage21, TextGenerate, UNETLoader, VAEDecode, VAEDecodeTiled, VAEEncode, VAEEncodeTiled, VAELoader, VOSR2ModelLoader, VOSR2Upscale, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/AniVive_Qwen21_Workflow动漫活化｜写实图生图一键出片_2110686664736722946.json, 图片生成/图生图/AniVive_Qwen21写实图生图，动漫真人化一键转换_2110795374985302018.json, 图片生成/图生图/Qwen Image2.1动漫转真人_2111507074009092098.json, 图片生成/图生图/Qwen Image2.1动漫转真人｜二次元一键写实化｜动漫角色变真实质感_2112087180964356098.json]
source: knowledge_consolidation
---

# text_to_image_upscale_lora_sampler_67

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/AniVive_Qwen21_Workflow动漫活化｜写实图生图一键出片_2110686664736722946.json、图片生成/图生图/AniVive_Qwen21写实图生图，动漫真人化一键转换_2110795374985302018.json、图片生成/图生图/Qwen Image2.1动漫转真人_2111507074009092098.json、图片生成/图生图/Qwen Image2.1动漫转真人｜二次元一键写实化｜动漫角色变真实质感_2112087180964356098.json）

- **类型**：Text To Image
- **样本数**：4
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：85%

## 共有节点

全部 4 个 workflow 都包含：
- `BasicScheduler`
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfyMathExpression`
- `ConditioningZeroOut`
- `EmptyFlux2LatentImage`
- `EmptyLatentImage`
- `Fast Groups Bypasser (rgthree)`
- `GetImageSize`
- `Image Comparer (rgthree)`
- `ImageBlend`
- `ImageMergeTileList`
- `ImageResizeKJv2`
- `ImageScaleToTotalPixels`
- `KSampler`
- `KSamplerSelect`
- `LayerUtility: HLFrequencyDetailRestore`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ManualSigmas`
- `PreviewImage`
- `PrimitiveFloat`
- `PrimitiveInt`
- `PrimitiveStringMultiline`
- `QwenImage21Cache`
- `RH_DLSS5Enhance`
- `RandomNoise`
- `ReferenceLatent`
- `RegexReplace`
- `ResizeImageMaskNode`
- `SamplerCustomAdvanced`
- `SaveImage`
- `Seed (rgthree)`
- `SeedVR2Conditioning`
- `SeedVR2PostProcessing`
- `SeedVR2Preprocess`
- `SplitImageToTileList`
- `SplitImageWithAlpha`
- `StringConcatenate`
- `StringTrim`
- `TextEncodeQwenImage21`
- `TextGenerate`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeTiled`
- `VAEEncode`
- `VAEEncodeTiled`
- `VAELoader`
- `VOSR2ModelLoader`
- `VOSR2Upscale`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `JjkText` —— 3/4 个有
- `solarL_SaveImagesToZip` —— 3/4 个有
- `Anything Everywhere3` —— 2/4 个有
- `ComfySwitchNode` —— 2/4 个有
- `ResolutionSelector` —— 2/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 10 | 4 | 53% |
| Prompt 约束强度(CFG) | 4.5 | 1 - 4.5 | 4 | 58% |
| 采样算法 | er_sde | - | 4 | 75% |
| 调度器 | beta | - | 4 | 75% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |
| 宽度 | 80 | 80 - 1024 | 4 | 0% |
| 高度 | 80 | 80 - 1024 | 4 | 0% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 7/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 10，4 个样本
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 1 - 4.5，4 个样本
- 采样算法 最常用 er_sde，4 个样本，一致性 75%
- 调度器 最常用 beta，4 个样本，一致性 75%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 1024，4 个样本，取值分散，一致性仅 0%
- 高度 中位数 80，观测区间 80 - 1024，4 个样本，取值分散，一致性仅 0%
- 高发问题（7/4 个样本）：Steps较低可能导致细节不足

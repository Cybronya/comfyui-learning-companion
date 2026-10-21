---
name: text_to_image_upscale_lora_sampler_41
type: Text To Image
frequency: 3
level: weak
coverage: 0.691
common_nodes: [CFGGuider, CLIPLoader, CLIPTextEncode, CR Seed, CR Upscale Image, CheckpointLoaderSimple, ConditioningAverage, ConditioningZeroOut, EmptyFlux2LatentImage, EmptyLatentImage, Florence2ModelLoader, Florence2Run, Flux2Scheduler, GenerateNoise, GetImageSize, GetImageSize+, GetNode, Image Comparer (rgthree), ImageCompositeMasked, ImageScaleToTotalPixels, Int, KSampler, KSamplerSelect, LCSColorAnchor, LCSLoadData, LCSSharpnessCalibrate, LCSSharpnessIntervene, LGNoiseInjectionLatent, LoraLoaderBypassModelOnly, LoraLoaderModelOnly, PreviewImage, PrimitiveStringMultiline, RandomNoise, ReferenceLatent, ResizeMask, SamplerCustomAdvanced, SaveImage, SetNode, UNETLoader, UltimateSDUpscaleNoUpscale, VAEDecode, VAEEncode, VAELoader, VRAM_Debug, easy sam3ImageSegmentation, easy sam3ModelLoader, 孤海注释, 忽略多组孤海]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/三采专业洗图｜Krea 2+Flux2+zimage真实度提升版_2090941537101369346.json, 图片生成/文生图/自用版 Krea 2 +Flux2 图像高清放大修复工作流V2.0提高图_2089243311126179841.json, 图片生成/文生图/高清放大修复V2.0｜Krea 2+Flux2自用版图像画质提高_2089480954074193922.json]
source: knowledge_consolidation
---

# text_to_image_upscale_lora_sampler_41

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/三采专业洗图｜Krea 2+Flux2+zimage真实度提升版_2090941537101369346.json、图片生成/文生图/自用版 Krea 2 +Flux2 图像高清放大修复工作流V2.0提高图_2089243311126179841.json、图片生成/文生图/高清放大修复V2.0｜Krea 2+Flux2自用版图像画质提高_2089480954074193922.json）

- **类型**：Text To Image
- **样本数**：3
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：69%

## 共有节点

全部 3 个 workflow 都包含：
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Seed`
- `CR Upscale Image`
- `CheckpointLoaderSimple`
- `ConditioningAverage`
- `ConditioningZeroOut`
- `EmptyFlux2LatentImage`
- `EmptyLatentImage`
- `Florence2ModelLoader`
- `Florence2Run`
- `Flux2Scheduler`
- `GenerateNoise`
- `GetImageSize`
- `GetImageSize+`
- `GetNode`
- `Image Comparer (rgthree)`
- `ImageCompositeMasked`
- `ImageScaleToTotalPixels`
- `Int`
- `KSampler`
- `KSamplerSelect`
- `LCSColorAnchor`
- `LCSLoadData`
- `LCSSharpnessCalibrate`
- `LCSSharpnessIntervene`
- `LGNoiseInjectionLatent`
- `LoraLoaderBypassModelOnly`
- `LoraLoaderModelOnly`
- `PreviewImage`
- `PrimitiveStringMultiline`
- `RandomNoise`
- `ReferenceLatent`
- `ResizeMask`
- `SamplerCustomAdvanced`
- `SaveImage`
- `SetNode`
- `UNETLoader`
- `UltimateSDUpscaleNoUpscale`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `VRAM_Debug`
- `easy sam3ImageSegmentation`
- `easy sam3ModelLoader`
- `孤海注释`
- `忽略多组孤海`

**可变部分**（部分 workflow 才有）：
- `CR Text Concatenate` —— 2/3 个有
- `ConditioningKrea2Rebalance` —— 2/3 个有
- `JjkText` —— 2/3 个有
- `MaskPreview+` —— 2/3 个有
- `ResolutionSelector` —— 2/3 个有
- `solarL_SaveImagesToZip` —— 2/3 个有
- `DepthAnythingV2Preprocessor` —— 1/3 个有
- `EditTextEncode_EditUtils` —— 1/3 个有
- `Krea2EditApply_EditUtils` —— 1/3 个有
- `Krea2ModelConfig_EditUtils` —— 1/3 个有
- `LayerUtility: ImageReel` —— 1/3 个有
- `LayerUtility: ImageReelComposit` —— 1/3 个有
- `LoadImage` —— 1/3 个有
- `QwenConfigPreparer_EditUtils` —— 1/3 个有
- `ShowText|pysssss` —— 1/3 个有
- `easy promptConcat` —— 1/3 个有
- `llama_cpp_instruct_adv` —— 1/3 个有
- `llama_cpp_model_loader` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 8 | 3 | 65% |
| Prompt 约束强度(CFG) | 4.5 | 1 - 4.5 | 3 | 51% |
| 采样算法 | er_sde | - | 3 | 100% |
| 调度器 | beta | - | 3 | 67% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |
| 宽度 | 80 | 80 - 1280 | 3 | 0% |
| 高度 | 80 | 80 - 720 | 3 | 0% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 5/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 8，3 个样本
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 1 - 4.5，3 个样本
- 采样算法 最常用 er_sde，3 个样本，一致性 100%
- 调度器 最常用 beta，3 个样本，一致性 67%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 1280，3 个样本，取值分散，一致性仅 0%
- 高度 中位数 80，观测区间 80 - 720，3 个样本，取值分散，一致性仅 0%
- 高发问题（5/3 个样本）：Steps较低可能导致细节不足

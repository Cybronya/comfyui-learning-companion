---
name: text_to_image_upscale_lora_sampler_9
type: Text To Image
frequency: 4
level: weak
coverage: 0.5525
common_nodes: [Any Switch (rgthree), BasicScheduler, CFGGuider, CLIPLoader, CLIPTextEncode, ColorMatchV2, ConditioningKrea2Rebalance, ConditioningZeroOut, DepthAnythingV2Preprocessor, DyPE_FLUX, EmptyLatentImage, Fast Groups Bypasser (rgthree), GetImageSize, GetNode, Image Comparer (rgthree), ImageBlend, ImagePass, ImageUpscaleWithModel, ImpactStringSelector, KSampler, KSamplerAdvanced, KSamplerSelect, Krea2ControlApply, Krea2ControlImageEncode, Krea2ControlLoRALoader, LCSColorAnchor, LCSLoadData, LCSSharpnessCalibrate, LCSSharpnessIntervene, LCSToneAdjust, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: SaveImagePlus, LensBlur, LoadImage, LoaderGGUF, LoraLoaderModelOnly, ModelPassThrough, ModelPreviewOverrideKJ, ModelSamplingAuraFlow, PathchSageAttentionKJ, PlaySound|pysssss, PreviewImage, RandomNoise, ReferenceLatent, ResizeImageMaskNode, ResolutionSelector, SamplerCustomAdvanced, SaveImage, Seed (rgthree), SeedVR2Conditioning, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2PostProcessing, SeedVR2Preprocess, SeedVR2VideoUpscaler, SetNode, TextInput_, UNETLoader, UpscaleModelLoader, VAEDecode, VAEDecodeTiled, VAEEncode, VAEEncodeTiled, VAELoader, VOSR2ModelLoader, VOSR2Upscale, easy int, easy promptLine, easy showAnything, llama_cpp_instruct_adv, llama_cpp_model_loader, llama_cpp_parameters]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/反推提示词/Krea2三采修复+控制模型参考_int8（拒绝Turbo脸&三高清自选）_2094050032105385985.json, 图片生成/反推提示词/Krea2三采修复加控制模型参考拒绝Turbo脸三高清自选，文生图图生图方案_2106448759000489986.json, 图片生成/反推提示词/Krea2三采修复控制模型参考int8｜拒绝Turbo脸三高清自选_2106231696759812097.json, 视频生成/图生视频/Krea2三采修复控制模型参考_拒绝Turbo脸三高清自选_2101079965822439425.json]
source: knowledge_consolidation
---

# text_to_image_upscale_lora_sampler_9

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/反推提示词/Krea2三采修复+控制模型参考_int8（拒绝Turbo脸&三高清自选）_2094050032105385985.json、图片生成/反推提示词/Krea2三采修复加控制模型参考拒绝Turbo脸三高清自选，文生图图生图方案_2106448759000489986.json、图片生成/反推提示词/Krea2三采修复控制模型参考int8｜拒绝Turbo脸三高清自选_2106231696759812097.json、视频生成/图生视频/Krea2三采修复控制模型参考_拒绝Turbo脸三高清自选_2101079965822439425.json）

- **类型**：Text To Image
- **样本数**：4
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：55%

## 共有节点

全部 4 个 workflow 都包含：
- `Any Switch (rgthree)`
- `BasicScheduler`
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `ColorMatchV2`
- `ConditioningKrea2Rebalance`
- `ConditioningZeroOut`
- `DepthAnythingV2Preprocessor`
- `DyPE_FLUX`
- `EmptyLatentImage`
- `Fast Groups Bypasser (rgthree)`
- `GetImageSize`
- `GetNode`
- `Image Comparer (rgthree)`
- `ImageBlend`
- `ImagePass`
- `ImageUpscaleWithModel`
- `ImpactStringSelector`
- `KSampler`
- `KSamplerAdvanced`
- `KSamplerSelect`
- `Krea2ControlApply`
- `Krea2ControlImageEncode`
- `Krea2ControlLoRALoader`
- `LCSColorAnchor`
- `LCSLoadData`
- `LCSSharpnessCalibrate`
- `LCSSharpnessIntervene`
- `LCSToneAdjust`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: SaveImagePlus`
- `LensBlur`
- `LoadImage`
- `LoaderGGUF`
- `LoraLoaderModelOnly`
- `ModelPassThrough`
- `ModelPreviewOverrideKJ`
- `ModelSamplingAuraFlow`
- `PathchSageAttentionKJ`
- `PlaySound|pysssss`
- `PreviewImage`
- `RandomNoise`
- `ReferenceLatent`
- `ResizeImageMaskNode`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `SaveImage`
- `Seed (rgthree)`
- `SeedVR2Conditioning`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2PostProcessing`
- `SeedVR2Preprocess`
- `SeedVR2VideoUpscaler`
- `SetNode`
- `TextInput_`
- `UNETLoader`
- `UpscaleModelLoader`
- `VAEDecode`
- `VAEDecodeTiled`
- `VAEEncode`
- `VAEEncodeTiled`
- `VAELoader`
- `VOSR2ModelLoader`
- `VOSR2Upscale`
- `easy int`
- `easy promptLine`
- `easy showAnything`
- `llama_cpp_instruct_adv`
- `llama_cpp_model_loader`
- `llama_cpp_parameters`

**可变部分**（部分 workflow 才有）：
- `JjkText` —— 3/4 个有
- `solarL_SaveImagesToZip` —— 3/4 个有
- `JoinImageWithAlpha` —— 2/4 个有
- `Mute / Bypass Relay (rgthree)` —— 2/4 个有
- `Mute / Bypass Repeater (rgthree)` —— 2/4 个有
- `孤海注释` —— 2/4 个有
- `EmptyImage` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 1088 | 4 | 0% |
| 高度 | 80 | 80 - 1920 | 4 | 0% |
| 采样步数 | 4 | 1 - 4 | 4 | 60% |
| Prompt 约束强度(CFG) | 4.5 | 1 - 4.5 | 4 | 58% |
| 采样算法 | er_sde | - | 4 | 75% |
| 调度器 | beta | - | 4 | 75% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 7/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 1088，4 个样本，取值分散，一致性仅 0%
- 高度 中位数 80，观测区间 80 - 1920，4 个样本，取值分散，一致性仅 0%
- 采样步数 中位数 4，观测区间 1 - 4，4 个样本
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 1 - 4.5，4 个样本
- 采样算法 最常用 er_sde，4 个样本，一致性 75%
- 调度器 最常用 beta，4 个样本，一致性 75%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 高发问题（7/4 个样本）：Steps较低可能导致细节不足

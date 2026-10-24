---
name: text_to_image_upscale_lora_sampler_15
type: Text To Image
frequency: 10
level: weak
coverage: 0.5589
common_nodes: [Any Switch (rgthree), BasicScheduler, CFGGuider, CLIPLoader, CLIPTextEncode, ColorMatchV2, ConditioningKrea2Rebalance, ConditioningZeroOut, DyPE_FLUX, EmptyLatentImage, Fast Groups Bypasser (rgthree), GetImageSize, GetNode, Image Comparer (rgthree), ImageBlend, ImagePass, ImageUpscaleWithModel, ImpactStringSelector, KSampler, KSamplerAdvanced, KSamplerSelect, LCSColorAnchor, LCSLoadData, LCSSharpnessCalibrate, LCSSharpnessIntervene, LCSToneAdjust, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: SaveImagePlus, LensBlur, LoadImage, LoaderGGUF, LoraLoaderModelOnly, ModelPassThrough, ModelPreviewOverrideKJ, ModelSamplingAuraFlow, PathchSageAttentionKJ, PlaySound|pysssss, PreviewImage, RandomNoise, ReferenceLatent, ResizeImageMaskNode, ResolutionSelector, SamplerCustomAdvanced, SaveImage, Seed (rgthree), SeedVR2Conditioning, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2PostProcessing, SeedVR2Preprocess, SeedVR2VideoUpscaler, SetNode, TextInput_, UNETLoader, UpscaleModelLoader, VAEDecode, VAEDecodeTiled, VAEEncode, VAEEncodeTiled, VAELoader, easy int, easy promptLine, easy showAnything, llama_cpp_instruct_adv, llama_cpp_model_loader, llama_cpp_parameters]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/反推提示词/Krea2三采修复+控制模型参考_int8（拒绝Turbo脸&三高清自选）_2094050032105385985.json, 图片生成/反推提示词/Krea2三采修复加控制模型参考拒绝Turbo脸三高清自选，文生图图生图方案_2106448759000489986.json, 图片生成/反推提示词/Krea2三采修复控制模型参考int8｜拒绝Turbo脸三高清自选_2106231696759812097.json, 图片生成/图生图/Krea2三采修复+控制模型参考_int8拒绝Turbo脸&三高清自选_2099781290303254530.json, 图片生成/图生图/Krea2三采修复+控制模型参考_int8拒绝Turbo脸&三高清自选_2100040420905537537.json, 图片生成/文生图/Krea2 in 三采修复加控制模型参考，拒绝Turbo脸三高清自选_2110440704429350914.json, 图片生成/文生图/Krea2三采修复控制模型参考 拒绝Turbo脸三高清自选_2099945846145110018.json, 图片生成/文生图/Krea2三采质感修复｜TrueV3拒绝Turbo脸双高清可选_2096304896143355906.json, 图片生成/文生图/拒绝Turbo假脸｜Krea2三采质感修复双高清可选_2096584176781840385.json, 视频生成/图生视频/Krea2三采修复控制模型参考_拒绝Turbo脸三高清自选_2101079965822439425.json]
source: knowledge_consolidation
---

# text_to_image_upscale_lora_sampler_15

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（图片生成/反推提示词/Krea2三采修复+控制模型参考_int8（拒绝Turbo脸&三高清自选）_2094050032105385985.json、图片生成/反推提示词/Krea2三采修复加控制模型参考拒绝Turbo脸三高清自选，文生图图生图方案_2106448759000489986.json、图片生成/反推提示词/Krea2三采修复控制模型参考int8｜拒绝Turbo脸三高清自选_2106231696759812097.json、图片生成/图生图/Krea2三采修复+控制模型参考_int8拒绝Turbo脸&三高清自选_2099781290303254530.json、图片生成/图生图/Krea2三采修复+控制模型参考_int8拒绝Turbo脸&三高清自选_2100040420905537537.json…）

- **类型**：Text To Image
- **样本数**：10
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：56%

## 共有节点

全部 10 个 workflow 都包含：
- `Any Switch (rgthree)`
- `BasicScheduler`
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `ColorMatchV2`
- `ConditioningKrea2Rebalance`
- `ConditioningZeroOut`
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
- `easy int`
- `easy promptLine`
- `easy showAnything`
- `llama_cpp_instruct_adv`
- `llama_cpp_model_loader`
- `llama_cpp_parameters`

**可变部分**（部分 workflow 才有）：
- `DepthAnythingV2Preprocessor` —— 8/10 个有
- `Krea2ControlApply` —— 8/10 个有
- `Krea2ControlImageEncode` —— 8/10 个有
- `Krea2ControlLoRALoader` —— 8/10 个有
- `VOSR2ModelLoader` —— 8/10 个有
- `VOSR2Upscale` —— 8/10 个有
- `JjkText` —— 7/10 个有
- `JoinImageWithAlpha` —— 7/10 个有
- `solarL_SaveImagesToZip` —— 7/10 个有
- `孤海注释` —— 6/10 个有
- `Mute / Bypass Relay (rgthree)` —— 3/10 个有
- `Mute / Bypass Repeater (rgthree)` —— 3/10 个有
- `EmptyImage` —— 1/10 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 1088 | 10 | 0% |
| 高度 | 80 | 80 - 1920 | 10 | 0% |
| 采样步数 | 4 | 1 - 4 | 8 | 73% |
| Prompt 约束强度(CFG) | 4.5 | 1 - 16 | 10 | 24% |
| 采样算法 | er_sde | - | 10 | 70% |
| 调度器 | beta | - | 10 | 70% |
| 重绘幅度 | 1 | 1 - 1 | 8 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 17/10 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 1088，10 个样本，取值分散，一致性仅 0%
- 高度 中位数 80，观测区间 80 - 1920，10 个样本，取值分散，一致性仅 0%
- 采样步数 中位数 4，观测区间 1 - 4，8 个样本
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 1 - 16，10 个样本，取值分散，一致性仅 24%
- 采样算法 最常用 er_sde，10 个样本，一致性 70%
- 调度器 最常用 beta，10 个样本，一致性 70%
- 重绘幅度 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 风险：Prompt 约束强度(CFG) 观测到 16，超出安全上限 12（CFG 偏高容易出现过度约束（如脸部异常、过饱和））
- 高发问题（17/10 个样本）：Steps较低可能导致细节不足

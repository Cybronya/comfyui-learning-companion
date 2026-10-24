---
name: text_to_image_upscale_lora_sampler_25
type: Text To Image
frequency: 8
level: strong
coverage: 0.905375
common_nodes: [AILab_QwenVL, AdvancedLyingSigmaSampler, BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, CR Text, ConditioningZeroOut, DisableNoise, EmptyLatentImage, FlipSigmas, Float, FluxDeGuidance, FluxForwardODESampler, FluxReverseODESampler, Get resolution [Crystools], Image Comparer (rgthree), ImageResize+, ImageScaleBy, ImageUpscaleWithModel, InFluxModelSamplingPred, JWFloat, JjkText, KSampler, KSamplerSelect, Latent Noise Injection, LayerUtility: PurgeVRAM V2, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, NunchakuFluxDiTLoader, NunchakuTextEncoderLoader, OutFluxModelSamplingPred, PreviewImage, ReferenceLatent, SamplerCustomAdvanced, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, ShowText|pysssss, SimpleMath+, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, UNETLoader, UNETLoader_Any, UltimateSDUpscaleCustomSample, Upscale Model Loader, UpscaleModelLoader, VAEDecode, VAEEncode, VAELoader, easy cleanGpuUsed, easy imageColorMatch, easy int, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Z-image+Klein+SeedVR2去AI感｜商业级图片真实感放大_2100888588719312897.json, 图片生成/图生图/Z-image加Klein加SeedVR2去AI感商业级图片真实感放大_2099939087326208001.json, 图片生成/图生图/Z-image加Klein加SeedVR2去AI感商业级图片真实感放大_2100174854598254593.json, 图片生成/图生图/Z-image加Klein加SeedVR2去AI感商业级图片真实感放大_2100554114043305985.json, 图片生成/图生图/Z-image加Klein加SeedVR2去AI感商业级图片真实感放大_2101863276178141185.json, 图片生成/图生图/最真实的高清放大工作流，海报制作图生图利器_2111936649461583873.json, 图片生成/图生图/高清放大真实细节精修｜画质增强图生图工作流_2095561199550291970.json, 图片生成/文生图/高清放大真实细节精修｜画质增强图生图工作流（干净02）_2104408365530177537.json]
source: knowledge_consolidation
---

# text_to_image_upscale_lora_sampler_25

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/图生图/Z-image+Klein+SeedVR2去AI感｜商业级图片真实感放大_2100888588719312897.json、图片生成/图生图/Z-image加Klein加SeedVR2去AI感商业级图片真实感放大_2099939087326208001.json、图片生成/图生图/Z-image加Klein加SeedVR2去AI感商业级图片真实感放大_2100174854598254593.json、图片生成/图生图/Z-image加Klein加SeedVR2去AI感商业级图片真实感放大_2100554114043305985.json、图片生成/图生图/Z-image加Klein加SeedVR2去AI感商业级图片真实感放大_2101863276178141185.json…）

- **类型**：Text To Image
- **样本数**：8
- **可信度**：强结论
- **平均知识覆盖**：91%

## 共有节点

全部 8 个 workflow 都包含：
- `AILab_QwenVL`
- `AdvancedLyingSigmaSampler`
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Text`
- `ConditioningZeroOut`
- `DisableNoise`
- `EmptyLatentImage`
- `FlipSigmas`
- `Float`
- `FluxDeGuidance`
- `FluxForwardODESampler`
- `FluxReverseODESampler`
- `Get resolution [Crystools]`
- `Image Comparer (rgthree)`
- `ImageResize+`
- `ImageScaleBy`
- `ImageUpscaleWithModel`
- `InFluxModelSamplingPred`
- `JWFloat`
- `JjkText`
- `KSampler`
- `KSamplerSelect`
- `Latent Noise Injection`
- `LayerUtility: PurgeVRAM V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `NunchakuFluxDiTLoader`
- `NunchakuTextEncoderLoader`
- `OutFluxModelSamplingPred`
- `PreviewImage`
- `ReferenceLatent`
- `SamplerCustomAdvanced`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `ShowText|pysssss`
- `SimpleMath+`
- `TTP_Image_Assy`
- `TTP_Image_Tile_Batch`
- `TTP_Tile_image_size`
- `UNETLoader`
- `UNETLoader_Any`
- `UltimateSDUpscaleCustomSample`
- `Upscale Model Loader`
- `UpscaleModelLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy cleanGpuUsed`
- `easy imageColorMatch`
- `easy int`
- `solarL_SaveImagesToZip`

**可变部分**（部分 workflow 才有）：
- `孤海注释` —— 5/8 个有
- `EmptyImage` —— 4/8 个有
- `LayerColor: RGB` —— 3/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 8 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 8 | 100% |
| 采样算法 | er_sde | - | 8 | 100% |
| 调度器 | beta | - | 8 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 8 | 100% |
| 宽度 | 80 | 80 - 80 | 8 | 100% |
| 高度 | 80 | 80 - 80 | 8 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 33/8 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，8 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，8 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，8 个样本，一致性 100%
- 调度器 最常用 beta，8 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，8 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，8 个样本，取值集中（一致性 100%）
- 高发问题（33/8 个样本）：Steps较低可能导致细节不足

---
name: image_to_image_upscale_lora_sampler_17
type: Image To Image
frequency: 9
level: strong
coverage: 0.862889
common_nodes: [AdvancedLyingSigmaSampler, CLIPLoader, CLIPTextEncode, ConditioningZeroOut, Float, Get resolution [Crystools], Image Comparer (rgthree), ImageResize+, ImageScaleBy, ImageUpscaleWithModel, Int, KSampler, KSamplerSelect, KuwaharaBlur, Latent Noise Injection, LayerUtility: PurgeVRAM V2, LoadImage, LoraLoaderModelOnly, PreviewImage, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, ShowText|pysssss, SimpleMath+, SimpleMathSlider+, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, UNETLoader, UltimateSDUpscaleCustomSample, Upscale Model Loader, UpscaleModelLoader, VAEDecode, VAEEncode, VAELoader, easy int]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Z-image+SeedVR2  去ai感真实放大商业级细节放大_1993989093778456577.json, 图片生成/图生图/Z-image+SeedVR2_去ai感真实放大商业级细节放大_2097173668689432577.json, 图片生成/图生图/Z-image+SeedVR2_去ai感真实放大商业级细节放大_2097512424256659457.json, 图片生成/图生图/ZimageSeedVR2去ai感真实放大商业级细节放大_2058087357148131329.json, 图片生成/图生图/去ai感可重绘-真实商业级放大_2064252813978456066.json, 图片生成/图生图/通用放大1.0_2084180528563048449.json, 图片生成/图生图/通用放大1.0变化较大_2105125594831876097.json, 图片生成/图生图/通用放大1.0变化较大_2105504410754437122.json, 图片生成/图生图/通用放大1.0（变化较大）_2046770171917897729.json]
source: knowledge_consolidation
---

# image_to_image_upscale_lora_sampler_17

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（图片生成/图生图/Z-image+SeedVR2  去ai感真实放大商业级细节放大_1993989093778456577.json、图片生成/图生图/Z-image+SeedVR2_去ai感真实放大商业级细节放大_2097173668689432577.json、图片生成/图生图/Z-image+SeedVR2_去ai感真实放大商业级细节放大_2097512424256659457.json、图片生成/图生图/ZimageSeedVR2去ai感真实放大商业级细节放大_2058087357148131329.json、图片生成/图生图/去ai感可重绘-真实商业级放大_2064252813978456066.json…）

- **类型**：Image To Image
- **样本数**：9
- **可信度**：强结论
- **平均知识覆盖**：86%

## 共有节点

全部 9 个 workflow 都包含：
- `AdvancedLyingSigmaSampler`
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `Float`
- `Get resolution [Crystools]`
- `Image Comparer (rgthree)`
- `ImageResize+`
- `ImageScaleBy`
- `ImageUpscaleWithModel`
- `Int`
- `KSampler`
- `KSamplerSelect`
- `KuwaharaBlur`
- `Latent Noise Injection`
- `LayerUtility: PurgeVRAM V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PreviewImage`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `ShowText|pysssss`
- `SimpleMath+`
- `SimpleMathSlider+`
- `TTP_Image_Assy`
- `TTP_Image_Tile_Batch`
- `TTP_Tile_image_size`
- `UNETLoader`
- `UltimateSDUpscaleCustomSample`
- `Upscale Model Loader`
- `UpscaleModelLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy int`

**可变部分**（部分 workflow 才有）：
- `ImageFromBatch` —— 8/9 个有
- `ImpactMakeAnyList` —— 8/9 个有
- `AILab_QwenVL` —— 7/9 个有
- `easy cleanGpuUsed` —— 6/9 个有
- `llama_cpp_instruct_adv` —— 6/9 个有
- `llama_cpp_model_loader` —— 6/9 个有
- `llama_cpp_parameters` —— 6/9 个有
- `CR Text` —— 5/9 个有
- `DF_Integer` —— 5/9 个有
- `Fast Groups Bypasser (rgthree)` —— 5/9 个有
- `ImageCASharpening+` —— 5/9 个有
- `ImpactMinMax` —— 5/9 个有
- `easy imageSize` —— 5/9 个有
- `GrowMask` —— 4/9 个有
- `InvertMask` —— 4/9 个有
- `JoinImageWithAlpha` —— 4/9 个有
- `LayerColor: RGB` —— 4/9 个有
- `LayerMask: BiRefNetUltraV2` —— 4/9 个有
- `LayerMask: LoadBiRefNetModelV2` —— 4/9 个有
- `MuyeTextEditOutput` —— 4/9 个有
- `RHHiddenNodes` —— 4/9 个有
- `GroupExecutor` —— 3/9 个有
- `YUAN_TXTConvertAny` —— 1/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 3 | 3 - 3 | 9 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 9 | 100% |
| 采样算法 | er_sde | - | 9 | 100% |
| 调度器 | sgm_uniform | - | 9 | 100% |
| 重绘幅度 | 0.45 | 0.45 - 0.45 | 9 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 18/9 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 3，观测区间 3 - 3，9 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，9 个样本，一致性 100%
- 调度器 最常用 sgm_uniform，9 个样本，一致性 100%
- 重绘幅度 中位数 0.45，观测区间 0.45 - 0.45，9 个样本，取值集中（一致性 100%）
- 高发问题（18/9 个样本）：Steps较低可能导致细节不足

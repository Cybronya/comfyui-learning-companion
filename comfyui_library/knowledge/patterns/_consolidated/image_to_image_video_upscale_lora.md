---
name: image_to_image_video_upscale_lora
type: Image To Image
frequency: 6
level: strong
coverage: 0.6005
common_nodes: [AILab_QwenVL, BiRefNetRMBG, CLIPLoader, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, CR Text, CheckpointLoaderSimple, ColorTransfer, Fast Bypasser (rgthree), Fast Groups Bypasser (rgthree), GetNode, ICLightConditioning, ImageCompositeFromMaskBatch+, ImageCrop+, ImageScale, ImageScaleToTotalPixels, ImageToMask, ImpactGaussianBlurMask, Int, JWInteger, KSampler, KSamplerAdvanced, LayerColor: AutoAdjustV2, LayerColor: ColorTemperature, LayerFilter: FilmV2, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: NanoBananaImageScale, LoadImage, LoraLoaderModelOnly, MaskBoundingBox+, MathExpression|pysssss, ModelPatchTorchSettings, ModelSamplingSD3, Mute / Bypass Repeater (rgthree), PainterI2V, PathchSageAttentionKJ, PreviewImage, RHHiddenNodes, RIFE VFI, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, SetNode, Text Concatenate, TextInput_, UNETLoader, VAEDecode, VAEEncode, VAELoader, VHS_LoadVideo, VHS_VideoCombine, easy showAnything, wanBlockSwap]
problems: []
missing: []
members: [视频生成/图生视频/2057362585078558722.json, 视频生成/图生视频/2058793721805754369.json, 视频生成/图生视频/2059078448089489410.json, 视频生成/图生视频/2059523614877249538.json, 视频生成/图生视频/2053805894110072833.json, 视频生成/图生视频/2064586564524658690.json]
source: knowledge_consolidation
---

# image_to_image_video_upscale_lora

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（视频生成/图生视频/2057362585078558722.json、视频生成/图生视频/2058793721805754369.json、视频生成/图生视频/2059078448089489410.json、视频生成/图生视频/2059523614877249538.json、视频生成/图生视频/2053805894110072833.json…）

- **类型**：Image To Image
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：60%

## 共有节点

全部 6 个 workflow 都包含：
- `AILab_QwenVL`
- `BiRefNetRMBG`
- `CLIPLoader`
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `CR Text`
- `CheckpointLoaderSimple`
- `ColorTransfer`
- `Fast Bypasser (rgthree)`
- `Fast Groups Bypasser (rgthree)`
- `GetNode`
- `ICLightConditioning`
- `ImageCompositeFromMaskBatch+`
- `ImageCrop+`
- `ImageScale`
- `ImageScaleToTotalPixels`
- `ImageToMask`
- `ImpactGaussianBlurMask`
- `Int`
- `JWInteger`
- `KSampler`
- `KSamplerAdvanced`
- `LayerColor: AutoAdjustV2`
- `LayerColor: ColorTemperature`
- `LayerFilter: FilmV2`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: NanoBananaImageScale`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MaskBoundingBox+`
- `MathExpression|pysssss`
- `ModelPatchTorchSettings`
- `ModelSamplingSD3`
- `Mute / Bypass Repeater (rgthree)`
- `PainterI2V`
- `PathchSageAttentionKJ`
- `PreviewImage`
- `RHHiddenNodes`
- `RIFE VFI`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `SetNode`
- `Text Concatenate`
- `TextInput_`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `easy showAnything`
- `wanBlockSwap`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 6 | 100% |
| Prompt 约束强度(CFG) | 6 | 6 - 6 | 6 | 100% |
| 采样算法 | 0.8 | 0.8 - 0.8 | 6 | 100% |
| 调度器 | euler | - | 6 | 100% |
| 重绘幅度 | simple | - | 6 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，6 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 6，观测区间 6 - 6，6 个样本，取值集中（一致性 100%）
- 采样算法 中位数 0.8，观测区间 0.8 - 0.8，6 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler，6 个样本，一致性 100%
- 重绘幅度 最常用 simple，6 个样本，一致性 100%

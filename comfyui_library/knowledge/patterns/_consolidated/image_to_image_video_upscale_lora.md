---
name: image_to_image_video_upscale_lora
type: Image To Image
frequency: 7
level: strong
coverage: 0.600429
common_nodes: [AILab_QwenVL, BiRefNetRMBG, CLIPLoader, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, CR Text, CheckpointLoaderSimple, ColorTransfer, Fast Bypasser (rgthree), Fast Groups Bypasser (rgthree), GetNode, ICLightConditioning, ImageCompositeFromMaskBatch+, ImageCrop+, ImageScale, ImageScaleToTotalPixels, ImageToMask, ImpactGaussianBlurMask, Int, JWInteger, KSampler, KSamplerAdvanced, LayerColor: AutoAdjustV2, LayerColor: ColorTemperature, LayerFilter: FilmV2, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: NanoBananaImageScale, LoadImage, LoraLoaderModelOnly, MaskBoundingBox+, MathExpression|pysssss, ModelPatchTorchSettings, ModelSamplingSD3, Mute / Bypass Repeater (rgthree), PainterI2V, PathchSageAttentionKJ, PreviewImage, RHHiddenNodes, RIFE VFI, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, SetNode, Text Concatenate, TextInput_, UNETLoader, VAEDecode, VAEEncode, VAELoader, VHS_LoadVideo, VHS_VideoCombine, easy showAnything, wanBlockSwap]
problems: []
missing: []
members: [图片生成/图生图/wan2.2一键融图 _ 正方格动画 任意背景 自动构图  反推 调色补帧_2059896882591264769.json, 视频生成/图生视频/wan2.2一键融图 _ 正方格动画 任意背景 自动构图  反推 调色补帧_2057362585078558722.json, 视频生成/图生视频/wan2.2一键融图 _ 正方格动画 任意背景 自动构图  反推 调色补帧_2058793721805754369.json, 视频生成/图生视频/wan2.2一键融图+_+正方格动画+任意背景+自动构图++反推+调色补帧_2059078448089489410.json, 视频生成/图生视频/wan2.2一键融图+_+正方格动画+任意背景调色补帧_2059523614877249538.json, 视频生成/图生视频/一键融图 _ 正方格动画 任意背景 自动构图 反推调色 补帧超分 剪辑素材一件入库-wan2.2_2053805894110072833.json, 视频生成/图生视频/动画生图任意背景调色补帧_2064586564524658690.json]
source: knowledge_consolidation
---

# image_to_image_video_upscale_lora

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/图生图/wan2.2一键融图 _ 正方格动画 任意背景 自动构图  反推 调色补帧_2059896882591264769.json、视频生成/图生视频/wan2.2一键融图 _ 正方格动画 任意背景 自动构图  反推 调色补帧_2057362585078558722.json、视频生成/图生视频/wan2.2一键融图 _ 正方格动画 任意背景 自动构图  反推 调色补帧_2058793721805754369.json、视频生成/图生视频/wan2.2一键融图+_+正方格动画+任意背景+自动构图++反推+调色补帧_2059078448089489410.json、视频生成/图生视频/wan2.2一键融图+_+正方格动画+任意背景调色补帧_2059523614877249538.json…）

- **类型**：Image To Image
- **样本数**：7
- **可信度**：强结论
- **平均知识覆盖**：60%

## 共有节点

全部 7 个 workflow 都包含：
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
| 采样步数 | fixed | - | 7 | 100% |
| Prompt 约束强度(CFG) | 6 | 6 - 6 | 7 | 100% |
| 采样算法 | 0.8 | 0.8 - 0.8 | 7 | 100% |
| 调度器 | euler | - | 7 | 100% |
| 重绘幅度 | simple | - | 7 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，7 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 6，观测区间 6 - 6，7 个样本，取值集中（一致性 100%）
- 采样算法 中位数 0.8，观测区间 0.8 - 0.8，7 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler，7 个样本，一致性 100%
- 重绘幅度 最常用 simple，7 个样本，一致性 100%

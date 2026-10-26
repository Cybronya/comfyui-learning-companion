---
name: image_to_image_upscale_lora_sampler_65
type: Image To Image
frequency: 3
level: strong
coverage: 0.685
common_nodes: [AILab_ImagePreview, AILab_Preview, AILab_QwenVL, CFGNorm, CLIPLoader, FluxKontextMultiReferenceLatentMethod, GetImageSize, GetNode, GrowMaskWithBlur, Image Comparer (rgthree), Image Paste Crop, ImageBlend, ImageCrop, ImageInvert, ImageResizeKJv2, ImageScaleToMaxDimension, ImageToMask, InvertMask, KSampler, LoadImage, LoraLoaderModelOnly, Mask Crop Region, MaskToImage, ModelSamplingAuraFlow, PreviewAny, PreviewImage, PrimitiveStringMultiline, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, SetNode, StringConcatenate, TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode, VAEEncode, VAELoader, easy imageConcat, easy int]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/图片编辑_主体替换(视频首帧)_Qwen-Image-Edit-2511_2002954167557734401.json, 图片生成/图生图/图片编辑_任意角度换脸_QWen-Image-Edit-2509_vs_2511_2003051533484867585.json, 图片生成/图生图/超好用🔥图片任意角度换脸，丝滑好用_2056668213433421826.json]
source: knowledge_consolidation
---

# image_to_image_upscale_lora_sampler_65

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/图片编辑_主体替换(视频首帧)_Qwen-Image-Edit-2511_2002954167557734401.json、图片生成/图生图/图片编辑_任意角度换脸_QWen-Image-Edit-2509_vs_2511_2003051533484867585.json、图片生成/图生图/超好用🔥图片任意角度换脸，丝滑好用_2056668213433421826.json）

- **类型**：Image To Image
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：68%

## 共有节点

全部 3 个 workflow 都包含：
- `AILab_ImagePreview`
- `AILab_Preview`
- `AILab_QwenVL`
- `CFGNorm`
- `CLIPLoader`
- `FluxKontextMultiReferenceLatentMethod`
- `GetImageSize`
- `GetNode`
- `GrowMaskWithBlur`
- `Image Comparer (rgthree)`
- `Image Paste Crop`
- `ImageBlend`
- `ImageCrop`
- `ImageInvert`
- `ImageResizeKJv2`
- `ImageScaleToMaxDimension`
- `ImageToMask`
- `InvertMask`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `Mask Crop Region`
- `MaskToImage`
- `ModelSamplingAuraFlow`
- `PreviewAny`
- `PreviewImage`
- `PrimitiveStringMultiline`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `SetNode`
- `StringConcatenate`
- `TextEncodeQwenImageEditPlus`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy imageConcat`
- `easy int`

**可变部分**（部分 workflow 才有）：
- `AILab_ICLoRAConcat` —— 2/3 个有
- `AIO_Preprocessor` —— 2/3 个有
- `AutoCropFaces` —— 2/3 个有
- `Bounded Image Crop with Mask` —— 2/3 个有
- `ColorMatch` —— 2/3 个有
- `INTConstant` —— 2/3 个有
- `ImagePadForOutpaint` —— 2/3 个有
- `ImpactMinMax` —— 2/3 个有
- `LoadSAM3Model` —— 2/3 个有
- `SAM3Segmentation` —— 2/3 个有
- `UnetLoaderGGUF` —— 2/3 个有
- `easy boolean` —— 2/3 个有
- `easy compare` —— 2/3 个有
- `easy ifElse` —— 2/3 个有
- `easy mathInt` —— 2/3 个有
- `DrawViTPose` —— 1/3 个有
- `GroundingDinoModelLoader (segment anything2)` —— 1/3 个有
- `GroundingDinoSAM2Segment (segment anything2)` —— 1/3 个有
- `OnnxDetectionModelLoader` —— 1/3 个有
- `PoseAndFaceDetection` —— 1/3 个有
- `ReferenceLatent` —— 1/3 个有
- `SAM2ModelLoader (segment anything2)` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 3 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | simple | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 5/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 simple，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 高发问题（5/3 个样本）：Steps较低可能导致细节不足

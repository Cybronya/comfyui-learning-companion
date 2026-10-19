---
name: image_to_image_video_lora_sampler_13
type: Image To Image
frequency: 3
level: strong
coverage: 0.761667
common_nodes: [AdvancedLivePortrait, AutoCropFaces, CLIPLoader, CLIPVisionLoader, CR Prompt Text, ConditioningZeroOut, ExpressionEditor, FantasyPortraitFaceDetector, FantasyPortraitModelLoader, Float, FluxKontextImageScale, GetImageSizeAndCount, GetNode, Image Comparer (rgthree), ImageConcanate, ImageConcatMulti, ImageRemoveAlpha_UTK, ImageResizeKJv2, Int, JWInteger, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, MaskPreview+, ModelSamplingAuraFlow, OnnxDetectionModelLoader, PainterFluxImageEdit, PixelSmileConditioning, PoseAndFaceDetection, PreviewAny, PreviewImage, RMBG, ReplaceText, SDPoseOODLoader, SDPoseOODProcessor, SaveImage, SetNode, SolidMask, Text, TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode, VAEEncode, VAELoader, VHS_LoadVideo, VHS_VideoCombine, VHS_VideoInfo, WanVideoAddFantasyPortrait, WanVideoAnimateEmbeds, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoImageToVideoEncode, WanVideoLoraSelect, WanVideoLoraSelectMulti, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncodeCached, WanVideoTorchCompileSettings, WanVideoVAELoader, YOLOModelLoader, easy ifElse, easy isMaskEmpty, easy showAnything, llama_cpp_instruct_adv, llama_cpp_model_loader, llama_cpp_parameters]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/2065051559821668354.json, 视频生成/图生视频/2067049648237400065.json, 视频生成/图生视频/2068183647156527106.json]
source: knowledge_consolidation
---

# image_to_image_video_lora_sampler_13

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/图生视频/2065051559821668354.json、视频生成/图生视频/2067049648237400065.json、视频生成/图生视频/2068183647156527106.json）

- **类型**：Image To Image
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：76%

## 共有节点

全部 3 个 workflow 都包含：
- `AdvancedLivePortrait`
- `AutoCropFaces`
- `CLIPLoader`
- `CLIPVisionLoader`
- `CR Prompt Text`
- `ConditioningZeroOut`
- `ExpressionEditor`
- `FantasyPortraitFaceDetector`
- `FantasyPortraitModelLoader`
- `Float`
- `FluxKontextImageScale`
- `GetImageSizeAndCount`
- `GetNode`
- `Image Comparer (rgthree)`
- `ImageConcanate`
- `ImageConcatMulti`
- `ImageRemoveAlpha_UTK`
- `ImageResizeKJv2`
- `Int`
- `JWInteger`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MaskPreview+`
- `ModelSamplingAuraFlow`
- `OnnxDetectionModelLoader`
- `PainterFluxImageEdit`
- `PixelSmileConditioning`
- `PoseAndFaceDetection`
- `PreviewAny`
- `PreviewImage`
- `RMBG`
- `ReplaceText`
- `SDPoseOODLoader`
- `SDPoseOODProcessor`
- `SaveImage`
- `SetNode`
- `SolidMask`
- `Text`
- `TextEncodeQwenImageEditPlus`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `VHS_VideoInfo`
- `WanVideoAddFantasyPortrait`
- `WanVideoAnimateEmbeds`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoDecode`
- `WanVideoImageToVideoEncode`
- `WanVideoLoraSelect`
- `WanVideoLoraSelectMulti`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoTextEncodeCached`
- `WanVideoTorchCompileSettings`
- `WanVideoVAELoader`
- `YOLOModelLoader`
- `easy ifElse`
- `easy isMaskEmpty`
- `easy showAnything`
- `llama_cpp_instruct_adv`
- `llama_cpp_model_loader`
- `llama_cpp_parameters`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 8 | 3 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | res_multistep | - | 3 | 100% |
| 调度器 | simple | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 9/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 8，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 res_multistep，3 个样本，一致性 100%
- 调度器 最常用 simple，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 高发问题（9/3 个样本）：Steps较低可能导致细节不足

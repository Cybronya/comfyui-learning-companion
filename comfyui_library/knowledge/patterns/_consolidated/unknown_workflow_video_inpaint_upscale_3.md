---
name: unknown_workflow_video_inpaint_upscale_3
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.856
common_nodes: [AddMask, CLIPTextEncode, CLIPVisionLoader, CR Text, DWPreprocessor, DualCLIPLoader, FaceMaskFromPoseKeypoints, FluxGuidance, GetImageSize+, GetNode, ImageConcanate, ImageCrop+, ImageCropByMaskAndResize, ImageResizeKJ, ImageResizeKJv2, ImageToMask, ImageUpscaleWithModel, ImpactInt, InpaintModelConditioning, JWInteger, KSampler, LayerMask: BiRefNetUltraV2, LayerMask: LoadBiRefNetModelV2, LayerMask: MaskGrow, LayerMask: ObjectDetectorYOLO8, LayerMask: PersonMaskUltra V2, LayerMask: SAM2Ultra, LayerStyle: ColorOverlay V2, LayerUtility: ColorImage V2, LayerUtility: CropByMask, LoadImage, LoraLoaderModelOnly, Mask Threshold Region, MaskPreview+, MaskToImage, PixelPerfectResolution, PreviewImage, PrimitiveStringMultiline, RHHiddenNodes, ReduxAdvanced, SetNode, SimpleMath+, StyleModelLoader, SubtractMask, Switch any [Crystools], TeaCache, UNETLoader, UpscaleModelLoader, VAEDecode, VAELoader, VHS_LoadVideo, VHS_VideoCombine, VHS_VideoInfo, WanVideoAnimateEmbeds, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncodeCached, WanVideoVAELoader, easy cleanGpuUsed]
problems: []
missing: []
members: [视频生成/图生视频/1975404266829557762.json, 视频生成/图生视频/1975527114818629634.json]
source: knowledge_consolidation
---

# unknown_workflow_video_inpaint_upscale_3

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/1975404266829557762.json、视频生成/图生视频/1975527114818629634.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：86%

## 共有节点

全部 2 个 workflow 都包含：
- `AddMask`
- `CLIPTextEncode`
- `CLIPVisionLoader`
- `CR Text`
- `DWPreprocessor`
- `DualCLIPLoader`
- `FaceMaskFromPoseKeypoints`
- `FluxGuidance`
- `GetImageSize+`
- `GetNode`
- `ImageConcanate`
- `ImageCrop+`
- `ImageCropByMaskAndResize`
- `ImageResizeKJ`
- `ImageResizeKJv2`
- `ImageToMask`
- `ImageUpscaleWithModel`
- `ImpactInt`
- `InpaintModelConditioning`
- `JWInteger`
- `KSampler`
- `LayerMask: BiRefNetUltraV2`
- `LayerMask: LoadBiRefNetModelV2`
- `LayerMask: MaskGrow`
- `LayerMask: ObjectDetectorYOLO8`
- `LayerMask: PersonMaskUltra V2`
- `LayerMask: SAM2Ultra`
- `LayerStyle: ColorOverlay V2`
- `LayerUtility: ColorImage V2`
- `LayerUtility: CropByMask`
- `LoadImage`
- `LoraLoaderModelOnly`
- `Mask Threshold Region`
- `MaskPreview+`
- `MaskToImage`
- `PixelPerfectResolution`
- `PreviewImage`
- `PrimitiveStringMultiline`
- `RHHiddenNodes`
- `ReduxAdvanced`
- `SetNode`
- `SimpleMath+`
- `StyleModelLoader`
- `SubtractMask`
- `Switch any [Crystools]`
- `TeaCache`
- `UNETLoader`
- `UpscaleModelLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `VHS_VideoInfo`
- `WanVideoAnimateEmbeds`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoDecode`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoTextEncodeCached`
- `WanVideoVAELoader`
- `easy cleanGpuUsed`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 25 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 1.5 | - | 2 | 100% |
| 采样算法 | euler | - | 2 | 100% |
| 调度器 | normal | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 25，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1.5，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，2 个样本，一致性 100%
- 调度器 最常用 normal，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参

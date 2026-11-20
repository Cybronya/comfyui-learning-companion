---
name: unknown_workflow_controlnet_video_upscale_4
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.556
common_nodes: [Any Switch (rgthree), BlockifyMask, CLIPVisionLoader, CR Prompt Text, DWPreprocessor, Display Int (rgthree), DownloadAndLoadSAM2Model, DrawMaskOnImage, EmptyImage, FaceMaskFromPoseKeypoints, Fast Bypasser (rgthree), Fast Groups Bypasser (rgthree), Fast Muter (rgthree), Get resolution [Crystools], GetImageSizeAndCount, GetNode, GrowMask, ImageConcatMulti, ImageCropByMaskAndResize, ImageResizeKJv2, ImageUpscaleWithModelBatched, ImpactInt, LayerMask: LoadSegmentAnythingModels, LayerMask: SegmentAnythingUltra V3, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, Mute / Bypass Repeater (rgthree), PixelPerfectResolution, PointsEditor, PreviewAny, PreviewImage, PrimitiveStringMultiline, RIFE VFI, RepeatImageBatch, Sam2Segmentation, Seed (rgthree), SetNode, Upscale Model Loader, VHS_LoadVideo, VHS_VideoCombine, WanVideoAnimateEmbeds, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoContextOptions, WanVideoDecode, WanVideoEncode, WanVideoLoraSelectMulti, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncodeCached, WanVideoUni3C_ControlnetLoader, WanVideoUni3C_embeds, WanVideoVAELoader, easy compare, easy ifElse, easy imageCount]
problems: []
missing: []
members: [平台全量/视频换衣_1980654820577202177.json, 视频生成/图生视频/视频换衣-邻家AI大女孩_2041747126299926529.json]
source: knowledge_consolidation
---

# unknown_workflow_controlnet_video_upscale_4

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（平台全量/视频换衣_1980654820577202177.json、视频生成/图生视频/视频换衣-邻家AI大女孩_2041747126299926529.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：56%

## 共有节点

全部 2 个 workflow 都包含：
- `Any Switch (rgthree)`
- `BlockifyMask`
- `CLIPVisionLoader`
- `CR Prompt Text`
- `DWPreprocessor`
- `Display Int (rgthree)`
- `DownloadAndLoadSAM2Model`
- `DrawMaskOnImage`
- `EmptyImage`
- `FaceMaskFromPoseKeypoints`
- `Fast Bypasser (rgthree)`
- `Fast Groups Bypasser (rgthree)`
- `Fast Muter (rgthree)`
- `Get resolution [Crystools]`
- `GetImageSizeAndCount`
- `GetNode`
- `GrowMask`
- `ImageConcatMulti`
- `ImageCropByMaskAndResize`
- `ImageResizeKJv2`
- `ImageUpscaleWithModelBatched`
- `ImpactInt`
- `LayerMask: LoadSegmentAnythingModels`
- `LayerMask: SegmentAnythingUltra V3`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `Mute / Bypass Repeater (rgthree)`
- `PixelPerfectResolution`
- `PointsEditor`
- `PreviewAny`
- `PreviewImage`
- `PrimitiveStringMultiline`
- `RIFE VFI`
- `RepeatImageBatch`
- `Sam2Segmentation`
- `Seed (rgthree)`
- `SetNode`
- `Upscale Model Loader`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `WanVideoAnimateEmbeds`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoContextOptions`
- `WanVideoDecode`
- `WanVideoEncode`
- `WanVideoLoraSelectMulti`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoTextEncodeCached`
- `WanVideoUni3C_ControlnetLoader`
- `WanVideoUni3C_embeds`
- `WanVideoVAELoader`
- `easy compare`
- `easy ifElse`
- `easy imageCount`

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参

---
name: unknown_workflow_video_lora_sampler_657
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.714667
common_nodes: [BlockifyMask, CLIPVisionLoader, DWPreprocessor, DownloadAndLoadSAM2Model, DrawMaskOnImage, FaceMaskFromPoseKeypoints, GetImageSizeAndCount, INTConstant, ImageConcatMulti, ImageCropByMaskAndResize, ImageResizeKJv2, LoadImage, PixelPerfectResolution, PointsEditor, Sam2Segmentation, VHS_LoadVideo, VHS_VideoCombine, WanVideoAnimateEmbeds, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoLoraSelectMulti, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncodeCached, WanVideoTorchCompileSettings, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/1969957827202719745.json, 视频生成/图生视频/2000210160024944641.json, 视频生成/图生视频/1976173547762647041.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_657

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/图生视频/1969957827202719745.json、视频生成/图生视频/2000210160024944641.json、视频生成/图生视频/1976173547762647041.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：71%

## 共有节点

全部 3 个 workflow 都包含：
- `BlockifyMask`
- `CLIPVisionLoader`
- `DWPreprocessor`
- `DownloadAndLoadSAM2Model`
- `DrawMaskOnImage`
- `FaceMaskFromPoseKeypoints`
- `GetImageSizeAndCount`
- `INTConstant`
- `ImageConcatMulti`
- `ImageCropByMaskAndResize`
- `ImageResizeKJv2`
- `LoadImage`
- `PixelPerfectResolution`
- `PointsEditor`
- `Sam2Segmentation`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `WanVideoAnimateEmbeds`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoDecode`
- `WanVideoLoraSelectMulti`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoTextEncodeCached`
- `WanVideoTorchCompileSettings`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `AudioCropProcessUTK` —— 2/3 个有
- `GetImageRangeFromBatch` —— 2/3 个有
- `GetNode` —— 2/3 个有
- `Int` —— 2/3 个有
- `MathExpression|pysssss` —— 2/3 个有
- `PreviewImage` —— 2/3 个有
- `SetNode` —— 2/3 个有
- `Text` —— 2/3 个有
- `WanVideoContextOptions` —— 2/3 个有
- `CM_IntToFloat` —— 1/3 个有
- `CR Text` —— 1/3 个有
- `DilateErodeMask` —— 1/3 个有
- `Fast Bypasser (rgthree)` —— 1/3 个有
- `Fast Groups Bypasser (rgthree)` —— 1/3 个有
- `Float` —— 1/3 个有
- `GrowMask` —— 1/3 个有
- `GrowMaskWithBlur` —— 1/3 个有
- `ImageFromBatch` —— 1/3 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/3 个有
- `Mask Invert` —— 1/3 个有
- `MaskSmooth+` —— 1/3 个有
- `Mute / Bypass Repeater (rgthree)` —— 1/3 个有
- `OpenDWPose_JK` —— 1/3 个有
- `OpenposePreprocessor` —— 1/3 个有
- `PlaySound|pysssss` —— 1/3 个有
- `Seed_` —— 1/3 个有
- `Switch any [Crystools]` —— 1/3 个有
- `ToFloat` —— 1/3 个有
- `easy cleanGpuUsed` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

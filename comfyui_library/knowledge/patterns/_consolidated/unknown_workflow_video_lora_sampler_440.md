---
name: unknown_workflow_video_lora_sampler_440
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.668
common_nodes: [CLIPVisionLoader, DWPreprocessor, FaceMaskFromPoseKeypoints, GetImageSizeAndCount, INTConstant, ImageConcatMulti, ImageCropByMaskAndResize, ImageResizeKJv2, LoadImage, PixelPerfectResolution, VHS_LoadVideo, VHS_VideoCombine, WanVideoAnimateEmbeds, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoLoraSelectMulti, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncodeCached, WanVideoTorchCompileSettings, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/1970492700644548609.json, 视频生成/图生视频/1970100224154890241.json, 视频生成/图生视频/1970797508848984065.json, 视频生成/图生视频/1969039434375176194.json, 视频生成/图生视频/1969648359260758017.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_440

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（视频生成/图生视频/1970492700644548609.json、视频生成/图生视频/1970100224154890241.json、视频生成/图生视频/1970797508848984065.json、视频生成/图生视频/1969039434375176194.json、视频生成/图生视频/1969648359260758017.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：67%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPVisionLoader`
- `DWPreprocessor`
- `FaceMaskFromPoseKeypoints`
- `GetImageSizeAndCount`
- `INTConstant`
- `ImageConcatMulti`
- `ImageCropByMaskAndResize`
- `ImageResizeKJv2`
- `LoadImage`
- `PixelPerfectResolution`
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
- `BlockifyMask` —— 4/5 个有
- `DownloadAndLoadSAM2Model` —— 4/5 个有
- `DrawMaskOnImage` —— 4/5 个有
- `GrowMask` —— 4/5 个有
- `PointsEditor` —— 4/5 个有
- `PreviewImage` —— 4/5 个有
- `Sam2Segmentation` —— 4/5 个有
- `GetImageRangeFromBatch` —— 3/5 个有
- `GetNode` —— 3/5 个有
- `SetNode` —— 3/5 个有
- `SimpleMath+` —— 3/5 个有
- `AudioCropProcessUTK` —— 2/5 个有
- `CM_FloatToInt` —— 2/5 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/5 个有
- `LayerUtility: PurgeVRAM` —— 2/5 个有
- `PrimitiveFloat` —— 2/5 个有
- `PrimitiveStringMultiline` —— 2/5 个有
- `VHS_VideoInfo` —— 2/5 个有
- `WanVideoContextOptions` —— 2/5 个有
- `easy float` —— 2/5 个有
- `Fast Groups Muter (rgthree)` —— 1/5 个有
- `Fast Muter (rgthree)` —— 1/5 个有
- `LayerMask: BiRefNetUltraV2` —— 1/5 个有
- `LayerMask: LoadBiRefNetModelV2` —— 1/5 个有
- `LayerUtility: CropByMask V2` —— 1/5 个有
- `MaskToImage` —— 1/5 个有
- `RH_Captioner` —— 1/5 个有
- `WanVideoImageResizeToClosest` —— 1/5 个有
- `easy imageRemBg` —— 1/5 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

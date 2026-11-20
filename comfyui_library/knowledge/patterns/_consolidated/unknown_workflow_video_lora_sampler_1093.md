---
name: unknown_workflow_video_lora_sampler_1093
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.856
common_nodes: [CLIPVisionLoader, CM_FloatToInt, DWPreprocessor, FaceMaskFromPoseKeypoints, GetImageSizeAndCount, INTConstant, ImageConcatMulti, ImageCropByMaskAndResize, ImageResizeKJv2, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: PurgeVRAM, LoadImage, PixelPerfectResolution, PrimitiveFloat, PrimitiveStringMultiline, SimpleMath+, VHS_LoadVideo, VHS_VideoCombine, VHS_VideoInfo, WanVideoAnimateEmbeds, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoLoraSelectMulti, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncodeCached, WanVideoTorchCompileSettings, WanVideoVAELoader, easy float]
problems: []
missing: []
members: [视频生成/图生视频/Wan2_2_Animate_长视频动作加表情迁移工作流_1970492700644548609.json, 视频生成/图生视频/Wan2_2_Animate_长视频动画角色替换工作流_1970100224154890241.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_1093

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/Wan2_2_Animate_长视频动作加表情迁移工作流_1970492700644548609.json、视频生成/图生视频/Wan2_2_Animate_长视频动画角色替换工作流_1970100224154890241.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：86%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPVisionLoader`
- `CM_FloatToInt`
- `DWPreprocessor`
- `FaceMaskFromPoseKeypoints`
- `GetImageSizeAndCount`
- `INTConstant`
- `ImageConcatMulti`
- `ImageCropByMaskAndResize`
- `ImageResizeKJv2`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: PurgeVRAM`
- `LoadImage`
- `PixelPerfectResolution`
- `PrimitiveFloat`
- `PrimitiveStringMultiline`
- `SimpleMath+`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `VHS_VideoInfo`
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
- `easy float`

**可变部分**（部分 workflow 才有）：
- `BlockifyMask` —— 1/2 个有
- `DownloadAndLoadSAM2Model` —— 1/2 个有
- `DrawMaskOnImage` —— 1/2 个有
- `Fast Groups Muter (rgthree)` —— 1/2 个有
- `GetImageRangeFromBatch` —— 1/2 个有
- `GrowMask` —— 1/2 个有
- `MaskToImage` —— 1/2 个有
- `PointsEditor` —— 1/2 个有
- `PreviewImage` —— 1/2 个有
- `Sam2Segmentation` —— 1/2 个有
- `WanVideoImageResizeToClosest` —— 1/2 个有
- `easy imageRemBg` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参

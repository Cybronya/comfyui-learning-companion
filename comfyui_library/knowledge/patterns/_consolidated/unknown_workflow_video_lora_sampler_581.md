---
name: unknown_workflow_video_lora_sampler_581
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.78775
common_nodes: [CLIPVisionLoader, DWPreprocessor, FaceMaskFromPoseKeypoints, GetImageSizeAndCount, ImageCropByMaskAndResize, ImageResizeKJv2, LoadImage, PixelPerfectResolution, VHS_LoadVideo, VHS_VideoCombine, WanVideoAnimateEmbeds, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoLoraSelectMulti, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncodeCached, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/Wan2_2_Animate_长视频动作加表情迁移工作流_1970492700644548609.json, 视频生成/图生视频/Wan2_2_Animate_长视频动画角色替换工作流_1970100224154890241.json, 视频生成/图生视频/wan 2.2 Animate 视频动作迁移，人物替换，图生视频，脸部参考，基础用法简单演示_1970498046612172801.json, 视频生成/图生视频/wan2.2-animate动作迁移_1969648359260758017.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_581

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（视频生成/图生视频/Wan2_2_Animate_长视频动作加表情迁移工作流_1970492700644548609.json、视频生成/图生视频/Wan2_2_Animate_长视频动画角色替换工作流_1970100224154890241.json、视频生成/图生视频/wan 2.2 Animate 视频动作迁移，人物替换，图生视频，脸部参考，基础用法简单演示_1970498046612172801.json、视频生成/图生视频/wan2.2-animate动作迁移_1969648359260758017.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：79%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPVisionLoader`
- `DWPreprocessor`
- `FaceMaskFromPoseKeypoints`
- `GetImageSizeAndCount`
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
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `BlockifyMask` —— 3/4 个有
- `DownloadAndLoadSAM2Model` —— 3/4 个有
- `DrawMaskOnImage` —— 3/4 个有
- `GrowMask` —— 3/4 个有
- `INTConstant` —— 3/4 个有
- `ImageConcatMulti` —— 3/4 个有
- `PointsEditor` —— 3/4 个有
- `PreviewImage` —— 3/4 个有
- `Sam2Segmentation` —— 3/4 个有
- `SimpleMath+` —— 3/4 个有
- `WanVideoTorchCompileSettings` —— 3/4 个有
- `CM_FloatToInt` —— 2/4 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/4 个有
- `LayerUtility: PurgeVRAM` —— 2/4 个有
- `PrimitiveFloat` —— 2/4 个有
- `PrimitiveStringMultiline` —— 2/4 个有
- `SetNode` —— 2/4 个有
- `VHS_VideoInfo` —— 2/4 个有
- `easy float` —— 2/4 个有
- `Fast Groups Muter (rgthree)` —— 1/4 个有
- `Fast Muter (rgthree)` —— 1/4 个有
- `GetImageRangeFromBatch` —— 1/4 个有
- `GetImageSize+` —— 1/4 个有
- `GetNode` —— 1/4 个有
- `LayerMask: BiRefNetUltraV2` —— 1/4 个有
- `LayerMask: LoadBiRefNetModelV2` —— 1/4 个有
- `LayerUtility: CropByMask V2` —— 1/4 个有
- `MaskToImage` —— 1/4 个有
- `RH_Captioner` —— 1/4 个有
- `WanVideoImageResizeToClosest` —— 1/4 个有
- `easy imageRemBg` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

---
name: unknown_workflow_video_lora_sampler_796
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.706
common_nodes: [BlockifyMask, CLIPVisionLoader, DWPreprocessor, DownloadAndLoadSAM2Model, DrawMaskOnImage, FaceMaskFromPoseKeypoints, GetImageSizeAndCount, ImageCropByMaskAndResize, ImageResizeKJv2, LoadImage, PixelPerfectResolution, PreviewImage, Sam2Segmentation, SetNode, VHS_LoadVideo, VHS_VideoCombine, WanVideoAnimateEmbeds, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoLoraSelectMulti, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncodeCached, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/Wan-Animate动作表情迁移遮罩_1969402248658907137.json, 视频生成/图生视频/wan 2.2 Animate 视频动作迁移，人物替换，图生视频，脸部参考，基础用法简单演示_1970498046612172801.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_796

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/Wan-Animate动作表情迁移遮罩_1969402248658907137.json、视频生成/图生视频/wan 2.2 Animate 视频动作迁移，人物替换，图生视频，脸部参考，基础用法简单演示_1970498046612172801.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：71%

## 共有节点

全部 2 个 workflow 都包含：
- `BlockifyMask`
- `CLIPVisionLoader`
- `DWPreprocessor`
- `DownloadAndLoadSAM2Model`
- `DrawMaskOnImage`
- `FaceMaskFromPoseKeypoints`
- `GetImageSizeAndCount`
- `ImageCropByMaskAndResize`
- `ImageResizeKJv2`
- `LoadImage`
- `PixelPerfectResolution`
- `PreviewImage`
- `Sam2Segmentation`
- `SetNode`
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
- `DownloadAndLoadFlorence2Model` —— 1/2 个有
- `Florence2Run` —— 1/2 个有
- `Florence2toCoordinates` —— 1/2 个有
- `GetImageSize+` —— 1/2 个有
- `GetNode` —— 1/2 个有
- `GrowMask` —— 1/2 个有
- `GrowMaskWithBlur` —— 1/2 个有
- `INTConstant` —— 1/2 个有
- `InvertMask` —— 1/2 个有
- `MaskToImage` —— 1/2 个有
- `Mix Color By Mask` —— 1/2 个有
- `PointsEditor` —— 1/2 个有
- `RMBG` —— 1/2 个有
- `Switch image [Crystools]` —— 1/2 个有
- `VHS_VideoInfoLoaded` —— 1/2 个有
- `WanVideoTorchCompileSettings` —— 1/2 个有
- `easy cleanGpuUsed` —— 1/2 个有
- `easy showAnything` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参

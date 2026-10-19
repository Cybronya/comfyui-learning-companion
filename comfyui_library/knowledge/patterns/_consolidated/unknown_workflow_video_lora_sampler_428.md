---
name: unknown_workflow_video_lora_sampler_428
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.6078
common_nodes: [BlockifyMask, CLIPVisionLoader, DWPreprocessor, DownloadAndLoadSAM2Model, DrawMaskOnImage, FaceMaskFromPoseKeypoints, ImageCropByMaskAndResize, ImageResizeKJv2, LoadImage, PixelPerfectResolution, Sam2Segmentation, SetNode, VHS_LoadVideo, VHS_VideoCombine, WanVideoAnimateEmbeds, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoLoraSelectMulti, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncodeCached, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/1969402248658907137.json, 视频生成/图生视频/1970498046612172801.json, 视频生成/图生视频/1970004050341208065.json, 视频生成/文生视频/1969435322595635201.json, 视频生成/文生视频/Wan-Animate角色替换 (Character Replacement)_2072999562299875328.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_428

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（视频生成/图生视频/1969402248658907137.json、视频生成/图生视频/1970498046612172801.json、视频生成/图生视频/1970004050341208065.json、视频生成/文生视频/1969435322595635201.json、视频生成/文生视频/Wan-Animate角色替换 (Character Replacement)_2072999562299875328.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：61%

## 共有节点

全部 5 个 workflow 都包含：
- `BlockifyMask`
- `CLIPVisionLoader`
- `DWPreprocessor`
- `DownloadAndLoadSAM2Model`
- `DrawMaskOnImage`
- `FaceMaskFromPoseKeypoints`
- `ImageCropByMaskAndResize`
- `ImageResizeKJv2`
- `LoadImage`
- `PixelPerfectResolution`
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
- `GetImageSizeAndCount` —— 4/5 个有
- `GetNode` —— 4/5 个有
- `GrowMask` —— 4/5 个有
- `INTConstant` —— 4/5 个有
- `PointsEditor` —— 4/5 个有
- `WanVideoTorchCompileSettings` —— 4/5 个有
- `easy showAnything` —— 4/5 个有
- `Fast Groups Bypasser (rgthree)` —— 3/5 个有
- `GetImageSize` —— 3/5 个有
- `WanVideoContextOptions` —— 3/5 个有
- `ImageConcatMulti` —— 2/5 个有
- `PreviewImage` —— 2/5 个有
- `DownloadAndLoadFlorence2Model` —— 1/5 个有
- `Florence2Run` —— 1/5 个有
- `Florence2toCoordinates` —— 1/5 个有
- `GetImageSize+` —— 1/5 个有
- `GrowMaskWithBlur` —— 1/5 个有
- `InvertMask` —— 1/5 个有
- `MaskToImage` —— 1/5 个有
- `Mix Color By Mask` —— 1/5 个有
- `RMBG` —— 1/5 个有
- `Switch image [Crystools]` —— 1/5 个有
- `VHS_VideoInfoLoaded` —— 1/5 个有
- `easy cleanGpuUsed` —— 1/5 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

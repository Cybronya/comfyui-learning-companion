---
name: unknown_workflow_video_lora_sampler_88
type: Unknown Workflow
frequency: 16
level: moderate
coverage: 0.54
common_nodes: [BlockifyMask, CLIPVisionLoader, DWPreprocessor, DownloadAndLoadSAM2Model, DrawMaskOnImage, FaceMaskFromPoseKeypoints, GetImageSizeAndCount, GetNode, GrowMask, ImageConcatMulti, ImageCropByMaskAndResize, ImageResizeKJv2, LoadImage, PixelPerfectResolution, PointsEditor, Sam2Segmentation, SetNode, VHS_LoadVideo, VHS_VideoCombine, WanVideoAnimateEmbeds, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoLoraSelectMulti, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncodeCached, WanVideoTorchCompileSettings, WanVideoVAELoader]
problems: []
missing: [LayerUtility: ImageScaleByAspectRatio V2, SimpleMath+, CR Prompt Text]
members: [视频生成/图生视频/1969341000269373441.json, 视频生成/图生视频/1969352799354056706.json, 视频生成/图生视频/1969219198985662465.json, 视频生成/图生视频/1969110399318716418.json, 视频生成/图生视频/2073212185333026818.json, 视频生成/图生视频/1969703078859579394.json, 视频生成/图生视频/1969116607094157313.json, 视频生成/图生视频/2073212149740163073.json, 视频生成/图生视频/1981706242731196418.json, 视频生成/图生视频/1970283537297514497.json, 视频生成/图生视频/2059310361421115394.json, 视频生成/图生视频/2044021235868241922.json, 视频生成/图生视频/1970399426625892354.json, 视频生成/文生视频/1970311265270853633.json, 视频生成/文生视频/1969355024180649986.json, 视频生成/文生视频/1969358943149563905.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_88

> 由 `engine/knowledge_consolidation` 从 16 个 workflow 归纳得出（视频生成/图生视频/1969341000269373441.json、视频生成/图生视频/1969352799354056706.json、视频生成/图生视频/1969219198985662465.json、视频生成/图生视频/1969110399318716418.json、视频生成/图生视频/2073212185333026818.json…）

- **类型**：Unknown Workflow
- **样本数**：16
- **可信度**：中等可信
- **平均知识覆盖**：54%

## 共有节点

全部 16 个 workflow 都包含：
- `BlockifyMask`
- `CLIPVisionLoader`
- `DWPreprocessor`
- `DownloadAndLoadSAM2Model`
- `DrawMaskOnImage`
- `FaceMaskFromPoseKeypoints`
- `GetImageSizeAndCount`
- `GetNode`
- `GrowMask`
- `ImageConcatMulti`
- `ImageCropByMaskAndResize`
- `ImageResizeKJv2`
- `LoadImage`
- `PixelPerfectResolution`
- `PointsEditor`
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
- `WanVideoTorchCompileSettings`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `WanVideoContextOptions` —— 12/16 个有
- `JWInteger` —— 11/16 个有
- `CR Prompt Text` —— 10/16 个有
- `WanVideoEncode` —— 8/16 个有
- `WanVideoUni3C_ControlnetLoader` —— 8/16 个有
- `WanVideoUni3C_embeds` —— 8/16 个有
- `INTConstant` —— 5/16 个有
- `LayerUtility: PurgeVRAM` —— 2/16 个有
- `AudioCrop` —— 1/16 个有
- `AudioSeparation` —— 1/16 个有
- `Bjornulf_ShowInt` —— 1/16 个有
- `DownloadAndLoadWav2VecModel` —— 1/16 个有
- `ImageGetSize` —— 1/16 个有
- `ImageListToImageBatch` —— 1/16 个有
- `ImageResize` —— 1/16 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/16 个有
- `MultiTalkModelLoader` —— 1/16 个有
- `MultiTalkWav2VecEmbeds` —— 1/16 个有
- `PreviewAny` —— 1/16 个有
- `ResizeLongestToNode` —— 1/16 个有
- `SDVN Image Repeat` —— 1/16 个有
- `SimpleMath+` —— 1/16 个有
- `WanVideoCombineEmbeds` —— 1/16 个有
- `WanVideoImageToVideoMultiTalk` —— 1/16 个有
- `easy cleanGpuUsed` —— 1/16 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 这些节点还没有知识卡，系统对它们的理解有限：LayerUtility: ImageScaleByAspectRatio V2、SimpleMath+、CR Prompt Text

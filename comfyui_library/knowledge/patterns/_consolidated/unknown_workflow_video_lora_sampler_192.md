---
name: unknown_workflow_video_lora_sampler_192
type: Unknown Workflow
frequency: 10
level: moderate
coverage: 0.5425
common_nodes: [BlockifyMask, CLIPVisionLoader, DrawMaskOnImage, FaceMaskFromPoseKeypoints, GetImageSizeAndCount, GetNode, GrowMask, INTConstant, ImageConcatMulti, ImageCropByMaskAndResize, ImageResizeKJv2, LoadImage, SetNode, VHS_LoadVideo, VHS_VideoCombine, WanVideoAnimateEmbeds, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoLoraSelectMulti, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/1969709240275378178.json, 视频生成/图生视频/1969437139119337473.json, 视频生成/图生视频/2017571137424723969.json, 视频生成/图生视频/1973029204331728897.json, 视频生成/图生视频/2042478976223940610.json, 视频生成/图生视频/2042488839909937154.json, 视频生成/图生视频/2044301999423889409.json, 视频生成/图生视频/2047561888975822849.json, 视频生成/图生视频/1971421860208558082.json, 视频生成/图生视频/1969703350885380098.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_192

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（视频生成/图生视频/1969709240275378178.json、视频生成/图生视频/1969437139119337473.json、视频生成/图生视频/2017571137424723969.json、视频生成/图生视频/1973029204331728897.json、视频生成/图生视频/2042478976223940610.json…）

- **类型**：Unknown Workflow
- **样本数**：10
- **可信度**：中等可信
- **平均知识覆盖**：54%

## 共有节点

全部 10 个 workflow 都包含：
- `BlockifyMask`
- `CLIPVisionLoader`
- `DrawMaskOnImage`
- `FaceMaskFromPoseKeypoints`
- `GetImageSizeAndCount`
- `GetNode`
- `GrowMask`
- `INTConstant`
- `ImageConcatMulti`
- `ImageCropByMaskAndResize`
- `ImageResizeKJv2`
- `LoadImage`
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
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `DWPreprocessor` —— 9/10 个有
- `DownloadAndLoadSAM2Model` —— 9/10 个有
- `PixelPerfectResolution` —— 9/10 个有
- `PointsEditor` —— 9/10 个有
- `Sam2Segmentation` —— 9/10 个有
- `WanVideoTorchCompileSettings` —— 9/10 个有
- `WanVideoTextEncodeCached` —— 8/10 个有
- `WanVideoContextOptions` —— 7/10 个有
- `AudioCropProcessUTK` —— 5/10 个有
- `GetImageRangeFromBatch` —— 5/10 个有
- `PreviewImage` —— 5/10 个有
- `CLIPLoader` —— 2/10 个有
- `CLIPTextEncode` —— 2/10 个有
- `WanVideoTextEmbedBridge` —— 2/10 个有
- `easy int` —— 2/10 个有
- `Fast Groups Bypasser (rgthree)` —— 1/10 个有
- `GroundingDinoModelLoader_SDPose` —— 1/10 个有
- `InspyrenetRembgAdvanced` —— 1/10 个有
- `MathExpression|pysssss` —— 1/10 个有
- `PreviewAnimation` —— 1/10 个有
- `PrimitiveStringMultiline` —— 1/10 个有
- `RIFEInterpolation` —— 1/10 个有
- `SDPoseOODLoader` —— 1/10 个有
- `SDPoseOODProcessor` —— 1/10 个有
- `UNETLoader` —— 1/10 个有
- `UltimateSDUpscaleNoUpscale` —— 1/10 个有
- `VAELoader` —— 1/10 个有
- `YOLOModelLoader` —— 1/10 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

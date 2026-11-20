---
name: unknown_workflow_video_lora_sampler_992
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.4085
common_nodes: [CLIPVisionLoader, DWPreprocessor, DrawViTPose, FaceMaskFromPoseKeypoints, FancyTimerNode, Fast Groups Bypasser (rgthree), GetImageSizeAndCount, GetNode, ImageConcatMulti, ImageCropByMaskAndResize, ImageResizeKJv2, JWInteger, LoadImage, OnnxDetectionModelLoader, OpenposePreprocessor, PixelPerfectResolution, PoseAndFaceDetection, SDPoseOODLoader, SDPoseOODProcessor, SetNode, SimpleMath+, VHS_LoadVideo, VHS_VideoCombine, VHS_VideoInfoLoaded, WanVideoAnimateEmbeds, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoLoraSelectMulti, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncodeCached, WanVideoTorchCompileSettings, WanVideoVAELoader]
problems: []
missing: []
members: [平台全量/人物替换+对口型_2004791778450567170.json, 视频生成/图生视频/影视动作迁移_2030257978057695233.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_992

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（平台全量/人物替换+对口型_2004791778450567170.json、视频生成/图生视频/影视动作迁移_2030257978057695233.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：41%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPVisionLoader`
- `DWPreprocessor`
- `DrawViTPose`
- `FaceMaskFromPoseKeypoints`
- `FancyTimerNode`
- `Fast Groups Bypasser (rgthree)`
- `GetImageSizeAndCount`
- `GetNode`
- `ImageConcatMulti`
- `ImageCropByMaskAndResize`
- `ImageResizeKJv2`
- `JWInteger`
- `LoadImage`
- `OnnxDetectionModelLoader`
- `OpenposePreprocessor`
- `PixelPerfectResolution`
- `PoseAndFaceDetection`
- `SDPoseOODLoader`
- `SDPoseOODProcessor`
- `SetNode`
- `SimpleMath+`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `VHS_VideoInfoLoaded`
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
- `BlockifyMask` —— 1/2 个有
- `DrawMaskOnImage` —— 1/2 个有
- `FastUnsharpSharpen` —— 1/2 个有
- `GrowMask` —— 1/2 个有
- `ImageBlend` —— 1/2 个有
- `ImageFromBatch` —— 1/2 个有
- `Label (rgthree)` —— 1/2 个有
- `PointsEditor` —— 1/2 个有
- `PreviewImage` —— 1/2 个有
- `PrimitiveInt` —— 1/2 个有
- `RHHiddenNodes` —— 1/2 个有
- `SaveImage` —— 1/2 个有
- `SeCModelLoader` —— 1/2 个有
- `SeCVideoSegmentation` —— 1/2 个有
- `YOLOModelLoader` —— 1/2 个有
- `easy framesEditor` —— 1/2 个有
- `easy seed` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参

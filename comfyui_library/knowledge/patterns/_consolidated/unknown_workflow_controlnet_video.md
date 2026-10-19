---
name: unknown_workflow_controlnet_video
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.8645
common_nodes: [CLIPVisionLoader, ConvertOpenPoseKeypointsToDWPose, DWPreprocessor, DownloadAndLoadNLFModel, GetImageSize, ImageResizeKJv2, LoadImage, NLFPredict, OnnxDetectionModelLoader, PoseDetectionVitPoseToDWPose, PrimitiveInt, PrimitiveStringMultiline, RenderNLFPoses, SaveImage, SaveVideoRGBA, SimpleMathDual+, VHS_LoadVideo, VHS_VideoInfoLoaded, WanVideoContextOptions, WanVideoEncode, WanVideoTextEncode, WanVideoUni3C_ControlnetLoader, WanVideoUni3C_embeds, easy blocker, easy cleanGpuUsed, easy compare, easy ifElse, easy int, easy seed, workflow>Scail embeds, workflow>Wan2.1采样器]
problems: []
missing: []
members: [视频生成/图生视频/2003449655788748801.json, 视频生成/图生视频/2009862240601645057.json]
source: knowledge_consolidation
---

# unknown_workflow_controlnet_video

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/2003449655788748801.json、视频生成/图生视频/2009862240601645057.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：86%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPVisionLoader`
- `ConvertOpenPoseKeypointsToDWPose`
- `DWPreprocessor`
- `DownloadAndLoadNLFModel`
- `GetImageSize`
- `ImageResizeKJv2`
- `LoadImage`
- `NLFPredict`
- `OnnxDetectionModelLoader`
- `PoseDetectionVitPoseToDWPose`
- `PrimitiveInt`
- `PrimitiveStringMultiline`
- `RenderNLFPoses`
- `SaveImage`
- `SaveVideoRGBA`
- `SimpleMathDual+`
- `VHS_LoadVideo`
- `VHS_VideoInfoLoaded`
- `WanVideoContextOptions`
- `WanVideoEncode`
- `WanVideoTextEncode`
- `WanVideoUni3C_ControlnetLoader`
- `WanVideoUni3C_embeds`
- `easy blocker`
- `easy cleanGpuUsed`
- `easy compare`
- `easy ifElse`
- `easy int`
- `easy seed`
- `workflow>Scail embeds`
- `workflow>Wan2.1采样器`

**可变部分**（部分 workflow 才有）：
- `INTConstant` —— 1/2 个有
- `LoadWanVideoT5TextEncoder` —— 1/2 个有
- `MathExpression|pysssss` —— 1/2 个有
- `VHS_VideoCombine` —— 1/2 个有
- `WanVideoBlockSwap` —— 1/2 个有
- `WanVideoLoraSelect` —— 1/2 个有
- `WanVideoModelLoader` —— 1/2 个有
- `WanVideoSetBlockSwap` —— 1/2 个有
- `WanVideoSetLoRAs` —— 1/2 个有
- `WanVideoTorchCompileSettings` —— 1/2 个有
- `WanVideoVAELoader` —— 1/2 个有
- `easy boolean` —— 1/2 个有
- `workflow>Wan2.1模型加载器` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参

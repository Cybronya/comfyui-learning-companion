---
name: unknown_workflow_video_lora_sampler_860
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.376
common_nodes: [BlockifyMask, CLIPVisionLoader, DrawMaskOnImage, Fast Groups Bypasser (rgthree), GetImageSizeAndCount, GrowMaskWithBlur, INTConstant, ImageFromBatch, ImageResizeKJv2, LoadImage, OnnxDetectionModelLoader, PointsEditor, PoseAndFaceDetection, PreviewImage, PrimitiveInt, SeCModelLoader, SeCVideoSegmentation, VHS_LoadVideo, VHS_VideoCombine, WanVideoAnimateEmbeds, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoLoraSelectMulti, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncodeCached, WanVideoTorchCompileSettings, WanVideoVAELoader, easy int, easy showAnything]
problems: []
missing: []
members: [视频生成/图生视频/【前瞻预览】Wan 2.2 animate究极形态 暴力骨骼动捕SDPose+kj循环+Sec遮罩_1985641855952068610.json, 视频生成/图生视频/无线时长视频换人_2001302724798971906.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_860

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/【前瞻预览】Wan 2.2 animate究极形态 暴力骨骼动捕SDPose+kj循环+Sec遮罩_1985641855952068610.json、视频生成/图生视频/无线时长视频换人_2001302724798971906.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：38%

## 共有节点

全部 2 个 workflow 都包含：
- `BlockifyMask`
- `CLIPVisionLoader`
- `DrawMaskOnImage`
- `Fast Groups Bypasser (rgthree)`
- `GetImageSizeAndCount`
- `GrowMaskWithBlur`
- `INTConstant`
- `ImageFromBatch`
- `ImageResizeKJv2`
- `LoadImage`
- `OnnxDetectionModelLoader`
- `PointsEditor`
- `PoseAndFaceDetection`
- `PreviewImage`
- `PrimitiveInt`
- `SeCModelLoader`
- `SeCVideoSegmentation`
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
- `easy int`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `DrawViTPose` —— 1/2 个有
- `GroundingDinoModelLoader_SDPose` —— 1/2 个有
- `ImageCompositeMasked` —— 1/2 个有
- `InvertMask` —— 1/2 个有
- `LayerUtility: TextBox` —— 1/2 个有
- `PlaySound|pysssss` —— 1/2 个有
- `SDPoseOODLoader` —— 1/2 个有
- `SDPoseOODProcessor` —— 1/2 个有
- `SaveImage` —— 1/2 个有
- `SaveText` —— 1/2 个有
- `YOLOModelLoader` —— 1/2 个有
- `easy imageRemBg` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参

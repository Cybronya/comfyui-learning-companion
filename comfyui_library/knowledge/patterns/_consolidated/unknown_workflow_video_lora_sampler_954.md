---
name: unknown_workflow_video_lora_sampler_954
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.6365
common_nodes: [CLIPVisionLoader, Fast Groups Bypasser (rgthree), Float, GetImageSize+, GetNode, INTConstant, ImageResizeKJv2, LoadImage, OnnxDetectionModelLoader, PoseDetectionOneToAllAnimation, PreviewImage, SetNode, VHS_LoadVideo, VHS_VideoCombine, WanVideoAnimateEmbeds, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoLoraSelectMulti, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncodeCached, WanVideoTorchCompileSettings, WanVideoVAELoader, easy showAnything]
problems: []
missing: []
members: [视频生成/文生视频/Wan-Animate视频风格化_1998364370491047938.json, 视频生成/文生视频/kj新Pose Detection + Wan-Animate_1998289350926458882.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_954

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/文生视频/Wan-Animate视频风格化_1998364370491047938.json、视频生成/文生视频/kj新Pose Detection + Wan-Animate_1998289350926458882.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：64%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPVisionLoader`
- `Fast Groups Bypasser (rgthree)`
- `Float`
- `GetImageSize+`
- `GetNode`
- `INTConstant`
- `ImageResizeKJv2`
- `LoadImage`
- `OnnxDetectionModelLoader`
- `PoseDetectionOneToAllAnimation`
- `PreviewImage`
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
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `DWPreprocessor` —— 1/2 个有
- `PointsEditor` —— 1/2 个有
- `SDPoseOODLoader` —— 1/2 个有
- `SDPoseOODProcessor` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参

---
name: unknown_workflow_video_lora_sampler_825
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.678
common_nodes: [CLIPVisionLoader, DWPreprocessor, FaceMaskFromPoseKeypoints, GetNode, ImageConcatMulti, ImageCropByMaskAndResize, ImageResizeKJv2, LoadImage, SetNode, VHS_LoadVideo, VHS_VideoCombine, WanVideoAnimateEmbeds, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoLoraSelectMulti, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoTextEncodeCached, WanVideoVAELoader, easy cleanGpuUsed]
problems: []
missing: []
members: [视频生成/图生视频/1969999696024510466.json, 视频生成/图生视频/2033057095406329858.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_825

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/1969999696024510466.json、视频生成/图生视频/2033057095406329858.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：68%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPVisionLoader`
- `DWPreprocessor`
- `FaceMaskFromPoseKeypoints`
- `GetNode`
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
- `WanVideoTextEncodeCached`
- `WanVideoVAELoader`
- `easy cleanGpuUsed`

**可变部分**（部分 workflow 才有）：
- `Anything Everywhere3` —— 1/2 个有
- `INTConstant` —— 1/2 个有
- `ImageFromBatch` —— 1/2 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/2 个有
- `MathExpression|pysssss` —— 1/2 个有
- `PixelPerfectResolution` —— 1/2 个有
- `PreviewImage` —— 1/2 个有
- `PrimitiveInt` —— 1/2 个有
- `PrimitiveStringMultiline` —— 1/2 个有
- `WanVideoSetLoRAs` —— 1/2 个有
- `WanVideoTorchCompileSettings` —— 1/2 个有
- `easy showAnything` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参

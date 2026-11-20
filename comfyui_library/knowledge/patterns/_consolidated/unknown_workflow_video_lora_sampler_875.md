---
name: unknown_workflow_video_lora_sampler_875
type: Unknown Workflow
frequency: 2
level: weak
coverage: 1
common_nodes: [CLIPVisionLoader, DWPreprocessor, FaceMaskFromPoseKeypoints, GetImageSizeAndCount, ImageCropByMaskAndResize, ImageFromBatch, ImageResizeKJv2, Int, JWInteger, LoadImage, MathExpression|pysssss, Note Plus (mtb), PixelPerfectResolution, PlaySound|pysssss, VHS_LoadVideo, VHS_VideoCombine, WanVideoAnimateEmbeds, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoLoraSelectMulti, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncodeCached, WanVideoVAELoader, easy convertAnything, easy positive]
problems: []
missing: []
members: [视频生成/图生视频/SP503-表情迁移（wan2.2 Animate）加速版视频表情迁移_1969386195249733634.json, 视频生成/图生视频/SP504-视频换装换脸（wan2.2 Animate）_1970147620683476994.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_875

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/SP503-表情迁移（wan2.2 Animate）加速版视频表情迁移_1969386195249733634.json、视频生成/图生视频/SP504-视频换装换脸（wan2.2 Animate）_1970147620683476994.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：100%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPVisionLoader`
- `DWPreprocessor`
- `FaceMaskFromPoseKeypoints`
- `GetImageSizeAndCount`
- `ImageCropByMaskAndResize`
- `ImageFromBatch`
- `ImageResizeKJv2`
- `Int`
- `JWInteger`
- `LoadImage`
- `MathExpression|pysssss`
- `Note Plus (mtb)`
- `PixelPerfectResolution`
- `PlaySound|pysssss`
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
- `easy convertAnything`
- `easy positive`

**可变部分**（部分 workflow 才有）：
- `BlockifyMask` —— 1/2 个有
- `DrawMaskOnImage` —— 1/2 个有
- `GrowMask` —— 1/2 个有
- `LayerMask: SegformerClothesPipelineLoader` —— 1/2 个有
- `LayerMask: SegformerUltraV2` —— 1/2 个有
- `WanVideoTorchCompileSettings` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参

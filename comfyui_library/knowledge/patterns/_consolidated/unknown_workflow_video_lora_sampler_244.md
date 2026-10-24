---
name: unknown_workflow_video_lora_sampler_244
type: Unknown Workflow
frequency: 8
level: moderate
coverage: 0.672625
common_nodes: [CLIPVisionLoader, DWPreprocessor, FaceMaskFromPoseKeypoints, ImageCropByMaskAndResize, ImageResizeKJv2, JWInteger, LoadImage, PixelPerfectResolution, VHS_LoadVideo, VHS_VideoCombine, WanVideoAnimateEmbeds, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoLoraSelectMulti, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncodeCached, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/Best_Wan2.2_图片跳舞指定动作_1973849425091104769.json, 视频生成/图生视频/SP503-表情迁移（wan2.2 Animate）加速版视频表情迁移_1969386195249733634.json, 视频生成/图生视频/SP504-视频换装换脸（wan2.2 Animate）_1970147620683476994.json, 视频生成/图生视频/WAN2.2Animate美女图片跳舞工作流【动作，表情迁移】_1971382412112510978.json, 视频生成/图生视频/Wan Animate2.2动作迁移Move加速版V1_1969195120677580801.json, 视频生成/图生视频/最强视频换装+Animate+Wan2.2_1985660962449629185.json, 视频生成/图生视频/视频换装 Animate Wan2.2_1976261739643838466.json, 视频生成/文生视频/Animate+Wan2.2 视频换装 模特服装更换_1970644180198453250.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_244

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（视频生成/图生视频/Best_Wan2.2_图片跳舞指定动作_1973849425091104769.json、视频生成/图生视频/SP503-表情迁移（wan2.2 Animate）加速版视频表情迁移_1969386195249733634.json、视频生成/图生视频/SP504-视频换装换脸（wan2.2 Animate）_1970147620683476994.json、视频生成/图生视频/WAN2.2Animate美女图片跳舞工作流【动作，表情迁移】_1971382412112510978.json、视频生成/图生视频/Wan Animate2.2动作迁移Move加速版V1_1969195120677580801.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：中等可信
- **平均知识覆盖**：67%

## 共有节点

全部 8 个 workflow 都包含：
- `CLIPVisionLoader`
- `DWPreprocessor`
- `FaceMaskFromPoseKeypoints`
- `ImageCropByMaskAndResize`
- `ImageResizeKJv2`
- `JWInteger`
- `LoadImage`
- `PixelPerfectResolution`
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
- `GetNode` —— 6/8 个有
- `ImageConcatMulti` —— 6/8 个有
- `SetNode` —— 6/8 个有
- `VHS_VideoInfo` —— 5/8 个有
- `easy cleanGpuUsed` —— 5/8 个有
- `BlockifyMask` —— 4/8 个有
- `DrawMaskOnImage` —— 4/8 个有
- `GrowMask` —— 4/8 个有
- `LayerUtility: PurgeVRAM` —— 4/8 个有
- `GetImageSizeAndCount` —— 3/8 个有
- `LayerMask: SegformerB2ClothesUltra` —— 3/8 个有
- `ImageFromBatch` —— 2/8 个有
- `Int` —— 2/8 个有
- `MathExpression|pysssss` —— 2/8 个有
- `Note Plus (mtb)` —— 2/8 个有
- `PlaySound|pysssss` —— 2/8 个有
- `Text` —— 2/8 个有
- `WanVideoTorchCompileSettings` —— 2/8 个有
- `easy convertAnything` —— 2/8 个有
- `easy positive` —— 2/8 个有
- `Anything Everywhere` —— 1/8 个有
- `LayerMask: SegformerClothesPipelineLoader` —— 1/8 个有
- `LayerMask: SegformerUltraV2` —— 1/8 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

---
name: unknown_workflow_video_lora_sampler_277
type: Unknown Workflow
frequency: 8
level: moderate
coverage: 0.492
common_nodes: [GetImageRangeFromBatch, GetImageSizeAndCount, GetNode, INTConstant, ImageBatchExtendWithOverlap, ImageResizeKJv2, LoadImage, LoadWanVideoT5TextEncoder, OnnxDetectionModelLoader, PoseDetectionOneToAllAnimation, PreviewImage, SetNode, VHS_LoadVideo, VHS_VideoCombine, WanVideoAddOneToAllExtendEmbeds, WanVideoAddOneToAllPoseEmbeds, WanVideoAddOneToAllReferenceEmbeds, WanVideoBlockSwap, WanVideoDecode, WanVideoEmptyEmbeds, WanVideoEncode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncode, WanVideoVAELoader]
problems: []
missing: [MathExpression|pysssss, easy forLoopEnd, easy forLoopStart]
members: [视频生成/图生视频/2062171748241596417.json, 视频生成/图生视频/1998679386968743937.json, 视频生成/图生视频/1998642568097357826.json, 视频生成/图生视频/2054099257644331010.json, 视频生成/图生视频/2006242992251740162.json, 视频生成/图生视频/2000904519246639105.json, 视频生成/文生视频/1999868233400414209.json, 视频生成/文生视频/One-to-All Animation角色动画与图像姿态迁移延长流_1999029619397382145.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_277

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（视频生成/图生视频/2062171748241596417.json、视频生成/图生视频/1998679386968743937.json、视频生成/图生视频/1998642568097357826.json、视频生成/图生视频/2054099257644331010.json、视频生成/图生视频/2006242992251740162.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：中等可信
- **平均知识覆盖**：49%

## 共有节点

全部 8 个 workflow 都包含：
- `GetImageRangeFromBatch`
- `GetImageSizeAndCount`
- `GetNode`
- `INTConstant`
- `ImageBatchExtendWithOverlap`
- `ImageResizeKJv2`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `OnnxDetectionModelLoader`
- `PoseDetectionOneToAllAnimation`
- `PreviewImage`
- `SetNode`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `WanVideoAddOneToAllExtendEmbeds`
- `WanVideoAddOneToAllPoseEmbeds`
- `WanVideoAddOneToAllReferenceEmbeds`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoEmptyEmbeds`
- `WanVideoEncode`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoTextEncode`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `FloatConstant` —— 7/8 个有
- `WanVideoScheduler` —— 7/8 个有
- `MathExpression|pysssss` —— 3/8 个有
- `WanVideoTorchCompileSettings` —— 3/8 个有
- `easy forLoopEnd` —— 3/8 个有
- `easy forLoopStart` —— 3/8 个有
- `MaskPreview+` —— 2/8 个有
- `DownloadAndLoadGIMMVFIModel` —— 1/8 个有
- `GIMMVFI_interpolate` —— 1/8 个有
- `ImageConcatMulti` —— 1/8 个有
- `ImpactInt` —— 1/8 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/8 个有
- `LayerUtility: PurgeVRAM V2` —— 1/8 个有
- `Text Multiline` —— 1/8 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 这些节点还没有知识卡，系统对它们的理解有限：MathExpression|pysssss、easy forLoopEnd、easy forLoopStart

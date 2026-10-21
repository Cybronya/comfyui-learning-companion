---
name: unknown_workflow_video_lora_sampler_844
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.834
common_nodes: [BasicScheduler, CLIPLoader, CLIPTextEncode, CLIPVisionLoader, CheckpointLoaderSimple, ImageResizeKJv2, KSamplerSelect, LoadImage, LoraLoaderModelOnly, ModelSamplingSD3, PrimitiveInt, SCAIL2ScheduledLongVideoWithSAM, SCAIL2SegmentPlanBuilder, VAELoader, VHS_LoadVideo, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/scail-2视频动作迁移【small-JJ小健健】_2077275327600095233.json, 视频生成/图生视频/2071865157709557762.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_844

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/scail-2视频动作迁移【small-JJ小健健】_2077275327600095233.json、视频生成/图生视频/2071865157709557762.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：83%

## 共有节点

全部 2 个 workflow 都包含：
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `CLIPVisionLoader`
- `CheckpointLoaderSimple`
- `ImageResizeKJv2`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingSD3`
- `PrimitiveInt`
- `SCAIL2ScheduledLongVideoWithSAM`
- `SCAIL2SegmentPlanBuilder`
- `VAELoader`
- `VHS_LoadVideo`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `ComfyMathExpression` —— 1/2 个有
- `DiffusionModelLoaderKJ` —— 1/2 个有
- `DownloadAndLoadGIMMVFIModel` —— 1/2 个有
- `Fast Groups Bypasser (rgthree)` —— 1/2 个有
- `GIMMVFI_interpolate` —— 1/2 个有
- `ImageFromBatch` —— 1/2 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/2 个有
- `PrimitiveString` —— 1/2 个有
- `UNETLoader` —— 1/2 个有
- `easy cleanGpuUsed` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参

---
name: unknown_workflow_video_lora_sampler_523
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.4355
common_nodes: [BasicScheduler, CLIPLoader, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, CheckpointLoaderSimple, DiffusionModelLoaderKJ, GetNode, ImageResizeKJv2, Int, KSamplerSelect, LoadImage, LoraLoaderModelOnly, PreviewImage, SAM3_VideoTrack, SCAIL2ColoredMask, SamplerCustom, SetNode, VAEDecode, VAELoader, VHS_LoadVideo, VHS_VideoCombine, VHS_VideoInfo, WanSCAILToVideo, easy imageRemBg, easy showAnything]
problems: []
missing: []
members: [视频生成/图生视频/scall2  单人动作迁移_2069034704543764482.json, 视频生成/图生视频/scall2单人循环动作迁移_2069027789755469826.json, 视频生成/图生视频/女装带货_2074116583454236674.json, 视频生成/图生视频/数字人女装带货视频_2082802589850230786.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_523

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（视频生成/图生视频/scall2  单人动作迁移_2069034704543764482.json、视频生成/图生视频/scall2单人循环动作迁移_2069027789755469826.json、视频生成/图生视频/女装带货_2074116583454236674.json、视频生成/图生视频/数字人女装带货视频_2082802589850230786.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：44%

## 共有节点

全部 4 个 workflow 都包含：
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `CheckpointLoaderSimple`
- `DiffusionModelLoaderKJ`
- `GetNode`
- `ImageResizeKJv2`
- `Int`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PreviewImage`
- `SAM3_VideoTrack`
- `SCAIL2ColoredMask`
- `SamplerCustom`
- `SetNode`
- `VAEDecode`
- `VAELoader`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `VHS_VideoInfo`
- `WanSCAILToVideo`
- `easy imageRemBg`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `ComfyMathExpression` —— 3/4 个有
- `GetImageRangeFromBatch` —— 3/4 个有
- `easy batchAnything` —— 3/4 个有
- `easy forLoopEnd` —— 3/4 个有
- `easy forLoopStart` —— 3/4 个有
- `DF_Int_to_Float` —— 2/4 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/4 个有
- `TTResolutionSelector` —— 2/4 个有
- `SimpleMath+` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

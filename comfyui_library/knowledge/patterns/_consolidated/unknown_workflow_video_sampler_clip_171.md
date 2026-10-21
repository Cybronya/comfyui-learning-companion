---
name: unknown_workflow_video_sampler_clip_171
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.880667
common_nodes: [CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, ConditioningZeroOut, DualCLIPLoader, FramePackFindNearestBucket, FramePackSampler, ImageResize+, LoadFramePackModel, LoadImage, VAEDecodeTiled, VAEEncode, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/2005639077577846785.json, 视频生成/图生视频/1952976283438411778.json, 视频生成/图生视频/1933133286371958785.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_171

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/图生视频/2005639077577846785.json、视频生成/图生视频/1952976283438411778.json、视频生成/图生视频/1933133286371958785.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：88%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `FramePackFindNearestBucket`
- `FramePackSampler`
- `ImageResize+`
- `LoadFramePackModel`
- `LoadImage`
- `VAEDecodeTiled`
- `VAEEncode`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `GetImageSizeAndCount` —— 2/3 个有
- `PrimitiveFloat` —— 2/3 个有
- `CR Text Concatenate` —— 1/3 个有
- `FramePackTorchCompileSettings` —— 1/3 个有
- `GetNode` —— 1/3 个有
- `ImageUpscaleWithModelBatched` —— 1/3 个有
- `LayerUtility: PurgeVRAM V2` —— 1/3 个有
- `RH_Captioner` —— 1/3 个有
- `SetNode` —— 1/3 个有
- `StringConstantMultiline` —— 1/3 个有
- `UpscaleModelLoader` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

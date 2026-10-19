---
name: unknown_workflow_video_sampler_28
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.704
common_nodes: [ColorMatch, GetNode, ImageConcanate, ImageFromBatch, ImageResizeKJ, ImpactSwitch, LoadImage, PreviewImage, Primitive integer [Crystools], RHHiddenNodes, SetNode, SimpleMath+, VHS_LoadVideo, VHS_VideoCombine, WanVideoClipVisionEncode, WanVideoDecode, WanVideoEnhanceAVideo, WanVideoExperimentalArgs, WanVideoImageToVideoEncode, WanVideoSLG, WanVideoSampler, WanVideoTeaCache, WanVideoTextEncode, WanVideoUniAnimateDWPoseDetector, WanVideoUniAnimatePoseInput]
problems: []
missing: []
members: [视频生成/图生视频/1947143904128446465.json, 视频生成/图生视频/1955563973305405442.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_28

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/1947143904128446465.json、视频生成/图生视频/1955563973305405442.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：70%

## 共有节点

全部 2 个 workflow 都包含：
- `ColorMatch`
- `GetNode`
- `ImageConcanate`
- `ImageFromBatch`
- `ImageResizeKJ`
- `ImpactSwitch`
- `LoadImage`
- `PreviewImage`
- `Primitive integer [Crystools]`
- `RHHiddenNodes`
- `SetNode`
- `SimpleMath+`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `WanVideoClipVisionEncode`
- `WanVideoDecode`
- `WanVideoEnhanceAVideo`
- `WanVideoExperimentalArgs`
- `WanVideoImageToVideoEncode`
- `WanVideoSLG`
- `WanVideoSampler`
- `WanVideoTeaCache`
- `WanVideoTextEncode`
- `WanVideoUniAnimateDWPoseDetector`
- `WanVideoUniAnimatePoseInput`

**可变部分**（部分 workflow 才有）：
- `CLIPVisionLoader` —— 1/2 个有
- `LoadWanVideoT5TextEncoder` —— 1/2 个有
- `WanVideoVAELoader` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参

---
name: unknown_workflow_video_87
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.508
common_nodes: [GetNode, LayerUtility: ImageReel, LayerUtility: ImageReelComposit, PlaySound|pysssss, PreviewAny, PreviewImage, PrimitiveString, SeedVR2BlockSwap, SeedVR2ExtraArgs, SeedVR2GGUF, SetNode, StringConcatenate, VHS_LoadVideo, VHS_VideoCombine, VHS_VideoInfo, easy int]
problems: []
missing: []
members: [视频生成/图生视频/1999758543504932866.json, 视频生成/图生视频/1974856721065709570.json]
source: knowledge_consolidation
---

# unknown_workflow_video_87

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/1999758543504932866.json、视频生成/图生视频/1974856721065709570.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：51%

## 共有节点

全部 2 个 workflow 都包含：
- `GetNode`
- `LayerUtility: ImageReel`
- `LayerUtility: ImageReelComposit`
- `PlaySound|pysssss`
- `PreviewAny`
- `PreviewImage`
- `PrimitiveString`
- `SeedVR2BlockSwap`
- `SeedVR2ExtraArgs`
- `SeedVR2GGUF`
- `SetNode`
- `StringConcatenate`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `VHS_VideoInfo`
- `easy int`

**可变部分**（部分 workflow 才有）：
- `Bookmark (rgthree)` —— 1/2 个有
- `ImageResizeKJ` —— 1/2 个有
- `ImageResizeKJv2` —— 1/2 个有
- `Label (rgthree)` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参

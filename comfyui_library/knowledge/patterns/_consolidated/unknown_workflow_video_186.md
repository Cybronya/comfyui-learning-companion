---
name: unknown_workflow_video_186
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.9
common_nodes: [FlashVSRNode, Int, LayerUtility: ImageScaleByAspectRatio V2, MaxNode, MinNode, VHS_LoadVideo, VHS_VideoCombine, VHS_VideoInfoLoaded]
problems: []
missing: []
members: [平台全量/AI脑洞狮--视频高清放大修复_2071868749367570434.json, 平台全量/视频高清修复_2068703296851894273.json]
source: knowledge_consolidation
---

# unknown_workflow_video_186

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（平台全量/AI脑洞狮--视频高清放大修复_2071868749367570434.json、平台全量/视频高清修复_2068703296851894273.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：90%

## 共有节点

全部 2 个 workflow 都包含：
- `FlashVSRNode`
- `Int`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `MaxNode`
- `MinNode`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `VHS_VideoInfoLoaded`

**可变部分**（部分 workflow 才有）：
- `Fast Groups Muter (rgthree)` —— 1/2 个有
- `LoadImage` —— 1/2 个有
- `MuyeTextEditOutput` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参

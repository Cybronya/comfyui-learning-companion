---
name: unknown_workflow_video_135
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.78
common_nodes: [FlashVSRNode, Int, VHS_LoadVideo, VHS_VideoCombine, VHS_VideoInfo]
problems: []
missing: []
members: [平台全量/FlashVSR-视频放大-极速版_1981002603658088450.json, 平台全量/FlashVSR极速视频高清放大_2082720426693844994.json, 平台全量/视频放大指定放大倍数+FlashVSR_Ultra_Fast+全节点注释_2059521589053575170.json]
source: knowledge_consolidation
---

# unknown_workflow_video_135

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（平台全量/FlashVSR-视频放大-极速版_1981002603658088450.json、平台全量/FlashVSR极速视频高清放大_2082720426693844994.json、平台全量/视频放大指定放大倍数+FlashVSR_Ultra_Fast+全节点注释_2059521589053575170.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：78%

## 共有节点

全部 3 个 workflow 都包含：
- `FlashVSRNode`
- `Int`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `VHS_VideoInfo`

**可变部分**（部分 workflow 才有）：
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/3 个有
- `LoadImage` —— 2/3 个有
- `ImageConcanate` —— 1/3 个有
- `RHHiddenNodes` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

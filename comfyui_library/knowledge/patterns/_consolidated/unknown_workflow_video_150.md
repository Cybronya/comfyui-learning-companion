---
name: unknown_workflow_video_150
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.952333
common_nodes: [DownloadAndLoadGIMMVFIModel, FlashVSRNode, GIMMVFI_interpolate, VHS_LoadVideo, VHS_VideoCombine]
problems: []
missing: []
members: [平台全量/视频高清放大-极速版（seedance2.0适配）_2042100963560923138.json, 平台全量/视频高清放大-速度更快_2035625843556360194.json, 视频生成/文生视频/视频补帧+放大_2021549838894108674.json]
source: knowledge_consolidation
---

# unknown_workflow_video_150

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（平台全量/视频高清放大-极速版（seedance2.0适配）_2042100963560923138.json、平台全量/视频高清放大-速度更快_2035625843556360194.json、视频生成/文生视频/视频补帧+放大_2021549838894108674.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：95%

## 共有节点

全部 3 个 workflow 都包含：
- `DownloadAndLoadGIMMVFIModel`
- `FlashVSRNode`
- `GIMMVFI_interpolate`
- `VHS_LoadVideo`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/3 个有
- `PreviewImage` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

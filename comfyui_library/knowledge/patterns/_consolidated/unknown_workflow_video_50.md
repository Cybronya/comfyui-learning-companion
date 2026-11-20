---
name: unknown_workflow_video_50
type: Unknown Workflow
frequency: 6
level: moderate
coverage: 1
common_nodes: [VHS_LoadVideo, VHS_VideoCombine, VHS_VideoInfoLoaded]
problems: []
missing: []
members: [平台全量/DLSS5超分放大_2098077101739040770.json, 平台全量/DLSS5超分放大_2108440726576132097.json, 平台全量/DLSS5超分放大视频生成_2099332398176624641.json, 平台全量/DLSS5超分放大视频生成_2099668383385083906.json, 平台全量/DLSS5超分放大视频生成_2111070387458109441.json, 平台全量/视频缩放（自用）_2033547128051601409.json]
source: knowledge_consolidation
---

# unknown_workflow_video_50

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（平台全量/DLSS5超分放大_2098077101739040770.json、平台全量/DLSS5超分放大_2108440726576132097.json、平台全量/DLSS5超分放大视频生成_2099332398176624641.json、平台全量/DLSS5超分放大视频生成_2099668383385083906.json、平台全量/DLSS5超分放大视频生成_2111070387458109441.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：100%

## 共有节点

全部 6 个 workflow 都包含：
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `VHS_VideoInfoLoaded`

**可变部分**（部分 workflow 才有）：
- `RH_DLSS5Enhance` —— 5/6 个有
- `HAIGC_VideoResize` —— 1/6 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

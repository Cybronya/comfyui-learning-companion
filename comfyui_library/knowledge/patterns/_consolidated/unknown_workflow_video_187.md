---
name: unknown_workflow_video_187
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.9375
common_nodes: [GetVideoComponents, LoadVideo, MaskToImage, RembgByBiRefNet, VHS_VideoCombine]
problems: []
missing: []
members: [平台全量/Birefnet视频抠图工作流_1982731557792301058.json, 平台全量/视频背景转透明_2002340191396347906.json]
source: knowledge_consolidation
---

# unknown_workflow_video_187

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（平台全量/Birefnet视频抠图工作流_1982731557792301058.json、平台全量/视频背景转透明_2002340191396347906.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：94%

## 共有节点

全部 2 个 workflow 都包含：
- `GetVideoComponents`
- `LoadVideo`
- `MaskToImage`
- `RembgByBiRefNet`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `AutoDownloadBiRefNetModel` —— 1/2 个有
- `LoadRembgByBiRefNetModel` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参

---
name: unknown_workflow_video_216
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.818
common_nodes: [DeleteVideoSegmentXC, DownloadAndLoadTransNetModelXC, GetVideoComponents, Int, LoadVideo, PreviewAny, VHS_LoadVideoPath, VHS_VideoCombine, VideoConcatenatorXC]
problems: []
missing: []
members: [平台全量/分镜删除首个分镜头以及指定位置删除_1981898226540396545.json, 平台全量/分镜头识别以及指定位置删除_1982245927966654466.json]
source: knowledge_consolidation
---

# unknown_workflow_video_216

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（平台全量/分镜删除首个分镜头以及指定位置删除_1981898226540396545.json、平台全量/分镜头识别以及指定位置删除_1982245927966654466.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：82%

## 共有节点

全部 2 个 workflow 都包含：
- `DeleteVideoSegmentXC`
- `DownloadAndLoadTransNetModelXC`
- `GetVideoComponents`
- `Int`
- `LoadVideo`
- `PreviewAny`
- `VHS_LoadVideoPath`
- `VHS_VideoCombine`
- `VideoConcatenatorXC`

**可变部分**（部分 workflow 才有）：
- `TransNetV2_Run` —— 1/2 个有
- `TransNetV2_RunXC` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参

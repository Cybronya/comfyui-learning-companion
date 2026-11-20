---
name: unknown_workflow_video_143
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.615
common_nodes: [DWPreprocessor, DepthAnythingV2Preprocessor, MuyeImageBlendingMode, PreviewAny, VHS_LoadVideo, VHS_VideoCombine, VHS_VideoInfo]
problems: []
missing: []
members: [平台全量/深度视频制作-视频转深度视频_2102047280990867458.json, 平台全量/视频转深度视频_2107756043605467137.json, 视频生成/文生视频/minimax参考输入depth与openpose_2101320036567834625.json]
source: knowledge_consolidation
---

# unknown_workflow_video_143

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（平台全量/深度视频制作-视频转深度视频_2102047280990867458.json、平台全量/视频转深度视频_2107756043605467137.json、视频生成/文生视频/minimax参考输入depth与openpose_2101320036567834625.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：62%

## 共有节点

全部 3 个 workflow 都包含：
- `DWPreprocessor`
- `DepthAnythingV2Preprocessor`
- `MuyeImageBlendingMode`
- `PreviewAny`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `VHS_VideoInfo`

**可变部分**（部分 workflow 才有）：
- `GetNode` —— 2/3 个有
- `SaveImage` —— 2/3 个有
- `SetNode` —— 2/3 个有
- `孤海注释` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

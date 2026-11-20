---
name: unknown_workflow_video_188
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.65
common_nodes: [LoadImage, RH_DLSS5Enhance, RH_DLSS5FrameInterpolation, VHS_LoadVideo, VHS_VideoCombine, 忽略多组孤海]
problems: []
missing: []
members: [平台全量/DLSS5  图片+视频超分放大_2101593220928069633.json, 平台全量/NVIDIA DLSS5大力水手 高动态版120hz 超分高清放大视频超分 极致参数版+全节点注释_2099050532957671425.json]
source: knowledge_consolidation
---

# unknown_workflow_video_188

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（平台全量/DLSS5  图片+视频超分放大_2101593220928069633.json、平台全量/NVIDIA DLSS5大力水手 高动态版120hz 超分高清放大视频超分 极致参数版+全节点注释_2099050532957671425.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：65%

## 共有节点

全部 2 个 workflow 都包含：
- `LoadImage`
- `RH_DLSS5Enhance`
- `RH_DLSS5FrameInterpolation`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `忽略多组孤海`

**可变部分**（部分 workflow 才有）：
- `CR Text` —— 1/2 个有
- `SaveImage` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参

---
name: unknown_workflow_video_upscale_27
type: Unknown Workflow
frequency: 2
level: weak
coverage: 1
common_nodes: [ImageUpscaleWithModelBatched, RIFE VFI, UpscaleModelLoader, VHS_LoadVideo, VHS_VideoCombine]
problems: []
missing: []
members: [平台全量/视频修复补帧_2113441946902552577.json, 平台全量/视频高清处理_2084979827764973569.json]
source: knowledge_consolidation
---

# unknown_workflow_video_upscale_27

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（平台全量/视频修复补帧_2113441946902552577.json、平台全量/视频高清处理_2084979827764973569.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：100%

## 共有节点

全部 2 个 workflow 都包含：
- `ImageUpscaleWithModelBatched`
- `RIFE VFI`
- `UpscaleModelLoader`
- `VHS_LoadVideo`
- `VHS_VideoCombine`

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参

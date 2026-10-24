---
name: unknown_workflow_generic_1216
type: Unknown Workflow
frequency: 2
level: weak
coverage: 1
common_nodes: [Preview3D, SaveImage, Trellis2ExportMesh, Trellis2LoadModel, Trellis2MeshWithVoxelGenerator, Trellis2PostProcessAndUnWrapAndRasterizer, Trellis2SimplifyMesh]
problems: []
missing: []
members: [图片生成/图生图/ComfyUI-3D-Trellis2自动建模_2004456831420428290.json, 图片生成/图生图/Trellis2 3D_2005307477589716994.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_1216

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/ComfyUI-3D-Trellis2自动建模_2004456831420428290.json、图片生成/图生图/Trellis2 3D_2005307477589716994.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：100%

## 共有节点

全部 2 个 workflow 都包含：
- `Preview3D`
- `SaveImage`
- `Trellis2ExportMesh`
- `Trellis2LoadModel`
- `Trellis2MeshWithVoxelGenerator`
- `Trellis2PostProcessAndUnWrapAndRasterizer`
- `Trellis2SimplifyMesh`

**可变部分**（部分 workflow 才有）：
- `ImageResizeKJv2` —— 1/2 个有
- `LoadImage` —— 1/2 个有
- `Trellis2LoadImageWithTransparency` —— 1/2 个有
- `easy imageRemBg` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参

---
name: unknown_workflow_upscale_vae_57
type: Unknown Workflow
frequency: 2
level: weak
coverage: 1
common_nodes: [LoadImage, RH_RhartImageG2ImageToImage, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, easy imageRemBg]
problems: []
missing: []
members: [图片生成/图生图/详情图到白底图+高清_2065104369812590593.json, 图片生成/图生图/详情图到白底图+高清_2067519776129372161.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_vae_57

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/详情图到白底图+高清_2065104369812590593.json、图片生成/图生图/详情图到白底图+高清_2067519776129372161.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：100%

## 共有节点

全部 2 个 workflow 都包含：
- `LoadImage`
- `RH_RhartImageG2ImageToImage`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `easy imageRemBg`

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参

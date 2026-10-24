---
name: unknown_workflow_upscale_vae_56
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.778
common_nodes: [ImageScaleBy, LoadImage, PrimitiveInt, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, SimpleMath+]
problems: []
missing: []
members: [图片生成/图生图/花型设计图高清_2108474871826182146.json, 图片生成/图生图/花型高清_2111753801672773634.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_vae_56

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/花型设计图高清_2108474871826182146.json、图片生成/图生图/花型高清_2111753801672773634.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：78%

## 共有节点

全部 2 个 workflow 都包含：
- `ImageScaleBy`
- `LoadImage`
- `PrimitiveInt`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `SimpleMath+`

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参

---
name: unknown_workflow_upscale_vae_59
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.739
common_nodes: [CR Prompt Text, Comfly_api_set, INTConstant, LoadImage, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, easy showAnything]
problems: []
missing: []
members: [图片生成/文生图/13种比例gxx-image-2（5图）-支持4K（贞贞工坊分组：官方优质和Default）_2048029500130201602.json, 图片生成/文生图/顶级！全能图片G2-文生图-图生图+放大-贞贞的AI工坊_2046504582557212674.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_vae_59

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/13种比例gxx-image-2（5图）-支持4K（贞贞工坊分组：官方优质和Default）_2048029500130201602.json、图片生成/文生图/顶级！全能图片G2-文生图-图生图+放大-贞贞的AI工坊_2046504582557212674.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：74%

## 共有节点

全部 2 个 workflow 都包含：
- `CR Prompt Text`
- `Comfly_api_set`
- `INTConstant`
- `LoadImage`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `Comfly_gpt_image_2_S2A` —— 1/2 个有
- `Comfly_gpt_image_2_official_ratio` —— 1/2 个有
- `TextInputNode` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参

---
name: unknown_workflow_upscale_vae_52
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.7855
common_nodes: [LoadImage, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler]
problems: []
missing: []
members: [图片生成/图生图/快速人像表情迁移模仿_2004547165496242177.json, 图片生成/文生图/SeedVR2图片放大+高清放大+4K+8K+大分辨率+全节点注释_2057708544862023682.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_vae_52

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/快速人像表情迁移模仿_2004547165496242177.json、图片生成/文生图/SeedVR2图片放大+高清放大+4K+8K+大分辨率+全节点注释_2057708544862023682.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：79%

## 共有节点

全部 2 个 workflow 都包含：
- `LoadImage`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`

**可变部分**（部分 workflow 才有）：
- `ExpressionEditor` —— 1/2 个有
- `GetImage` —— 1/2 个有
- `RHHiddenNodes` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参

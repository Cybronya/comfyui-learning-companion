---
name: unknown_workflow_upscale_vae_4
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.707
common_nodes: [LoadImage, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler]
problems: []
missing: []
members: [图片生成/图生图/2084865194706161666.json, 图片生成/文生图/SeedVR2图片放大+高清放大+4K+8K+大分辨率+全节点注释_2057708544862023682.json, 图片生成/文生图/SeedVr2 图片放大_2020184274913202177.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_vae_4

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/2084865194706161666.json、图片生成/文生图/SeedVR2图片放大+高清放大+4K+8K+大分辨率+全节点注释_2057708544862023682.json、图片生成/文生图/SeedVr2 图片放大_2020184274913202177.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：71%

## 共有节点

全部 3 个 workflow 都包含：
- `LoadImage`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`

**可变部分**（部分 workflow 才有）：
- `PrimitiveInt` —— 2/3 个有
- `ComfyMathExpression` —— 1/3 个有
- `ComfySwitchNode` —— 1/3 个有
- `GetImageSize` —— 1/3 个有
- `RHHiddenNodes` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

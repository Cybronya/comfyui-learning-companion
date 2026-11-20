---
name: unknown_workflow_upscale_vae_66
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 1
common_nodes: [LoadImage, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler]
problems: []
missing: []
members: [图片生成/图生图/详情图到白底图+高清_2065104369812590593.json, 图片生成/图生图/详情图到白底图+高清_2067519776129372161.json, 平台全量/SeedVR2 图片4K无损高清放大_2078282399468834817.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_vae_66

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/详情图到白底图+高清_2065104369812590593.json、图片生成/图生图/详情图到白底图+高清_2067519776129372161.json、平台全量/SeedVR2 图片4K无损高清放大_2078282399468834817.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：100%

## 共有节点

全部 3 个 workflow 都包含：
- `LoadImage`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`

**可变部分**（部分 workflow 才有）：
- `RH_RhartImageG2ImageToImage` —— 2/3 个有
- `easy imageRemBg` —— 2/3 个有
- `PlaySound|pysssss` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

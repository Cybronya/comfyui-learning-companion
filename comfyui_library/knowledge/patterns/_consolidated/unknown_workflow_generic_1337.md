---
name: unknown_workflow_generic_1337
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.8375
common_nodes: [Fast Groups Bypasser (rgthree), LoadImage, RH_RhartImageG2ImageToImage, RH_RhartImageG2TextToImage, SaveImage, SeedVR2, SeedVR2BlockSwap]
problems: []
missing: []
members: [图片生成/图生图/全能图片G2-文生图_图片编辑工作流（0.1_张图）_2048687333809065986.json, 图片生成/文生图/iamge2 高清放大_2048950032338001921.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_1337

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/全能图片G2-文生图_图片编辑工作流（0.1_张图）_2048687333809065986.json、图片生成/文生图/iamge2 高清放大_2048950032338001921.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：84%

## 共有节点

全部 2 个 workflow 都包含：
- `Fast Groups Bypasser (rgthree)`
- `LoadImage`
- `RH_RhartImageG2ImageToImage`
- `RH_RhartImageG2TextToImage`
- `SaveImage`
- `SeedVR2`
- `SeedVR2BlockSwap`

**可变部分**（部分 workflow 才有）：
- `Image Comparer (rgthree)` —— 1/2 个有
- `SeedVR2ExtraArgs` —— 1/2 个有
- `Text Multiline` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参

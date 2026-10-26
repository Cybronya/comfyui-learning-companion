---
name: unknown_workflow_generic_1393
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.9775
common_nodes: [LoadImage, RH_RhartImageG2ImageToImage, RH_RhartImageV1Edit, RH_RhartImageV1OfficialEdit, RH_SeedreamV45ImageToImage, RH_SeedreamV4ImageToImage, RH_SeedreamV5LiteImageToImage, SaveImage]
problems: []
missing: []
members: [图片生成/图生图/RH-api生图合集_2047513433892986881.json, 图片生成/图生图/RH-api生图合集_2114321101349281793.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_1393

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/RH-api生图合集_2047513433892986881.json、图片生成/图生图/RH-api生图合集_2114321101349281793.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：98%

## 共有节点

全部 2 个 workflow 都包含：
- `LoadImage`
- `RH_RhartImageG2ImageToImage`
- `RH_RhartImageV1Edit`
- `RH_RhartImageV1OfficialEdit`
- `RH_SeedreamV45ImageToImage`
- `RH_SeedreamV4ImageToImage`
- `RH_SeedreamV5LiteImageToImage`
- `SaveImage`

**可变部分**（部分 workflow 才有）：
- `EmptyImage` —— 1/2 个有
- `PreviewImage` —— 1/2 个有
- `SeedVR2` —— 1/2 个有
- `SeedVR2BlockSwap` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参

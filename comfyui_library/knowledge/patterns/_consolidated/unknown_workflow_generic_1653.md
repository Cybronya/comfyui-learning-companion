---
name: unknown_workflow_generic_1653
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.8615
common_nodes: [ApplyHairRemover, ApplyHairTransfer, CropFace, ImageResize+, LoadImage, LoadStableHairRemoverModel, LoadStableHairTransferModel, SaveImage, easy cleanGpuUsed]
problems: []
missing: []
members: [图片生成/图生图/一键换发型工作流_1882394937219076097.json, 平台全量/头发迁移 StableHair_ll_1882849970465263618.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_1653

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/一键换发型工作流_1882394937219076097.json、平台全量/头发迁移 StableHair_ll_1882849970465263618.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：86%

## 共有节点

全部 2 个 workflow 都包含：
- `ApplyHairRemover`
- `ApplyHairTransfer`
- `CropFace`
- `ImageResize+`
- `LoadImage`
- `LoadStableHairRemoverModel`
- `LoadStableHairTransferModel`
- `SaveImage`
- `easy cleanGpuUsed`

**可变部分**（部分 workflow 才有）：
- `PreviewImage` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参

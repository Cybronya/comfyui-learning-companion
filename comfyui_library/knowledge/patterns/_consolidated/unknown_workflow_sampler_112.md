---
name: unknown_workflow_sampler_112
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.842
common_nodes: [Display Int (rgthree), GetImageSizeAndCount, ImageResize+, LayerUtility: ExtendCanvas, LoadImage, PreviewImage, SaveImage, StableMakeup_LoadModel, StableMakeup_Sampler, easy imageInsetCrop]
problems: []
missing: []
members: [平台全量/【丝滑化妆】喜欢哪个妆容换哪个，百搭绝绝子_1888854811956207617.json, 平台全量/人像妆容体验_1834124618973212673.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_112

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（平台全量/【丝滑化妆】喜欢哪个妆容换哪个，百搭绝绝子_1888854811956207617.json、平台全量/人像妆容体验_1834124618973212673.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：84%

## 共有节点

全部 2 个 workflow 都包含：
- `Display Int (rgthree)`
- `GetImageSizeAndCount`
- `ImageResize+`
- `LayerUtility: ExtendCanvas`
- `LoadImage`
- `PreviewImage`
- `SaveImage`
- `StableMakeup_LoadModel`
- `StableMakeup_Sampler`
- `easy imageInsetCrop`

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参

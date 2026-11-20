---
name: unknown_workflow_upscale_80
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.8055
common_nodes: [Image Comparer (rgthree), ImageScaleBy, ImageUpscaleWithModel, LoadImage, SaveImage, UpscaleModelLoader]
problems: []
missing: []
members: [平台全量/模型高清放大，不改变原图。_1918284643882438657.json, 平台全量/通过模型放大工作流（高性价比放大）_2049693690616135681.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_80

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（平台全量/模型高清放大，不改变原图。_1918284643882438657.json、平台全量/通过模型放大工作流（高性价比放大）_2049693690616135681.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：81%

## 共有节点

全部 2 个 workflow 都包含：
- `Image Comparer (rgthree)`
- `ImageScaleBy`
- `ImageUpscaleWithModel`
- `LoadImage`
- `SaveImage`
- `UpscaleModelLoader`

**可变部分**（部分 workflow 才有）：
- `GetImageSize` —— 1/2 个有
- `ImageScale` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参

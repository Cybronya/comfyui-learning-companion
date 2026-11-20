---
name: unknown_workflow_generic_1920
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.675
common_nodes: [Image Comparer (rgthree), ImageScaleToTotalPixels, LoadImage, PreviewImage, SaveImage, SeedVR2BlockSwap, SeedVR2ExtraArgs]
problems: []
missing: []
members: [平台全量/seedvr2图像高清放大_1990773658010464257.json, 平台全量/电商（人像）高清放大工作流SeedVR2_2035252601658281985.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_1920

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（平台全量/seedvr2图像高清放大_1990773658010464257.json、平台全量/电商（人像）高清放大工作流SeedVR2_2035252601658281985.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：68%

## 共有节点

全部 2 个 workflow 都包含：
- `Image Comparer (rgthree)`
- `ImageScaleToTotalPixels`
- `LoadImage`
- `PreviewImage`
- `SaveImage`
- `SeedVR2BlockSwap`
- `SeedVR2ExtraArgs`

**可变部分**（部分 workflow 才有）：
- `SeedVR2` —— 1/2 个有
- `SeedVR2GGUF` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参

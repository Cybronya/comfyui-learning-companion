---
name: unknown_workflow_generic_1295
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.839667
common_nodes: [BBoxesToSAM2, DownloadAndLoadQwenModel, LayerMask: LoadSAM2Model, LayerMask: SAM2UltraV2, LoadImage, MaskToImage, QwenVLDetection, SaveImage, easy showAnything]
problems: []
missing: []
members: [平台全量/Qwen精准抠图，支持中英文描述_1934041387723874306.json, 平台全量/Qwen精准抠图，支持中英文描述_1934049376371134465.json, 平台全量/抠图工作流_1942577686130962433.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_1295

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（平台全量/Qwen精准抠图，支持中英文描述_1934041387723874306.json、平台全量/Qwen精准抠图，支持中英文描述_1934049376371134465.json、平台全量/抠图工作流_1942577686130962433.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：84%

## 共有节点

全部 3 个 workflow 都包含：
- `BBoxesToSAM2`
- `DownloadAndLoadQwenModel`
- `LayerMask: LoadSAM2Model`
- `LayerMask: SAM2UltraV2`
- `LoadImage`
- `MaskToImage`
- `QwenVLDetection`
- `SaveImage`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `ImageConcatMulti` —— 2/3 个有
- `DeepTranslatorTextNode` —— 1/3 个有
- `JjkText` —— 1/3 个有
- `PrimitiveStringMultiline` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

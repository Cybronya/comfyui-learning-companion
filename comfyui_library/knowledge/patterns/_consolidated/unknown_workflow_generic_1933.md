---
name: unknown_workflow_generic_1933
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.735
common_nodes: [Any To Any, CR Text, DF_Float, Image Comparer (rgthree), ImageScaleBy, LoadImage, PreviewImage, RHHiddenNodes, SaveImage, Text, easy imageSize, int _O]
problems: []
missing: []
members: [平台全量/人物场景超级细化（脸部_场景_人物增加细节拒绝无效放大）V1.0_1954748281614155778.json, 平台全量/人物场景超级细化（脸部_场景_人物增加细节拒绝无效放大）V1.2_1954870821212884994.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_1933

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（平台全量/人物场景超级细化（脸部_场景_人物增加细节拒绝无效放大）V1.0_1954748281614155778.json、平台全量/人物场景超级细化（脸部_场景_人物增加细节拒绝无效放大）V1.2_1954870821212884994.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：74%

## 共有节点

全部 2 个 workflow 都包含：
- `Any To Any`
- `CR Text`
- `DF_Float`
- `Image Comparer (rgthree)`
- `ImageScaleBy`
- `LoadImage`
- `PreviewImage`
- `RHHiddenNodes`
- `SaveImage`
- `Text`
- `easy imageSize`
- `int _O`

**可变部分**（部分 workflow 才有）：
- `CR Text Concatenate` —— 1/2 个有
- `RH_Captioner` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参

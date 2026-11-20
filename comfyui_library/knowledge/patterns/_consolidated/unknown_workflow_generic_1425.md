---
name: unknown_workflow_generic_1425
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.479
common_nodes: [CR Text Concatenate, LoadImagesFromURL, LoadMultiImage, PrimitiveString, RH_LLMAPI_Pro_Node, RH_Nano_Banana2_Image2Image, RH_RhartImageG2ImageToImage, SaveImage, Text Find and Replace, Text Multiline, ZML_MergeText, easy promptLine, easy showAnything]
problems: []
missing: []
members: [图片生成/图生图/【Auto-Generate-Goods-Detail】自动生成产品详情页-API调用_2069077738174115842.json, 图片生成/图生图/【Auto-Generate-Goods-Detail】自动生成产品详情页-无文字版-API调用_2065355371576913922.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_1425

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/【Auto-Generate-Goods-Detail】自动生成产品详情页-API调用_2069077738174115842.json、图片生成/图生图/【Auto-Generate-Goods-Detail】自动生成产品详情页-无文字版-API调用_2065355371576913922.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：48%

## 共有节点

全部 2 个 workflow 都包含：
- `CR Text Concatenate`
- `LoadImagesFromURL`
- `LoadMultiImage`
- `PrimitiveString`
- `RH_LLMAPI_Pro_Node`
- `RH_Nano_Banana2_Image2Image`
- `RH_RhartImageG2ImageToImage`
- `SaveImage`
- `Text Find and Replace`
- `Text Multiline`
- `ZML_MergeText`
- `easy promptLine`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `CR String To Combo` —— 1/2 个有
- `JjkText` —— 1/2 个有
- `RHHiddenNodes` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参

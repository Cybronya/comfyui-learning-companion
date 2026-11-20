---
name: unknown_workflow_generic_1516
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.9715
common_nodes: [CR Text, Fast Groups Bypasser (rgthree), ImageBatchMulti, ImageConcatMulti, LayerUtility: TextJoin, LoadImage, RH_LLMAPI_Pro_Node, RH_RhartImageG2ImageToImage_Batch, RH_RhartImageG2OfficialImageToImage, RH_RhartImageNG31FlashImageToImage, SaveImage]
problems: []
missing: []
members: [图片生成/图生图/家清详情页_2069299106266304513.json, 图片生成/图生图/居家——原文详情页_2069011307801698306.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_1516

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/家清详情页_2069299106266304513.json、图片生成/图生图/居家——原文详情页_2069011307801698306.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：97%

## 共有节点

全部 2 个 workflow 都包含：
- `CR Text`
- `Fast Groups Bypasser (rgthree)`
- `ImageBatchMulti`
- `ImageConcatMulti`
- `LayerUtility: TextJoin`
- `LoadImage`
- `RH_LLMAPI_Pro_Node`
- `RH_RhartImageG2ImageToImage_Batch`
- `RH_RhartImageG2OfficialImageToImage`
- `RH_RhartImageNG31FlashImageToImage`
- `SaveImage`

**可变部分**（部分 workflow 才有）：
- `easy showAnything` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参

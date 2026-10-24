---
name: unknown_workflow_generic_1432
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.682
common_nodes: [CR Text, Image Comparer (rgthree), LayerFilter: GaussianBlur, LoadImage, PreviewImage, RHLLMChatNode, RH_RhartImageG2ImageToImage, SaveImage, Seed (rgthree), StringFunction|pysssss, easy showAnything, 孤海注释]
problems: []
missing: []
members: [图片生成/图生图/脏图修复重绘｜消除多次生成残留噪点_2069604605264224257.json, 图片生成/图生图/脏图重绘还原【适合还原噪点过多或全能图片G多次重绘后噪点过多的图】_2069242537495326722.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_1432

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/脏图修复重绘｜消除多次生成残留噪点_2069604605264224257.json、图片生成/图生图/脏图重绘还原【适合还原噪点过多或全能图片G多次重绘后噪点过多的图】_2069242537495326722.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：68%

## 共有节点

全部 2 个 workflow 都包含：
- `CR Text`
- `Image Comparer (rgthree)`
- `LayerFilter: GaussianBlur`
- `LoadImage`
- `PreviewImage`
- `RHLLMChatNode`
- `RH_RhartImageG2ImageToImage`
- `SaveImage`
- `Seed (rgthree)`
- `StringFunction|pysssss`
- `easy showAnything`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `AspectRatioSelect` —— 1/2 个有
- `GetNode` —— 1/2 个有
- `Note Plus (mtb)` —— 1/2 个有
- `SetNode` —— 1/2 个有
- `孤海图像裁剪按比例` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参

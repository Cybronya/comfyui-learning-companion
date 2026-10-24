---
name: unknown_workflow_generic_1480
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.6375
common_nodes: [AspectRatioSelect, CR Text Replace, JjkText, LoadImage, RH_Captioner_Pro, RH_RhartImageG2TextToImage, SaveImage, easy showAnything]
problems: []
missing: []
members: [图片生成/文生图/gemini-3-pro 图像反推 + 全能图片G2.0 【公式版】_1922305291264675842.json, 图片生成/文生图/全能图片2.0高质量洗图——gemini-3-pro 图像反推0.1元1张图_2053377949067431937.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_1480

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/gemini-3-pro 图像反推 + 全能图片G2.0 【公式版】_1922305291264675842.json、图片生成/文生图/全能图片2.0高质量洗图——gemini-3-pro 图像反推0.1元1张图_2053377949067431937.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：64%

## 共有节点

全部 2 个 workflow 都包含：
- `AspectRatioSelect`
- `CR Text Replace`
- `JjkText`
- `LoadImage`
- `RH_Captioner_Pro`
- `RH_RhartImageG2TextToImage`
- `SaveImage`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `AIO_Preprocessor` —— 1/2 个有
- `PreviewImage` —— 1/2 个有
- `RH_RhartImageG2ImageToImage` —— 1/2 个有
- `easy saveText` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参

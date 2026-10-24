---
name: unknown_workflow_generic_1246
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.8515
common_nodes: [CR Prompt Text, Fast Groups Bypasser (rgthree), LoadImage, RH_RhartImageG2ImageToImage, RH_RhartImageG2OfficialImageToImage, RH_RhartImageG2OfficialTextToImage, RH_RhartImageG2TextToImage, SaveImage]
problems: []
missing: []
members: [图片生成/图生图/KR_image2图像编辑（4号流）_2048600998565908481.json, 图片生成/文生图/全能图片G2.0 你懂的_2047299239650271234.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_1246

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/KR_image2图像编辑（4号流）_2048600998565908481.json、图片生成/文生图/全能图片G2.0 你懂的_2047299239650271234.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：85%

## 共有节点

全部 2 个 workflow 都包含：
- `CR Prompt Text`
- `Fast Groups Bypasser (rgthree)`
- `LoadImage`
- `RH_RhartImageG2ImageToImage`
- `RH_RhartImageG2OfficialImageToImage`
- `RH_RhartImageG2OfficialTextToImage`
- `RH_RhartImageG2TextToImage`
- `SaveImage`

**可变部分**（部分 workflow 才有）：
- `Comfly_api_set` —— 1/2 个有
- `Comfly_gpt_image_2_official_ratio` —— 1/2 个有
- `Image Comparer (rgthree)` —— 1/2 个有
- `RH_Nano_Banana2_Gemini31Flash` —— 1/2 个有
- `RH_Nano_Banana2_Image2Image` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参

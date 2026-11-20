---
name: unknown_workflow_generic_1548
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.866
common_nodes: [CR Text, ImageCrop+, ImageScale, JjkText, LoadImage, RH_Captioner_Pro, RH_LLMAPI_Pro_Node, RH_Nano_Banana2_Image2Image, SaveImage, ShowText|pysssss, easy imageSplitGrid]
problems: []
missing: []
members: [图片生成/图生图/柏辰电商-宠物服装卖点生成工作流V1_2016301967601045505.json, 图片生成/图生图/柏辰电商-宠物服装卖点生成工作流V2-自定义品种_2016759236046364673.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_1548

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/柏辰电商-宠物服装卖点生成工作流V1_2016301967601045505.json、图片生成/图生图/柏辰电商-宠物服装卖点生成工作流V2-自定义品种_2016759236046364673.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：87%

## 共有节点

全部 2 个 workflow 都包含：
- `CR Text`
- `ImageCrop+`
- `ImageScale`
- `JjkText`
- `LoadImage`
- `RH_Captioner_Pro`
- `RH_LLMAPI_Pro_Node`
- `RH_Nano_Banana2_Image2Image`
- `SaveImage`
- `ShowText|pysssss`
- `easy imageSplitGrid`

**可变部分**（部分 workflow 才有）：
- `CR Text Concatenate` —— 1/2 个有
- `CR Text Replace` —— 1/2 个有
- `ImageCombine` —— 1/2 个有
- `LoadImagesFromURL` —— 1/2 个有
- `MultiTextConcatenate` —— 1/2 个有
- `MuyeTextEditOutput` —— 1/2 个有
- `PreviewImage` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参

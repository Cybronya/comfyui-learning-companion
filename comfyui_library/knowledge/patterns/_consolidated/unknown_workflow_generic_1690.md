---
name: unknown_workflow_generic_1690
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.878
common_nodes: [Any Switch (rgthree), CR Prompt Text, CR Text, CR Text Concatenate, Fast Groups Muter (rgthree), ImageConcanate, LoadImage, SaveImage, easy int, easy textIndexSwitch]
problems: []
missing: []
members: [图片生成/图生图/创意玩法_2011843932308643841.json, 平台全量/111_2034687360310452225.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_1690

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/创意玩法_2011843932308643841.json、平台全量/111_2034687360310452225.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：88%

## 共有节点

全部 2 个 workflow 都包含：
- `Any Switch (rgthree)`
- `CR Prompt Text`
- `CR Text`
- `CR Text Concatenate`
- `Fast Groups Muter (rgthree)`
- `ImageConcanate`
- `LoadImage`
- `SaveImage`
- `easy int`
- `easy textIndexSwitch`

**可变部分**（部分 workflow 才有）：
- `Comfly_api_set` —— 1/2 个有
- `Comfly_gemini_3_1_flash_image_edit_S2A` —— 1/2 个有
- `Comfly_nano_banana2_edit` —— 1/2 个有
- `PreviewImage` —— 1/2 个有
- `RH_Nano_Banana2_Image2Image` —— 1/2 个有
- `easy showAnything` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参

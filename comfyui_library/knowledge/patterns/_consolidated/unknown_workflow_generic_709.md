---
name: unknown_workflow_generic_709
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.7085
common_nodes: [LoadImage, QWEN_TextDisplay, RHLLMChatNode, RH_Nano_Banana2_Image2Image, SaveImage, StringMergeNode, Text]
problems: []
missing: []
members: [图片生成/图生图/批量换衣新_2076845701216165889.json, 图片生成/图生图/批量换衣新_2077564298649493506.json, 图片生成/图生图/抄袭大师2_2082846764389978114.json, 图片生成/图生图/抄袭大师_2082785466595758082.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_709

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/批量换衣新_2076845701216165889.json、图片生成/图生图/批量换衣新_2077564298649493506.json、图片生成/图生图/抄袭大师2_2082846764389978114.json、图片生成/图生图/抄袭大师_2082785466595758082.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：71%

## 共有节点

全部 4 个 workflow 都包含：
- `LoadImage`
- `QWEN_TextDisplay`
- `RHLLMChatNode`
- `RH_Nano_Banana2_Image2Image`
- `SaveImage`
- `StringMergeNode`
- `Text`

**可变部分**（部分 workflow 才有）：
- `GetNode` —— 2/4 个有
- `GroupSwitcher` —— 2/4 个有
- `PreviewImage` —— 2/4 个有
- `SetNode` —— 2/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

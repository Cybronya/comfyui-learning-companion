---
name: unknown_workflow_generic_1518
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.7275
common_nodes: [CR Text, HAIGC_TextRelay, LoadImage, RH_LLMAPI_NODE, SaveImage, TextInput_, easy showAnything]
problems: []
missing: []
members: [图片生成/图生图/建筑-kimi2.5效果图提示词生成万能工作流_2044244712390926338.json, 图片生成/图生图/建筑-万能2天气变换工作流_2027365305361633281.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_1518

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/建筑-kimi2.5效果图提示词生成万能工作流_2044244712390926338.json、图片生成/图生图/建筑-万能2天气变换工作流_2027365305361633281.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：73%

## 共有节点

全部 2 个 workflow 都包含：
- `CR Text`
- `HAIGC_TextRelay`
- `LoadImage`
- `RH_LLMAPI_NODE`
- `SaveImage`
- `TextInput_`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `CR Text Concatenate` —— 1/2 个有
- `RH_Nano_Banana2_Gemini31Flash` —— 1/2 个有
- `ShellAgentPluginOutputText` —— 1/2 个有
- `easy promptReplace` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参

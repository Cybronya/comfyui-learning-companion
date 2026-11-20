---
name: unknown_workflow_generic_918
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.877333
common_nodes: [JoyAI_Image_SM_Clip, JoyAI_Image_Understand, LoadImage, PreviewAny, SaveImage, ShellAgentPluginOutputText]
problems: []
missing: []
members: [图片生成/反推提示词/JoyAI_Image图像反推_2042045578409938945.json, 图片生成/反推提示词/JoyAI_Image图像对比_2042043171374374914.json, 图片生成/图生图/JoyAI_图像反推_2042252443634896898.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_918

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/反推提示词/JoyAI_Image图像反推_2042045578409938945.json、图片生成/反推提示词/JoyAI_Image图像对比_2042043171374374914.json、图片生成/图生图/JoyAI_图像反推_2042252443634896898.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：88%

## 共有节点

全部 3 个 workflow 都包含：
- `JoyAI_Image_SM_Clip`
- `JoyAI_Image_Understand`
- `LoadImage`
- `PreviewAny`
- `SaveImage`
- `ShellAgentPluginOutputText`

**可变部分**（部分 workflow 才有）：
- `CR Prompt Text` —— 2/3 个有
- `ImageBatch` —— 1/3 个有
- `JjkShowText` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

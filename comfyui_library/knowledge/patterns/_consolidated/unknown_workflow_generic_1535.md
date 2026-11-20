---
name: unknown_workflow_generic_1535
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.741
common_nodes: [CR Prompt Text, LoadImage, RH_LLMAPI_Pro_Node, easy saveText, easy showAnything]
problems: []
missing: []
members: [图片生成/反推提示词/人物提示词反推_多人分镜格式_Gemini3flash_2022618091552772097.json, 平台全量/视频_图像 提示词 分析_2032282559035482113.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_1535

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/反推提示词/人物提示词反推_多人分镜格式_Gemini3flash_2022618091552772097.json、平台全量/视频_图像 提示词 分析_2032282559035482113.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：74%

## 共有节点

全部 2 个 workflow 都包含：
- `CR Prompt Text`
- `LoadImage`
- `RH_LLMAPI_Pro_Node`
- `easy saveText`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `CR Text Concatenate` —— 1/2 个有
- `LoadVideo` —— 1/2 个有
- `SaveStringKJ` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参

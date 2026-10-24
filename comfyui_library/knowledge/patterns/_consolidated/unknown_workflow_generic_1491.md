---
name: unknown_workflow_generic_1491
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.6415
common_nodes: [LoadImage, RH_Nano_Banana2_Image2Image, SaveImage, SetNode, Text Multiline, easy showAnything]
problems: []
missing: []
members: [图片生成/文生图/人物设计工作流_2019661430148046849.json, 图片生成/文生图/全能图片V1 2 & Pro 电商模特手持商品万能工作流 V2.0_1991534578351480833.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_1491

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/人物设计工作流_2019661430148046849.json、图片生成/文生图/全能图片V1 2 & Pro 电商模特手持商品万能工作流 V2.0_1991534578351480833.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：64%

## 共有节点

全部 2 个 workflow 都包含：
- `LoadImage`
- `RH_Nano_Banana2_Image2Image`
- `SaveImage`
- `SetNode`
- `Text Multiline`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `GetNode` —— 1/2 个有
- `ImageScale` —— 1/2 个有
- `RH_LLMAPI_NODE` —— 1/2 个有
- `RH_LLMAPI_Pro_Node` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参

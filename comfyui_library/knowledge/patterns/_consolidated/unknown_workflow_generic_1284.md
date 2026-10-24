---
name: unknown_workflow_generic_1284
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.8045
common_nodes: [LoadImage, RH_Nano_Banana2_Image2Image, SaveImage, Text Multiline, easy showAnything]
problems: []
missing: []
members: [图片生成/图生图/nano 全能图片V1 2 pro_1993227466487644161.json, 图片生成/图生图/主图测试-Pro_2042175020784422914.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_1284

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/nano 全能图片V1 2 pro_1993227466487644161.json、图片生成/图生图/主图测试-Pro_2042175020784422914.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：80%

## 共有节点

全部 2 个 workflow 都包含：
- `LoadImage`
- `RH_Nano_Banana2_Image2Image`
- `SaveImage`
- `Text Multiline`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `CR Text Concatenate` —— 1/2 个有
- `MultiTextConcatenate` —— 1/2 个有
- `Qwen3_VQA` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参

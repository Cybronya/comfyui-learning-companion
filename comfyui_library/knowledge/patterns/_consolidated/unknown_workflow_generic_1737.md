---
name: unknown_workflow_generic_1737
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.7
common_nodes: [Int, LoadImage, SaveImage, easy forLoopEnd, easy forLoopStart, easy showAnything]
problems: []
missing: []
members: [图片生成/图生图/批量产品模特通用产品_2034513734130995201.json, 平台全量/For循环1加到100_1896082392539398145.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_1737

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/批量产品模特通用产品_2034513734130995201.json、平台全量/For循环1加到100_1896082392539398145.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：70%

## 共有节点

全部 2 个 workflow 都包含：
- `Int`
- `LoadImage`
- `SaveImage`
- `easy forLoopEnd`
- `easy forLoopStart`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `CR Text Concatenate` —— 1/2 个有
- `JjkText` —— 1/2 个有
- `RH_Nano_Banana_Image2Image` —— 1/2 个有
- `easy mathInt` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参

---
name: unknown_workflow_generic_1280
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.9
common_nodes: [BagelImageUnderstanding, BagelModelLoader, LoadImage, SaveImage]
problems: []
missing: []
members: [图片生成/反推提示词/Bagel反推_1926998734700236802.json, 图片生成/反推提示词/Bagel提示词反推V2（10倍加速版）_1926956885998796801.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_1280

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/反推提示词/Bagel反推_1926998734700236802.json、图片生成/反推提示词/Bagel提示词反推V2（10倍加速版）_1926956885998796801.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：90%

## 共有节点

全部 2 个 workflow 都包含：
- `BagelImageUnderstanding`
- `BagelModelLoader`
- `LoadImage`
- `SaveImage`

**可变部分**（部分 workflow 才有）：
- `Bjornulf_ShowStringText` —— 1/2 个有
- `ShowText|pysssss` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参

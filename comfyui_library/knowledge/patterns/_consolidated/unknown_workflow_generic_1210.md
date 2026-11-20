---
name: unknown_workflow_generic_1210
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.985
common_nodes: [InvertMask, JoinImageWithAlpha, LoadImage, SaveImage, String, workflow>文字抠图]
problems: []
missing: []
members: [图片生成/图生图/文字logo抠图_1959870100813852673.json, 平台全量/logo抠文字_1960172998005305346.json, 平台全量/文字logo抠图LLM自动识别物体_1960603850686234625.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_1210

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/文字logo抠图_1959870100813852673.json、平台全量/logo抠文字_1960172998005305346.json、平台全量/文字logo抠图LLM自动识别物体_1960603850686234625.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：98%

## 共有节点

全部 3 个 workflow 都包含：
- `InvertMask`
- `JoinImageWithAlpha`
- `LoadImage`
- `SaveImage`
- `String`
- `workflow>文字抠图`

**可变部分**（部分 workflow 才有）：
- `MaskComposite` —— 2/3 个有
- `workflow>主体抠图` —— 2/3 个有
- `MaskToImage` —— 1/3 个有
- `PreviewImage` —— 1/3 个有
- `RH_LLMAPI_NODE` —— 1/3 个有
- `ShowText` —— 1/3 个有
- `easy imageRemBg` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

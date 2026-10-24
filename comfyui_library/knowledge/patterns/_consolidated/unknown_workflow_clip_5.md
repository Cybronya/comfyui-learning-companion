---
name: unknown_workflow_clip_5
type: Unknown Workflow
frequency: 3
level: strong
coverage: 1
common_nodes: [CLIPTextEncode, EmptyLatentImage, SaveImage, easy promptList, workflow>qwen, workflow>工作区]
problems: []
missing: []
members: [图片生成/文生图/【学员练习工作流】Day 1——文生图工作流_2043565514655539201.json, 图片生成/文生图/易大师课堂day1作业演示工作流_2052083024245870593.json, 图片生成/文生图/易大师课堂day1作业演示工作流_2072323138414800898.json]
source: knowledge_consolidation
---

# unknown_workflow_clip_5

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/【学员练习工作流】Day 1——文生图工作流_2043565514655539201.json、图片生成/文生图/易大师课堂day1作业演示工作流_2052083024245870593.json、图片生成/文生图/易大师课堂day1作业演示工作流_2072323138414800898.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：100%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPTextEncode`
- `EmptyLatentImage`
- `SaveImage`
- `easy promptList`
- `workflow>qwen`
- `workflow>工作区`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1280 | 1280 - 1280 | 3 | 100% |
| 高度 | 1920 | 1920 - 1920 | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1280，观测区间 1280 - 1280，3 个样本，取值集中（一致性 100%）
- 高度 中位数 1920，观测区间 1920 - 1920，3 个样本，取值集中（一致性 100%）

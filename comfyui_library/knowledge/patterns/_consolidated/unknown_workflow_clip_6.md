---
name: unknown_workflow_clip_6
type: Unknown Workflow
frequency: 2
level: weak
coverage: 1
common_nodes: [CLIPTextEncode, EmptyLatentImage, SaveImage, workflow>1]
problems: []
missing: []
members: [图片生成/文生图/krea写实混血少女_1956597003583193089.json, 图片生成/文生图/krea真实感男生_1955893393337581569.json]
source: knowledge_consolidation
---

# unknown_workflow_clip_6

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/krea写实混血少女_1956597003583193089.json、图片生成/文生图/krea真实感男生_1955893393337581569.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：100%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPTextEncode`
- `EmptyLatentImage`
- `SaveImage`
- `workflow>1`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 960 | - | 2 | 100% |
| 高度 | 1280 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 960，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高度 中位数 1280，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参

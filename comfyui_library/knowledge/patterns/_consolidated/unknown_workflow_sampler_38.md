---
name: unknown_workflow_sampler_38
type: Unknown Workflow
frequency: 2
level: weak
coverage: 1
common_nodes: [CR Prompt Text, JWInteger, LoadImage, RunningHub OmniWeaving Loader, SaveVideo]
problems: []
missing: []
members: [视频生成/图生视频/2042119081003847682.json, 视频生成/图生视频/2042124474220290049.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_38

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/2042119081003847682.json、视频生成/图生视频/2042124474220290049.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：100%

## 共有节点

全部 2 个 workflow 都包含：
- `CR Prompt Text`
- `JWInteger`
- `LoadImage`
- `RunningHub OmniWeaving Loader`
- `SaveVideo`

**可变部分**（部分 workflow 才有）：
- `RunningHub OmniWeaving Sampler(Interpolation)` —— 1/2 个有
- `RunningHub OmniWeaving Sampler(Ref2V)` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参

---
name: unknown_workflow_unet_vae_10
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.928
common_nodes: [CLIPLoader, ComfyMiniMaxH3Director, CreateVideo, SaveVideo, UNETLoader, VAELoader]
problems: []
missing: []
members: [视频生成/文生视频/Fast H3 4步极速版_2094688586812710914.json, 视频生成/文生视频/MiniMax H3 全能导演台_2091791862691618817.json, 视频生成/文生视频/MiniMax H3 全能导演台_2092150523830030338.json, 视频生成/文生视频/minimax导演台工作流_2079449672288129026.json, 视频生成/文生视频/全能导演工作台_2092099189571407873.json]
source: knowledge_consolidation
---

# unknown_workflow_unet_vae_10

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（视频生成/文生视频/Fast H3 4步极速版_2094688586812710914.json、视频生成/文生视频/MiniMax H3 全能导演台_2091791862691618817.json、视频生成/文生视频/MiniMax H3 全能导演台_2092150523830030338.json、视频生成/文生视频/minimax导演台工作流_2079449672288129026.json、视频生成/文生视频/全能导演工作台_2092099189571407873.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：93%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPLoader`
- `ComfyMiniMaxH3Director`
- `CreateVideo`
- `SaveVideo`
- `UNETLoader`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LoraLoaderModelOnly` —— 4/5 个有
- `MiniMaxH3DirectorRefine` —— 4/5 个有
- `LoraLoaderBypassModelOnly` —— 3/5 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 1/5 个有
- `PathchSageAttentionKJ` —— 1/5 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

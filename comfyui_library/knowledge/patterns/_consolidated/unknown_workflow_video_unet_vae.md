---
name: unknown_workflow_video_unet_vae
type: Unknown Workflow
frequency: 10
level: moderate
coverage: 0.8475
common_nodes: [CLIPLoader, MiniMaxH3Director, MiniMaxH3MemoryEfficientSageAttentionPatch, UNETLoader, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/Minimax-H3 导演台 首尾帧生视频（加速版）_2087216505112059905.json, 视频生成/图生视频/Minimax-H3导演台 参考改视频（加速版）_2087208935521607681.json, 视频生成/文生视频/MiniMax H3 AIMixer 导演台_2087791306260180994.json, 视频生成/文生视频/MiniMax H3 导演台｜无限长视频玩法_2090426764001636354.json, 视频生成/文生视频/MiniMax H3 导演台｜无限长视频玩法_2092539959881322498.json, 视频生成/文生视频/Minimax-H3 导演台 文生视频（加速版）_2087206515097825281.json, 视频生成/文生视频/Minimax-H3导演台 [图_视频_音频]参考生视频（加速版）_2087214823493951490.json, 视频生成/文生视频/Ref2va工作流｜MiniMax H3导演台_2093343614062649345.json, 视频生成/文生视频/minimax H3导演台_2092876631428919298.json, 视频生成/文生视频/minimax H3导演台多模式视频生成_2094684141672554497.json]
source: knowledge_consolidation
---

# unknown_workflow_video_unet_vae

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（视频生成/图生视频/Minimax-H3 导演台 首尾帧生视频（加速版）_2087216505112059905.json、视频生成/图生视频/Minimax-H3导演台 参考改视频（加速版）_2087208935521607681.json、视频生成/文生视频/MiniMax H3 AIMixer 导演台_2087791306260180994.json、视频生成/文生视频/MiniMax H3 导演台｜无限长视频玩法_2090426764001636354.json、视频生成/文生视频/MiniMax H3 导演台｜无限长视频玩法_2092539959881322498.json…）

- **类型**：Unknown Workflow
- **样本数**：10
- **可信度**：中等可信
- **平均知识覆盖**：85%

## 共有节点

全部 10 个 workflow 都包含：
- `CLIPLoader`
- `MiniMaxH3Director`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `UNETLoader`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `PathchSageAttentionKJ` —— 8/10 个有
- `LoraLoaderModelOnly` —— 6/10 个有
- `Label (rgthree)` —— 1/10 个有
- `ModelAttentionBackend` —— 1/10 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

---
name: unknown_workflow_video_unet_vae
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.877
common_nodes: [CLIPLoader, MiniMaxH3Director, MiniMaxH3MemoryEfficientSageAttentionPatch, UNETLoader, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/文生视频/Minimax-H3 导演台 文生视频（加速版）_2087206515097825281.json, 视频生成/文生视频/Minimax-H3导演台 [图_视频_音频]参考生视频（加速版）_2087214823493951490.json, 视频生成/文生视频/Ref2va工作流｜MiniMax H3导演台_2093343614062649345.json, 视频生成/文生视频/minimax H3导演台_2092876631428919298.json, 视频生成/文生视频/minimax H3导演台多模式视频生成_2094684141672554497.json]
source: knowledge_consolidation
---

# unknown_workflow_video_unet_vae

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（视频生成/文生视频/Minimax-H3 导演台 文生视频（加速版）_2087206515097825281.json、视频生成/文生视频/Minimax-H3导演台 [图_视频_音频]参考生视频（加速版）_2087214823493951490.json、视频生成/文生视频/Ref2va工作流｜MiniMax H3导演台_2093343614062649345.json、视频生成/文生视频/minimax H3导演台_2092876631428919298.json、视频生成/文生视频/minimax H3导演台多模式视频生成_2094684141672554497.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：88%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPLoader`
- `MiniMaxH3Director`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `UNETLoader`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `LoraLoaderModelOnly` —— 3/5 个有
- `PathchSageAttentionKJ` —— 3/5 个有
- `ModelAttentionBackend` —— 1/5 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

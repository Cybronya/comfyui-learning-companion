---
name: unknown_workflow_unet_vae_5
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.8568
common_nodes: [CLIPLoader, CreateVideo, LoadAudio, LoadImage, MiniMaxH3Director, MiniMaxH3DirectorGroupReferenceToVideo, MiniMaxH3DirectorGroupsCombine, MiniMaxH3MemoryEfficientSageAttentionPatch, SaveVideo, UNETLoader, VAELoader]
problems: []
missing: []
members: [视频生成/图生视频/MiniMax H3 导演台全能工作流（外接参数版-R2V）_2090270058009415681.json, 视频生成/文生视频/H3导演台唱歌数字人版_2101659906209312770.json, 视频生成/文生视频/MiniMax H3 导演台全能工作流（外接参数版-R2V）_2086289926563385346.json, 视频生成/文生视频/MiniMax H3 导演台全能工作流（外接参数版-R2V）_2096863617500139522.json, 视频生成/文生视频/MiniMaxH3导演台_AIMixer_2091197123118321665.json]
source: knowledge_consolidation
---

# unknown_workflow_unet_vae_5

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（视频生成/图生视频/MiniMax H3 导演台全能工作流（外接参数版-R2V）_2090270058009415681.json、视频生成/文生视频/H3导演台唱歌数字人版_2101659906209312770.json、视频生成/文生视频/MiniMax H3 导演台全能工作流（外接参数版-R2V）_2086289926563385346.json、视频生成/文生视频/MiniMax H3 导演台全能工作流（外接参数版-R2V）_2096863617500139522.json、视频生成/文生视频/MiniMaxH3导演台_AIMixer_2091197123118321665.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：86%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPLoader`
- `CreateVideo`
- `LoadAudio`
- `LoadImage`
- `MiniMaxH3Director`
- `MiniMaxH3DirectorGroupReferenceToVideo`
- `MiniMaxH3DirectorGroupsCombine`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `SaveVideo`
- `UNETLoader`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `PathchSageAttentionKJ` —— 4/5 个有
- `PreviewAny` —— 4/5 个有
- `VHS_LoadVideo` —— 3/5 个有
- `LoraLoaderModelOnly` —— 2/5 个有
- `ManualSigmas` —— 1/5 个有
- `MiniMaxH3DirectorRefine` —— 1/5 个有
- `ModelAttentionBackend` —— 1/5 个有
- `TrimAudioDuration` —— 1/5 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

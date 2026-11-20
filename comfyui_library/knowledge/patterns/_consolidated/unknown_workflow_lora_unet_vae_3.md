---
name: unknown_workflow_lora_unet_vae_3
type: Unknown Workflow
frequency: 14
level: moderate
coverage: 0.862643
common_nodes: [CLIPLoader, CreateVideo, LoraLoaderModelOnly, MiniMaxH3Director, MiniMaxH3MemoryEfficientSageAttentionPatch, PathchSageAttentionKJ, SaveVideo, UNETLoader, VAELoader]
problems: []
missing: []
members: [视频生成/图生视频/H3 导演台-R2V参考主体生视频_2089168093019987970.json, 视频生成/图生视频/MiniMax H3 导演台 · 图生视频（多角色音色锁定）_2113992498598203394.json, 视频生成/图生视频/MiniMax H3 导演台-加速-长视频分段生成-多主体绑定_2090328893898186753.json, 视频生成/图生视频/MiniMax H3 导演台_2091304369898737665.json, 视频生成/图生视频/MiniMax H3 导演台全能工作流 (v2)_2109484168831913986.json, 视频生成/图生视频/MiniMax H3 导演台全能工作流_2104745162994966529.json, 视频生成/图生视频/MiniMax+H3+导演台全能工作流_2114144273812770817.json, 视频生成/图生视频/MiniMax_H3_导演台全能工作流_2108029810021851137.json, 视频生成/文生视频/MiniMax H3 导演台全能工作流_2084788947984666625.json, 视频生成/文生视频/MiniMax H3 导演台全能工作流_2102976985982136321.json, 视频生成/文生视频/MiniMax H3 导演台全能工作流_2104947736662597633.json, 视频生成/文生视频/MiniMax_H3_导演台全能工作流_(v2)_2113779471554801666.json, 视频生成/文生视频/minimax_h3_director_导演台全能工作流_2102804572346609666.json, 视频生成/文生视频/minimax_h3_director_导演台全能工作流_2102965461339164674.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_unet_vae_3

> 由 `engine/knowledge_consolidation` 从 14 个 workflow 归纳得出（视频生成/图生视频/H3 导演台-R2V参考主体生视频_2089168093019987970.json、视频生成/图生视频/MiniMax H3 导演台 · 图生视频（多角色音色锁定）_2113992498598203394.json、视频生成/图生视频/MiniMax H3 导演台-加速-长视频分段生成-多主体绑定_2090328893898186753.json、视频生成/图生视频/MiniMax H3 导演台_2091304369898737665.json、视频生成/图生视频/MiniMax H3 导演台全能工作流 (v2)_2109484168831913986.json…）

- **类型**：Unknown Workflow
- **样本数**：14
- **可信度**：中等可信
- **平均知识覆盖**：86%

## 共有节点

全部 14 个 workflow 都包含：
- `CLIPLoader`
- `CreateVideo`
- `LoraLoaderModelOnly`
- `MiniMaxH3Director`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `PathchSageAttentionKJ`
- `SaveVideo`
- `UNETLoader`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `BasicScheduler` —— 13/14 个有
- `MiniMaxH3DirectorRefine` —— 13/14 个有
- `PreviewAny` —— 13/14 个有
- `MiniMaxH3DirectorFaceRefine` —— 10/14 个有
- `MiniMaxH3DirectorSelfLift` —— 10/14 个有
- `UpscaleModelLoader` —— 10/14 个有
- `EmptyImage` —— 2/14 个有
- `PreViewVideo` —— 2/14 个有
- `PreviewImage` —— 2/14 个有
- `忽略多组孤海` —— 2/14 个有
- `Fast Groups Bypasser (rgthree)` —— 1/14 个有
- `孤海注释` —— 1/14 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

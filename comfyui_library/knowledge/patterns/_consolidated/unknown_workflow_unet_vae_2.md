---
name: unknown_workflow_unet_vae_2
type: Unknown Workflow
frequency: 17
level: moderate
coverage: 0.848176
common_nodes: [CLIPLoader, MiniMaxH3Director, MiniMaxH3MemoryEfficientSageAttentionPatch, UNETLoader, VAELoader]
problems: []
missing: []
members: [视频生成/图生视频/MiniMax H3导演台长视频生成_段间引导_turbo_2088450232764944385.json, 视频生成/图生视频/MiniMax H3开源 导演台全能工作流无水印版_2092549957147521025.json, 视频生成/图生视频/Minimax-H3 导演台 首尾帧生视频（加速版）_2087216505112059905.json, 视频生成/图生视频/Minimax-H3导演台 参考改视频（加速版）_2087208935521607681.json, 视频生成/文生视频/H3图生视频-高清版_2099038143218536450.json, 视频生成/文生视频/MiniMax H3 AIMixer 导演台_2087791306260180994.json, 视频生成/文生视频/MiniMax H3 导演台全能工作流无水印版_2091949246240092162.json, 视频生成/文生视频/MiniMax H3 导演台全能工作流无水印版_2093187899088003073.json, 视频生成/文生视频/MiniMax H3 导演台工作流-fl2va_2091328355697250305.json, 视频生成/文生视频/MiniMax H3 导演台｜无限长视频玩法_2090426764001636354.json, 视频生成/文生视频/MiniMax H3 导演台｜无限长视频玩法_2092539959881322498.json, 视频生成/文生视频/MiniMax H3 电影级运镜全能导演台｜二采精修｜分镜合成｜加速版_2096009884130177025.json, 视频生成/文生视频/MiniMax H3 电影质感全能导演台｜二采放大｜分镜合成｜8步加速版_2100406933353226242.json, 视频生成/文生视频/MiniMax-H3_Director_导演台多参模式_2101083112175394817.json, 视频生成/文生视频/minimax_h3_director_二采+导演台_2089917916656525313.json, 视频生成/文生视频/minimax_h3_director_导演台全能工作流_2102965461339164674.json, 视频生成/文生视频/导演台全能工作流_2093548311629361154.json]
source: knowledge_consolidation
---

# unknown_workflow_unet_vae_2

> 由 `engine/knowledge_consolidation` 从 17 个 workflow 归纳得出（视频生成/图生视频/MiniMax H3导演台长视频生成_段间引导_turbo_2088450232764944385.json、视频生成/图生视频/MiniMax H3开源 导演台全能工作流无水印版_2092549957147521025.json、视频生成/图生视频/Minimax-H3 导演台 首尾帧生视频（加速版）_2087216505112059905.json、视频生成/图生视频/Minimax-H3导演台 参考改视频（加速版）_2087208935521607681.json、视频生成/文生视频/H3图生视频-高清版_2099038143218536450.json…）

- **类型**：Unknown Workflow
- **样本数**：17
- **可信度**：中等可信
- **平均知识覆盖**：85%

## 共有节点

全部 17 个 workflow 都包含：
- `CLIPLoader`
- `MiniMaxH3Director`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `UNETLoader`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LoraLoaderModelOnly` —— 14/17 个有
- `PathchSageAttentionKJ` —— 12/17 个有
- `VHS_VideoCombine` —— 12/17 个有
- `MiniMaxH3DirectorRefine` —— 11/17 个有
- `UpscaleModelLoader` —— 10/17 个有
- `PreviewAny` —— 7/17 个有
- `CreateVideo` —— 6/17 个有
- `SaveVideo` —— 6/17 个有
- `BasicScheduler` —— 2/17 个有
- `EmptyImage` —— 2/17 个有
- `PreviewImage` —— 2/17 个有
- `Label (rgthree)` —— 1/17 个有
- `MiniMaxH3DirectorFaceRefine` —— 1/17 个有
- `MiniMaxH3DirectorSelfLift` —— 1/17 个有
- `easy sleep` —— 1/17 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

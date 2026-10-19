---
name: text_to_image_lora_sampler_clip_51
type: Text To Image
frequency: 15
level: strong
coverage: 0.879867
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, LoraLoaderModelOnly, MiniMaxH3MemoryEfficientSageAttentionPatch, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/MiniMax-H3导演台多合一｜文生图生首尾帧多参视频制作_2094867179169730562.json, 视频生成/图生视频/minimax_h3 短剧动漫分镜｜转场运镜视频生成 图生视频_2097559236938133506.json, 视频生成/图生视频/minimax_h3短剧动漫分镜工作流｜转场运镜图生视频生成_2097503251691298818.json, 视频生成/图生视频/minimax_h3短剧动漫分镜｜转场运镜视频生成_2095590603890450433.json, 视频生成/图生视频/minimax_h3短剧动漫分镜｜转场运镜视频生成_2097236090833956866.json, 视频生成/图生视频/文生图生首尾帧多参多合一｜MiniMax-H3导演台制作_2092752481414639618.json, 视频生成/图生视频/文生图生首尾帧多参｜MiniMax-H3导演台多合一制作_2095058109722091521.json, 视频生成/文生视频/fl2v全能导演台｜MiniMax H3文生视频生成_2091244438382268418.json, 视频生成/文生视频/fl2v全能工作流｜MiniMax H3导演台文生视频_2092705414675779585.json, 视频生成/文生视频/fl2v导演台全能｜MiniMax H3文生视频生成_2092560452915126274.json, 视频生成/文生视频/一次60秒全能生成｜海螺H3搅拌手大佬版导演台_2092749641665306626.json, 视频生成/文生视频/一次60秒出片｜海螺 H3 导演台搅拌手大佬版_2090893932635967490.json, 视频生成/文生视频/全能导演工作台｜minimax视频生成一站式_2091202175820193794.json, 视频生成/文生视频/导演台一次60秒｜海螺H3搅拌手大佬版全能s_2091190910787874818.json, 视频生成/文生视频/搅拌手大佬版导演台｜海螺H3全能60秒生成_2091195180161519618.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_51

> 由 `engine/knowledge_consolidation` 从 15 个 workflow 归纳得出（视频生成/图生视频/MiniMax-H3导演台多合一｜文生图生首尾帧多参视频制作_2094867179169730562.json、视频生成/图生视频/minimax_h3 短剧动漫分镜｜转场运镜视频生成 图生视频_2097559236938133506.json、视频生成/图生视频/minimax_h3短剧动漫分镜工作流｜转场运镜图生视频生成_2097503251691298818.json、视频生成/图生视频/minimax_h3短剧动漫分镜｜转场运镜视频生成_2095590603890450433.json、视频生成/图生视频/minimax_h3短剧动漫分镜｜转场运镜视频生成_2097236090833956866.json…）

- **类型**：Text To Image
- **样本数**：15
- **可信度**：强结论
- **平均知识覆盖**：88%

## 共有节点

全部 15 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `LoraLoaderModelOnly`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `solarL_SaveImagesToZip`

**可变部分**（部分 workflow 才有）：
- `VHS_VideoCombine` —— 14/15 个有
- `孤海注释` —— 14/15 个有
- `PreviewAny` —— 12/15 个有
- `LoraLoaderBypassModelOnly` —— 11/15 个有
- `MiniMaxH3Director` —— 11/15 个有
- `MiniMaxH3DirectorRefine` —— 10/15 个有
- `UpscaleModelLoader` —— 8/15 个有
- `Fast Groups Bypasser (rgthree)` —— 7/15 个有
- `ModelAttentionBackend` —— 7/15 个有
- `CreateVideo` —— 6/15 个有
- `SaveVideo` —— 6/15 个有
- `BasicScheduler` —— 5/15 个有
- `PathchSageAttentionKJ` —— 5/15 个有
- `ComfyMiniMaxH3Director` —— 4/15 个有
- `FastGroupsBypassSwitch` —— 4/15 个有
- `Any Switch (rgthree)` —— 3/15 个有
- `SolAttnMiniMax` —— 3/15 个有
- `ManualSigmas` —— 2/15 个有
- `SaveImage` —— 1/15 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 15 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 15 | 100% |
| 采样算法 | er_sde | - | 15 | 100% |
| 调度器 | beta | - | 15 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 15 | 100% |
| 宽度 | 80 | 80 - 80 | 15 | 100% |
| 高度 | 80 | 80 - 80 | 15 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 18/15 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，15 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，15 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，15 个样本，一致性 100%
- 调度器 最常用 beta，15 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，15 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，15 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，15 个样本，取值集中（一致性 100%）
- 高发问题（18/15 个样本）：Steps较低可能导致细节不足

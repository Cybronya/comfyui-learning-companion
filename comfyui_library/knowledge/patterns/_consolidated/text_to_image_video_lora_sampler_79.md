---
name: text_to_image_video_lora_sampler_79
type: Text To Image
frequency: 9
level: strong
coverage: 0.882222
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, LoraLoaderModelOnly, MiniMaxH3MemoryEfficientSageAttentionPatch, ModelAttentionBackend, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/MiniMax-H3导演台多合一｜文生图生首尾帧多参视频制作_2094867179169730562.json, 视频生成/图生视频/minimax_h3 短剧动漫分镜｜转场运镜视频生成 图生视频_2097559236938133506.json, 视频生成/图生视频/minimax_h3短剧动漫分镜工作流｜转场运镜图生视频生成_2097503251691298818.json, 视频生成/图生视频/minimax_h3短剧动漫分镜｜转场运镜视频生成_2095590603890450433.json, 视频生成/图生视频/minimax_h3短剧动漫分镜｜转场运镜视频生成_2097236090833956866.json, 视频生成/图生视频/文生图生首尾帧多参多合一｜MiniMax-H3导演台制作_2092752481414639618.json, 视频生成/图生视频/文生图生首尾帧多参｜MiniMax-H3导演台多合一制作_2095058109722091521.json, 视频生成/文生视频/minimax H3导演台工作流｜文生图生视频一站式_2094560745752195073.json, 视频生成/文生视频/导演台工作流｜minimax H3三模视频一键生成_2094760059535450113.json]
source: knowledge_consolidation
---

# text_to_image_video_lora_sampler_79

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（视频生成/图生视频/MiniMax-H3导演台多合一｜文生图生首尾帧多参视频制作_2094867179169730562.json、视频生成/图生视频/minimax_h3 短剧动漫分镜｜转场运镜视频生成 图生视频_2097559236938133506.json、视频生成/图生视频/minimax_h3短剧动漫分镜工作流｜转场运镜图生视频生成_2097503251691298818.json、视频生成/图生视频/minimax_h3短剧动漫分镜｜转场运镜视频生成_2095590603890450433.json、视频生成/图生视频/minimax_h3短剧动漫分镜｜转场运镜视频生成_2097236090833956866.json…）

- **类型**：Text To Image
- **样本数**：9
- **可信度**：强结论
- **平均知识覆盖**：88%

## 共有节点

全部 9 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `LoraLoaderModelOnly`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `ModelAttentionBackend`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `solarL_SaveImagesToZip`

**可变部分**（部分 workflow 才有）：
- `孤海注释` —— 8/9 个有
- `LoraLoaderBypassModelOnly` —— 7/9 个有
- `MiniMaxH3Director` —— 5/9 个有
- `ComfyMiniMaxH3Director` —— 4/9 个有
- `PreviewAny` —— 4/9 个有
- `Any Switch (rgthree)` —— 3/9 个有
- `Fast Groups Bypasser (rgthree)` —— 3/9 个有
- `SolAttnMiniMax` —— 3/9 个有
- `ManualSigmas` —— 2/9 个有
- `MiniMaxH3DirectorRefine` —— 2/9 个有
- `SaveImage` —— 1/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 9 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 9 | 100% |
| 采样算法 | er_sde | - | 9 | 100% |
| 调度器 | beta | - | 9 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 9 | 100% |
| 宽度 | 80 | 80 - 80 | 9 | 100% |
| 高度 | 80 | 80 - 80 | 9 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 11/9 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，9 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，9 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，9 个样本，一致性 100%
- 调度器 最常用 beta，9 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，9 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，9 个样本，取值集中（一致性 100%）
- 高发问题（11/9 个样本）：Steps较低可能导致细节不足

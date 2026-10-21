---
name: text_to_image_lora_sampler_clip_277
type: Text To Image
frequency: 4
level: strong
coverage: 0.857
common_nodes: [CLIPLoader, CLIPTextEncode, CreateVideo, EmptyLatentImage, JjkText, KSampler, LoraLoaderModelOnly, SaveVideo, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/文生视频/R2V）导演台全能工作流（外接参数版MiniMax_2086534641690963970.json, 视频生成/文生视频/minimax h3导演全能工作台｜文生视频文生图图生图_2100801737908117505.json, 视频生成/文生视频/加速视频生成｜Wan2.2文生图生视频人物特效_2091227342952812546.json, 视频生成/文生视频/导演台全能工作流外接参数版｜MiniMax H3参考生视频R2V_2097041962636500994.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_277

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（视频生成/文生视频/R2V）导演台全能工作流（外接参数版MiniMax_2086534641690963970.json、视频生成/文生视频/minimax h3导演全能工作台｜文生视频文生图图生图_2100801737908117505.json、视频生成/文生视频/加速视频生成｜Wan2.2文生图生视频人物特效_2091227342952812546.json、视频生成/文生视频/导演台全能工作流外接参数版｜MiniMax H3参考生视频R2V_2097041962636500994.json）

- **类型**：Text To Image
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：86%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CreateVideo`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `LoraLoaderModelOnly`
- `SaveVideo`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `LoadImage` —— 3/4 个有
- `MiniMaxH3Director` —— 3/4 个有
- `PathchSageAttentionKJ` —— 3/4 个有
- `PreviewAny` —— 3/4 个有
- `LoadAudio` —— 2/4 个有
- `MiniMaxH3DirectorGroupReferenceToVideo` —— 2/4 个有
- `MiniMaxH3DirectorGroupsCombine` —— 2/4 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 2/4 个有
- `VHS_LoadVideo` —— 2/4 个有
- `KSamplerAdvanced` —— 1/4 个有
- `ModelSamplingSD3` —— 1/4 个有
- `SaveImage` —— 1/4 个有
- `WanImageToVideo` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 4 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 4 | 100% |
| 采样算法 | er_sde | - | 4 | 100% |
| 调度器 | beta | - | 4 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |
| 宽度 | 80 | 80 - 80 | 4 | 100% |
| 高度 | 80 | 80 - 80 | 4 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，4 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，4 个样本，一致性 100%
- 调度器 最常用 beta，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，4 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，4 个样本，取值集中（一致性 100%）
- 高发问题（4/4 个样本）：Steps较低可能导致细节不足

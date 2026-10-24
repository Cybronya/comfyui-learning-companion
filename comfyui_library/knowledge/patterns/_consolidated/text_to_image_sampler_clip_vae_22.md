---
name: text_to_image_sampler_clip_vae_22
type: Text To Image
frequency: 7
level: strong
coverage: 0.968714
common_nodes: [CLIPTextEncode, EmptyLatentImage, KSampler, SaveImage, VAEDecode]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Z-Image去网红感+QWEN自动反推提示词真实图生文生图_2012370345021415426.json, 图片生成/文生图/FLUX文生图基础工作流（极速版）_1947277056507793410.json, 图片生成/文生图/KREA2-CC人像版_2095722389442224130.json, 图片生成/文生图/Kook_Flux_klein_亚洲人像_2019704034847891458.json, 图片生成/文生图/Krea 2 分层控制_2072527998418513922.json, 图片生成/文生图/Krea 2 反推生图 +LoRA_2080138987389411330.json, 图片生成/文生图/Krea2的可解释性(这个偏原理性，看我B站教程)_2073829223965487105.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_vae_22

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/图生图/Z-Image去网红感+QWEN自动反推提示词真实图生文生图_2012370345021415426.json、图片生成/文生图/FLUX文生图基础工作流（极速版）_1947277056507793410.json、图片生成/文生图/KREA2-CC人像版_2095722389442224130.json、图片生成/文生图/Kook_Flux_klein_亚洲人像_2019704034847891458.json、图片生成/文生图/Krea 2 分层控制_2072527998418513922.json…）

- **类型**：Text To Image
- **样本数**：7
- **可信度**：强结论
- **平均知识覆盖**：97%

## 共有节点

全部 7 个 workflow 都包含：
- `CLIPTextEncode`
- `EmptyLatentImage`
- `KSampler`
- `SaveImage`
- `VAEDecode`

**可变部分**（部分 workflow 才有）：
- `CLIPLoader` —— 6/7 个有
- `LoraLoaderModelOnly` —— 6/7 个有
- `VAELoader` —— 6/7 个有
- `ConditioningZeroOut` —— 5/7 个有
- `UNETLoader` —— 5/7 个有
- `LoadImage` —— 3/7 个有
- `CheckpointLoaderSimple` —— 2/7 个有
- `ConditioningKrea2Rebalance` —— 2/7 个有
- `Seed (rgthree)` —— 2/7 个有
- `DownloadAndLoadFlorence2Model` —— 1/7 个有
- `DuckHideNode` —— 1/7 个有
- `Florence2Run` —— 1/7 个有
- `Qwen3VL_Advanced` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 720 - 1280 | 7 | 81% |
| 高度 | 1280 | 1024 - 1984 | 7 | 72% |
| 采样步数 | 8 | 8 - 10 | 7 | 89% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 7 | 100% |
| 采样算法 | euler | - | 7 | 86% |
| 调度器 | simple | - | 7 | 71% |
| 重绘幅度 | 1 | 1 - 1 | 7 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 14/7 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 1024，观测区间 720 - 1280，7 个样本，取值集中（一致性 81%）
- 高度 中位数 1280，观测区间 1024 - 1984，7 个样本
- 采样步数 中位数 8，观测区间 8 - 10，7 个样本，取值集中（一致性 89%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，7 个样本，一致性 86%
- 调度器 最常用 simple，7 个样本，一致性 71%
- 重绘幅度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 高发问题（14/7 个样本）：Steps较低可能导致细节不足

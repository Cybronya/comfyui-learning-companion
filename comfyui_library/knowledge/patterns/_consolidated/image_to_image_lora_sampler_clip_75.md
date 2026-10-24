---
name: image_to_image_lora_sampler_clip_75
type: Image To Image
frequency: 4
level: weak
coverage: 0.8625
common_nodes: [CLIPTextEncode, CheckpointLoaderSimple, KSampler, LoadImage, LoraLoaderModelOnly, SaveImage, VAEDecode, VAEEncode]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/SDXL图生图（含lora+固定种子）_2064230188745056257.json, 图片生成/图生图/klein4b-fp8 图生图_2020060758679228417.json, 图片生成/图生图/场景融合_2031968343585984514.json, 图片生成/图生图/高级人像质感+Qwen_Rebalance_1982003573984763906.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_clip_75

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/SDXL图生图（含lora+固定种子）_2064230188745056257.json、图片生成/图生图/klein4b-fp8 图生图_2020060758679228417.json、图片生成/图生图/场景融合_2031968343585984514.json、图片生成/图生图/高级人像质感+Qwen_Rebalance_1982003573984763906.json）

- **类型**：Image To Image
- **样本数**：4
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：86%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `SaveImage`
- `VAEDecode`
- `VAEEncode`

**可变部分**（部分 workflow 才有）：
- `Image Comparer (rgthree)` —— 3/4 个有
- `ConditioningZeroOut` —— 2/4 个有
- `LayerUtility: ImageScaleByAspectRatio` —— 2/4 个有
- `CLIPLoader` —— 1/4 个有
- `Latent Noise Injection` —— 1/4 个有
- `ModelSamplingDiscrete` —— 1/4 个有
- `Seed (rgthree)` —— 1/4 个有
- `UNETLoader` —— 1/4 个有
- `VAELoader` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 2 - 30 | 4 | 11% |
| Prompt 约束强度(CFG) | 1.4 | 1 - 5 | 4 | 25% |
| 采样算法 | euler | - | 4 | 50% |
| 调度器 | beta | - | 4 | 50% |
| 重绘幅度 | 0.275 | 0.2 - 0.7 | 4 | 45% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 2 - 30，4 个样本，取值分散，一致性仅 11%
- Prompt 约束强度(CFG) 中位数 1.4，观测区间 1 - 5，4 个样本，取值分散，一致性仅 25%
- 采样算法 最常用 euler，4 个样本，一致性 50%
- 调度器 最常用 beta，4 个样本，一致性 50%
- 重绘幅度 中位数 0.275，观测区间 0.2 - 0.7，4 个样本，取值分散，一致性仅 45%
- 高发问题（3/4 个样本）：Steps较低可能导致细节不足

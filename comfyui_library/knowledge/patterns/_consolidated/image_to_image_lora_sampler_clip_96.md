---
name: image_to_image_lora_sampler_clip_96
type: Image To Image
frequency: 3
level: weak
coverage: 0.858333
common_nodes: [CLIPTextEncode, CheckpointLoaderSimple, KSampler, LoadImage, LoraLoaderModelOnly, SaveImage, VAEDecode, VAEEncode]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/SDXL图生图（含lora+固定种子）_2064230188745056257.json, 图片生成/图生图/klein4b-fp8 图生图_2020060758679228417.json, 图片生成/图生图/场景融合_2031968343585984514.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_clip_96

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/SDXL图生图（含lora+固定种子）_2064230188745056257.json、图片生成/图生图/klein4b-fp8 图生图_2020060758679228417.json、图片生成/图生图/场景融合_2031968343585984514.json）

- **类型**：Image To Image
- **样本数**：3
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：86%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `SaveImage`
- `VAEDecode`
- `VAEEncode`

**可变部分**（部分 workflow 才有）：
- `Image Comparer (rgthree)` —— 2/3 个有
- `ConditioningZeroOut` —— 1/3 个有
- `LayerUtility: ImageScaleByAspectRatio` —— 1/3 个有
- `ModelSamplingDiscrete` —— 1/3 个有
- `Seed (rgthree)` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 2 - 30 | 3 | 10% |
| Prompt 约束强度(CFG) | 1.8 | 1 - 5 | 3 | 34% |
| 采样算法 | euler_ancestral | - | 3 | 33% |
| 调度器 | normal | - | 3 | 33% |
| 重绘幅度 | 0.25 | 0.2 - 0.7 | 3 | 41% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 2 - 30，3 个样本，取值分散，一致性仅 10%
- Prompt 约束强度(CFG) 中位数 1.8，观测区间 1 - 5，3 个样本，取值分散，一致性仅 34%
- 采样算法 最常用 euler_ancestral，3 个样本，一致性 33%
- 调度器 最常用 normal，3 个样本，一致性 33%
- 重绘幅度 中位数 0.25，观测区间 0.2 - 0.7，3 个样本，取值分散，一致性仅 41%
- 高发问题（2/3 个样本）：Steps较低可能导致细节不足

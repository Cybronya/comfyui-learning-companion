---
name: image_to_image_lora_sampler_unet_14
type: Image To Image
frequency: 3
level: moderate
coverage: 0.886667
common_nodes: [CLIPLoader, KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: [easy imageScaleDownToSize, LayerUtility: ImageScaleByAspectRatio V2]
members: [图片生成/图生图/2068683270535081985.json, 图片生成/图生图/2093230068645584897.json, 图片生成/图生图/2102280831946547201.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_unet_14

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/2068683270535081985.json、图片生成/图生图/2093230068645584897.json、图片生成/图生图/2102280831946547201.json）

- **类型**：Image To Image
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：89%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CFGNorm` —— 2/3 个有
- `TextEncodeQwenImageEditPlus` —— 2/3 个有
- `CLIPTextEncode` —— 1/3 个有
- `FluxKontextMultiReferenceLatentMethod` —— 1/3 个有
- `Image Comparer (rgthree)` —— 1/3 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/3 个有
- `QwenMultiangleCameraNode` —— 1/3 个有
- `RH_Nano_Banana2_Gemini31Flash` —— 1/3 个有
- `easy imageScaleDownToSize` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 4 - 22 | 3 | 32% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | simple | - | 3 | 67% |
| 重绘幅度 | 1 | 0.75 - 1 | 3 | 87% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 4 - 22，3 个样本，取值分散，一致性仅 32%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 simple，3 个样本，一致性 67%
- 重绘幅度 中位数 1，观测区间 0.75 - 1，3 个样本，取值集中（一致性 87%）
- 高发问题（2/3 个样本）：Steps较低可能导致细节不足
- 这些节点还没有知识卡，系统对它们的理解有限：easy imageScaleDownToSize、LayerUtility: ImageScaleByAspectRatio V2

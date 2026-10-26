---
name: image_to_image_lora_sampler_unet_161
type: Image To Image
frequency: 4
level: strong
coverage: 0.89075
common_nodes: [CFGNorm, CLIPLoader, FluxKontextMultiReferenceLatentMethod, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, SaveImage, TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/qwen-image-deit-2511单图多图，换装 打光 融图 转角度，提示词模板大全_2004105975781072898.json, 图片生成/图生图/qwen2511零位移图像编辑_2004809145012416513.json, 图片生成/图生图/万物套丝袜_2034969729160450050.json, 图片生成/图生图/多图万能处理（QWEN EDIT 2511）_2015346327189725186.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_unet_161

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/qwen-image-deit-2511单图多图，换装 打光 融图 转角度，提示词模板大全_2004105975781072898.json、图片生成/图生图/qwen2511零位移图像编辑_2004809145012416513.json、图片生成/图生图/万物套丝袜_2034969729160450050.json、图片生成/图生图/多图万能处理（QWEN EDIT 2511）_2015346327189725186.json）

- **类型**：Image To Image
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：89%

## 共有节点

全部 4 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `FluxKontextMultiReferenceLatentMethod`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `TextEncodeQwenImageEditPlus`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CR Text` —— 3/4 个有
- `Image Comparer (rgthree)` —— 2/4 个有
- `Int` —— 2/4 个有
- `ReferenceLatent` —— 2/4 个有
- `EmptyImage` —— 1/4 个有
- `Fast Groups Bypasser (rgthree)` —— 1/4 个有
- `RH_LLMAPI_NODE` —— 1/4 个有
- `SetLatentNoiseMask` —— 1/4 个有
- `ShowText|pysssss` —— 1/4 个有
- `TwoWaySwitch` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 4 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 4 | 100% |
| 采样算法 | euler | - | 4 | 75% |
| 调度器 | simple | - | 4 | 75% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，4 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，4 个样本，一致性 75%
- 调度器 最常用 simple，4 个样本，一致性 75%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 高发问题（4/4 个样本）：Steps较低可能导致细节不足

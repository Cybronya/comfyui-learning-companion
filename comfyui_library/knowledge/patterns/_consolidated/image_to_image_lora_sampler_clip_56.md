---
name: image_to_image_lora_sampler_clip_56
type: Image To Image
frequency: 5
level: weak
coverage: 0.8876
common_nodes: [CLIPLoader, CLIPTextEncode, Image Comparer (rgthree), KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Wan2.2洗图(单图)_1975814294828879873.json, 图片生成/图生图/人像去Ai油腻真实表现工作流_1964510532202020866.json, 图片生成/图生图/去除AI味重绘流_2085202651817533441.json, 图片生成/图生图/去除AI味重绘流_2085207804310282242.json, 图片生成/图生图/洗图+细节增强【WAN2.1】_1946052911623270402.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_clip_56

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/Wan2.2洗图(单图)_1975814294828879873.json、图片生成/图生图/人像去Ai油腻真实表现工作流_1964510532202020866.json、图片生成/图生图/去除AI味重绘流_2085202651817533441.json、图片生成/图生图/去除AI味重绘流_2085207804310282242.json、图片生成/图生图/洗图+细节增强【WAN2.1】_1946052911623270402.json）

- **类型**：Image To Image
- **样本数**：5
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：89%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `Image Comparer (rgthree)`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ModelSamplingSD3` —— 4/5 个有
- `RH_Captioner` —— 2/5 个有
- `easy showAnything` —— 2/5 个有
- `Anything Everywhere3` —— 1/5 个有
- `DeepTranslatorTextNode` —— 1/5 个有
- `LayerUtility: ImageScaleRestore` —— 1/5 个有
- `PDIMAGE_LongerSize` —— 1/5 个有
- `StringFunction|pysssss` —— 1/5 个有
- `Text Concatenate` —— 1/5 个有
- `Text Multiline` —— 1/5 个有
- `easy stylesSelector` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 6 | 6 - 10 | 5 | 76% |
| Prompt 约束强度(CFG) | 1 | 1 - 3.5 | 5 | 33% |
| 采样算法 | euler | - | 5 | 60% |
| 调度器 | simple | - | 5 | 60% |
| 重绘幅度 | 0.02 | 0.01 - 0.2 | 5 | 0% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 5/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 6，观测区间 6 - 10，5 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 3.5，5 个样本，取值分散，一致性仅 33%
- 采样算法 最常用 euler，5 个样本，一致性 60%
- 调度器 最常用 simple，5 个样本，一致性 60%
- 重绘幅度 中位数 0.02，观测区间 0.01 - 0.2，5 个样本，取值分散，一致性仅 0%
- 风险：重绘幅度 观测到 0.01，低于常用下限 0.1（）
- 高发问题（5/5 个样本）：Steps较低可能导致细节不足

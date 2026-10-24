---
name: image_to_image_lora_sampler_clip_77
type: Image To Image
frequency: 4
level: weak
coverage: 0.905
common_nodes: [CLIPLoader, CLIPTextEncode, Image Comparer (rgthree), KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, ModelSamplingSD3, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Wan2.2洗图(单图)_1975814294828879873.json, 图片生成/图生图/人像去Ai油腻真实表现工作流_1964510532202020866.json, 图片生成/图生图/去除AI味重绘流_2085202651817533441.json, 图片生成/图生图/去除AI味重绘流_2085207804310282242.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_clip_77

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/Wan2.2洗图(单图)_1975814294828879873.json、图片生成/图生图/人像去Ai油腻真实表现工作流_1964510532202020866.json、图片生成/图生图/去除AI味重绘流_2085202651817533441.json、图片生成/图生图/去除AI味重绘流_2085207804310282242.json）

- **类型**：Image To Image
- **样本数**：4
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：90%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `Image Comparer (rgthree)`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingSD3`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `DeepTranslatorTextNode` —— 1/4 个有
- `PDIMAGE_LongerSize` —— 1/4 个有
- `RH_Captioner` —— 1/4 个有
- `StringFunction|pysssss` —— 1/4 个有
- `easy showAnything` —— 1/4 个有
- `easy stylesSelector` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 6 | 6 - 6 | 4 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 3.5 | 4 | 33% |
| 采样算法 | euler | - | 4 | 75% |
| 调度器 | simple | - | 4 | 75% |
| 重绘幅度 | 0.02 | 0.01 - 0.2 | 4 | 0% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 5/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 6，观测区间 6 - 6，4 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 3.5，4 个样本，取值分散，一致性仅 33%
- 采样算法 最常用 euler，4 个样本，一致性 75%
- 调度器 最常用 simple，4 个样本，一致性 75%
- 重绘幅度 中位数 0.02，观测区间 0.01 - 0.2，4 个样本，取值分散，一致性仅 0%
- 风险：重绘幅度 观测到 0.01，低于常用下限 0.1（）
- 高发问题（5/4 个样本）：Steps较低可能导致细节不足

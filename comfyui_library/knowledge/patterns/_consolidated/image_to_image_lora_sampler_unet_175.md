---
name: image_to_image_lora_sampler_unet_175
type: Image To Image
frequency: 3
level: moderate
coverage: 0.916
common_nodes: [CFGNorm, CLIPLoader, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, SaveImage, TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen光影_2002990949435338754.json, 图片生成/图生图/image2，gemini2，Qwen2511文字生成对比_2049381140200427521.json, 图片生成/图生图/qwen-image-deit-2511单图多图，换装 打光 融图 转角度，提示词模板大全_2004105975781072898.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_unet_175

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/Qwen光影_2002990949435338754.json、图片生成/图生图/image2，gemini2，Qwen2511文字生成对比_2049381140200427521.json、图片生成/图生图/qwen-image-deit-2511单图多图，换装 打光 融图 转角度，提示词模板大全_2004105975781072898.json）

- **类型**：Image To Image
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：92%

## 共有节点

全部 3 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
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
- `CR Text` —— 2/3 个有
- `FluxKontextMultiReferenceLatentMethod` —— 2/3 个有
- `Image Comparer (rgthree)` —— 2/3 个有
- `Text` —— 2/3 个有
- `EmptyImage` —— 1/3 个有
- `Fast Groups Bypasser (rgthree)` —— 1/3 个有
- `Fast Groups Muter (rgthree)` —— 1/3 个有
- `Int` —— 1/3 个有
- `PreviewImage` —— 1/3 个有
- `RH_Nano_Banana2_Gemini31Flash` —— 1/3 个有
- `RH_RhartImageG2OfficialImageToImage` —— 1/3 个有
- `Text Concatenate` —— 1/3 个有
- `TwoWaySwitch` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 4 - 30 | 3 | 18% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | simple | - | 3 | 67% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 4 - 30，3 个样本，取值分散，一致性仅 18%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 simple，3 个样本，一致性 67%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 高发问题（2/3 个样本）：Steps较低可能导致细节不足

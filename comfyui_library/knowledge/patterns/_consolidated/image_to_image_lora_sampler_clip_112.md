---
name: image_to_image_lora_sampler_clip_112
type: Image To Image
frequency: 3
level: moderate
coverage: 0.895667
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, Image Comparer (rgthree), KSampler, LayerMask: MaskGrow, LayerUtility: ImageMaskScaleAs, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, PreviewImage, ReferenceLatent, SaveImage, Text, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/平台用-汽车合成保留细节_2061249533987868674.json, 图片生成/图生图/汽车合成保留细节_2090248247645396994.json, 图片生成/图生图/通道ID图2.1_2061262748247486466.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_clip_112

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/平台用-汽车合成保留细节_2061249533987868674.json、图片生成/图生图/汽车合成保留细节_2090248247645396994.json、图片生成/图生图/通道ID图2.1_2061262748247486466.json）

- **类型**：Image To Image
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：90%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `Image Comparer (rgthree)`
- `KSampler`
- `LayerMask: MaskGrow`
- `LayerUtility: ImageMaskScaleAs`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PreviewImage`
- `ReferenceLatent`
- `SaveImage`
- `Text`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CheckpointLoaderSimple` —— 2/3 个有
- `GetImageSize` —— 2/3 个有
- `Image Premultiply (mtb)` —— 2/3 个有
- `LayerUtility: HLFrequencyDetailRestore` —— 2/3 个有
- `RH_Translator` —— 2/3 个有
- `SAM3_Detect` —— 2/3 个有
- `LayerMask: BiRefNetUltraV2` —— 1/3 个有
- `LayerMask: LoadBiRefNetModelV2` —— 1/3 个有
- `LayerStyle: ColorOverlay V2` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 10 | 3 | 53% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | simple | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 10，3 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 simple，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 高发问题（2/3 个样本）：Steps较低可能导致细节不足

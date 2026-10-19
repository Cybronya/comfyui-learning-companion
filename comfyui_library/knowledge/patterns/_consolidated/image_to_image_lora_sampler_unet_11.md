---
name: image_to_image_lora_sampler_unet_11
type: Image To Image
frequency: 4
level: moderate
coverage: 0.8945
common_nodes: [CFGNorm, CLIPLoader, ImageStitch, KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, SaveImage, TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: [LayerUtility: ImageScaleByAspectRatio V2, Text Multiline]
members: [图片生成/文生图/1986720327151595522.json, 图片生成/文生图/1986721390671949825.json, 数字人/数字人/人物-一键换装-文字描述版_2109828236317380609.json, 数字人/数字人/人物-一键换装-服装图版_2109490336476262401.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_unet_11

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/文生图/1986720327151595522.json、图片生成/文生图/1986721390671949825.json、数字人/数字人/人物-一键换装-文字描述版_2109828236317380609.json、数字人/数字人/人物-一键换装-服装图版_2109490336476262401.json）

- **类型**：Image To Image
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：89%

## 共有节点

全部 4 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `ImageStitch`
- `KSampler`
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
- `ConditioningZeroOut` —— 2/4 个有
- `FluxKontextImageScale` —— 2/4 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/4 个有
- `StringConcatenate` —— 2/4 个有
- `StringConstantMultiline` —— 2/4 个有
- `Text Multiline` —— 2/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 12 | 4 - 20 | 4 | 33% |
| Prompt 约束强度(CFG) | 1.75 | 1 - 2.5 | 4 | 57% |
| 采样算法 | euler | - | 4 | 100% |
| 调度器 | simple | - | 4 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 12，观测区间 4 - 20，4 个样本，取值分散，一致性仅 33%
- Prompt 约束强度(CFG) 中位数 1.75，观测区间 1 - 2.5，4 个样本
- 采样算法 最常用 euler，4 个样本，一致性 100%
- 调度器 最常用 simple，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 高发问题（2/4 个样本）：Steps较低可能导致细节不足
- 这些节点还没有知识卡，系统对它们的理解有限：LayerUtility: ImageScaleByAspectRatio V2、Text Multiline

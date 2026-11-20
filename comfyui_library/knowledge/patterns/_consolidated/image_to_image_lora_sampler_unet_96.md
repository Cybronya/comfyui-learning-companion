---
name: image_to_image_lora_sampler_unet_96
type: Image To Image
frequency: 7
level: strong
coverage: 0.916143
common_nodes: [CLIPLoader, KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, SaveImage, TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/图生图(一生三图版)_2039549230775279618.json, 图片生成/图生图/图生图111_2039507362217730050.json, 图片生成/图生图/图生图工作流_2050738339095040002.json, 图片生成/图生图/场景一键多角度切换Qwen-Edit-2509_1991347951650058242.json, 图片生成/图生图/多图融合编辑-Qwen Image Edit2509_1977676716300730369.json, 图片生成/图生图/工作流系列10-物品多视角工作流-基于QWEN-EDIT-2511_2056559560298684417.json, 图片生成/图生图/移除、换背景、换色、模特图、改文字-Qwen Image Edit2509_1976837741126336513.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_unet_96

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/图生图/图生图(一生三图版)_2039549230775279618.json、图片生成/图生图/图生图111_2039507362217730050.json、图片生成/图生图/图生图工作流_2050738339095040002.json、图片生成/图生图/场景一键多角度切换Qwen-Edit-2509_1991347951650058242.json、图片生成/图生图/多图融合编辑-Qwen Image Edit2509_1977676716300730369.json…）

- **类型**：Image To Image
- **样本数**：7
- **可信度**：强结论
- **平均知识覆盖**：92%

## 共有节点

全部 7 个 workflow 都包含：
- `CLIPLoader`
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
- `CFGNorm` —— 5/7 个有
- `ImageScaleToTotalPixels` —— 4/7 个有
- `PreviewImage` —— 4/7 个有
- `ConditioningZeroOut` —— 3/7 个有
- `Image Comparer (rgthree)` —— 3/7 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 3/7 个有
- `QwenMultiangleCameraNode` —— 3/7 个有
- `Seed (rgthree)` —— 3/7 个有
- `KepStringList` —— 2/7 个有
- `Label (rgthree)` —— 2/7 个有
- `Note Plus (mtb)` —— 2/7 个有
- `TextEncodeQwenImageEditPlusAdvance_lrzjason` —— 2/7 个有
- `TextInput_` —— 2/7 个有
- `AddLabel` —— 1/7 个有
- `easy promptLine` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 4 - 9 | 7 | 72% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 7 | 100% |
| 采样算法 | euler | - | 7 | 71% |
| 调度器 | simple | - | 7 | 57% |
| 重绘幅度 | 1 | 1 - 1 | 7 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 17/7 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 4 - 9，7 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，7 个样本，一致性 71%
- 调度器 最常用 simple，7 个样本，一致性 57%
- 重绘幅度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 高发问题（17/7 个样本）：Steps较低可能导致细节不足

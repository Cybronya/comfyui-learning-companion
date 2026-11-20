---
name: text_to_image_lora_sampler_clip_75
type: Text To Image
frequency: 15
level: moderate
coverage: 0.946933
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyLatentImage, ImageScaleToTotalPixels, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoader, PIP_图像联结, ReferenceLatent, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/切换视角和动作-klein9b_2027969479132585986.json, 图片生成/图生图/国漫cg风格-klein9b_2024460012998893570.json, 图片生成/图生图/国漫cg风格-klein9b_2028102345585860609.json, 图片生成/图生图/国漫cg风格-klein9b_2031990103983263746.json, 图片生成/图生图/国漫cg风格-klein9b_2052665732449751042.json, 图片生成/图生图/国漫cg风格-klein9b_2067121185074274306.json, 图片生成/图生图/真人转CG风格-klein9b_2059182977392930817.json, 图片生成/图生图/真人转CG风格-klein9b_2094958094802579458.json, 图片生成/图生图/真人转cg风格-klein9b_2052675274935939073.json, 图片生成/图生图/真人转cg风格_2108739746154500098.json, 图片生成/图生图/真人转国漫cg风格-klein9b_2057723052485599234.json, 图片生成/图生图/真人转国漫cg风格-klein9b_2061408134274568193.json, 图片生成/图生图/真人转国漫cg风格-klein9b_2061671172663758850.json, 图片生成/图生图/轮回插画风格-klein9b_2026225008095268866.json, 图片生成/图生图/鬼刀插画风格-klein9b_2029692807648120833.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_75

> 由 `engine/knowledge_consolidation` 从 15 个 workflow 归纳得出（图片生成/图生图/切换视角和动作-klein9b_2027969479132585986.json、图片生成/图生图/国漫cg风格-klein9b_2024460012998893570.json、图片生成/图生图/国漫cg风格-klein9b_2028102345585860609.json、图片生成/图生图/国漫cg风格-klein9b_2031990103983263746.json、图片生成/图生图/国漫cg风格-klein9b_2052665732449751042.json…）

- **类型**：Text To Image
- **样本数**：15
- **可信度**：中等可信
- **平均知识覆盖**：95%

## 共有节点

全部 15 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `ImageScaleToTotalPixels`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoader`
- `PIP_图像联结`
- `ReferenceLatent`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `JjkText` —— 12/15 个有
- `CR Prompt List` —— 2/15 个有
- `GetImage` —— 2/15 个有
- `LineArtPreprocessor` —— 2/15 个有
- `MuyeImageBlendingMode` —— 2/15 个有
- `PreviewImage` —— 2/15 个有
- `FlashVSRNode` —— 1/15 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 512 | 512 - 1920 | 15 | 34% |
| 高度 | 512 | 512 - 1536 | 15 | 54% |
| 采样步数 | 4 | 2 - 8 | 15 | 68% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 15 | 100% |
| 采样算法 | euler | - | 15 | 100% |
| 调度器 | beta | - | 15 | 80% |
| 重绘幅度 | 1 | 1 - 1 | 15 | 100% |
| LoRA 模型强度 | 1 | 1 - 1 | 15 | 100% |
| LoRA 文本强度 | 1 | 1 - 1 | 15 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 15/15 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 512，观测区间 512 - 1920，15 个样本，取值分散，一致性仅 34%
- 高度 中位数 512，观测区间 512 - 1536，15 个样本
- 采样步数 中位数 4，观测区间 2 - 8，15 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，15 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，15 个样本，一致性 100%
- 调度器 最常用 beta，15 个样本，一致性 80%
- 重绘幅度 中位数 1，观测区间 1 - 1，15 个样本，取值集中（一致性 100%）
- LoRA 模型强度 中位数 1，观测区间 1 - 1，15 个样本，取值集中（一致性 100%）
- LoRA 文本强度 中位数 1，观测区间 1 - 1，15 个样本，取值集中（一致性 100%）
- 高发问题（15/15 个样本）：Steps较低可能导致细节不足

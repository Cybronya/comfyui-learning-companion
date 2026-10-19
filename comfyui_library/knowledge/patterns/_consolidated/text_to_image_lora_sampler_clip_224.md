---
name: text_to_image_lora_sampler_clip_224
type: Text To Image
frequency: 3
level: moderate
coverage: 0.894
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, KSampler, LoraLoaderModelOnly, ModelSamplingAuraFlow, RHHiddenNodes, SaveImage, Textbox, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: [LayerUtility: ColorImage V2, LayerUtility: ImageCombineAlpha, Text Multiline, easy int, CR SDXL Aspect Ratio]
members: [图片生成/文生图/1953640642129920001.json, 图片生成/文生图/1955456412216430594.json, 图片生成/文生图/1955557022977572865.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_224

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/1953640642129920001.json、图片生成/文生图/1955456412216430594.json、图片生成/文生图/1955557022977572865.json）

- **类型**：Text To Image
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：89%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `KSampler`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `RHHiddenNodes`
- `SaveImage`
- `Textbox`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CR SDXL Aspect Ratio` —— 1/3 个有
- `ImageToMask` —— 1/3 个有
- `LayerUtility: ColorImage V2` —— 1/3 个有
- `LayerUtility: ImageCombineAlpha` —— 1/3 个有
- `Text Multiline` —— 1/3 个有
- `easy int` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1104 | 512 - 1104 | 3 | 69% |
| 高度 | 1472 | 512 - 1472 | 3 | 61% |
| 采样步数 | 20 | 8 - 20 | 3 | 65% |
| Prompt 约束强度(CFG) | 2.5 | 2.5 - 2.5 | 3 | 100% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | simple | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 1104，观测区间 512 - 1104，3 个样本
- 高度 中位数 1472，观测区间 512 - 1472，3 个样本
- 采样步数 中位数 20，观测区间 8 - 20，3 个样本
- Prompt 约束强度(CFG) 中位数 2.5，观测区间 2.5 - 2.5，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 simple，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 这些节点还没有知识卡，系统对它们的理解有限：LayerUtility: ColorImage V2、LayerUtility: ImageCombineAlpha、Text Multiline、easy int、CR SDXL Aspect Ratio

---
name: image_to_image_lora_sampler_unet_18
type: Image To Image
frequency: 5
level: strong
coverage: 0.6428
common_nodes: [CFGNorm, CLIPLoader, CR Overlay Text, CR Text, ImageFromBatch, ImageListToImageBatch, ImageScaleToTotalPixels, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, PreviewImage, SaveImage, String Literal, Text, TextEncodeQwenImageEdit, TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: [CR Overlay Text, CR Text, LayerUtility: ImageScaleByAspectRatio V2, SDVM Image List Repeat, String Literal, easy batchAnything, easy forLoopEnd, CR Text Concatenate, easy promptList]
members: [图片生成/文生图/1982644350511390722.json, 图片生成/文生图/1983145644221210625.json, 图片生成/文生图/1983150926611554306.json, 图片生成/文生图/1985867106191323137.json, 视频生成/图生视频/1982644350511390722.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_unet_18

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/文生图/1982644350511390722.json、图片生成/文生图/1983145644221210625.json、图片生成/文生图/1983150926611554306.json、图片生成/文生图/1985867106191323137.json、视频生成/图生视频/1982644350511390722.json）

- **类型**：Image To Image
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：64%

## 共有节点

全部 5 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `CR Overlay Text`
- `CR Text`
- `ImageFromBatch`
- `ImageListToImageBatch`
- `ImageScaleToTotalPixels`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `PreviewImage`
- `SaveImage`
- `String Literal`
- `Text`
- `TextEncodeQwenImageEdit`
- `TextEncodeQwenImageEditPlus`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ImageConcatFromBatch` —— 4/5 个有
- `RHHiddenNodes` —— 4/5 个有
- `SDVM Image List Repeat` —— 4/5 个有
- `easy batchAnything` —— 4/5 个有
- `easy forLoopEnd` —— 4/5 个有
- `CR Text Concatenate` —— 1/5 个有
- `DeepTranslatorTextNode` —— 1/5 个有
- `GODMT_ListSlice` —— 1/5 个有
- `ImageConcatMulti` —— 1/5 个有
- `JDCN_ListToString` —— 1/5 个有
- `RH_LLMAPI_NODE` —— 1/5 个有
- `ShowText|pysssss` —— 1/5 个有
- `TextListSplit` —— 1/5 个有
- `easy promptList` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 8 | 5 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 5 | 100% |
| 采样算法 | euler | - | 5 | 80% |
| 调度器 | simple | - | 5 | 80% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 5/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 8，5 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，5 个样本，一致性 80%
- 调度器 最常用 simple，5 个样本，一致性 80%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 高发问题（5/5 个样本）：Steps较低可能导致细节不足
- 这些节点还没有知识卡，系统对它们的理解有限：CR Overlay Text、CR Text、LayerUtility: ImageScaleByAspectRatio V2、SDVM Image List Repeat、String Literal

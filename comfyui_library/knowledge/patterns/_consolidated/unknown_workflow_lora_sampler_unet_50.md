---
name: unknown_workflow_lora_sampler_unet_50
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.667
common_nodes: [CLIPLoader, EmptySD3LatentImage, GetNode, KSampler, LoadImage, LoraLoaderModelOnly, SaveImage, SetNode, TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: [Label (rgthree), GetImageSize+]
members: [图片生成/文生图/1974486765111218177.json, 图片生成/文生图/Qwen Edit Plus 2image_2005489054781243393.json, 视频生成/图生视频/2029100909296361474.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_50

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/1974486765111218177.json、图片生成/文生图/Qwen Edit Plus 2image_2005489054781243393.json、视频生成/图生视频/2029100909296361474.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：67%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `EmptySD3LatentImage`
- `GetNode`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `SaveImage`
- `SetNode`
- `TextEncodeQwenImageEditPlus`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CFGNorm` —— 2/3 个有
- `ImageResizeKJv2` —— 2/3 个有
- `LayerUtility: PurgeVRAM` —— 2/3 个有
- `ModelSamplingAuraFlow` —— 2/3 个有
- `PrimitiveInt` —— 2/3 个有
- `Text Multiline` —— 2/3 个有
- `ConditioningZeroOut` —— 1/3 个有
- `GetImageSize+` —— 1/3 个有
- `ImageConcatMulti` —— 1/3 个有
- `ImageScaleToTotalPixels` —— 1/3 个有
- `ImageStitch` —— 1/3 个有
- `Label (rgthree)` —— 1/3 个有
- `TextEncodeQwenImageEdit` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 4 - 8 | 3 | 72% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | simple | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 4 - 8，3 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 simple，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 高发问题（3/3 个样本）：Steps较低可能导致细节不足
- 这些节点还没有知识卡，系统对它们的理解有限：Label (rgthree)、GetImageSize+

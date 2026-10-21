---
name: unknown_workflow_lora_sampler_unet_37
type: Unknown Workflow
frequency: 4
level: strong
coverage: 0.814
common_nodes: [CFGNorm, CLIPLoader, ConditioningZeroOut, EmptySD3LatentImage, GetImageSize, ImageScaleToTotalPixels, ImageStitch, KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, PreviewImage, SaveImage, TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: [LayerUtility: PurgeVRAM V2, Text Multiline, easy joinImageBatch, CR Text, ImageCASharpening+, Text Concatenate]
members: [图片生成/文生图/1978372865714229249.json, 图片生成/文生图/1979932270746308610.json, 图片生成/文生图/1983355804264898562.json, 图片生成/文生图/1983422173471776770.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_37

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/文生图/1978372865714229249.json、图片生成/文生图/1979932270746308610.json、图片生成/文生图/1983355804264898562.json、图片生成/文生图/1983422173471776770.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：81%

## 共有节点

全部 4 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `ConditioningZeroOut`
- `EmptySD3LatentImage`
- `GetImageSize`
- `ImageScaleToTotalPixels`
- `ImageStitch`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `PreviewImage`
- `SaveImage`
- `TextEncodeQwenImageEditPlus`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ImageBatch` —— 3/4 个有
- `PrimitiveInt` —— 3/4 个有
- `Text Multiline` —— 3/4 个有
- `easy joinImageBatch` —— 3/4 个有
- `Fast Groups Bypasser (rgthree)` —— 2/4 个有
- `LayerUtility: PurgeVRAM V2` —— 2/4 个有
- `ShowText|pysssss` —— 2/4 个有
- `Text Concatenate` —— 2/4 个有
- `CR Text` —— 1/4 个有
- `DWPreprocessor` —— 1/4 个有
- `ImageCASharpening+` —— 1/4 个有
- `Int` —— 1/4 个有
- `RMBG` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 8 | 4 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 4 | 100% |
| 采样算法 | euler | - | 4 | 100% |
| 调度器 | simple | - | 4 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 7/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 8，4 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，4 个样本，一致性 100%
- 调度器 最常用 simple，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 高发问题（7/4 个样本）：Steps较低可能导致细节不足
- 这些节点还没有知识卡，系统对它们的理解有限：LayerUtility: PurgeVRAM V2、Text Multiline、easy joinImageBatch、CR Text、ImageCASharpening+

---
name: unknown_workflow_lora_sampler_unet_39
type: Unknown Workflow
frequency: 4
level: strong
coverage: 0.93975
common_nodes: [CLIPLoader, EmptyLatentImage, ImageScaleToTotalPixels, KSampler, LoadImage, LoraLoaderModelOnly, SaveImage, TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Qwen Image Edit 2511_2004568468768915457.json, 图片生成/文生图/Qwen-Image Edit Plus换装双人同框_1994201692587622402.json, 图片生成/文生图/qwen_image_edit_2511_2003692026312966146.json, 图片生成/文生图/换装同服装双人或者多人同框_1994237410244493314.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_39

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/文生图/Qwen Image Edit 2511_2004568468768915457.json、图片生成/文生图/Qwen-Image Edit Plus换装双人同框_1994201692587622402.json、图片生成/文生图/qwen_image_edit_2511_2003692026312966146.json、图片生成/文生图/换装同服装双人或者多人同框_1994237410244493314.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：94%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `EmptyLatentImage`
- `ImageScaleToTotalPixels`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `SaveImage`
- `TextEncodeQwenImageEditPlus`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CFGNorm` —— 3/4 个有
- `ModelSamplingAuraFlow` —— 3/4 个有
- `BiRefNetRMBG` —— 2/4 个有
- `ConstrainImage|pysssss` —— 2/4 个有
- `LayerUtility: ExtendCanvas` —— 2/4 个有
- `PreviewImage` —— 2/4 个有
- `FluxKontextMultiReferenceLatentMethod` —— 1/4 个有
- `GetImageSizeAndCount` —— 1/4 个有
- `UnetLoaderGGUF` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 4 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 4 | 100% |
| 采样算法 | euler | - | 4 | 100% |
| 调度器 | simple | - | 4 | 50% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |
| 宽度 | 1024 | 768 - 1280 | 4 | 82% |
| 高度 | 1280 | 720 - 1536 | 4 | 71% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 6/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，4 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，4 个样本，一致性 100%
- 调度器 最常用 simple，4 个样本，一致性 50%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 宽度 中位数 1024，观测区间 768 - 1280，4 个样本，取值集中（一致性 82%）
- 高度 中位数 1280，观测区间 720 - 1536，4 个样本
- 高发问题（6/4 个样本）：Steps较低可能导致细节不足

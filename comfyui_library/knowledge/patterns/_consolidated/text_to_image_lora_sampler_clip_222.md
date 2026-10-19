---
name: text_to_image_lora_sampler_clip_222
type: Text To Image
frequency: 3
level: strong
coverage: 0.483
common_nodes: [Anything Everywhere, CLIPTextEncode, Display Any (rgthree), EmptyImage, EmptyLatentImage, GODMT_SplitString, GetNode, ImageBatch, Int, KSampler, LoraLoader, Manual XY Entry Info, PreviewImage, PrimitiveStringMultiline, SaveImage, SetNode, Text Load Line From File, UNETLoader, VAEDecode, VAELoader, easy forLoopEnd, easy forLoopStart, easy seed]
problems: []
missing: [Display Any (rgthree), Manual XY Entry Info, Text Load Line From File, easy forLoopEnd, easy forLoopStart, easy seed, LayerMask: BiRefNetUltraV2, LayerMask: LoadBiRefNetModelV2, LayerUtility: ImageScaleByAspectRatio V2]
members: [图片生成/文生图/1945128839305678849.json, 图片生成/文生图/1963602782727147522.json, 图片生成/文生图/1964237525097267201.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_222

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/1945128839305678849.json、图片生成/文生图/1963602782727147522.json、图片生成/文生图/1964237525097267201.json）

- **类型**：Text To Image
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：48%

## 共有节点

全部 3 个 workflow 都包含：
- `Anything Everywhere`
- `CLIPTextEncode`
- `Display Any (rgthree)`
- `EmptyImage`
- `EmptyLatentImage`
- `GODMT_SplitString`
- `GetNode`
- `ImageBatch`
- `Int`
- `KSampler`
- `LoraLoader`
- `Manual XY Entry Info`
- `PreviewImage`
- `PrimitiveStringMultiline`
- `SaveImage`
- `SetNode`
- `Text Load Line From File`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy forLoopEnd`
- `easy forLoopStart`
- `easy seed`

**可变部分**（部分 workflow 才有）：
- `ConditioningZeroOut` —— 2/3 个有
- `DualCLIPLoader` —— 2/3 个有
- `FluxGuidance` —— 2/3 个有
- `CLIPLoader` —— 1/3 个有
- `InvertMask` —— 1/3 个有
- `JoinImageWithAlpha` —— 1/3 个有
- `LayerMask: BiRefNetUltraV2` —— 1/3 个有
- `LayerMask: LoadBiRefNetModelV2` —— 1/3 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/3 个有
- `ModelSamplingAuraFlow` —— 1/3 个有
- `ResizeMask` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| LoRA 模型强度 | 1 | 0.93 - 1 | 3 | 97% |
| LoRA 文本强度 | 1 | 1 - 1 | 3 | 100% |
| 采样步数 | 20 | 20 - 20 | 3 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 2.5 | 3 | 53% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | normal | - | 3 | 67% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |
| 宽度 | 1280 | 1280 - 1280 | 3 | 100% |
| 高度 | 720 | 720 - 720 | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- LoRA 模型强度 中位数 1，观测区间 0.93 - 1，3 个样本，取值集中（一致性 97%）
- LoRA 文本强度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样步数 中位数 20，观测区间 20 - 20，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 2.5，3 个样本
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 normal，3 个样本，一致性 67%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 宽度 中位数 1280，观测区间 1280 - 1280，3 个样本，取值集中（一致性 100%）
- 高度 中位数 720，观测区间 720 - 720，3 个样本，取值集中（一致性 100%）
- 这些节点还没有知识卡，系统对它们的理解有限：Display Any (rgthree)、Manual XY Entry Info、Text Load Line From File、easy forLoopEnd、easy forLoopStart

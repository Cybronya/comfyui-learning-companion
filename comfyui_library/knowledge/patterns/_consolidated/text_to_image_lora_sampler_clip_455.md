---
name: text_to_image_lora_sampler_clip_455
type: Text To Image
frequency: 4
level: strong
coverage: 0.66075
common_nodes: [Anything Everywhere, CLIPTextEncode, Display Any (rgthree), EmptyImage, EmptyLatentImage, GODMT_SplitString, GetNode, ImageBatch, Int, KSampler, LoraLoader, Manual XY Entry Info, PreviewImage, PrimitiveStringMultiline, SaveImage, SetNode, Text Load Line From File, UNETLoader, VAEDecode, VAELoader, easy forLoopEnd, easy forLoopStart, easy seed]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/批量文生图(FLUX版)_1945128839305678849.json, 图片生成/文生图/批量文生图(Qwen版本)_1964237525097267201.json, 图片生成/文生图/批量文生图(Z-image版)_1997631900376346625.json, 图片生成/文生图/批量生成透明PNG素材(文生图+抠图)_1963602782727147522.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_455

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/文生图/批量文生图(FLUX版)_1945128839305678849.json、图片生成/文生图/批量文生图(Qwen版本)_1964237525097267201.json、图片生成/文生图/批量文生图(Z-image版)_1997631900376346625.json、图片生成/文生图/批量生成透明PNG素材(文生图+抠图)_1963602782727147522.json）

- **类型**：Text To Image
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：66%

## 共有节点

全部 4 个 workflow 都包含：
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
- `ConditioningZeroOut` —— 3/4 个有
- `CLIPLoader` —— 2/4 个有
- `DualCLIPLoader` —— 2/4 个有
- `FluxGuidance` —— 2/4 个有
- `InvertMask` —— 1/4 个有
- `JoinImageWithAlpha` —— 1/4 个有
- `LayerMask: BiRefNetUltraV2` —— 1/4 个有
- `LayerMask: LoadBiRefNetModelV2` —— 1/4 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/4 个有
- `ModelSamplingAuraFlow` —— 1/4 个有
- `ResizeMask` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| LoRA 模型强度 | 1 | 0.93 - 1 | 4 | 97% |
| LoRA 文本强度 | 1 | 1 - 1 | 4 | 100% |
| 采样步数 | 20 | 9 - 20 | 4 | 72% |
| Prompt 约束强度(CFG) | 1 | 1 - 2.5 | 4 | 53% |
| 采样算法 | euler | - | 4 | 100% |
| 调度器 | normal | - | 4 | 50% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |
| 宽度 | 1280 | 1280 - 1280 | 4 | 100% |
| 高度 | 720 | 720 - 720 | 4 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- LoRA 模型强度 中位数 1，观测区间 0.93 - 1，4 个样本，取值集中（一致性 97%）
- LoRA 文本强度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样步数 中位数 20，观测区间 9 - 20，4 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 2.5，4 个样本
- 采样算法 最常用 euler，4 个样本，一致性 100%
- 调度器 最常用 normal，4 个样本，一致性 50%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 宽度 中位数 1280，观测区间 1280 - 1280，4 个样本，取值集中（一致性 100%）
- 高度 中位数 720，观测区间 720 - 720，4 个样本，取值集中（一致性 100%）

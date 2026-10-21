---
name: image_to_image_sampler_vae_2
type: Image To Image
frequency: 5
level: strong
coverage: 0.4152
common_nodes: [Any Switch (rgthree), CFGNorm, CLIPLoader, EmptyLatentImage, GetNode, ImageScaleToTotalPixels, KSampler, LoadImage, ModelPatchTorchSettings, ModelSamplingAuraFlow, PathchSageAttentionKJ, PrimitiveInt, PrimitiveString, PrimitiveStringMultiline, SaveImage, SetNode, StringConcatenate, TextEncodeQwenImageEditPlus, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: [Label (rgthree), Mute / Bypass Relay (rgthree), Mute / Bypass Repeater (rgthree), easy bookmark]
members: [图片生成/文生图/1978121708173451266.json, 图片生成/文生图/1980485872774762497.json, 图片生成/文生图/qwen多视角生成图片_2001986168365412353.json, 图片生成/文生图/一张图出人物全角度V2-人物一致性-加速版一次性出15张人物一致性图片_2095333742851223554.json, 图片生成/文生图/一张图生成人物全角度_2011206036333535234.json]
source: knowledge_consolidation
---

# image_to_image_sampler_vae_2

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/文生图/1978121708173451266.json、图片生成/文生图/1980485872774762497.json、图片生成/文生图/qwen多视角生成图片_2001986168365412353.json、图片生成/文生图/一张图出人物全角度V2-人物一致性-加速版一次性出15张人物一致性图片_2095333742851223554.json、图片生成/文生图/一张图生成人物全角度_2011206036333535234.json）

- **类型**：Image To Image
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：42%

## 共有节点

全部 5 个 workflow 都包含：
- `Any Switch (rgthree)`
- `CFGNorm`
- `CLIPLoader`
- `EmptyLatentImage`
- `GetNode`
- `ImageScaleToTotalPixels`
- `KSampler`
- `LoadImage`
- `ModelPatchTorchSettings`
- `ModelSamplingAuraFlow`
- `PathchSageAttentionKJ`
- `PrimitiveInt`
- `PrimitiveString`
- `PrimitiveStringMultiline`
- `SaveImage`
- `SetNode`
- `StringConcatenate`
- `TextEncodeQwenImageEditPlus`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Label (rgthree)` —— 4/5 个有
- `Mute / Bypass Relay (rgthree)` —— 4/5 个有
- `Mute / Bypass Repeater (rgthree)` —— 4/5 个有
- `RHHiddenNodes` —— 4/5 个有
- `easy bookmark` —— 4/5 个有
- `ImageFlip` —— 3/5 个有
- `Fast Groups Muter (rgthree)` —— 1/5 个有
- `GeminiImageNode` —— 1/5 个有
- `LoraLoaderModelOnly` —— 1/5 个有
- `UNETLoader` —— 1/5 个有
- `孤海注释` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 960 | 480 - 960 | 5 | 76% |
| 高度 | 1304 | 832 - 1304 | 5 | 83% |
| 采样步数 | 8 | 8 - 8 | 5 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 5 | 100% |
| 采样算法 | euler | - | 5 | 100% |
| 调度器 | simple | - | 5 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 83/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 960，观测区间 480 - 960，5 个样本
- 高度 中位数 1304，观测区间 832 - 1304，5 个样本，取值集中（一致性 83%）
- 采样步数 中位数 8，观测区间 8 - 8，5 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，5 个样本，一致性 100%
- 调度器 最常用 simple，5 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 高发问题（83/5 个样本）：Steps较低可能导致细节不足
- 这些节点还没有知识卡，系统对它们的理解有限：Label (rgthree)、Mute / Bypass Relay (rgthree)、Mute / Bypass Repeater (rgthree)、easy bookmark

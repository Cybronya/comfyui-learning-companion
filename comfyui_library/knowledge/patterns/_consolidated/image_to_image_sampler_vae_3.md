---
name: image_to_image_sampler_vae_3
type: Image To Image
frequency: 2
level: weak
coverage: 0.375
common_nodes: [Any Switch (rgthree), CFGNorm, CLIPLoader, EmptyLatentImage, GetNode, ImageFlip, ImageScaleToTotalPixels, KSampler, Label (rgthree), LoadImage, ModelPatchTorchSettings, ModelSamplingAuraFlow, Mute / Bypass Relay (rgthree), Mute / Bypass Repeater (rgthree), PathchSageAttentionKJ, PrimitiveInt, PrimitiveString, PrimitiveStringMultiline, RHHiddenNodes, SaveImage, SetNode, StringConcatenate, TextEncodeQwenImageEditPlus, VAEDecode, VAEEncode, VAELoader, easy bookmark]
problems: [Steps较低可能导致细节不足]
missing: [Label (rgthree), Mute / Bypass Relay (rgthree), Mute / Bypass Repeater (rgthree), easy bookmark]
members: [图片生成/文生图/1978121708173451266.json, 图片生成/文生图/1980485872774762497.json]
source: knowledge_consolidation
---

# image_to_image_sampler_vae_3

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/1978121708173451266.json、图片生成/文生图/1980485872774762497.json）

- **类型**：Image To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：38%

## 共有节点

全部 2 个 workflow 都包含：
- `Any Switch (rgthree)`
- `CFGNorm`
- `CLIPLoader`
- `EmptyLatentImage`
- `GetNode`
- `ImageFlip`
- `ImageScaleToTotalPixels`
- `KSampler`
- `Label (rgthree)`
- `LoadImage`
- `ModelPatchTorchSettings`
- `ModelSamplingAuraFlow`
- `Mute / Bypass Relay (rgthree)`
- `Mute / Bypass Repeater (rgthree)`
- `PathchSageAttentionKJ`
- `PrimitiveInt`
- `PrimitiveString`
- `PrimitiveStringMultiline`
- `RHHiddenNodes`
- `SaveImage`
- `SetNode`
- `StringConcatenate`
- `TextEncodeQwenImageEditPlus`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy bookmark`

**可变部分**（部分 workflow 才有）：
- `Fast Groups Muter (rgthree)` —— 1/2 个有
- `GeminiImageNode` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 840 | - | 2 | 86% |
| 高度 | 1164 | - | 2 | 88% |
| 采样步数 | 8 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | euler | - | 2 | 100% |
| 调度器 | simple | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 29/2 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 840，样本不足，未给区间，2 个样本，取值集中（一致性 86%）
- 高度 中位数 1164，样本不足，未给区间，2 个样本，取值集中（一致性 88%）
- 采样步数 中位数 8，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，2 个样本，一致性 100%
- 调度器 最常用 simple，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高发问题（29/2 个样本）：Steps较低可能导致细节不足
- 这些节点还没有知识卡，系统对它们的理解有限：Label (rgthree)、Mute / Bypass Relay (rgthree)、Mute / Bypass Repeater (rgthree)、easy bookmark
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参

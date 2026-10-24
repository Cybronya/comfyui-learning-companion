---
name: image_to_image_sampler_vae_30
type: Image To Image
frequency: 3
level: strong
coverage: 0.509333
common_nodes: [Any Switch (rgthree), Bookmark (rgthree), CFGNorm, ConditioningZeroOut, Fast Groups Muter (rgthree), GetNode, Image Comparer (rgthree), ImageResize+, KSampler, Label (rgthree), LoadImage, ModelPatchTorchSettings, ModelSamplingAuraFlow, PathchSageAttentionKJ, PreviewAny, PrimitiveString, PrimitiveStringMultiline, RHHiddenNodes, RH_Captioner, SaveImage, SeedVR2BlockSwap, SeedVR2ExtraArgs, SeedVR2GGUF, SetNode, StringConcatenate, StringLength, Switch any [Crystools], TextEncodeQwenImageEditPlus, VAEDecode, VAEEncode, easy cleanGpuUsed, easy compare, easy int, easy seed]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/动漫转真人—阿浩_2027587565737484290.json, 图片生成/图生图/漫画转真人V2_2008418258508058626.json, 图片生成/图生图/漫画转真人_1999492726724980737.json]
source: knowledge_consolidation
---

# image_to_image_sampler_vae_30

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/动漫转真人—阿浩_2027587565737484290.json、图片生成/图生图/漫画转真人V2_2008418258508058626.json、图片生成/图生图/漫画转真人_1999492726724980737.json）

- **类型**：Image To Image
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：51%

## 共有节点

全部 3 个 workflow 都包含：
- `Any Switch (rgthree)`
- `Bookmark (rgthree)`
- `CFGNorm`
- `ConditioningZeroOut`
- `Fast Groups Muter (rgthree)`
- `GetNode`
- `Image Comparer (rgthree)`
- `ImageResize+`
- `KSampler`
- `Label (rgthree)`
- `LoadImage`
- `ModelPatchTorchSettings`
- `ModelSamplingAuraFlow`
- `PathchSageAttentionKJ`
- `PreviewAny`
- `PrimitiveString`
- `PrimitiveStringMultiline`
- `RHHiddenNodes`
- `RH_Captioner`
- `SaveImage`
- `SeedVR2BlockSwap`
- `SeedVR2ExtraArgs`
- `SeedVR2GGUF`
- `SetNode`
- `StringConcatenate`
- `StringLength`
- `Switch any [Crystools]`
- `TextEncodeQwenImageEditPlus`
- `VAEDecode`
- `VAEEncode`
- `easy cleanGpuUsed`
- `easy compare`
- `easy int`
- `easy seed`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 5 | 5 - 5 | 3 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | beta | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 5，观测区间 5 - 5，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 beta，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 高发问题（3/3 个样本）：Steps较低可能导致细节不足

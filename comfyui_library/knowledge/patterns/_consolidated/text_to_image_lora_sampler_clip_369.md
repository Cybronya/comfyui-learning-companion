---
name: text_to_image_lora_sampler_clip_369
type: Text To Image
frequency: 2
level: weak
coverage: 0.6555
common_nodes: [CLIPTextEncode, CR Text, ConditioningZeroOut, ConstrainImage|pysssss, EmptyLatentImage, Fast Groups Bypasser (rgthree), Image Compare (mtb), JanusImageUnderstanding, JanusModelLoader, KSampler, LayerUtility: PurgeVRAM, LoadImage, LoraLoaderModelOnly, PreviewImage, SaveImage, ShowText|pysssss, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Flux-文生图-图生图-加速版_2009553183344959489.json, 图片生成/文生图/Qwen-Image-Edit-文生图-图生图-加速版_2007390911692541953.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_369

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/Flux-文生图-图生图-加速版_2009553183344959489.json、图片生成/文生图/Qwen-Image-Edit-文生图-图生图-加速版_2007390911692541953.json）

- **类型**：Text To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：66%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPTextEncode`
- `CR Text`
- `ConditioningZeroOut`
- `ConstrainImage|pysssss`
- `EmptyLatentImage`
- `Fast Groups Bypasser (rgthree)`
- `Image Compare (mtb)`
- `JanusImageUnderstanding`
- `JanusModelLoader`
- `KSampler`
- `LayerUtility: PurgeVRAM`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PreviewImage`
- `SaveImage`
- `ShowText|pysssss`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CLIPLoader` —— 1/2 个有
- `DualCLIPLoader` —— 1/2 个有
- `ModelSamplingAuraFlow` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 2.5 | - | 2 | 100% |
| 采样算法 | euler | - | 2 | 100% |
| 调度器 | normal | - | 2 | 100% |
| 重绘幅度 | 0.6 | - | 2 | 100% |
| 宽度 | 1104 | - | 2 | 100% |
| 高度 | 1472 | - | 2 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/2 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 20，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 2.5，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，2 个样本，一致性 100%
- 调度器 最常用 normal，2 个样本，一致性 100%
- 重绘幅度 中位数 0.6，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 宽度 中位数 1104，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高度 中位数 1472，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高发问题（1/2 个样本）：Steps较低可能导致细节不足
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参

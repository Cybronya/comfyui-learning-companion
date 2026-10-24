---
name: text_to_image_lora_sampler_clip_625
type: Text To Image
frequency: 2
level: weak
coverage: 0.939
common_nodes: [Anything Everywhere, BasicScheduler, CFGGuider, CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyLatentImage, FastFilmGrain, Image H264 Compression (mtb), KSampler, KSamplerSelect, LatentRotate, LoraLoaderModelOnly, ModelSamplingAuraFlow, MuyeTextEditOutput, RandomNoise, RebatchLatents, RepeatLatentBatch, SamplerCustomAdvanced, SamplerEulerAncestral, SaveImage, SplitSigmas, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Krea 2 RAW to Turbo 高低噪采样文生图_2103129634291404801.json, 图片生成/文生图/Krea2 RAW to Turbo高低噪采样文生图，高质量文本到图像生成方案_2103598177789243394.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_625

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/Krea 2 RAW to Turbo 高低噪采样文生图_2103129634291404801.json、图片生成/文生图/Krea2 RAW to Turbo高低噪采样文生图，高质量文本到图像生成方案_2103598177789243394.json）

- **类型**：Text To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：94%

## 共有节点

全部 2 个 workflow 都包含：
- `Anything Everywhere`
- `BasicScheduler`
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `FastFilmGrain`
- `Image H264 Compression (mtb)`
- `KSampler`
- `KSamplerSelect`
- `LatentRotate`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `MuyeTextEditOutput`
- `RandomNoise`
- `RebatchLatents`
- `RepeatLatentBatch`
- `SamplerCustomAdvanced`
- `SamplerEulerAncestral`
- `SaveImage`
- `SplitSigmas`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `JjkText` —— 1/2 个有
- `solarL_SaveImagesToZip` —— 1/2 个有
- `孤海注释` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1000 | - | 2 | 8% |
| 高度 | 580 | - | 2 | 14% |
| 采样步数 | 4 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 2.75 | - | 2 | 36% |
| 采样算法 | euler | - | 2 | 50% |
| 调度器 | kl_optimal | - | 2 | 50% |
| 重绘幅度 | 0.725 | - | 2 | 62% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/2 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 1000，样本不足，未给区间，2 个样本，取值分散，一致性仅 8%
- 高度 中位数 580，样本不足，未给区间，2 个样本，取值分散，一致性仅 14%
- 采样步数 中位数 4，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 2.75，样本不足，未给区间，2 个样本，取值分散，一致性仅 36%
- 采样算法 最常用 euler，2 个样本，一致性 50%
- 调度器 最常用 kl_optimal，2 个样本，一致性 50%
- 重绘幅度 中位数 0.725，样本不足，未给区间，2 个样本
- 高发问题（3/2 个样本）：Steps较低可能导致细节不足
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参

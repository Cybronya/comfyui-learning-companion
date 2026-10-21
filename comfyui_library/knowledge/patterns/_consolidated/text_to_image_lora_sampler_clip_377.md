---
name: text_to_image_lora_sampler_clip_377
type: Text To Image
frequency: 2
level: weak
coverage: 0.773
common_nodes: [CLIPLoader, CLIPTextEncode, ComfySwitchNode, ConditioningZeroOut, DepthAnythingV2Preprocessor, EmptyLatentImage, Fast Groups Bypasser (rgthree), GetImageSize, KSampler, Krea2ControlApply, Krea2ControlImageEncode, Krea2ControlLoRALoader, LoadImage, PreviewImage, PrimitiveBoolean, PrimitiveStringMultiline, ResolutionSelector, SaveImage, TextGenerate, UNETLoader, VAEDecode, VAELoader, easy showAnything]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Krea2 深度图控制-全自动反推洗图-高清4K_2076852160796643329.json, 图片生成/文生图/Krea2 深度控制自动反推洗图 Depth ControlNet_2075102694674616322.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_377

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/Krea2 深度图控制-全自动反推洗图-高清4K_2076852160796643329.json、图片生成/文生图/Krea2 深度控制自动反推洗图 Depth ControlNet_2075102694674616322.json）

- **类型**：Text To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：77%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfySwitchNode`
- `ConditioningZeroOut`
- `DepthAnythingV2Preprocessor`
- `EmptyLatentImage`
- `Fast Groups Bypasser (rgthree)`
- `GetImageSize`
- `KSampler`
- `Krea2ControlApply`
- `Krea2ControlImageEncode`
- `Krea2ControlLoRALoader`
- `LoadImage`
- `PreviewImage`
- `PrimitiveBoolean`
- `PrimitiveStringMultiline`
- `ResolutionSelector`
- `SaveImage`
- `TextGenerate`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `Image Comparer (rgthree)` —— 1/2 个有
- `JWImageResizeByLongerSide` —— 1/2 个有
- `LatentUpscaleBy` —— 1/2 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/2 个有
- `LoraLoaderModelOnly` —— 1/2 个有
- `ModelSamplingAuraFlow` —— 1/2 个有
- `SeedVR2` —— 1/2 个有
- `SeedVR2BlockSwap` —— 1/2 个有
- `VAEEncode` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 768 | - | 2 | 67% |
| 高度 | 768 | - | 2 | 67% |
| 采样步数 | 7 | - | 2 | 86% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | res_multistep | - | 2 | 50% |
| 调度器 | simple | - | 2 | 100% |
| 重绘幅度 | 0.7 | - | 2 | 57% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/2 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 768，样本不足，未给区间，2 个样本
- 高度 中位数 768，样本不足，未给区间，2 个样本
- 采样步数 中位数 7，样本不足，未给区间，2 个样本，取值集中（一致性 86%）
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 res_multistep，2 个样本，一致性 50%
- 调度器 最常用 simple，2 个样本，一致性 100%
- 重绘幅度 中位数 0.7，样本不足，未给区间，2 个样本
- 高发问题（3/2 个样本）：Steps较低可能导致细节不足
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参

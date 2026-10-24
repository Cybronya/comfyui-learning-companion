---
name: text_to_image_lora_sampler_clip_641
type: Text To Image
frequency: 2
level: weak
coverage: 0.9285
common_nodes: [CFGGuider, CLIPLoader, CLIPTextEncode, ColorMatch, EmptyFlux2LatentImage, EmptyLatentImage, Fast Groups Bypasser (rgthree), Flux2Scheduler, GetImageSize, ImageScaleToTotalPixels, KSampler, KSamplerSelect, Label (rgthree), LoraLoaderModelOnly, PreviewImage, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/【Supermate】z-image编辑工作流(Flux2 Klein版)_2013269468192968706.json, 图片生成/文生图/全新工作流！动漫生图+风格转绘二合一！_2058011143603576833.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_641

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/【Supermate】z-image编辑工作流(Flux2 Klein版)_2013269468192968706.json、图片生成/文生图/全新工作流！动漫生图+风格转绘二合一！_2058011143603576833.json）

- **类型**：Text To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：93%

## 共有节点

全部 2 个 workflow 都包含：
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `ColorMatch`
- `EmptyFlux2LatentImage`
- `EmptyLatentImage`
- `Fast Groups Bypasser (rgthree)`
- `Flux2Scheduler`
- `GetImageSize`
- `ImageScaleToTotalPixels`
- `KSampler`
- `KSamplerSelect`
- `Label (rgthree)`
- `LoraLoaderModelOnly`
- `PreviewImage`
- `RandomNoise`
- `ReferenceLatent`
- `SamplerCustomAdvanced`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CR Text` —— 1/2 个有
- `ConditioningZeroOut` —— 1/2 个有
- `DrawMaskOnImage` —— 1/2 个有
- `Image Comparer (rgthree)` —— 1/2 个有
- `ImageConcanate` —— 1/2 个有
- `ImagePadForOutpaint` —— 1/2 个有
- `ImageSharpen` —— 1/2 个有
- `ImageUpscaleWithModel` —— 1/2 个有
- `JoinStringMulti` —— 1/2 个有
- `LoadImage` —— 1/2 个有
- `TTResolutionSelector` —— 1/2 个有
- `UpscaleModelLoader` —— 1/2 个有
- `easy cleanGpuUsed` —— 1/2 个有
- `easy seed` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1032 | - | 2 | 70% |
| 高度 | 1024 | - | 2 | 75% |
| 采样步数 | 35 | - | 2 | 86% |
| Prompt 约束强度(CFG) | 3 | - | 2 | 33% |
| 采样算法 | euler_ancestral | - | 2 | 50% |
| 调度器 | simple | - | 2 | 50% |
| 重绘幅度 | 1 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1032，样本不足，未给区间，2 个样本
- 高度 中位数 1024，样本不足，未给区间，2 个样本
- 采样步数 中位数 35，样本不足，未给区间，2 个样本，取值集中（一致性 86%）
- Prompt 约束强度(CFG) 中位数 3，样本不足，未给区间，2 个样本，取值分散，一致性仅 33%
- 采样算法 最常用 euler_ancestral，2 个样本，一致性 50%
- 调度器 最常用 simple，2 个样本，一致性 50%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参

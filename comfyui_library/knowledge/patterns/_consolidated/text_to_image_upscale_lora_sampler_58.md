---
name: text_to_image_upscale_lora_sampler_58
type: Text To Image
frequency: 2
level: weak
coverage: 0.8955
common_nodes: [CLIPLoader, CLIPTextEncode, CR Text, ConditioningZeroOut, EmptyLatentImage, ImageScaleBy, KSampler, LoadImage, LoraLoaderModelOnly, PreviewImage, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Qwen-Image-2512-图片重绘_文生图_2007853900451291137.json, 图片生成/文生图/Z-IMAGE文生图+图生图(YIHAN AIGC)_2026990202874503170.json]
source: knowledge_consolidation
---

# text_to_image_upscale_lora_sampler_58

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/Qwen-Image-2512-图片重绘_文生图_2007853900451291137.json、图片生成/文生图/Z-IMAGE文生图+图生图(YIHAN AIGC)_2026990202874503170.json）

- **类型**：Text To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：90%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Text`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `ImageScaleBy`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PreviewImage`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CR Latent Input Switch` —— 1/2 个有
- `Fast Groups Bypasser (rgthree)` —— 1/2 个有
- `Image Comparer (rgthree)` —— 1/2 个有
- `ImpactGaussianBlurMask` —— 1/2 个有
- `InpaintModelConditioning` —— 1/2 个有
- `Mask Fill Holes` —— 1/2 个有
- `MaskPreview+` —— 1/2 个有
- `Qwen3_VQA` —— 1/2 个有
- `ShowText` —— 1/2 个有
- `TextConcatenate` —— 1/2 个有
- `easy cleanGpuUsed` —— 1/2 个有
- `easy showAnything` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 872 | - | 2 | 83% |
| 高度 | 872 | - | 2 | 83% |
| 采样步数 | 11 | - | 2 | 91% |
| Prompt 约束强度(CFG) | 2 | - | 2 | 50% |
| 采样算法 | ddim | - | 2 | 50% |
| 调度器 | ddim_uniform | - | 2 | 50% |
| 重绘幅度 | 0.595 | - | 2 | 84% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/2 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 872，样本不足，未给区间，2 个样本，取值集中（一致性 83%）
- 高度 中位数 872，样本不足，未给区间，2 个样本，取值集中（一致性 83%）
- 采样步数 中位数 11，样本不足，未给区间，2 个样本，取值集中（一致性 91%）
- Prompt 约束强度(CFG) 中位数 2，样本不足，未给区间，2 个样本
- 采样算法 最常用 ddim，2 个样本，一致性 50%
- 调度器 最常用 ddim_uniform，2 个样本，一致性 50%
- 重绘幅度 中位数 0.595，样本不足，未给区间，2 个样本，取值集中（一致性 84%）
- 高发问题（1/2 个样本）：Steps较低可能导致细节不足
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参

---
name: text_to_image_inpaint_sampler_clip
type: Text To Image
frequency: 3
level: moderate
coverage: 0.696667
common_nodes: [CLIPLoaderGGUF, CLIPTextEncode, ConditioningZeroOut, DifferentialDiffusion, EmptyLatentImage, Fast Groups Bypasser (rgthree), FluxGuidance, GetNode, GrowMaskWithBlur, InpaintModelConditioning, KSampler, LoadImage, SaveImage, SetNode, UnetLoaderGGUF, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/Z-image 文生图+局部重绘+CN控制 汇总_1995296468326080514.json, 图片生成/文生图/Z-image 文生图+局部重绘_1995283943396139010.json, 图片生成/文生图/Z-image系列 文生图+CN2控制+重绘_2001079224679231490.json]
source: knowledge_consolidation
---

# text_to_image_inpaint_sampler_clip

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/Z-image 文生图+局部重绘+CN控制 汇总_1995296468326080514.json、图片生成/文生图/Z-image 文生图+局部重绘_1995283943396139010.json、图片生成/文生图/Z-image系列 文生图+CN2控制+重绘_2001079224679231490.json）

- **类型**：Text To Image
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：70%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoaderGGUF`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `DifferentialDiffusion`
- `EmptyLatentImage`
- `Fast Groups Bypasser (rgthree)`
- `FluxGuidance`
- `GetNode`
- `GrowMaskWithBlur`
- `InpaintModelConditioning`
- `KSampler`
- `LoadImage`
- `SaveImage`
- `SetNode`
- `UnetLoaderGGUF`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `AIO_Preprocessor` —— 2/3 个有
- `ModelPatchLoader` —— 2/3 个有
- `ModelSamplingAuraFlow` —— 2/3 个有
- `QwenImageDiffsynthControlnet` —— 2/3 个有
- `GetImageSize` —— 1/3 个有
- `Image Comparer (rgthree)` —— 1/3 个有
- `ImpactSwitch` —— 1/3 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/3 个有
- `Preview from image [Crystools]` —— 1/3 个有
- `PreviewImage` —— 1/3 个有
- `SetLatentNoiseMask` —— 1/3 个有
- `ZImageFunControlnet` —— 1/3 个有
- `easy imagePixelPerfect` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1080 | 512 - 1920 | 3 | 51% |
| 高度 | 1080 | 512 - 1920 | 3 | 51% |
| 采样步数 | 10 | 10 - 10 | 3 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | simple | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1080，观测区间 512 - 1920，3 个样本
- 高度 中位数 1080，观测区间 512 - 1920，3 个样本
- 采样步数 中位数 10，观测区间 10 - 10，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 simple，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）

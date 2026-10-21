---
name: image_to_image_controlnet_upscale_sampler_2
type: Image To Image
frequency: 2
level: weak
coverage: 0.398
common_nodes: [AIO_Preprocessor, CLIPLoader, CLIPTextEncode, CR SDXL Aspect Ratio, ConditioningZeroOut, DifferentialDiffusion, Fast Groups Bypasser (rgthree), GetNode, GrowMaskWithBlur, Image Comparer (rgthree), ImageAndMaskPreview, ImagePadForOutpaint, ImageScale, ImageScaleToTotalPixels, KSampler, KSamplerAdvanced, LanPaint_MaskBlend, LatentColorMatch, LayerUtility: ImageReel, LayerUtility: ImageReelComposit, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: PurgeVRAM V2, LoadImage, MaskPreview, ModelPatchLoader, ModelSamplingAuraFlow, PlaySound|pysssss, PreviewImage, Qwen3_VQA, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, SetNode, ShowText|pysssss, UNETLoader, VAEDecode, VAEEncode, VAELoader, ZImageFunControlnet, easy seed]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/YZ金鱼-Z-image-超强多合一、文生图、洗图、局部重绘、扩图、高清修复_2002021645600583681.json, 图片生成/文生图/YZ金鱼-Z-image-超强多合一、文生图、洗图、局部重绘、扩图、高清修复_2059460929003286530.json]
source: knowledge_consolidation
---

# image_to_image_controlnet_upscale_sampler_2

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/YZ金鱼-Z-image-超强多合一、文生图、洗图、局部重绘、扩图、高清修复_2002021645600583681.json、图片生成/文生图/YZ金鱼-Z-image-超强多合一、文生图、洗图、局部重绘、扩图、高清修复_2059460929003286530.json）

- **类型**：Image To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：40%

## 共有节点

全部 2 个 workflow 都包含：
- `AIO_Preprocessor`
- `CLIPLoader`
- `CLIPTextEncode`
- `CR SDXL Aspect Ratio`
- `ConditioningZeroOut`
- `DifferentialDiffusion`
- `Fast Groups Bypasser (rgthree)`
- `GetNode`
- `GrowMaskWithBlur`
- `Image Comparer (rgthree)`
- `ImageAndMaskPreview`
- `ImagePadForOutpaint`
- `ImageScale`
- `ImageScaleToTotalPixels`
- `KSampler`
- `KSamplerAdvanced`
- `LanPaint_MaskBlend`
- `LatentColorMatch`
- `LayerUtility: ImageReel`
- `LayerUtility: ImageReelComposit`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: PurgeVRAM V2`
- `LoadImage`
- `MaskPreview`
- `ModelPatchLoader`
- `ModelSamplingAuraFlow`
- `PlaySound|pysssss`
- `PreviewImage`
- `Qwen3_VQA`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `SetNode`
- `ShowText|pysssss`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `ZImageFunControlnet`
- `easy seed`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 10 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | euler_ancestral | - | 2 | 100% |
| 调度器 | sgm_uniform | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/2 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 10，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler_ancestral，2 个样本，一致性 100%
- 调度器 最常用 sgm_uniform，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高发问题（2/2 个样本）：Steps较低可能导致细节不足
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参

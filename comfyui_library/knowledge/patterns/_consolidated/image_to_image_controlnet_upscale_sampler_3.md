---
name: image_to_image_controlnet_upscale_sampler_3
type: Image To Image
frequency: 6
level: moderate
coverage: 0.399
common_nodes: [AIO_Preprocessor, CLIPLoader, CLIPTextEncode, CR SDXL Aspect Ratio, ConditioningZeroOut, DifferentialDiffusion, Fast Groups Bypasser (rgthree), GetNode, GrowMaskWithBlur, Image Comparer (rgthree), ImageAndMaskPreview, ImagePadForOutpaint, ImageScale, ImageScaleToTotalPixels, KSampler, KSamplerAdvanced, LanPaint_MaskBlend, LatentColorMatch, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: PurgeVRAM V2, LoadImage, MaskPreview, ModelPatchLoader, ModelSamplingAuraFlow, PlaySound|pysssss, PreviewImage, Qwen3_VQA, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, SetNode, ShowText|pysssss, UNETLoader, VAEDecode, VAEEncode, VAELoader, ZImageFunControlnet, easy seed]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Z-image-超强多合一、文生图、洗图、局部重绘、扩图、高清修复_2058392762575310849.json, 图片生成/文生图/YZ金鱼-Z-image-超强多合一、文生图、洗图、局部重绘、扩图、高清修复_2002021645600583681.json, 图片生成/文生图/YZ金鱼-Z-image-超强多合一、文生图、洗图、局部重绘、扩图、高清修复_2059460929003286530.json, 图片生成/文生图/Z-image-可超限-超强多合一、文生图、洗图、局部重绘、扩图、高清修复_2042440577345654786.json, 图片生成/文生图/【808】Z-image-超强多合一&文生图&洗图&局部重绘&图像扩展&高清修复_2036993908210671617.json, 图片生成/文生图/超强多合一、文生图、洗图、局部重绘、扩图、高清修复-邻家AI大女孩_2044407326270033921.json]
source: knowledge_consolidation
---

# image_to_image_controlnet_upscale_sampler_3

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/图生图/Z-image-超强多合一、文生图、洗图、局部重绘、扩图、高清修复_2058392762575310849.json、图片生成/文生图/YZ金鱼-Z-image-超强多合一、文生图、洗图、局部重绘、扩图、高清修复_2002021645600583681.json、图片生成/文生图/YZ金鱼-Z-image-超强多合一、文生图、洗图、局部重绘、扩图、高清修复_2059460929003286530.json、图片生成/文生图/Z-image-可超限-超强多合一、文生图、洗图、局部重绘、扩图、高清修复_2042440577345654786.json、图片生成/文生图/【808】Z-image-超强多合一&文生图&洗图&局部重绘&图像扩展&高清修复_2036993908210671617.json…）

- **类型**：Image To Image
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：40%

## 共有节点

全部 6 个 workflow 都包含：
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

**可变部分**（部分 workflow 才有）：
- `LayerUtility: ImageReel` —— 5/6 个有
- `LayerUtility: ImageReelComposit` —— 5/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 10 | 10 - 10 | 5 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 8 | 6 | 0% |
| 采样算法 | euler_ancestral | - | 6 | 83% |
| 调度器 | sgm_uniform | - | 6 | 83% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 6/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 10，观测区间 10 - 10，5 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 8，6 个样本，取值分散，一致性仅 0%
- 采样算法 最常用 euler_ancestral，6 个样本，一致性 83%
- 调度器 最常用 sgm_uniform，6 个样本，一致性 83%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 高发问题（6/6 个样本）：Steps较低可能导致细节不足

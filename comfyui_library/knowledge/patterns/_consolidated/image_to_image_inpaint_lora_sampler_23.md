---
name: image_to_image_inpaint_lora_sampler_23
type: Image To Image
frequency: 2
level: weak
coverage: 0.529
common_nodes: [CFGNorm, CLIPLoader, CLIPTextEncode, ColorMatch, DF_Integer, DWPreprocessor, DifferentialDiffusion, DualCLIPLoaderGGUF, Fast Groups Muter (rgthree), Get Image Size, GetImageSize, GetNode, INPAINT_MaskedBlur, INPAINT_MaskedFill, Image Comparer (rgthree), ImageCASharpening+, ImageConcatMulti, ImageResize+, ImageResizeKJv2, ImpactMinMax, InpaintCropImproved, InpaintModelConditioning, InpaintStitchImproved, KSampler, KSamplerAdvanced, LG_ImageSender, LG_LoadImage, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, MaskBlur+, ModelSamplingAuraFlow, PreviewImage, ReferenceLatent, ResizeMask, SaveImage, SeedVR2, SetNode, SimpleMath+, TTP_Image_Assy, TTP_Image_Tile_Batch, TextEncodeQwenImageEditPlus, UNETLoader, UnetLoaderGGUF, VAEDecode, VAEEncode, VAELoader, easy cleanGpuUsed]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/千问换头修复高清工作流_1977641033439813633.json, 平台全量/千问换头修复高清工作流（自用流程）_1978759971938701314.json]
source: knowledge_consolidation
---

# image_to_image_inpaint_lora_sampler_23

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/千问换头修复高清工作流_1977641033439813633.json、平台全量/千问换头修复高清工作流（自用流程）_1978759971938701314.json）

- **类型**：Image To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：53%

## 共有节点

全部 2 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `CLIPTextEncode`
- `ColorMatch`
- `DF_Integer`
- `DWPreprocessor`
- `DifferentialDiffusion`
- `DualCLIPLoaderGGUF`
- `Fast Groups Muter (rgthree)`
- `Get Image Size`
- `GetImageSize`
- `GetNode`
- `INPAINT_MaskedBlur`
- `INPAINT_MaskedFill`
- `Image Comparer (rgthree)`
- `ImageCASharpening+`
- `ImageConcatMulti`
- `ImageResize+`
- `ImageResizeKJv2`
- `ImpactMinMax`
- `InpaintCropImproved`
- `InpaintModelConditioning`
- `InpaintStitchImproved`
- `KSampler`
- `KSamplerAdvanced`
- `LG_ImageSender`
- `LG_LoadImage`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MaskBlur+`
- `ModelSamplingAuraFlow`
- `PreviewImage`
- `ReferenceLatent`
- `ResizeMask`
- `SaveImage`
- `SeedVR2`
- `SetNode`
- `SimpleMath+`
- `TTP_Image_Assy`
- `TTP_Image_Tile_Batch`
- `TextEncodeQwenImageEditPlus`
- `UNETLoader`
- `UnetLoaderGGUF`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy cleanGpuUsed`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | euler | - | 2 | 100% |
| 调度器 | beta | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/2 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，2 个样本，一致性 100%
- 调度器 最常用 beta，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高发问题（2/2 个样本）：Steps较低可能导致细节不足
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参

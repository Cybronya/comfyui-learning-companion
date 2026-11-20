---
name: image_to_image_upscale_lora_sampler_139
type: Image To Image
frequency: 2
level: weak
coverage: 0.651
common_nodes: [CLIPLoader, CLIPTextEncode, ComfySwitchNode, ConditioningZeroOut, Fast Groups Bypasser (rgthree), GetImageSize+, Image Comparer (rgthree), ImageResize+, ImageResizeKJv2, ImageScaleBy, ImageScaleToTotalPixels, JoinImageWithAlpha, KOOK_ImageCompression, KSampler, KSamplerAdvanced, LoadImage, LoraLoaderModelOnly, PreviewImage, PrimitiveStringMultiline, QwenImage21Cache, RH_RhartImageG25FlareImageToImage, ReferenceLatent, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, SplitImageWithAlpha, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, TextEncodeQwenImage21, UNETLoader, VAEDecode, VAEEncode, VAELoader, easy imageColorMatch, easy showAnything]
problems: []
missing: []
members: [平台全量/COS自动修图（厚涂版）_2111353244940324865.json, 平台全量/COS自动修图（自然感）_2104393550585745410.json]
source: knowledge_consolidation
---

# image_to_image_upscale_lora_sampler_139

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（平台全量/COS自动修图（厚涂版）_2111353244940324865.json、平台全量/COS自动修图（自然感）_2104393550585745410.json）

- **类型**：Image To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：65%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfySwitchNode`
- `ConditioningZeroOut`
- `Fast Groups Bypasser (rgthree)`
- `GetImageSize+`
- `Image Comparer (rgthree)`
- `ImageResize+`
- `ImageResizeKJv2`
- `ImageScaleBy`
- `ImageScaleToTotalPixels`
- `JoinImageWithAlpha`
- `KOOK_ImageCompression`
- `KSampler`
- `KSamplerAdvanced`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PreviewImage`
- `PrimitiveStringMultiline`
- `QwenImage21Cache`
- `RH_RhartImageG25FlareImageToImage`
- `ReferenceLatent`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `SplitImageWithAlpha`
- `TTP_Image_Assy`
- `TTP_Image_Tile_Batch`
- `TTP_Tile_image_size`
- `TextEncodeQwenImage21`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy imageColorMatch`
- `easy showAnything`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 30 | - | 1 | 100% |
| Prompt 约束强度(CFG) | 2.5 | - | 2 | 40% |
| 采样算法 | 1 | - | 1 | 100% |
| 调度器 | sa_solver | - | 2 | 50% |
| 重绘幅度 | 1 | - | 1 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- Prompt 约束强度(CFG) 中位数 2.5，样本不足，未给区间，2 个样本，取值分散，一致性仅 40%
- 调度器 最常用 sa_solver，2 个样本，一致性 50%
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参

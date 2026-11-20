---
name: text_to_image_controlnet_sampler_clip_24
type: Text To Image
frequency: 2
level: weak
coverage: 0.784
common_nodes: [AIO_Preprocessor, BoolOperationNode, CLIPLoader, CLIPTextEncode, ControlNetPreprocessorSelector, EmptyLatentImage, Fast Groups Bypasser (rgthree), GetImageSize, Image Comparer (rgthree), ImageCASharpening+, ImageResize+, ImageScaleToTotalPixels, IntConditions, KSampler, LayerUtility: ImageReel, LayerUtility: ImageReelComposit, LayerUtility: PurgeVRAM V2, LoadImage, MaraScottIsEmptyOrNone_v1, MinNode, ModelPatchLoader, PreviewImage, PrimitiveInt, PrimitiveStringMultiline, QwenImageDiffsynthControlnet, RH_Captioner, SaveImage, SeedVR2, ShowText|pysssss, StringListToCombo, TTP_Image_Assy, TTP_Image_Tile_Batch, UNETLoader, VAEDecode, VAELoader, easy cleanGpuUsed, easy ifElse, easy showAnything, int _O]
problems: []
missing: []
members: [图片生成/图生图/Z-Image+ControlNet 2最新洗图_2011988079548047361.json, 图片生成/文生图/Z-Image+ControlNet 2最新洗图+放大_2045506985763807234.json]
source: knowledge_consolidation
---

# text_to_image_controlnet_sampler_clip_24

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/Z-Image+ControlNet 2最新洗图_2011988079548047361.json、图片生成/文生图/Z-Image+ControlNet 2最新洗图+放大_2045506985763807234.json）

- **类型**：Text To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：78%

## 共有节点

全部 2 个 workflow 都包含：
- `AIO_Preprocessor`
- `BoolOperationNode`
- `CLIPLoader`
- `CLIPTextEncode`
- `ControlNetPreprocessorSelector`
- `EmptyLatentImage`
- `Fast Groups Bypasser (rgthree)`
- `GetImageSize`
- `Image Comparer (rgthree)`
- `ImageCASharpening+`
- `ImageResize+`
- `ImageScaleToTotalPixels`
- `IntConditions`
- `KSampler`
- `LayerUtility: ImageReel`
- `LayerUtility: ImageReelComposit`
- `LayerUtility: PurgeVRAM V2`
- `LoadImage`
- `MaraScottIsEmptyOrNone_v1`
- `MinNode`
- `ModelPatchLoader`
- `PreviewImage`
- `PrimitiveInt`
- `PrimitiveStringMultiline`
- `QwenImageDiffsynthControlnet`
- `RH_Captioner`
- `SaveImage`
- `SeedVR2`
- `ShowText|pysssss`
- `StringListToCombo`
- `TTP_Image_Assy`
- `TTP_Image_Tile_Batch`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy cleanGpuUsed`
- `easy ifElse`
- `easy showAnything`
- `int _O`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 512 | - | 2 | 100% |
| 高度 | 512 | - | 2 | 100% |
| 采样步数 | 10 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | euler | - | 2 | 100% |
| 调度器 | FlowMatchEulerDiscreteScheduler | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 512，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高度 中位数 512，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样步数 中位数 10，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，2 个样本，一致性 100%
- 调度器 最常用 FlowMatchEulerDiscreteScheduler，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参

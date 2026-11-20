---
name: image_to_image_ipadapter_inpaint_sampler
type: Image To Image
frequency: 2
level: weak
coverage: 0.807
common_nodes: [BRIA_RMBG_ModelLoader_Zho, BRIA_RMBG_Zho, CLIPTextEncode, CR Prompt Text, CheckpointLoaderSimple, DifferentialDiffusion, Display Any (rgthree), INPAINT_ApplyFooocusInpaint, INPAINT_LoadFooocusInpaint, INPAINT_MaskedBlur, INPAINT_MaskedFill, INPAINT_VAEEncodeInpaintConditioning, IPAdapter, IPAdapterUnifiedLoader, Image Comparer (rgthree), Image Overlay, ImageCompositeMasked, ImagePadForOutpaintMasked, ImageResize+, ImageSizeAndBatchSize, KSampler, LoadImage, MaskPreview+, PreviewBridge, PreviewImage, RemoveNoiseMask, SaveImage, Text Concatenate, VAEDecode, VAEEncode, WD14Tagger|pysssss]
problems: []
missing: []
members: [图片生成/图生图/春日效果图_2026309680598880257.json, 平台全量/自定义比例扩图_1804043628418424834.json]
source: knowledge_consolidation
---

# image_to_image_ipadapter_inpaint_sampler

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/春日效果图_2026309680598880257.json、平台全量/自定义比例扩图_1804043628418424834.json）

- **类型**：Image To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：81%

## 共有节点

全部 2 个 workflow 都包含：
- `BRIA_RMBG_ModelLoader_Zho`
- `BRIA_RMBG_Zho`
- `CLIPTextEncode`
- `CR Prompt Text`
- `CheckpointLoaderSimple`
- `DifferentialDiffusion`
- `Display Any (rgthree)`
- `INPAINT_ApplyFooocusInpaint`
- `INPAINT_LoadFooocusInpaint`
- `INPAINT_MaskedBlur`
- `INPAINT_MaskedFill`
- `INPAINT_VAEEncodeInpaintConditioning`
- `IPAdapter`
- `IPAdapterUnifiedLoader`
- `Image Comparer (rgthree)`
- `Image Overlay`
- `ImageCompositeMasked`
- `ImagePadForOutpaintMasked`
- `ImageResize+`
- `ImageSizeAndBatchSize`
- `KSampler`
- `LoadImage`
- `MaskPreview+`
- `PreviewBridge`
- `PreviewImage`
- `RemoveNoiseMask`
- `SaveImage`
- `Text Concatenate`
- `VAEDecode`
- `VAEEncode`
- `WD14Tagger|pysssss`

**可变部分**（部分 workflow 才有）：
- `DF_Integer` —— 1/2 个有
- `Get Image Size` —— 1/2 个有
- `GetNode` —— 1/2 个有
- `ImageCASharpening+` —— 1/2 个有
- `ImpactMinMax` —— 1/2 个有
- `MuyeTextEditOutput` —— 1/2 个有
- `RH_Nano_Banana2_Image2Image` —— 1/2 个有
- `SeedVR2` —— 1/2 个有
- `SetNode` —— 1/2 个有
- `SimpleMath+` —— 1/2 个有
- `TTP_Image_Assy` —— 1/2 个有
- `TTP_Image_Tile_Batch` —— 1/2 个有
- `easy cleanGpuUsed` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 8 | - | 2 | 100% |
| 采样算法 | euler_ancestral | - | 2 | 100% |
| 调度器 | normal | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 8，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler_ancestral，2 个样本，一致性 100%
- 调度器 最常用 normal，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参

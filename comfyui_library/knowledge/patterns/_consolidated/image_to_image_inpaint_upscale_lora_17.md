---
name: image_to_image_inpaint_upscale_lora_17
type: Image To Image
frequency: 2
level: weak
coverage: 0.667
common_nodes: [Anything Everywhere3, CFGGuider, CLIPLoader, CLIPTextEncode, CR SDXL Aspect Ratio, CR Text, ConditioningZeroOut, EmptyFlux2LatentImage, Fast Groups Bypasser (rgthree), Flux2Scheduler, GetImageSize, GetImageSize+, GetNode, Image Comparer (rgthree), ImageCASharpening+, ImagePadForOutpaint, ImagePass, ImageResize+, ImageScaleBy, InpaintModelConditioning, KOOK_SaveJPGImage, KSampler, KSamplerAdvanced, KSamplerSelect, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, PlaySound|pysssss, PreviewImage, RandomNoise, ReferenceLatent, RunningHub Deepcleaner, SamplerCustomAdvanced, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, SetNode, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, UNETLoader, VAEDecode, VAEEncode, VAELoader, easy cleanGpuUsed]
problems: [Steps较低可能导致细节不足]
missing: []
members: [平台全量/法外狂徒Flux Klein文生图、单图、多图编辑+人像修复+高清放大大合集_2012188047617560577.json, 平台全量/法外狂徒Flux Klein文生图、图像编辑卷王全能合集V2版_2014622911713255425.json]
source: knowledge_consolidation
---

# image_to_image_inpaint_upscale_lora_17

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（平台全量/法外狂徒Flux Klein文生图、单图、多图编辑+人像修复+高清放大大合集_2012188047617560577.json、平台全量/法外狂徒Flux Klein文生图、图像编辑卷王全能合集V2版_2014622911713255425.json）

- **类型**：Image To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：67%

## 共有节点

全部 2 个 workflow 都包含：
- `Anything Everywhere3`
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `CR SDXL Aspect Ratio`
- `CR Text`
- `ConditioningZeroOut`
- `EmptyFlux2LatentImage`
- `Fast Groups Bypasser (rgthree)`
- `Flux2Scheduler`
- `GetImageSize`
- `GetImageSize+`
- `GetNode`
- `Image Comparer (rgthree)`
- `ImageCASharpening+`
- `ImagePadForOutpaint`
- `ImagePass`
- `ImageResize+`
- `ImageScaleBy`
- `InpaintModelConditioning`
- `KOOK_SaveJPGImage`
- `KSampler`
- `KSamplerAdvanced`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `PlaySound|pysssss`
- `PreviewImage`
- `RandomNoise`
- `ReferenceLatent`
- `RunningHub Deepcleaner`
- `SamplerCustomAdvanced`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `SetNode`
- `TTP_Image_Assy`
- `TTP_Image_Tile_Batch`
- `TTP_Tile_image_size`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy cleanGpuUsed`

**可变部分**（部分 workflow 才有）：
- `AILab_QwenVL` —— 1/2 个有
- `AIO_Preprocessor` —— 1/2 个有
- `Anything Everywhere` —— 1/2 个有
- `CR Text Concatenate` —— 1/2 个有
- `ColorMatch` —— 1/2 个有
- `DWPreprocessor` —— 1/2 个有
- `FastCanvas` —— 1/2 个有
- `FastCanvasTool` —— 1/2 个有
- `IfInnerExecute` —— 1/2 个有
- `ImageCrop+` —— 1/2 个有
- `LayerMask: BiRefNetUltraV2` —— 1/2 个有
- `LayerMask: LoadBiRefNetModelV2` —— 1/2 个有
- `LayerMask: MaskGrow` —— 1/2 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/2 个有
- `Mask Fill Holes` —— 1/2 个有
- `QwenMultiangleCameraNode` —— 1/2 个有
- `easy compare` —— 1/2 个有
- `easy showAnything` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | randomize | - | 2 | 100% |
| Prompt 约束强度(CFG) | 8 | - | 2 | 100% |
| 采样算法 | 1 | - | 2 | 100% |
| 调度器 | euler | - | 2 | 100% |
| 重绘幅度 | beta57 | - | 2 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 5/2 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 最常用 randomize，2 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 8，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler，2 个样本，一致性 100%
- 重绘幅度 最常用 beta57，2 个样本，一致性 100%
- 高发问题（5/2 个样本）：Steps较低可能导致细节不足
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参

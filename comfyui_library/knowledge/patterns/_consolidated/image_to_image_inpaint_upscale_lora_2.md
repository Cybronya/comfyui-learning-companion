---
name: image_to_image_inpaint_upscale_lora_2
type: Image To Image
frequency: 7
level: strong
coverage: 0.827
common_nodes: [BatchCropFromMask, BboxToInt, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, CR Combine Prompt, CR Simple Image Compare, CheckpointLoaderSimple, Cut By Mask, DifferentialDiffusion, DownloadAndLoadFlorence2Model, DualCLIPLoader, EmptyImage, FaceParse(FaceParsing), FaceParsingModelLoader(FaceParsing), FaceParsingProcessorLoader(FaceParsing), FaceParsingResultsParser(FaceParsing), Florence2Run, FluxGuidance, Get resolution [Crystools], GrowMaskWithBlur, Image Comparer (rgthree), ImageCompositeMasked, ImageConcanate, ImageResizeKJ, ImageToMask, ImageUpscaleWithModel, InpaintModelConditioning, Int, InvertMask, KSampler, KSamplerAdvanced, LayerColor: ColorAdapter, LayerMask: PersonMaskUltra, LayerMask: PersonMaskUltra V2, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: PurgeVRAM, LoadImage, MaskComposite, MaskPreview+, MaskSmooth+, MaskToImage, MathExpression|pysssss, Power Lora Loader (rgthree), PreviewBridge, PreviewImage, RHHiddenNodes, RH_Captioner, SaveImage, SetLatentNoiseMask, ShowText|pysssss, StyleModelApply, StyleModelLoader, UNETLoader, UpscaleModelLoader, VAEDecode, VAEEncode, VAELoader, easy imageInsetCrop, easy showAnything]
problems: []
missing: []
members: [图片生成/图生图/图片换脸-高清放大-去AI感-高清修复图片_2055897052659363842.json, 图片生成/图生图/图片换脸-高清放大-去AI感-高清修复图片_2055929233310011393.json, 图片生成/图生图/图片换脸-高清放大-去AI感-高清修复图片_2079536132789985282.json, 图片生成/图生图/换脸+高清放大去AI高清修复_1920734252449595394.json, 图片生成/图生图/换脸100%相识度，高清放大去AI高清修复，保留2张照片1是人脸痣都100%相识，2是皮肤去AI化_1971715229170266113.json, 图片生成/图生图/换脸100%相识度，高清放大去AI高清修复，保留2张照片1是人脸痣都100%相识，2是皮肤去AI化_1975071074062872577.json, 图片生成/图生图/换脸只要两张图片高清放大去AI高清修复图片换脸最高级直接换头发型都换了_2037844745040437250.json]
source: knowledge_consolidation
---

# image_to_image_inpaint_upscale_lora_2

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/图生图/图片换脸-高清放大-去AI感-高清修复图片_2055897052659363842.json、图片生成/图生图/图片换脸-高清放大-去AI感-高清修复图片_2055929233310011393.json、图片生成/图生图/图片换脸-高清放大-去AI感-高清修复图片_2079536132789985282.json、图片生成/图生图/换脸+高清放大去AI高清修复_1920734252449595394.json、图片生成/图生图/换脸100%相识度，高清放大去AI高清修复，保留2张照片1是人脸痣都100%相识，2是皮肤去AI化_1971715229170266113.json…）

- **类型**：Image To Image
- **样本数**：7
- **可信度**：强结论
- **平均知识覆盖**：83%

## 共有节点

全部 7 个 workflow 都包含：
- `BatchCropFromMask`
- `BboxToInt`
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `CR Combine Prompt`
- `CR Simple Image Compare`
- `CheckpointLoaderSimple`
- `Cut By Mask`
- `DifferentialDiffusion`
- `DownloadAndLoadFlorence2Model`
- `DualCLIPLoader`
- `EmptyImage`
- `FaceParse(FaceParsing)`
- `FaceParsingModelLoader(FaceParsing)`
- `FaceParsingProcessorLoader(FaceParsing)`
- `FaceParsingResultsParser(FaceParsing)`
- `Florence2Run`
- `FluxGuidance`
- `Get resolution [Crystools]`
- `GrowMaskWithBlur`
- `Image Comparer (rgthree)`
- `ImageCompositeMasked`
- `ImageConcanate`
- `ImageResizeKJ`
- `ImageToMask`
- `ImageUpscaleWithModel`
- `InpaintModelConditioning`
- `Int`
- `InvertMask`
- `KSampler`
- `KSamplerAdvanced`
- `LayerColor: ColorAdapter`
- `LayerMask: PersonMaskUltra`
- `LayerMask: PersonMaskUltra V2`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: PurgeVRAM`
- `LoadImage`
- `MaskComposite`
- `MaskPreview+`
- `MaskSmooth+`
- `MaskToImage`
- `MathExpression|pysssss`
- `Power Lora Loader (rgthree)`
- `PreviewBridge`
- `PreviewImage`
- `RHHiddenNodes`
- `RH_Captioner`
- `SaveImage`
- `SetLatentNoiseMask`
- `ShowText|pysssss`
- `StyleModelApply`
- `StyleModelLoader`
- `UNETLoader`
- `UpscaleModelLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy imageInsetCrop`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `LayerMask: MaskPreview` —— 6/7 个有
- `easy cleanGpuUsed` —— 6/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 30 | 30 - 30 | 7 | 100% |
| Prompt 约束强度(CFG) | 0.7 | 0.7 - 0.7 | 7 | 100% |
| 采样算法 | dpmpp_2m | - | 7 | 100% |
| 调度器 | normal | - | 7 | 100% |
| 重绘幅度 | 0.2 | 0.2 - 0.2 | 7 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 30，观测区间 30 - 30，7 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 0.7，观测区间 0.7 - 0.7，7 个样本，取值集中（一致性 100%）
- 采样算法 最常用 dpmpp_2m，7 个样本，一致性 100%
- 调度器 最常用 normal，7 个样本，一致性 100%
- 重绘幅度 中位数 0.2，观测区间 0.2 - 0.2，7 个样本，取值集中（一致性 100%）
- 风险：Prompt 约束强度(CFG) 观测到 0.7，低于常用下限 1（CFG 过低可能导致 Prompt 约束不足、结果偏离描述）

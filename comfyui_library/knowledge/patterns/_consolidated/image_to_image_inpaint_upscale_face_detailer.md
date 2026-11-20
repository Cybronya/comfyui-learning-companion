---
name: image_to_image_inpaint_upscale_face_detailer
type: Image To Image
frequency: 2
level: weak
coverage: 0.757
common_nodes: [CLIPTextEncode, CR Text, CheckpointLoaderSimple, DeepTranslatorTextNode, FaceDetailer, Float, GrowMaskWithBlur, Image Comparer (rgthree), ImageAndMaskPreview, ImageScaleBy, InpaintModelConditioning, KSampler, LayerMask: MaskPreview, LoadImage, LoraLoaderModelOnly, PreviewImage, RH_Captioner, SAMLoader, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, UltralyticsDetectorProvider, VAEDecode, VAEEncode, easy showAnything]
problems: []
missing: []
members: [图片生成/图生图/iL、Pony、XL通用动漫洗图修复_2073959860875837440.json, 视频生成/图生视频/王炸！iL、Pony、XL通用动漫洗图修复_2074498675400859650.json]
source: knowledge_consolidation
---

# image_to_image_inpaint_upscale_face_detailer

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/iL、Pony、XL通用动漫洗图修复_2073959860875837440.json、视频生成/图生视频/王炸！iL、Pony、XL通用动漫洗图修复_2074498675400859650.json）

- **类型**：Image To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：76%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPTextEncode`
- `CR Text`
- `CheckpointLoaderSimple`
- `DeepTranslatorTextNode`
- `FaceDetailer`
- `Float`
- `GrowMaskWithBlur`
- `Image Comparer (rgthree)`
- `ImageAndMaskPreview`
- `ImageScaleBy`
- `InpaintModelConditioning`
- `KSampler`
- `LayerMask: MaskPreview`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PreviewImage`
- `RH_Captioner`
- `SAMLoader`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `UltralyticsDetectorProvider`
- `VAEDecode`
- `VAEEncode`
- `easy showAnything`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 25 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 4.5 | - | 2 | 100% |
| 采样算法 | euler | - | 2 | 100% |
| 调度器 | normal | - | 2 | 100% |
| 重绘幅度 | 0.25 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 25，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，2 个样本，一致性 100%
- 调度器 最常用 normal，2 个样本，一致性 100%
- 重绘幅度 中位数 0.25，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参

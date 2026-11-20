---
name: unknown_workflow_inpaint_lora_sampler_17
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.9148
common_nodes: [BasicGuider, BasicScheduler, CLIPTextEncode, CLIPVisionLoader, CR Color Panel, ConditioningZeroOut, DifferentialDiffusion, DualCLIPLoader, FluxGuidance, GrowMaskWithBlur, ImageCompositeMasked, ImageCrop+, InpaintCrop, InpaintModelConditioning, InpaintStitch, Int, KSamplerSelect, LayerMask: MaskGrow, LayerMask: MaskPreview, LayerUtility: CropByMask V2, LayerUtility: ImageBlendAdvance, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, Mask Fill Holes, MaskPreview+, ModelSamplingFlux, PreviewImage, RMBG, RandomNoise, ReduxAdvanced, SamplerCustomAdvanced, SaveImage, StyleModelLoader, UNETLoader, VAEDecode, VAELoader, easy makeImageForICLora]
problems: []
missing: []
members: [图片生成/图生图/Flux 万物迁移_1983079864918024194.json, 图片生成/图生图/万物迁移（字节最新重绘模型）_1969029474002104321.json, 图片生成/图生图/万物迁移（河南ai之神）_1958511419870310401.json, 图片生成/图生图/最好用的 万物迁移（小物品可用）物品还原度99%_1936726800812904450.json, 图片生成/图生图/最好用的 万物迁移（小物品可用）物品还原度99%_1975103087293632513.json]
source: knowledge_consolidation
---

# unknown_workflow_inpaint_lora_sampler_17

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/Flux 万物迁移_1983079864918024194.json、图片生成/图生图/万物迁移（字节最新重绘模型）_1969029474002104321.json、图片生成/图生图/万物迁移（河南ai之神）_1958511419870310401.json、图片生成/图生图/最好用的 万物迁移（小物品可用）物品还原度99%_1936726800812904450.json、图片生成/图生图/最好用的 万物迁移（小物品可用）物品还原度99%_1975103087293632513.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：91%

## 共有节点

全部 5 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncode`
- `CLIPVisionLoader`
- `CR Color Panel`
- `ConditioningZeroOut`
- `DifferentialDiffusion`
- `DualCLIPLoader`
- `FluxGuidance`
- `GrowMaskWithBlur`
- `ImageCompositeMasked`
- `ImageCrop+`
- `InpaintCrop`
- `InpaintModelConditioning`
- `InpaintStitch`
- `Int`
- `KSamplerSelect`
- `LayerMask: MaskGrow`
- `LayerMask: MaskPreview`
- `LayerUtility: CropByMask V2`
- `LayerUtility: ImageBlendAdvance`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `Mask Fill Holes`
- `MaskPreview+`
- `ModelSamplingFlux`
- `PreviewImage`
- `RMBG`
- `RandomNoise`
- `ReduxAdvanced`
- `SamplerCustomAdvanced`
- `SaveImage`
- `StyleModelLoader`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy makeImageForICLora`

**可变部分**（部分 workflow 才有）：
- `Get Image Size` —— 4/5 个有
- `IsMaskEmpty` —— 4/5 个有
- `LayerUtility: ImageReel` —— 4/5 个有
- `LayerUtility: ImageReelComposit` —— 4/5 个有
- `Seed (rgthree)` —— 4/5 个有
- `easy anythingIndexSwitch` —— 4/5 个有
- `easy convertAnything` —— 4/5 个有
- `BiRefNetRMBG` —— 1/5 个有
- `Image Comparer (rgthree)` —— 1/5 个有
- `LayerUtility: CropByMask` —— 1/5 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

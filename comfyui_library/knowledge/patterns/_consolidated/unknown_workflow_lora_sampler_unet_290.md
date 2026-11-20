---
name: unknown_workflow_lora_sampler_unet_290
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.7505
common_nodes: [CLIPLoader, GetImageSize, GrowMaskWithBlur, Image Comparer (rgthree), ImageResizeKJv2, ImageScale, ImageToMask, Int, JjkText, KSamplerSelect, LayerMask: MaskGrow, LayerMask: MaskPreview, LayerUtility: ColorImage V2, LayerUtility: CropByMask V2, LayerUtility: ImageBlendAdvance, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: RestoreCropBox, LoadImage, LoraLoaderModelOnly, ManualSigmas, Mask Fill Holes, MathExpression|pysssss, MaxNode, PreviewBridge, PreviewImage, QwenImage21Cache, SamplerCustom, SaveImage, TextEncodeQwenImage21, UNETLoader, VAEDecode, VAELoader, easy showAnything, 孤海注释]
problems: []
missing: []
members: [图片生成/图生图/万物迁移_qwen_image_2.1_turbo_2113464453638479873.json, 图片生成/图生图/细节恢复 qwen_image_2.1_2107159669243473921.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_290

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/万物迁移_qwen_image_2.1_turbo_2113464453638479873.json、图片生成/图生图/细节恢复 qwen_image_2.1_2107159669243473921.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：75%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPLoader`
- `GetImageSize`
- `GrowMaskWithBlur`
- `Image Comparer (rgthree)`
- `ImageResizeKJv2`
- `ImageScale`
- `ImageToMask`
- `Int`
- `JjkText`
- `KSamplerSelect`
- `LayerMask: MaskGrow`
- `LayerMask: MaskPreview`
- `LayerUtility: ColorImage V2`
- `LayerUtility: CropByMask V2`
- `LayerUtility: ImageBlendAdvance`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: RestoreCropBox`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ManualSigmas`
- `Mask Fill Holes`
- `MathExpression|pysssss`
- `MaxNode`
- `PreviewBridge`
- `PreviewImage`
- `QwenImage21Cache`
- `SamplerCustom`
- `SaveImage`
- `TextEncodeQwenImage21`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy showAnything`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `EmptyImage` —— 1/2 个有
- `Image Overlay` —— 1/2 个有
- `KuwaharaBlur` —— 1/2 个有
- `LayerFilter: GaussianBlur` —— 1/2 个有
- `LayerUtility: ImageRemoveAlpha` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参

---
name: unknown_workflow_lora_sampler_unet_282
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.876
common_nodes: [BasicScheduler, BiRefNetRMBG, CFGGuider, CFGNorm, CLIPLoader, FluxKontextMultiReferenceLatentMethod, KSamplerSelect, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, PreviewImage, RandomNoise, SamplerCustomAdvanced, SaveImage, TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/qwen-edit-2511人物换脸最像_2039882640798523394.json, 图片生成/文生图/2511无痕换头大师版_2027327275267530754.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_282

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/qwen-edit-2511人物换脸最像_2039882640798523394.json、图片生成/文生图/2511无痕换头大师版_2027327275267530754.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：88%

## 共有节点

全部 2 个 workflow 都包含：
- `BasicScheduler`
- `BiRefNetRMBG`
- `CFGGuider`
- `CFGNorm`
- `CLIPLoader`
- `FluxKontextMultiReferenceLatentMethod`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `PreviewImage`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `TextEncodeQwenImageEditPlus`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `AddLabel` —— 1/2 个有
- `BodySegment` —— 1/2 个有
- `Image Comparer (rgthree)` —— 1/2 个有
- `ImageConcanate` —— 1/2 个有
- `ImageCropByMask` —— 1/2 个有
- `ImageResizeKJv2` —— 1/2 个有
- `InpaintCropImproved` —— 1/2 个有
- `InpaintStitchImproved` —— 1/2 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/2 个有
- `MaskPreview+` —— 1/2 个有
- `PrimitiveStringMultiline` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参

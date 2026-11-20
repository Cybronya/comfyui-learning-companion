---
name: unknown_workflow_lora_sampler_clip_112
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.976
common_nodes: [CFGGuider, CLIPLoader, CLIPTextEncode, CR Text, ClothesSegment, ConditioningZeroOut, Flux2Scheduler, GetImageSize, Image Comparer (rgthree), ImageScaleToTotalPixels, KSamplerSelect, LayerUtility: CropByMask V2, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: PurgeVRAM V2, LoadImage, LoraLoaderModelOnly, ModelPatchTorchSettings, PathchSageAttentionKJ, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader, easy int]
problems: []
missing: []
members: [图片生成/图生图/指定角色换头-图生图-FLUX.2-klein-换脸_2036347325433520129.json, 图片生成/图生图/指定角色换脸-FLUX.2-klein-_2036670076690112513.json, 图片生成/图生图/角色换头-单人版-图生图-FLUX.2-klein-换脸_2036297825587306498.json, 图片生成/图生图/角色换头-单人版-图生图-FLUX.2-klein-换脸_2037946174061154306.json, 图片生成/图生图/角色换脸-单人版-FLUX.2-klein-_2034978304230428674.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_112

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/指定角色换头-图生图-FLUX.2-klein-换脸_2036347325433520129.json、图片生成/图生图/指定角色换脸-FLUX.2-klein-_2036670076690112513.json、图片生成/图生图/角色换头-单人版-图生图-FLUX.2-klein-换脸_2036297825587306498.json、图片生成/图生图/角色换头-单人版-图生图-FLUX.2-klein-换脸_2037946174061154306.json、图片生成/图生图/角色换脸-单人版-FLUX.2-klein-_2034978304230428674.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：98%

## 共有节点

全部 5 个 workflow 都包含：
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Text`
- `ClothesSegment`
- `ConditioningZeroOut`
- `Flux2Scheduler`
- `GetImageSize`
- `Image Comparer (rgthree)`
- `ImageScaleToTotalPixels`
- `KSamplerSelect`
- `LayerUtility: CropByMask V2`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: PurgeVRAM V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelPatchTorchSettings`
- `PathchSageAttentionKJ`
- `RandomNoise`
- `ReferenceLatent`
- `SamplerCustomAdvanced`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy int`

**可变部分**（部分 workflow 才有）：
- `SeedVR2LoadDiTModel` —— 4/5 个有
- `SeedVR2LoadVAEModel` —— 4/5 个有
- `SeedVR2VideoUpscaler` —— 4/5 个有
- `BlockifyMask` —— 3/5 个有
- `EmptyFlux2LatentImage` —— 3/5 个有
- `GrowMaskWithBlur` —— 2/5 个有
- `ImageCompositeMasked` —— 2/5 个有
- `InpaintModelConditioning` —— 2/5 个有
- `LayerMask: MaskPreview` —— 2/5 个有
- `LayerUtility: ColorImage V2` —— 2/5 个有
- `RH_Translator` —— 2/5 个有
- `easy sam3ImageSegmentation` —— 2/5 个有
- `easy sam3ModelLoader` —— 2/5 个有
- `Int` —— 1/5 个有
- `SeedVR2` —— 1/5 个有
- `SeedVR2BlockSwap` —— 1/5 个有
- `TT_img_enc_v2` —— 1/5 个有
- `TwoWaySwitch` —— 1/5 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

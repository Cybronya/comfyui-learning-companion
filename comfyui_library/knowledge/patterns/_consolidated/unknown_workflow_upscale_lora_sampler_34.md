---
name: unknown_workflow_upscale_lora_sampler_34
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.7565
common_nodes: [Anything Everywhere, ApplyFBCacheOnModel, BasicGuider, BasicScheduler, CLIPTextEncode, CR SDXL Aspect Ratio, DepthAnythingPreprocessor, DisableNoise, DualCLIPLoader, FluxGuidance, GetNode, GrowMask, ImageScaleBy, ImageScaleToTotalPixels, ImageUpscaleWithModel, ImpactImageBatchToImageList, Joy_caption_two, Joy_caption_two_load, KSamplerSelect, LayerFilter: FilmV2, LayerMask: SegmentAnythingUltra V2, LoadImage, LoraLoaderModelOnly, LoraLoader|pysssss, MaskBlur+, MaskPreview+, ModelSamplingFlux, Note Plus (mtb), PreviewImage, RandomNoise, SamplerCustomAdvanced, SaveImage, SetLatentNoiseMask, SetNode, ShowText|pysssss, SplitSigmasDenoise, StringFunction|pysssss, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, TextInput_, UNETLoader, UpscaleModelLoader, VAEDecode, VAEEncode, VAELoader, easy cleanGpuUsed, easy clearCacheAll]
problems: []
missing: [LayerFilter: FilmV2, LayerMask: SegmentAnythingUltra V2, MaskBlur+, Note Plus (mtb), StringFunction|pysssss, easy cleanGpuUsed, easy clearCacheAll, LoraLoader|pysssss, CR SDXL Aspect Ratio, MaskPreview+]
members: [图片生成/文生图/1931364557795864578.json, 图片生成/文生图/邓诗宇生成器_1872182670309388289.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_lora_sampler_34

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/1931364557795864578.json、图片生成/文生图/邓诗宇生成器_1872182670309388289.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：76%

## 共有节点

全部 2 个 workflow 都包含：
- `Anything Everywhere`
- `ApplyFBCacheOnModel`
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncode`
- `CR SDXL Aspect Ratio`
- `DepthAnythingPreprocessor`
- `DisableNoise`
- `DualCLIPLoader`
- `FluxGuidance`
- `GetNode`
- `GrowMask`
- `ImageScaleBy`
- `ImageScaleToTotalPixels`
- `ImageUpscaleWithModel`
- `ImpactImageBatchToImageList`
- `Joy_caption_two`
- `Joy_caption_two_load`
- `KSamplerSelect`
- `LayerFilter: FilmV2`
- `LayerMask: SegmentAnythingUltra V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `LoraLoader|pysssss`
- `MaskBlur+`
- `MaskPreview+`
- `ModelSamplingFlux`
- `Note Plus (mtb)`
- `PreviewImage`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `SetLatentNoiseMask`
- `SetNode`
- `ShowText|pysssss`
- `SplitSigmasDenoise`
- `StringFunction|pysssss`
- `TTP_Image_Assy`
- `TTP_Image_Tile_Batch`
- `TTP_Tile_image_size`
- `TextInput_`
- `UNETLoader`
- `UpscaleModelLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy cleanGpuUsed`
- `easy clearCacheAll`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| LoRA 模型强度 | 0.6 | - | 2 | 100% |
| LoRA 文本强度 | 1 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- LoRA 模型强度 中位数 0.6，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- LoRA 文本强度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 这些节点还没有知识卡，系统对它们的理解有限：LayerFilter: FilmV2、LayerMask: SegmentAnythingUltra V2、MaskBlur+、Note Plus (mtb)、StringFunction|pysssss
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参

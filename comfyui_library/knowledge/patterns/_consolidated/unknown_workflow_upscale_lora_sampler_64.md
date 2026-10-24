---
name: unknown_workflow_upscale_lora_sampler_64
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.820667
common_nodes: [Anything Everywhere, ApplyFBCacheOnModel, BasicGuider, BasicScheduler, CLIPTextEncode, CR SDXL Aspect Ratio, DepthAnythingPreprocessor, DisableNoise, DualCLIPLoader, FluxGuidance, GetNode, GrowMask, ImageScaleBy, ImageScaleToTotalPixels, ImageUpscaleWithModel, ImpactImageBatchToImageList, Joy_caption_two, Joy_caption_two_load, KSamplerSelect, LayerFilter: FilmV2, LayerMask: SegmentAnythingUltra V2, LoadImage, LoraLoaderModelOnly, LoraLoader|pysssss, MaskBlur+, MaskPreview+, ModelSamplingFlux, PreviewImage, RandomNoise, SamplerCustomAdvanced, SetLatentNoiseMask, SetNode, ShowText|pysssss, SplitSigmasDenoise, StringFunction|pysssss, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, TextInput_, UNETLoader, UpscaleModelLoader, VAEDecode, VAEEncode, VAELoader, easy cleanGpuUsed, easy clearCacheAll]
problems: []
missing: []
members: [图片生成/图生图/美少女生成器-参考图自动反推_1933099671973756929.json, 图片生成/文生图/邓诗宇生成器-图片反推版_1931364557795864578.json, 图片生成/文生图/邓诗宇生成器_1872182670309388289.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_lora_sampler_64

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/美少女生成器-参考图自动反推_1933099671973756929.json、图片生成/文生图/邓诗宇生成器-图片反推版_1931364557795864578.json、图片生成/文生图/邓诗宇生成器_1872182670309388289.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：82%

## 共有节点

全部 3 个 workflow 都包含：
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
- `PreviewImage`
- `RandomNoise`
- `SamplerCustomAdvanced`
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

**可变部分**（部分 workflow 才有）：
- `Note Plus (mtb)` —— 2/3 个有
- `SaveImage` —— 2/3 个有
- `BaiduTranslateNode` —— 1/3 个有
- `SaveImageAndMetadata_` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| LoRA 模型强度 | 0.6 | 0.6 - 0.6 | 3 | 100% |
| LoRA 文本强度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- LoRA 模型强度 中位数 0.6，观测区间 0.6 - 0.6，3 个样本，取值集中（一致性 100%）
- LoRA 文本强度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）

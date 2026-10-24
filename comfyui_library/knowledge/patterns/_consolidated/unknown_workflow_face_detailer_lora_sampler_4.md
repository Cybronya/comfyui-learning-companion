---
name: unknown_workflow_face_detailer_lora_sampler_4
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.681
common_nodes: [BasicGuider, BasicScheduler, CLIPTextEncode, CLIPVisionLoader, CR Text, DeepTranslatorTextNode, DetailDaemonSamplerNode, DualCLIPLoader, EmptySD3LatentImage, FaceDetailer, Fast Groups Bypasser (rgthree), FluxAttentionSeeker+, FluxGuidance, Get resolution [Crystools], GetNode, INTConstant, ImageScale, ImpactImageBatchToImageList, KSamplerSelect, LoadImage, LoraLoaderModelOnly, ModelSamplingFlux, PreviewImage, RandomNoise, ReduxPromptStyler, SAMLoader, SamplerCustomAdvanced, SaveImage, Seed (rgthree), SetNode, ShowText|pysssss, StyleModelLoader, UltralyticsDetectorProvider, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/FLUX网红孵蛋器洗图【2张】_1937491891963215874.json, 图片生成/图生图/Flux-AI网红孵化器v1.0_1901941582348886018.json]
source: knowledge_consolidation
---

# unknown_workflow_face_detailer_lora_sampler_4

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/FLUX网红孵蛋器洗图【2张】_1937491891963215874.json、图片生成/图生图/Flux-AI网红孵化器v1.0_1901941582348886018.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：68%

## 共有节点

全部 2 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncode`
- `CLIPVisionLoader`
- `CR Text`
- `DeepTranslatorTextNode`
- `DetailDaemonSamplerNode`
- `DualCLIPLoader`
- `EmptySD3LatentImage`
- `FaceDetailer`
- `Fast Groups Bypasser (rgthree)`
- `FluxAttentionSeeker+`
- `FluxGuidance`
- `Get resolution [Crystools]`
- `GetNode`
- `INTConstant`
- `ImageScale`
- `ImpactImageBatchToImageList`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingFlux`
- `PreviewImage`
- `RandomNoise`
- `ReduxPromptStyler`
- `SAMLoader`
- `SamplerCustomAdvanced`
- `SaveImage`
- `Seed (rgthree)`
- `SetNode`
- `ShowText|pysssss`
- `StyleModelLoader`
- `UltralyticsDetectorProvider`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Any Switch (rgthree)` —— 1/2 个有
- `Anything Everywhere` —— 1/2 个有
- `Bookmark (rgthree)` —— 1/2 个有
- `CLIPLoader` —— 1/2 个有
- `CLIPtionGenerate` —— 1/2 个有
- `CLIPtionLoader` —— 1/2 个有
- `CheckpointLoaderSimple` —— 1/2 个有
- `ImageScaleToTotalPixels` —— 1/2 个有
- `ImageUpscaleWithModel` —— 1/2 个有
- `Joy_caption_two` —— 1/2 个有
- `Joy_caption_two_load` —— 1/2 个有
- `ModelPassThrough` —— 1/2 个有
- `TTP_Image_Assy` —— 1/2 个有
- `TTP_Image_Tile_Batch` —— 1/2 个有
- `TTP_Tile_image_size` —— 1/2 个有
- `Text Concatenate` —— 1/2 个有
- `UNETLoader` —— 1/2 个有
- `UpscaleModelLoader` —— 1/2 个有
- `VAEDecodeTiled` —— 1/2 个有
- `VAEEncode` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参

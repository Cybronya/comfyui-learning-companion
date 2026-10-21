---
name: unknown_workflow_video_sampler_clip_243
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.6975
common_nodes: [Audio Duration (mtb), AudioCrop, CLIPTextEncode, CR Text, CR Text Concatenate, CR Text Replace, DiffusionModelLoaderKJ, DualCLIPLoader, EmptyLTXVLatentVideo, Float, ImageResizeKJv2, Int to String, KSamplerSelect, LTX2_NAG, LTXVAudioVAEEncode, LTXVConcatAVLatent, LTXVConditioning, LTXVImgToVideoInplaceKJ, LTXVSeparateAVLatent, LoadAudio, LoadImage, MathExpression|pysssss, MelBandRoFormerModelLoader, MelBandRoFormerSampler, PreviewAny, PreviewAudio, PreviewImage, PromptRelayEncode, Qwen3ASRLoader, Qwen3ASRTranscribe, RHHiddenNodes, RH_Translator, SamplerCustom, SetLatentNoiseMask, ShowAnything|Mie, SolidMask, SomethingToString, Split String, TTResolutionSelector, Text, VAEDecodeTiled, VAELoaderKJ, VHS_VideoCombine, easy showAnything]
problems: []
missing: []
members: [视频生成/图生视频/2051860484126715906.json, 视频生成/图生视频/2050900841577623553.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_243

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/2051860484126715906.json、视频生成/图生视频/2050900841577623553.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：70%

## 共有节点

全部 2 个 workflow 都包含：
- `Audio Duration (mtb)`
- `AudioCrop`
- `CLIPTextEncode`
- `CR Text`
- `CR Text Concatenate`
- `CR Text Replace`
- `DiffusionModelLoaderKJ`
- `DualCLIPLoader`
- `EmptyLTXVLatentVideo`
- `Float`
- `ImageResizeKJv2`
- `Int to String`
- `KSamplerSelect`
- `LTX2_NAG`
- `LTXVAudioVAEEncode`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVImgToVideoInplaceKJ`
- `LTXVSeparateAVLatent`
- `LoadAudio`
- `LoadImage`
- `MathExpression|pysssss`
- `MelBandRoFormerModelLoader`
- `MelBandRoFormerSampler`
- `PreviewAny`
- `PreviewAudio`
- `PreviewImage`
- `PromptRelayEncode`
- `Qwen3ASRLoader`
- `Qwen3ASRTranscribe`
- `RHHiddenNodes`
- `RH_Translator`
- `SamplerCustom`
- `SetLatentNoiseMask`
- `ShowAnything|Mie`
- `SolidMask`
- `SomethingToString`
- `Split String`
- `TTResolutionSelector`
- `Text`
- `VAEDecodeTiled`
- `VAELoaderKJ`
- `VHS_VideoCombine`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `GuHaiAutoImageSplit` —— 1/2 个有
- `LoraLoaderModelOnly` —— 1/2 个有
- `ManualSigmas` —— 1/2 个有
- `RH_LLMAPI_Pro_Node` —— 1/2 个有
- `SaveImage` —— 1/2 个有
- `llama_cpp_instruct_adv` —— 1/2 个有
- `llama_cpp_model_loader` —— 1/2 个有
- `llama_cpp_parameters` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参

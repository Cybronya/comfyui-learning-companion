---
name: unknown_workflow_video_upscale_latent_upscale_138
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.795
common_nodes: [BasicGuider, BasicScheduler, CFGGuider, CLIPLoader, CLIPTextEncode, CR Prompt Text, CR Text, ComfyMathExpression, Float, GetImageSize, GetNode, ImageConcatMulti, ImageResize+, JoinStrings, KSamplerSelect, LTX2MemoryEfficientSageAttentionPatch, LTX2_NAG, LTXVAddGuideMulti, LTXVAudioVAEDecode, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVEmptyLatentAudio, LTXVLatentUpsampler, LTXVPreprocess, LTXVSeparateAVLatent, LatentUpscaleModelLoader, LoadImage, LoraLoaderModelOnly, ManualSigmas, MiniMaxH3ImageToVideo, MiniMaxH3MemoryEfficientSageAttentionPatch, MiniMaxH3ReferenceToVideo, MinimaxH3LatentUpscaler3D, ModelAttentionBackend, PreviewAny, PreviewImage, PrimitiveFloat, ProcessString, RandomNoise, ResolutionSelector, SLASageAttention, SamplerCustomAdvanced, SetNode, ShowText|pysssss, SomethingToString, TextInput_, UNETLoader, VAEDecode, VAEDecodeAudio, VAEDecodeTiled, VAEEncode, VAELoader, VHS_VideoCombine, easy cleanGpuUsed, easy showAnything, llama_cpp_instruct_adv, llama_cpp_model_loader, llama_cpp_parameters, 孤海注释]
problems: []
missing: []
members: [视频生成/图生视频/Minimax-h3 fl2va 首尾帧 2K 二采 Qwen3.8 27B反推版V1_2085988831085551618.json, 视频生成/图生视频/Minimaxh3-ltx2.5  fl2va首尾帧4K  Qwen3.8反推 V2_2087829357170610177.json]
source: knowledge_consolidation
---

# unknown_workflow_video_upscale_latent_upscale_138

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/Minimax-h3 fl2va 首尾帧 2K 二采 Qwen3.8 27B反推版V1_2085988831085551618.json、视频生成/图生视频/Minimaxh3-ltx2.5  fl2va首尾帧4K  Qwen3.8反推 V2_2087829357170610177.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：80%

## 共有节点

全部 2 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Prompt Text`
- `CR Text`
- `ComfyMathExpression`
- `Float`
- `GetImageSize`
- `GetNode`
- `ImageConcatMulti`
- `ImageResize+`
- `JoinStrings`
- `KSamplerSelect`
- `LTX2MemoryEfficientSageAttentionPatch`
- `LTX2_NAG`
- `LTXVAddGuideMulti`
- `LTXVAudioVAEDecode`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVCropGuides`
- `LTXVEmptyLatentAudio`
- `LTXVLatentUpsampler`
- `LTXVPreprocess`
- `LTXVSeparateAVLatent`
- `LatentUpscaleModelLoader`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ManualSigmas`
- `MiniMaxH3ImageToVideo`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `MiniMaxH3ReferenceToVideo`
- `MinimaxH3LatentUpscaler3D`
- `ModelAttentionBackend`
- `PreviewAny`
- `PreviewImage`
- `PrimitiveFloat`
- `ProcessString`
- `RandomNoise`
- `ResolutionSelector`
- `SLASageAttention`
- `SamplerCustomAdvanced`
- `SetNode`
- `ShowText|pysssss`
- `SomethingToString`
- `TextInput_`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAEDecodeTiled`
- `VAEEncode`
- `VAELoader`
- `VHS_VideoCombine`
- `easy cleanGpuUsed`
- `easy showAnything`
- `llama_cpp_instruct_adv`
- `llama_cpp_model_loader`
- `llama_cpp_parameters`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `CheckpointLoaderSimple` —— 1/2 个有
- `GetImageSizeAndCount` —— 1/2 个有
- `ImageResizeKJv2` —— 1/2 个有
- `ImageScaleBy` —— 1/2 个有
- `InjectLatentNoise+` —— 1/2 个有
- `Int` —— 1/2 个有
- `LTXAVTextEncoderLoader` —— 1/2 个有
- `LTXVAudioVAELoader` —— 1/2 个有
- `MathExpression|pysssss` —— 1/2 个有
- `MiniMaxH3LatentUpscaleCombined` —— 1/2 个有
- `PrimitiveStringMultiline` —— 1/2 个有
- `easy forLoopEnd` —— 1/2 个有
- `easy forLoopStart` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 97 | - | 2 | 100% |
| 高度 | 25 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 97，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高度 中位数 25，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参

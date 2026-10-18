---
key: 视频生成/图生视频/双剑合璧_MiniMax_H3_+_LTX2.5_多参视频生成_2105108981030146049.json
name: 双剑合璧_MiniMax_H3_+_LTX2.5_多参视频生成_2105108981030146049
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/双剑合璧_MiniMax_H3_+_LTX2.5_多参视频生成_2105108981030146049.json
hash: 64bd8cbcd24e9f09
coverage: 0.589552
learned_at: 2026-10-17 22:19:43
nodes: [LoraLoaderModelOnly, CLIPLoader, VAELoader, MiniMaxH3HybridLoader, RandomNoise, GetNode, GetNode, MiniMaxH3SigmaShift, ModelAttentionBackend, GetNode, ComfyMathExpression, SamplerCustomAdvanced, LTXVAudioVAEDecode, LTXVSeparateAVLatent, GetNode, LTXVCropGuides, ManualSigmas, LTXAddVideoICLoRAGuide, GetNode, GetNode, GetNode, GetNode, SolidMask, LTXVAudioVAEEncode, GetNode, ComfyMathExpression, RandomNoise, LTXVConcatAVLatent, KSamplerSelect, ModelAttentionBackend, LoraLoaderModelOnly, SetNode, SetNode, LoraLoaderModelOnly, MiniMaxH3MemoryEfficientSageAttentionPatch, MiniMaxH3SigmaShift, SetNode, GetNode, GetNode, KSamplerSelect, GetNode, GetNode, ComfyMathExpression, GetNode, GetNode, BasicScheduler, GetNode, ExtendIntermediateSigmas, GetNode, GetNode, PromptRelayEncode, LTXVConditioning, SetNode, SetNode, SetNode, SetNode, SetNode, LoraLoaderModelOnly, LTXICLoRALoaderModelOnly, PathchSageAttentionKJ, LTXVChunkFeedForward, UNETLoader, VAELoaderKJ, VAELoader, SetNode, CLIPLoader, SetNode, VAELoaderKJ, UNETLoader, SetNode, GetNode, SetNode, GetNode, ToString, GetNode, StringConcatenate, JoinStringMulti, GetNode, PrimitiveStringMultiline, llama_cpp_instruct_adv, llama_cpp_parameters, PurgeVRAM_UTK, PrimitiveStringMultiline, llama_cpp_model_loader, SetNode, Any Switch (rgthree), easy showAnything, easy showAnything, VAEEncode, LatentUpscaleModelLoader, GetNode, SamplerCustomAdvanced, MiniMaxH3AVDecodeT8, PurgeVRAM_UTK, CLIPTextEncode, GetNode, SetLatentNoiseMask, CFGGuider, LTXVLatentUpsampler, GetNode, StringLength, ComfyMathExpression, string_util_StrFind, StringSubstring, string_util_StrFind, StringSubstring, easy showAnything, easy showAnything, BasicGuider, MiniMaxH3ReferenceToVideo, VHS_VideoCombine, VHS_VideoCombine, LoadImage, LoadImage, GetNode, GetNode, SetNode, BatchImagesNode, LiconMSR, VAEDecode, SetNode, SetNode, easy showAnything, easy showAnything, ResolutionSelector, LoadImage, LoadAudio, LoadAudio, LoadAudio, SetNode, LTX2AttentionTunerPatch, PrimitiveFloat, EmptyImage, PreviewImage]
patterns: []
missing: []
---

# 视频生成/图生视频/双剑合璧_MiniMax_H3_+_LTX2.5_多参视频生成_2105108981030146049.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/双剑合璧_MiniMax_H3_+_LTX2.5_多参视频生成_2105108981030146049.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（134 个）：
- `LoraLoaderModelOnly` ★核心
- `CLIPLoader`
- `VAELoader`
- `MiniMaxH3HybridLoader`
- `RandomNoise`
- `GetNode`
- `GetNode`
- `MiniMaxH3SigmaShift`
- `ModelAttentionBackend`
- `GetNode`
- `ComfyMathExpression`
- `SamplerCustomAdvanced` ★核心
- `LTXVAudioVAEDecode` ★核心
- `LTXVSeparateAVLatent`
- `GetNode`
- `LTXVCropGuides`
- `ManualSigmas`
- `LTXAddVideoICLoRAGuide`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SolidMask`
- `LTXVAudioVAEEncode` ★核心
- `GetNode`
- `ComfyMathExpression`
- `RandomNoise`
- `LTXVConcatAVLatent`
- `KSamplerSelect` ★核心
- `ModelAttentionBackend`
- `LoraLoaderModelOnly` ★核心
- `SetNode`
- `SetNode`
- `LoraLoaderModelOnly` ★核心
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `MiniMaxH3SigmaShift`
- `SetNode`
- `GetNode`
- `GetNode`
- `KSamplerSelect` ★核心
- `GetNode`
- `GetNode`
- `ComfyMathExpression`
- `GetNode`
- `GetNode`
- `BasicScheduler`
- `GetNode`
- `ExtendIntermediateSigmas`
- `GetNode`
- `GetNode`
- `PromptRelayEncode`
- `LTXVConditioning`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `LoraLoaderModelOnly` ★核心
- `LTXICLoRALoaderModelOnly` ★核心
- `PathchSageAttentionKJ`
- `LTXVChunkFeedForward`
- `UNETLoader` ★核心
- `VAELoaderKJ`
- `VAELoader`
- `SetNode`
- `CLIPLoader`
- `SetNode`
- `VAELoaderKJ`
- `UNETLoader` ★核心
- `SetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `ToString`
- `GetNode`
- `StringConcatenate`
- `JoinStringMulti`
- `GetNode`
- `PrimitiveStringMultiline`
- `llama_cpp_instruct_adv`
- `llama_cpp_parameters`
- `PurgeVRAM_UTK`
- `PrimitiveStringMultiline`
- `llama_cpp_model_loader`
- `SetNode`
- `Any Switch (rgthree)`
- `easy showAnything`
- `easy showAnything`
- `VAEEncode` ★核心
- `LatentUpscaleModelLoader`
- `GetNode`
- `SamplerCustomAdvanced` ★核心
- `MiniMaxH3AVDecodeT8`
- `PurgeVRAM_UTK`
- `CLIPTextEncode` ★核心
- `GetNode`
- `SetLatentNoiseMask`
- `CFGGuider`
- `LTXVLatentUpsampler` ★核心
- `GetNode`
- `StringLength`
- `ComfyMathExpression`
- `string_util_StrFind`
- `StringSubstring`
- `string_util_StrFind`
- `StringSubstring`
- `easy showAnything`
- `easy showAnything`
- `BasicGuider`
- `MiniMaxH3ReferenceToVideo`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `LoadImage`
- `LoadImage`
- `GetNode`
- `GetNode`
- `SetNode`
- `BatchImagesNode`
- `LiconMSR`
- `VAEDecode` ★核心
- `SetNode`
- `SetNode`
- `easy showAnything`
- `easy showAnything`
- `ResolutionSelector`
- `LoadImage`
- `LoadAudio`
- `LoadAudio`
- `LoadAudio`
- `SetNode`
- `LTX2AttentionTunerPatch`
- `PrimitiveFloat`
- `EmptyImage`
- `PreviewImage`

## 知识

覆盖率 **59%**（79/134）

**有卡**：`LoraLoaderModelOnly`、`CLIPLoader`、`VAELoader`、`MiniMaxH3HybridLoader`、`RandomNoise`、`MiniMaxH3SigmaShift`、`ModelAttentionBackend`、`ComfyMathExpression`、`SamplerCustomAdvanced`、`LTXVAudioVAEDecode`、`LTXVSeparateAVLatent`、`LTXVCropGuides`、`ManualSigmas`、`LTXAddVideoICLoRAGuide`、`SolidMask`、`LTXVAudioVAEEncode`、`LTXVConcatAVLatent`、`KSamplerSelect`、`MiniMaxH3MemoryEfficientSageAttentionPatch`、`BasicScheduler`、`ExtendIntermediateSigmas`、`PromptRelayEncode`、`LTXVConditioning`、`LTXICLoRALoaderModelOnly`、`PathchSageAttentionKJ`、`LTXVChunkFeedForward`、`UNETLoader`、`VAELoaderKJ`、`ToString`、`StringConcatenate`、`JoinStringMulti`、`llama_cpp_instruct_adv`、`llama_cpp_parameters`、`PurgeVRAM_UTK`、`llama_cpp_model_loader`、`VAEEncode`、`LatentUpscaleModelLoader`、`MiniMaxH3AVDecodeT8`、`CLIPTextEncode`、`SetLatentNoiseMask`、`CFGGuider`、`LTXVLatentUpsampler`、`StringLength`、`string_util_StrFind`、`StringSubstring`、`BasicGuider`、`MiniMaxH3ReferenceToVideo`、`VHS_VideoCombine`、`LoadImage`、`BatchImagesNode`、`LiconMSR`、`VAEDecode`、`ResolutionSelector`、`LoadAudio`、`LTX2AttentionTunerPatch`、`EmptyImage`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、ResolutionSelector、LoadImage、UNETLoader

---
key: 视频生成/图生视频/MiniMax H3参考生视频-LTX2.5 MSR二采放大-音频参考-自动提示词优化-V1.1_2088533956374384642.json
name: MiniMax H3参考生视频-LTX2.5 MSR二采放大-音频参考-自动提示词优化-V1.1_2088533956374384642
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/MiniMax H3参考生视频-LTX2.5 MSR二采放大-音频参考-自动提示词优化-V1.1_2088533956374384642.json
hash: 7d99909f16ec3b0f
coverage: 0.613333
learned_at: 2026-10-16 21:43:26
nodes: [SetNode, llama_cpp_parameters, BatchImagesNode, MarkdownNote, SetNode, SetNode, easy showAnything, LoadImage, LoadImage, LoadImage, LoadImage, Fast Groups Bypasser (rgthree), Fast Groups Bypasser (rgthree), PurgeVRAM_UTK, BasicGuider, GetNode, llama_cpp_instruct_adv, VAELoader, SetNode, JoinStringMulti, StringConcatenate, GetNode, ToString, GetNode, SetNode, PrimitiveFloat, RandomNoise, GetNode, SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, VAELoader, LoadAudio, GetNode, ComfyMathExpression, UNETLoader, VAELoader, GetNode, LTXVConcatAVLatent, GetNode, GetNode, SamplerCustomAdvanced, GetNode, LTXVChunkFeedForward, PathchSageAttentionKJ, UNETLoader, LTX2AttentionTunerPatch, VAELoaderKJ, VAELoaderKJ, SetLatentNoiseMask, CLIPLoader, SetNode, SetNode, SetNode, SetNode, GetNode, MarkdownNote, MarkdownNote, UNETLoader, SolidMask, ComfyMathExpression, GetNode, GetNode, ComfyMathExpression, GetNode, GetNode, GetNode, GetNode, LTXVAudioVAEEncode, PurgeVRAM_UTK, VHS_VideoCombine, VHS_VideoCombine, PromptRelayEncode, LTXVConditioning, SetNode, SetNode, GetNode, GetNode, CLIPTextEncode, SetNode, GetNode, Any Switch (rgthree), easy showAnything, string_util_StrFind, easy showAnything, GetNode, ComfyMathExpression, string_util_StrFind, StringLength, easy showAnything, StringSubstring, StringSubstring, LoadAudio, LoadAudio, easy showAnything, LoadImage, LoadImage, LoadImage, LoadImage, MiniMaxH3AVDecodeT8, easy showAnything, SamplerCustomAdvanced, MiniMaxH3HybridLoader, LoraLoaderModelOnly, MiniMaxH3MemoryEfficientSageAttentionPatch, VAEEncode, LatentUpscaleModelLoader, LTXVLatentUpsampler, Label (rgthree), SetNode, SetNode, MarkdownNote, MiniMaxH3SigmaShift, LoraLoaderModelOnly, PrimitiveStringMultiline, MiniMaxH3MemoryEfficientSageAttentionPatch, MiniMaxH3SigmaShift, SetNode, ModelAttentionBackend, LoraLoaderModelOnly, ModelAttentionBackend, LoraLoaderModelOnly, CLIPLoader, Fast Groups Bypasser (rgthree), UNETLoader, PrimitiveStringMultiline, LoadImage, ResolutionSelector, llama_cpp_model_loader, LTXVSeparateAVLatent, VAEDecode, LTXVCropGuides, LTXVAudioVAEDecode, LTXVConditioning, RandomNoise, KSamplerSelect, ManualSigmas, ComfyUILTX25MSRMultiReferenceGuide, LoraLoaderModelOnly, LTXVDualCFGGuider, BasicScheduler, H3SigmaRefiner, ExtendIntermediateSigmas, KSamplerSelect, CLIPLoader, MiniMaxH3ReferenceToVideo, ComfyUILTX25MSRICLoRALoader]
patterns: []
missing: []
---

# 视频生成/图生视频/MiniMax H3参考生视频-LTX2.5 MSR二采放大-音频参考-自动提示词优化-V1.1_2088533956374384642.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/MiniMax H3参考生视频-LTX2.5 MSR二采放大-音频参考-自动提示词优化-V1.1_2088533956374384642.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Process → Other

**节点**（150 个）：
- `SetNode`
- `llama_cpp_parameters`
- `BatchImagesNode`
- `MarkdownNote`
- `SetNode`
- `SetNode`
- `easy showAnything`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `Fast Groups Bypasser (rgthree)`
- `Fast Groups Bypasser (rgthree)`
- `PurgeVRAM_UTK`
- `BasicGuider`
- `GetNode`
- `llama_cpp_instruct_adv`
- `VAELoader`
- `SetNode`
- `JoinStringMulti`
- `StringConcatenate`
- `GetNode`
- `ToString`
- `GetNode`
- `SetNode`
- `PrimitiveFloat`
- `RandomNoise`
- `GetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `VAELoader`
- `LoadAudio`
- `GetNode`
- `ComfyMathExpression`
- `UNETLoader` ★核心
- `VAELoader`
- `GetNode`
- `LTXVConcatAVLatent`
- `GetNode`
- `GetNode`
- `SamplerCustomAdvanced` ★核心
- `GetNode`
- `LTXVChunkFeedForward`
- `PathchSageAttentionKJ`
- `UNETLoader` ★核心
- `LTX2AttentionTunerPatch`
- `VAELoaderKJ`
- `VAELoaderKJ`
- `SetLatentNoiseMask`
- `CLIPLoader`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `MarkdownNote`
- `MarkdownNote`
- `UNETLoader` ★核心
- `SolidMask`
- `ComfyMathExpression`
- `GetNode`
- `GetNode`
- `ComfyMathExpression`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `LTXVAudioVAEEncode` ★核心
- `PurgeVRAM_UTK`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `PromptRelayEncode`
- `LTXVConditioning`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `CLIPTextEncode` ★核心
- `SetNode`
- `GetNode`
- `Any Switch (rgthree)`
- `easy showAnything`
- `string_util_StrFind`
- `easy showAnything`
- `GetNode`
- `ComfyMathExpression`
- `string_util_StrFind`
- `StringLength`
- `easy showAnything`
- `StringSubstring`
- `StringSubstring`
- `LoadAudio`
- `LoadAudio`
- `easy showAnything`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `MiniMaxH3AVDecodeT8`
- `easy showAnything`
- `SamplerCustomAdvanced` ★核心
- `MiniMaxH3HybridLoader`
- `LoraLoaderModelOnly` ★核心
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `VAEEncode` ★核心
- `LatentUpscaleModelLoader`
- `LTXVLatentUpsampler` ★核心
- `Label (rgthree)`
- `SetNode`
- `SetNode`
- `MarkdownNote`
- `MiniMaxH3SigmaShift`
- `LoraLoaderModelOnly` ★核心
- `PrimitiveStringMultiline`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `MiniMaxH3SigmaShift`
- `SetNode`
- `ModelAttentionBackend`
- `LoraLoaderModelOnly` ★核心
- `ModelAttentionBackend`
- `LoraLoaderModelOnly` ★核心
- `CLIPLoader`
- `Fast Groups Bypasser (rgthree)`
- `UNETLoader` ★核心
- `PrimitiveStringMultiline`
- `LoadImage`
- `ResolutionSelector`
- `llama_cpp_model_loader`
- `LTXVSeparateAVLatent`
- `VAEDecode` ★核心
- `LTXVCropGuides`
- `LTXVAudioVAEDecode` ★核心
- `LTXVConditioning`
- `RandomNoise`
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `ComfyUILTX25MSRMultiReferenceGuide`
- `LoraLoaderModelOnly` ★核心
- `LTXVDualCFGGuider`
- `BasicScheduler`
- `H3SigmaRefiner`
- `ExtendIntermediateSigmas`
- `KSamplerSelect` ★核心
- `CLIPLoader`
- `MiniMaxH3ReferenceToVideo`
- `ComfyUILTX25MSRICLoRALoader` ★核心

## 知识

覆盖率 **61%**（92/150）

**有卡**：`llama_cpp_parameters`、`BatchImagesNode`、`LoadImage`、`PurgeVRAM_UTK`、`BasicGuider`、`llama_cpp_instruct_adv`、`VAELoader`、`JoinStringMulti`、`StringConcatenate`、`ToString`、`RandomNoise`、`LoadAudio`、`ComfyMathExpression`、`UNETLoader`、`LTXVConcatAVLatent`、`SamplerCustomAdvanced`、`LTXVChunkFeedForward`、`PathchSageAttentionKJ`、`LTX2AttentionTunerPatch`、`VAELoaderKJ`、`SetLatentNoiseMask`、`CLIPLoader`、`SolidMask`、`LTXVAudioVAEEncode`、`VHS_VideoCombine`、`PromptRelayEncode`、`LTXVConditioning`、`CLIPTextEncode`、`string_util_StrFind`、`StringLength`、`StringSubstring`、`MiniMaxH3AVDecodeT8`、`MiniMaxH3HybridLoader`、`LoraLoaderModelOnly`、`MiniMaxH3MemoryEfficientSageAttentionPatch`、`VAEEncode`、`LatentUpscaleModelLoader`、`LTXVLatentUpsampler`、`Label (rgthree)`、`MiniMaxH3SigmaShift`、`ModelAttentionBackend`、`ResolutionSelector`、`llama_cpp_model_loader`、`LTXVSeparateAVLatent`、`VAEDecode`、`LTXVCropGuides`、`LTXVAudioVAEDecode`、`KSamplerSelect`、`ManualSigmas`、`ComfyUILTX25MSRMultiReferenceGuide`、`LTXVDualCFGGuider`、`BasicScheduler`、`H3SigmaRefiner`、`ExtendIntermediateSigmas`、`MiniMaxH3ReferenceToVideo`、`ComfyUILTX25MSRICLoRALoader`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、ResolutionSelector、LoadImage、UNETLoader

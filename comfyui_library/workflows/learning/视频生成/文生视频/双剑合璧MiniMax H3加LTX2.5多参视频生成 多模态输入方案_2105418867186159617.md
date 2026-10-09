---
key: 视频生成/文生视频/双剑合璧MiniMax H3加LTX2.5多参视频生成 多模态输入方案_2105418867186159617.json
name: 双剑合璧MiniMax H3加LTX2.5多参视频生成 多模态输入方案_2105418867186159617
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/双剑合璧MiniMax H3加LTX2.5多参视频生成 多模态输入方案_2105418867186159617.json
hash: 94846fd142b009ca
coverage: 0.652695
learned_at: 2026-10-10 00:07:23
nodes: [LoraLoaderModelOnly, CLIPLoader, VAELoader, MiniMaxH3HybridLoader, RandomNoise, GetNode, GetNode, MiniMaxH3SigmaShift, ModelAttentionBackend, GetNode, ComfyMathExpression, SamplerCustomAdvanced, LTXVAudioVAEDecode, LTXVSeparateAVLatent, GetNode, LTXVCropGuides, ManualSigmas, LTXAddVideoICLoRAGuide, GetNode, GetNode, GetNode, GetNode, SolidMask, LTXVAudioVAEEncode, GetNode, RandomNoise, LTXVConcatAVLatent, KSamplerSelect, ModelAttentionBackend, LoraLoaderModelOnly, SetNode, SetNode, LoraLoaderModelOnly, MiniMaxH3MemoryEfficientSageAttentionPatch, MiniMaxH3SigmaShift, SetNode, GetNode, GetNode, KSamplerSelect, GetNode, GetNode, ComfyMathExpression, GetNode, GetNode, BasicScheduler, GetNode, ExtendIntermediateSigmas, GetNode, GetNode, PromptRelayEncode, LTXVConditioning, SetNode, SetNode, SetNode, SetNode, SetNode, LoraLoaderModelOnly, LTXICLoRALoaderModelOnly, PathchSageAttentionKJ, LTXVChunkFeedForward, UNETLoader, VAELoaderKJ, VAELoader, SetNode, CLIPLoader, SetNode, VAELoaderKJ, UNETLoader, SetNode, GetNode, SetNode, GetNode, ToString, GetNode, StringConcatenate, JoinStringMulti, GetNode, llama_cpp_instruct_adv, llama_cpp_parameters, PurgeVRAM_UTK, PrimitiveStringMultiline, llama_cpp_model_loader, SetNode, Any Switch (rgthree), easy showAnything, easy showAnything, VAEEncode, LatentUpscaleModelLoader, GetNode, SamplerCustomAdvanced, MiniMaxH3AVDecodeT8, PurgeVRAM_UTK, CLIPTextEncode, GetNode, SetLatentNoiseMask, CFGGuider, LTXVLatentUpsampler, GetNode, StringSubstring, StringSubstring, easy showAnything, easy showAnything, BasicGuider, MiniMaxH3ReferenceToVideo, VHS_VideoCombine, VHS_VideoCombine, VAEDecode, SetNode, SetNode, easy showAnything, easy showAnything, LoadAudio, LoadAudio, LoadAudio, SetNode, LTX2AttentionTunerPatch, ComfyMathExpression, string_util_StrFind, string_util_StrFind, ComfyMathExpression, StringLength, LoadImage, ResolutionSelector, PrimitiveStringMultiline, PrimitiveFloat, BatchImagesNode, LiconMSR, GetNode, GetNode, SetNode, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, 孤海注释, 孤海注释, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, KSampler, EmptyLatentImage, JjkText, CLIPTextEncode, CLIPTextEncode, solarL_SaveImagesToZip, VAEDecode, CLIPLoader, VAELoader, Note, SaveImage]
patterns: [text_to_image, image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/文生视频/双剑合璧MiniMax H3加LTX2.5多参视频生成 多模态输入方案_2105418867186159617.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/双剑合璧MiniMax H3加LTX2.5多参视频生成 多模态输入方案_2105418867186159617.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（167 个）：
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
- `StringSubstring`
- `StringSubstring`
- `easy showAnything`
- `easy showAnything`
- `BasicGuider`
- `MiniMaxH3ReferenceToVideo`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `VAEDecode` ★核心
- `SetNode`
- `SetNode`
- `easy showAnything`
- `easy showAnything`
- `LoadAudio`
- `LoadAudio`
- `LoadAudio`
- `SetNode`
- `LTX2AttentionTunerPatch`
- `ComfyMathExpression`
- `string_util_StrFind`
- `string_util_StrFind`
- `ComfyMathExpression`
- `StringLength`
- `LoadImage`
- `ResolutionSelector`
- `PrimitiveStringMultiline`
- `PrimitiveFloat`
- `BatchImagesNode`
- `LiconMSR`
- `GetNode`
- `GetNode`
- `SetNode`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `孤海注释`
- `孤海注释`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `KSampler` ★核心
- `EmptyLatentImage` ★核心
- `JjkText`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `solarL_SaveImagesToZip`
- `VAEDecode` ★核心
- `CLIPLoader`
- `VAELoader`
- `Note`
- `SaveImage`

**识别到的模式**：text_to_image、image_to_image

## 关键参数

- `seed` = `598626327129635`
- `steps` = `4`
- `cfg` = `4.5`
- `sampler_name` = `er_sde`
- `scheduler` = `beta`
- `denoise` = `1`
- `width` = `80`
- `height` = `80`
- `batch_size` = `1`

## 知识

覆盖率 **65%**（109/167）

**有卡**：`LoraLoaderModelOnly`、`CLIPLoader`、`VAELoader`、`MiniMaxH3HybridLoader`、`RandomNoise`、`MiniMaxH3SigmaShift`、`ModelAttentionBackend`、`ComfyMathExpression`、`SamplerCustomAdvanced`、`LTXVAudioVAEDecode`、`LTXVSeparateAVLatent`、`LTXVCropGuides`、`ManualSigmas`、`LTXAddVideoICLoRAGuide`、`SolidMask`、`LTXVAudioVAEEncode`、`LTXVConcatAVLatent`、`KSamplerSelect`、`MiniMaxH3MemoryEfficientSageAttentionPatch`、`BasicScheduler`、`ExtendIntermediateSigmas`、`PromptRelayEncode`、`LTXVConditioning`、`LTXICLoRALoaderModelOnly`、`PathchSageAttentionKJ`、`LTXVChunkFeedForward`、`UNETLoader`、`VAELoaderKJ`、`ToString`、`StringConcatenate`、`JoinStringMulti`、`llama_cpp_instruct_adv`、`llama_cpp_parameters`、`PurgeVRAM_UTK`、`llama_cpp_model_loader`、`VAEEncode`、`LatentUpscaleModelLoader`、`MiniMaxH3AVDecodeT8`、`CLIPTextEncode`、`SetLatentNoiseMask`、`CFGGuider`、`LTXVLatentUpsampler`、`StringSubstring`、`BasicGuider`、`MiniMaxH3ReferenceToVideo`、`VHS_VideoCombine`、`VAEDecode`、`LoadAudio`、`LTX2AttentionTunerPatch`、`string_util_StrFind`、`StringLength`、`LoadImage`、`ResolutionSelector`、`BatchImagesNode`、`LiconMSR`、`KSampler`、`EmptyLatentImage`、`solarL_SaveImagesToZip`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage、ResolutionSelector

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

---
key: 视频生成/文生视频/LTX2.5 MSR二采放大｜MiniMax H3参考生音频提示词优化V1.1_2091907695048740866.json
name: LTX2.5 MSR二采放大｜MiniMax H3参考生音频提示词优化V1.1_2091907695048740866
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/LTX2.5 MSR二采放大｜MiniMax H3参考生音频提示词优化V1.1_2091907695048740866.json
hash: 46a72b602fea3c6f
coverage: 0.648045
learned_at: 2026-10-11 21:19:42
nodes: [SetNode, llama_cpp_parameters, BatchImagesNode, SetNode, SetNode, easy showAnything, LoadImage, LoadImage, LoadImage, Fast Groups Bypasser (rgthree), Fast Groups Bypasser (rgthree), PurgeVRAM_UTK, BasicGuider, GetNode, llama_cpp_instruct_adv, VAELoader, SetNode, JoinStringMulti, StringConcatenate, GetNode, ToString, GetNode, KSamplerSelect, SetNode, PrimitiveFloat, RandomNoise, GetNode, SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, VAELoader, LoadAudio, GetNode, ComfyMathExpression, UNETLoader, VAELoader, RandomNoise, GetNode, CFGGuider, LTXVConcatAVLatent, GetNode, GetNode, SamplerCustomAdvanced, LTXVSeparateAVLatent, LTXVAudioVAEDecode, VAEDecode, LTXVCropGuides, GetNode, GetNode, GetNode, GetNode, KSamplerSelect, LTXVChunkFeedForward, PathchSageAttentionKJ, UNETLoader, LTX2AttentionTunerPatch, ManualSigmas, LoraLoaderModelOnly, VAELoaderKJ, VAELoaderKJ, LTXICLoRALoaderModelOnly, SetLatentNoiseMask, CLIPLoader, SetNode, SetNode, SetNode, SetNode, LTXAddVideoICLoRAGuide, GetNode, UNETLoader, LiconMSR, SolidMask, ComfyMathExpression, GetNode, GetNode, ComfyMathExpression, GetNode, GetNode, GetNode, SetNode, GetNode, LTXVAudioVAEEncode, PurgeVRAM_UTK, PromptRelayEncode, LTXVConditioning, SetNode, SetNode, GetNode, GetNode, CLIPTextEncode, SetNode, GetNode, Any Switch (rgthree), easy showAnything, string_util_StrFind, easy showAnything, GetNode, ComfyMathExpression, string_util_StrFind, StringLength, easy showAnything, StringSubstring, StringSubstring, LoadAudio, LoadAudio, easy showAnything, LoadImage, LoadImage, MiniMaxH3AVDecodeT8, easy showAnything, SamplerCustomAdvanced, BasicScheduler, MiniMaxH3HybridLoader, LoraLoaderModelOnly, MiniMaxH3MemoryEfficientSageAttentionPatch, VAEEncode, LatentUpscaleModelLoader, LTXVLatentUpsampler, Label (rgthree), SetNode, SetNode, MiniMaxH3ReferenceToVideo, MiniMaxH3SigmaShift, LoraLoaderModelOnly, PrimitiveStringMultiline, MiniMaxH3MemoryEfficientSageAttentionPatch, MiniMaxH3SigmaShift, SetNode, ModelAttentionBackend, LoraLoaderModelOnly, ModelAttentionBackend, LoraLoaderModelOnly, CLIPLoader, CLIPLoader, ExtendIntermediateSigmas, Fast Groups Bypasser (rgthree), UNETLoader, LoadImage, ResolutionSelector, llama_cpp_model_loader, 孤海注释, 孤海注释, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, UNETLoader, KSampler, CLIPTextEncode, solarL_SaveImagesToZip, VAEDecode, VAELoader, CLIPLoader, EmptyLatentImage, JjkText, CLIPTextEncode, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, Note, LoadImage, LoadImage, LoadImage, PrimitiveStringMultiline, VHS_VideoCombine, VHS_VideoCombine, VHS_VideoCombine]
patterns: [text_to_image, image_to_image]
missing: [Label (rgthree)]
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [次要节点 `Label (rgthree)` 知识库中没有该节点类型的任何知识, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/文生视频/LTX2.5 MSR二采放大｜MiniMax H3参考生音频提示词优化V1.1_2091907695048740866.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/LTX2.5 MSR二采放大｜MiniMax H3参考生音频提示词优化V1.1_2091907695048740866.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（179 个）：
- `SetNode`
- `llama_cpp_parameters`
- `BatchImagesNode`
- `SetNode`
- `SetNode`
- `easy showAnything`
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
- `KSamplerSelect` ★核心
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
- `RandomNoise`
- `GetNode`
- `CFGGuider`
- `LTXVConcatAVLatent`
- `GetNode`
- `GetNode`
- `SamplerCustomAdvanced` ★核心
- `LTXVSeparateAVLatent`
- `LTXVAudioVAEDecode` ★核心
- `VAEDecode` ★核心
- `LTXVCropGuides`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `KSamplerSelect` ★核心
- `LTXVChunkFeedForward`
- `PathchSageAttentionKJ`
- `UNETLoader` ★核心
- `LTX2AttentionTunerPatch`
- `ManualSigmas`
- `LoraLoaderModelOnly` ★核心
- `VAELoaderKJ`
- `VAELoaderKJ`
- `LTXICLoRALoaderModelOnly` ★核心
- `SetLatentNoiseMask`
- `CLIPLoader`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `LTXAddVideoICLoRAGuide`
- `GetNode`
- `UNETLoader` ★核心
- `LiconMSR`
- `SolidMask`
- `ComfyMathExpression`
- `GetNode`
- `GetNode`
- `ComfyMathExpression`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `LTXVAudioVAEEncode` ★核心
- `PurgeVRAM_UTK`
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
- `MiniMaxH3AVDecodeT8`
- `easy showAnything`
- `SamplerCustomAdvanced` ★核心
- `BasicScheduler`
- `MiniMaxH3HybridLoader`
- `LoraLoaderModelOnly` ★核心
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `VAEEncode` ★核心
- `LatentUpscaleModelLoader`
- `LTXVLatentUpsampler` ★核心
- `Label (rgthree)`
- `SetNode`
- `SetNode`
- `MiniMaxH3ReferenceToVideo`
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
- `CLIPLoader`
- `ExtendIntermediateSigmas`
- `Fast Groups Bypasser (rgthree)`
- `UNETLoader` ★核心
- `LoadImage`
- `ResolutionSelector`
- `llama_cpp_model_loader`
- `孤海注释`
- `孤海注释`
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
- `UNETLoader` ★核心
- `KSampler` ★核心
- `CLIPTextEncode` ★核心
- `solarL_SaveImagesToZip`
- `VAEDecode` ★核心
- `VAELoader`
- `CLIPLoader`
- `EmptyLatentImage` ★核心
- `JjkText`
- `CLIPTextEncode` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `Note`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `PrimitiveStringMultiline`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `VHS_VideoCombine`

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

覆盖率 **65%**（116/179）

**有卡**：`llama_cpp_parameters`、`BatchImagesNode`、`LoadImage`、`PurgeVRAM_UTK`、`BasicGuider`、`llama_cpp_instruct_adv`、`VAELoader`、`JoinStringMulti`、`StringConcatenate`、`ToString`、`KSamplerSelect`、`RandomNoise`、`LoadAudio`、`ComfyMathExpression`、`UNETLoader`、`CFGGuider`、`LTXVConcatAVLatent`、`SamplerCustomAdvanced`、`LTXVSeparateAVLatent`、`LTXVAudioVAEDecode`、`VAEDecode`、`LTXVCropGuides`、`LTXVChunkFeedForward`、`PathchSageAttentionKJ`、`LTX2AttentionTunerPatch`、`ManualSigmas`、`LoraLoaderModelOnly`、`VAELoaderKJ`、`LTXICLoRALoaderModelOnly`、`SetLatentNoiseMask`、`CLIPLoader`、`LTXAddVideoICLoRAGuide`、`LiconMSR`、`SolidMask`、`LTXVAudioVAEEncode`、`PromptRelayEncode`、`LTXVConditioning`、`CLIPTextEncode`、`string_util_StrFind`、`StringLength`、`StringSubstring`、`MiniMaxH3AVDecodeT8`、`BasicScheduler`、`MiniMaxH3HybridLoader`、`MiniMaxH3MemoryEfficientSageAttentionPatch`、`VAEEncode`、`LatentUpscaleModelLoader`、`LTXVLatentUpsampler`、`MiniMaxH3ReferenceToVideo`、`MiniMaxH3SigmaShift`、`ModelAttentionBackend`、`ExtendIntermediateSigmas`、`ResolutionSelector`、`llama_cpp_model_loader`、`KSampler`、`solarL_SaveImagesToZip`、`EmptyLatentImage`、`VHS_VideoCombine`

**缺卡**（1）：`Label (rgthree)`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage、ResolutionSelector

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- 次要节点 `Label (rgthree)` 知识库中没有该节点类型的任何知识
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

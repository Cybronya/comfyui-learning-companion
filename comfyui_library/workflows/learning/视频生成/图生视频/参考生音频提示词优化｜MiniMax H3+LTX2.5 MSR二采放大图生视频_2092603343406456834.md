---
key: 视频生成/图生视频/参考生音频提示词优化｜MiniMax H3+LTX2.5 MSR二采放大图生视频_2092603343406456834.json
name: 参考生音频提示词优化｜MiniMax H3+LTX2.5 MSR二采放大图生视频_2092603343406456834
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/参考生音频提示词优化｜MiniMax H3+LTX2.5 MSR二采放大图生视频_2092603343406456834.json
hash: b4ede07dad0640fe
coverage: 0.651163
learned_at: 2026-10-16 22:59:52
nodes: [SetNode, llama_cpp_parameters, BatchImagesNode, SetNode, SetNode, easy showAnything, LoadImage, LoadImage, LoadImage, Fast Groups Bypasser (rgthree), Fast Groups Bypasser (rgthree), PurgeVRAM_UTK, BasicGuider, GetNode, llama_cpp_instruct_adv, VAELoader, SetNode, JoinStringMulti, StringConcatenate, GetNode, ToString, GetNode, KSamplerSelect, SetNode, PrimitiveFloat, RandomNoise, GetNode, SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, LoadAudio, GetNode, ComfyMathExpression, VAELoader, RandomNoise, GetNode, CFGGuider, LTXVConcatAVLatent, GetNode, GetNode, SamplerCustomAdvanced, LTXVSeparateAVLatent, LTXVAudioVAEDecode, VAEDecode, LTXVCropGuides, GetNode, GetNode, GetNode, GetNode, KSamplerSelect, LTXVChunkFeedForward, PathchSageAttentionKJ, UNETLoader, LTX2AttentionTunerPatch, ManualSigmas, LoraLoaderModelOnly, VAELoaderKJ, VAELoaderKJ, LTXICLoRALoaderModelOnly, SetLatentNoiseMask, CLIPLoader, SetNode, SetNode, SetNode, SetNode, LTXAddVideoICLoRAGuide, LiconMSR, SolidMask, ComfyMathExpression, GetNode, GetNode, ComfyMathExpression, GetNode, GetNode, GetNode, SetNode, GetNode, LTXVAudioVAEEncode, PurgeVRAM_UTK, PromptRelayEncode, LTXVConditioning, SetNode, SetNode, GetNode, GetNode, CLIPTextEncode, SetNode, GetNode, Any Switch (rgthree), easy showAnything, string_util_StrFind, easy showAnything, GetNode, ComfyMathExpression, string_util_StrFind, StringLength, easy showAnything, StringSubstring, StringSubstring, LoadAudio, LoadAudio, easy showAnything, LoadImage, LoadImage, MiniMaxH3AVDecodeT8, easy showAnything, SamplerCustomAdvanced, BasicScheduler, MiniMaxH3HybridLoader, LoraLoaderModelOnly, MiniMaxH3MemoryEfficientSageAttentionPatch, VAEEncode, LatentUpscaleModelLoader, LTXVLatentUpsampler, SetNode, SetNode, MiniMaxH3ReferenceToVideo, MiniMaxH3SigmaShift, LoraLoaderModelOnly, PrimitiveStringMultiline, MiniMaxH3MemoryEfficientSageAttentionPatch, MiniMaxH3SigmaShift, SetNode, ModelAttentionBackend, LoraLoaderModelOnly, ModelAttentionBackend, LoraLoaderModelOnly, CLIPLoader, ExtendIntermediateSigmas, Fast Groups Bypasser (rgthree), UNETLoader, ResolutionSelector, llama_cpp_model_loader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, UNETLoader, KSampler, CLIPTextEncode, solarL_SaveImagesToZip, VAEDecode, VAELoader, CLIPLoader, EmptyLatentImage, JjkText, CLIPTextEncode, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoadImage, VHS_VideoCombine, VHS_VideoCombine, VHS_VideoCombine, LoadImage, LoadImage, LoadImage, PrimitiveStringMultiline, 孤海注释, 孤海注释]
patterns: [text_to_image, image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/图生视频/参考生音频提示词优化｜MiniMax H3+LTX2.5 MSR二采放大图生视频_2092603343406456834.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/参考生音频提示词优化｜MiniMax H3+LTX2.5 MSR二采放大图生视频_2092603343406456834.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（172 个）：
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
- `LoadAudio`
- `GetNode`
- `ComfyMathExpression`
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
- `ExtendIntermediateSigmas`
- `Fast Groups Bypasser (rgthree)`
- `UNETLoader` ★核心
- `ResolutionSelector`
- `llama_cpp_model_loader`
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
- `LoadImage`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `PrimitiveStringMultiline`
- `孤海注释`
- `孤海注释`

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

覆盖率 **65%**（112/172）

**有卡**：`llama_cpp_parameters`、`BatchImagesNode`、`LoadImage`、`PurgeVRAM_UTK`、`BasicGuider`、`llama_cpp_instruct_adv`、`VAELoader`、`JoinStringMulti`、`StringConcatenate`、`ToString`、`KSamplerSelect`、`RandomNoise`、`LoadAudio`、`ComfyMathExpression`、`CFGGuider`、`LTXVConcatAVLatent`、`SamplerCustomAdvanced`、`LTXVSeparateAVLatent`、`LTXVAudioVAEDecode`、`VAEDecode`、`LTXVCropGuides`、`LTXVChunkFeedForward`、`PathchSageAttentionKJ`、`UNETLoader`、`LTX2AttentionTunerPatch`、`ManualSigmas`、`LoraLoaderModelOnly`、`VAELoaderKJ`、`LTXICLoRALoaderModelOnly`、`SetLatentNoiseMask`、`CLIPLoader`、`LTXAddVideoICLoRAGuide`、`LiconMSR`、`SolidMask`、`LTXVAudioVAEEncode`、`PromptRelayEncode`、`LTXVConditioning`、`CLIPTextEncode`、`string_util_StrFind`、`StringLength`、`StringSubstring`、`MiniMaxH3AVDecodeT8`、`BasicScheduler`、`MiniMaxH3HybridLoader`、`MiniMaxH3MemoryEfficientSageAttentionPatch`、`VAEEncode`、`LatentUpscaleModelLoader`、`LTXVLatentUpsampler`、`MiniMaxH3ReferenceToVideo`、`MiniMaxH3SigmaShift`、`ModelAttentionBackend`、`ExtendIntermediateSigmas`、`ResolutionSelector`、`llama_cpp_model_loader`、`KSampler`、`solarL_SaveImagesToZip`、`EmptyLatentImage`、`VHS_VideoCombine`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage、ResolutionSelector

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

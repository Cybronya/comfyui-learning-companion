---
key: 视频生成/图生视频/MiniMax H3参考生视频LTX2.5 MSR二采放大｜音频参考自动提示词优化V1.1图生视频_2090468504624521218.json
name: MiniMax H3参考生视频LTX2.5 MSR二采放大｜音频参考自动提示词优化V1.1图生视频_2090468504624521218
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/MiniMax H3参考生视频LTX2.5 MSR二采放大｜音频参考自动提示词优化V1.1图生视频_2090468504624521218.json
hash: 133ab87ef4bd940a
coverage: 0.643275
learned_at: 2026-10-16 22:02:04
nodes: [SetNode, llama_cpp_parameters, BatchImagesNode, SetNode, SetNode, easy showAnything, LoadImage, LoadImage, LoadImage, LoadImage, Fast Groups Bypasser (rgthree), Fast Groups Bypasser (rgthree), PurgeVRAM_UTK, BasicGuider, GetNode, llama_cpp_instruct_adv, VAELoader, SetNode, JoinStringMulti, StringConcatenate, GetNode, ToString, GetNode, KSamplerSelect, SetNode, PrimitiveFloat, RandomNoise, GetNode, SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, LoadAudio, GetNode, ComfyMathExpression, VAELoader, RandomNoise, GetNode, CFGGuider, LTXVConcatAVLatent, GetNode, GetNode, SamplerCustomAdvanced, LTXVSeparateAVLatent, LTXVAudioVAEDecode, VAEDecode, LTXVCropGuides, GetNode, GetNode, GetNode, GetNode, KSamplerSelect, LTXVChunkFeedForward, PathchSageAttentionKJ, UNETLoader, LTX2AttentionTunerPatch, ManualSigmas, LoraLoaderModelOnly, VAELoaderKJ, VAELoaderKJ, LTXICLoRALoaderModelOnly, SetLatentNoiseMask, CLIPLoader, SetNode, SetNode, SetNode, SetNode, LTXAddVideoICLoRAGuide, LiconMSR, SolidMask, ComfyMathExpression, GetNode, GetNode, ComfyMathExpression, GetNode, GetNode, GetNode, SetNode, VHS_VideoCombine, GetNode, LTXVAudioVAEEncode, PurgeVRAM_UTK, VHS_VideoCombine, VHS_VideoCombine, PromptRelayEncode, LTXVConditioning, SetNode, SetNode, GetNode, GetNode, CLIPTextEncode, SetNode, GetNode, Any Switch (rgthree), easy showAnything, string_util_StrFind, easy showAnything, GetNode, ComfyMathExpression, string_util_StrFind, StringLength, easy showAnything, StringSubstring, StringSubstring, LoadAudio, LoadAudio, easy showAnything, LoadImage, LoadImage, LoadImage, LoadImage, MiniMaxH3AVDecodeT8, easy showAnything, SamplerCustomAdvanced, BasicScheduler, MiniMaxH3HybridLoader, LoraLoaderModelOnly, MiniMaxH3MemoryEfficientSageAttentionPatch, VAEEncode, LatentUpscaleModelLoader, LTXVLatentUpsampler, SetNode, SetNode, MiniMaxH3ReferenceToVideo, MiniMaxH3SigmaShift, LoraLoaderModelOnly, PrimitiveStringMultiline, MiniMaxH3MemoryEfficientSageAttentionPatch, MiniMaxH3SigmaShift, SetNode, ModelAttentionBackend, LoraLoaderModelOnly, ModelAttentionBackend, LoraLoaderModelOnly, CLIPLoader, ExtendIntermediateSigmas, Fast Groups Bypasser (rgthree), UNETLoader, PrimitiveStringMultiline, LoadImage, ResolutionSelector, llama_cpp_model_loader, 孤海注释, 孤海注释, UNETLoader, CLIPLoader, CLIPTextEncode, VAELoader, EmptyLatentImage, KSampler, VAEDecode, JjkText, solarL_SaveImagesToZip, CLIPTextEncode, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, Note]
patterns: [text_to_image, image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/图生视频/MiniMax H3参考生视频LTX2.5 MSR二采放大｜音频参考自动提示词优化V1.1图生视频_2090468504624521218.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/MiniMax H3参考生视频LTX2.5 MSR二采放大｜音频参考自动提示词优化V1.1图生视频_2090468504624521218.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（171 个）：
- `SetNode`
- `llama_cpp_parameters`
- `BatchImagesNode`
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
- `VHS_VideoCombine`
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
- `PrimitiveStringMultiline`
- `LoadImage`
- `ResolutionSelector`
- `llama_cpp_model_loader`
- `孤海注释`
- `孤海注释`
- `UNETLoader` ★核心
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `VAELoader`
- `EmptyLatentImage` ★核心
- `KSampler` ★核心
- `VAEDecode` ★核心
- `JjkText`
- `solarL_SaveImagesToZip`
- `CLIPTextEncode` ★核心
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
- `Note`

**识别到的模式**：text_to_image、image_to_image

## 关键参数

- `width` = `80`
- `height` = `80`
- `batch_size` = `1`
- `seed` = `598626327129635`
- `steps` = `4`
- `cfg` = `4.5`
- `sampler_name` = `er_sde`
- `scheduler` = `beta`
- `denoise` = `1`

## 知识

覆盖率 **64%**（110/171）

**有卡**：`llama_cpp_parameters`、`BatchImagesNode`、`LoadImage`、`PurgeVRAM_UTK`、`BasicGuider`、`llama_cpp_instruct_adv`、`VAELoader`、`JoinStringMulti`、`StringConcatenate`、`ToString`、`KSamplerSelect`、`RandomNoise`、`LoadAudio`、`ComfyMathExpression`、`CFGGuider`、`LTXVConcatAVLatent`、`SamplerCustomAdvanced`、`LTXVSeparateAVLatent`、`LTXVAudioVAEDecode`、`VAEDecode`、`LTXVCropGuides`、`LTXVChunkFeedForward`、`PathchSageAttentionKJ`、`UNETLoader`、`LTX2AttentionTunerPatch`、`ManualSigmas`、`LoraLoaderModelOnly`、`VAELoaderKJ`、`LTXICLoRALoaderModelOnly`、`SetLatentNoiseMask`、`CLIPLoader`、`LTXAddVideoICLoRAGuide`、`LiconMSR`、`SolidMask`、`VHS_VideoCombine`、`LTXVAudioVAEEncode`、`PromptRelayEncode`、`LTXVConditioning`、`CLIPTextEncode`、`string_util_StrFind`、`StringLength`、`StringSubstring`、`MiniMaxH3AVDecodeT8`、`BasicScheduler`、`MiniMaxH3HybridLoader`、`MiniMaxH3MemoryEfficientSageAttentionPatch`、`VAEEncode`、`LatentUpscaleModelLoader`、`LTXVLatentUpsampler`、`MiniMaxH3ReferenceToVideo`、`MiniMaxH3SigmaShift`、`ModelAttentionBackend`、`ExtendIntermediateSigmas`、`ResolutionSelector`、`llama_cpp_model_loader`、`EmptyLatentImage`、`KSampler`、`solarL_SaveImagesToZip`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage、ResolutionSelector

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

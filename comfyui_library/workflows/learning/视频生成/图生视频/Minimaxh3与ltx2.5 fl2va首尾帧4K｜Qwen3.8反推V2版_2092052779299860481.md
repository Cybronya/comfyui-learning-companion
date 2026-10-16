---
key: 视频生成/图生视频/Minimaxh3与ltx2.5 fl2va首尾帧4K｜Qwen3.8反推V2版_2092052779299860481.json
name: Minimaxh3与ltx2.5 fl2va首尾帧4K｜Qwen3.8反推V2版_2092052779299860481
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Minimaxh3与ltx2.5 fl2va首尾帧4K｜Qwen3.8反推V2版_2092052779299860481.json
hash: e5558347679d6c48
coverage: 0.833333
learned_at: 2026-10-16 22:59:16
nodes: [RandomNoise, KSamplerSelect, CFGGuider, KSamplerSelect, easy cleanGpuUsed, SamplerCustomAdvanced, CLIPLoader, SetNode, VAEDecodeAudio, VAEDecodeAudio, VAELoader, CLIPLoader, MiniMaxH3ReferenceToVideo, VAELoader, VAELoader, PreviewImage, easy cleanGpuUsed, CLIPTextEncode, GetNode, SetNode, GetNode, LTXVConditioning, LatentUpscaleModelLoader, LTXVConcatAVLatent, LTXVSeparateAVLatent, LTXVAudioVAEDecode, VAEDecodeTiled, LTXVCropGuides, GetNode, GetNode, SetNode, LTXVLatentUpsampler, GetNode, VAELoader, SetNode, easy showAnything, VAEDecode, LTXVAddGuideMulti, ComfyMathExpression, LTXVEmptyLatentAudio, GetNode, VAEDecode, SamplerCustomAdvanced, CLIPTextEncode, VHS_VideoCombine, VHS_VideoCombine, SetNode, Float, GetNode, VHS_VideoCombine, GetNode, CR Text, LoadImage, VAEEncode, GetImageSize, ComfyMathExpression, ComfyMathExpression, ImageResizeKJv2, ImageResize+, LTXVPreprocess, LTXVPreprocess, LoadImage, ComfyMathExpression, ResolutionSelector, ImageResize+, ComfyMathExpression, UNETLoader, CLIPLoader, VHS_VideoCombine, LoraLoaderModelOnly, LoraLoaderModelOnly, LTX2MemoryEfficientSageAttentionPatch, LTX2_NAG, ManualSigmas, ImageResize+, ImageResize+, SamplerCustomAdvanced, LTXVConcatAVLatent, BasicScheduler, easy cleanGpuUsed, SetNode, easy cleanGpuUsed, SomethingToString, ProcessString, llama_cpp_parameters, llama_cpp_instruct_adv, JoinStrings, PreviewImage, PreviewAny, TextInput_, ShowText|pysssss, TextInput_, llama_cpp_model_loader, ImageConcatMulti, GetNode, CR Prompt Text, PrimitiveFloat, LTXVSeparateAVLatent, Float, VAELoader, VAELoader, LoraLoaderModelOnly, MiniMaxH3ImageToVideo, BasicGuider, RandomNoise, UNETLoader, MiniMaxH3MemoryEfficientSageAttentionPatch, SLASageAttention, LoraLoaderModelOnly, ModelAttentionBackend, SLASageAttention, UNETLoader, MiniMaxH3MemoryEfficientSageAttentionPatch, LoraLoaderModelOnly, RandomNoise, BasicGuider, KSamplerSelect, LoraLoaderModelOnly, BasicScheduler, MinimaxH3LatentUpscaler3D, ModelAttentionBackend, 孤海注释, 孤海注释, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, UNETLoader, KSampler, CLIPTextEncode, solarL_SaveImagesToZip, VAEDecode, VAELoader, CLIPLoader, EmptyLatentImage, JjkText, CLIPTextEncode, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, Note]
patterns: [text_to_image, image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/图生视频/Minimaxh3与ltx2.5 fl2va首尾帧4K｜Qwen3.8反推V2版_2092052779299860481.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/Minimaxh3与ltx2.5 fl2va首尾帧4K｜Qwen3.8反推V2版_2092052779299860481.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（150 个）：
- `RandomNoise`
- `KSamplerSelect` ★核心
- `CFGGuider`
- `KSamplerSelect` ★核心
- `easy cleanGpuUsed`
- `SamplerCustomAdvanced` ★核心
- `CLIPLoader`
- `SetNode`
- `VAEDecodeAudio` ★核心
- `VAEDecodeAudio` ★核心
- `VAELoader`
- `CLIPLoader`
- `MiniMaxH3ReferenceToVideo`
- `VAELoader`
- `VAELoader`
- `PreviewImage`
- `easy cleanGpuUsed`
- `CLIPTextEncode` ★核心
- `GetNode`
- `SetNode`
- `GetNode`
- `LTXVConditioning`
- `LatentUpscaleModelLoader`
- `LTXVConcatAVLatent`
- `LTXVSeparateAVLatent`
- `LTXVAudioVAEDecode` ★核心
- `VAEDecodeTiled` ★核心
- `LTXVCropGuides`
- `GetNode`
- `GetNode`
- `SetNode`
- `LTXVLatentUpsampler` ★核心
- `GetNode`
- `VAELoader`
- `SetNode`
- `easy showAnything`
- `VAEDecode` ★核心
- `LTXVAddGuideMulti`
- `ComfyMathExpression`
- `LTXVEmptyLatentAudio` ★核心
- `GetNode`
- `VAEDecode` ★核心
- `SamplerCustomAdvanced` ★核心
- `CLIPTextEncode` ★核心
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `SetNode`
- `Float`
- `GetNode`
- `VHS_VideoCombine`
- `GetNode`
- `CR Text`
- `LoadImage`
- `VAEEncode` ★核心
- `GetImageSize`
- `ComfyMathExpression`
- `ComfyMathExpression`
- `ImageResizeKJv2`
- `ImageResize+`
- `LTXVPreprocess`
- `LTXVPreprocess`
- `LoadImage`
- `ComfyMathExpression`
- `ResolutionSelector`
- `ImageResize+`
- `ComfyMathExpression`
- `UNETLoader` ★核心
- `CLIPLoader`
- `VHS_VideoCombine`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LTX2MemoryEfficientSageAttentionPatch`
- `LTX2_NAG`
- `ManualSigmas`
- `ImageResize+`
- `ImageResize+`
- `SamplerCustomAdvanced` ★核心
- `LTXVConcatAVLatent`
- `BasicScheduler`
- `easy cleanGpuUsed`
- `SetNode`
- `easy cleanGpuUsed`
- `SomethingToString`
- `ProcessString`
- `llama_cpp_parameters`
- `llama_cpp_instruct_adv`
- `JoinStrings`
- `PreviewImage`
- `PreviewAny`
- `TextInput_`
- `ShowText|pysssss`
- `TextInput_`
- `llama_cpp_model_loader`
- `ImageConcatMulti`
- `GetNode`
- `CR Prompt Text`
- `PrimitiveFloat`
- `LTXVSeparateAVLatent`
- `Float`
- `VAELoader`
- `VAELoader`
- `LoraLoaderModelOnly` ★核心
- `MiniMaxH3ImageToVideo`
- `BasicGuider`
- `RandomNoise`
- `UNETLoader` ★核心
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `SLASageAttention`
- `LoraLoaderModelOnly` ★核心
- `ModelAttentionBackend`
- `SLASageAttention`
- `UNETLoader` ★核心
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `LoraLoaderModelOnly` ★核心
- `RandomNoise`
- `BasicGuider`
- `KSamplerSelect` ★核心
- `LoraLoaderModelOnly` ★核心
- `BasicScheduler`
- `MinimaxH3LatentUpscaler3D`
- `ModelAttentionBackend`
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

覆盖率 **83%**（125/150）

**有卡**：`RandomNoise`、`KSamplerSelect`、`CFGGuider`、`easy cleanGpuUsed`、`SamplerCustomAdvanced`、`CLIPLoader`、`VAEDecodeAudio`、`VAELoader`、`MiniMaxH3ReferenceToVideo`、`CLIPTextEncode`、`LTXVConditioning`、`LatentUpscaleModelLoader`、`LTXVConcatAVLatent`、`LTXVSeparateAVLatent`、`LTXVAudioVAEDecode`、`VAEDecodeTiled`、`LTXVCropGuides`、`LTXVLatentUpsampler`、`VAEDecode`、`LTXVAddGuideMulti`、`ComfyMathExpression`、`LTXVEmptyLatentAudio`、`VHS_VideoCombine`、`Float`、`CR Text`、`LoadImage`、`VAEEncode`、`GetImageSize`、`ImageResizeKJv2`、`ImageResize+`、`LTXVPreprocess`、`ResolutionSelector`、`UNETLoader`、`LoraLoaderModelOnly`、`LTX2MemoryEfficientSageAttentionPatch`、`LTX2_NAG`、`ManualSigmas`、`BasicScheduler`、`SomethingToString`、`ProcessString`、`llama_cpp_parameters`、`llama_cpp_instruct_adv`、`JoinStrings`、`TextInput_`、`llama_cpp_model_loader`、`ImageConcatMulti`、`CR Prompt Text`、`MiniMaxH3ImageToVideo`、`BasicGuider`、`MiniMaxH3MemoryEfficientSageAttentionPatch`、`SLASageAttention`、`ModelAttentionBackend`、`MinimaxH3LatentUpscaler3D`、`KSampler`、`solarL_SaveImagesToZip`、`EmptyLatentImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage、ResolutionSelector

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

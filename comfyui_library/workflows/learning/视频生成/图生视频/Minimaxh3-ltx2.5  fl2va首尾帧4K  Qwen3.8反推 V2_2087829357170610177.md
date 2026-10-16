---
key: 视频生成/图生视频/Minimaxh3-ltx2.5  fl2va首尾帧4K  Qwen3.8反推 V2_2087829357170610177.json
name: Minimaxh3-ltx2.5  fl2va首尾帧4K  Qwen3.8反推 V2_2087829357170610177
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Minimaxh3-ltx2.5  fl2va首尾帧4K  Qwen3.8反推 V2_2087829357170610177.json
hash: e7083db46c2479af
coverage: 0.793651
learned_at: 2026-10-16 21:27:45
nodes: [RandomNoise, KSamplerSelect, CFGGuider, KSamplerSelect, easy cleanGpuUsed, SamplerCustomAdvanced, CLIPLoader, SetNode, VAEDecodeAudio, VAEDecodeAudio, VAELoader, CLIPLoader, MiniMaxH3ReferenceToVideo, VAELoader, VAELoader, 孤海注释, PreviewImage, easy cleanGpuUsed, CLIPTextEncode, GetNode, SetNode, GetNode, LTXVConditioning, LatentUpscaleModelLoader, LTXVConcatAVLatent, LTXVSeparateAVLatent, LTXVAudioVAEDecode, VAEDecodeTiled, LTXVCropGuides, MarkdownNote, GetNode, GetNode, SetNode, LTXVLatentUpsampler, GetNode, VAELoader, SetNode, easy showAnything, VAEDecode, LTXVAddGuideMulti, ComfyMathExpression, LTXVEmptyLatentAudio, GetNode, VAEDecode, SamplerCustomAdvanced, CLIPTextEncode, VHS_VideoCombine, VHS_VideoCombine, SetNode, Float, 孤海注释, GetNode, 孤海注释, VHS_VideoCombine, GetNode, CR Text, LoadImage, VAEEncode, GetImageSize, ComfyMathExpression, ComfyMathExpression, ImageResizeKJv2, ImageResize+, LTXVPreprocess, LTXVPreprocess, LoadImage, ComfyMathExpression, ResolutionSelector, ImageResize+, ComfyMathExpression, UNETLoader, CLIPLoader, VHS_VideoCombine, LoraLoaderModelOnly, LoraLoaderModelOnly, LTX2MemoryEfficientSageAttentionPatch, LTX2_NAG, ManualSigmas, ImageResize+, ImageResize+, SamplerCustomAdvanced, LTXVConcatAVLatent, BasicScheduler, easy cleanGpuUsed, SetNode, easy cleanGpuUsed, SomethingToString, ProcessString, llama_cpp_parameters, llama_cpp_instruct_adv, JoinStrings, PreviewImage, PreviewAny, TextInput_, ShowText|pysssss, TextInput_, llama_cpp_model_loader, ImageConcatMulti, GetNode, 孤海注释, CR Prompt Text, PrimitiveFloat, LTXVSeparateAVLatent, Float, VAELoader, VAELoader, LoraLoaderModelOnly, MiniMaxH3ImageToVideo, BasicGuider, RandomNoise, UNETLoader, MiniMaxH3MemoryEfficientSageAttentionPatch, SLASageAttention, LoraLoaderModelOnly, ModelAttentionBackend, SLASageAttention, UNETLoader, MiniMaxH3MemoryEfficientSageAttentionPatch, LoraLoaderModelOnly, RandomNoise, BasicGuider, KSamplerSelect, LoraLoaderModelOnly, BasicScheduler, MinimaxH3LatentUpscaler3D, ModelAttentionBackend]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 25, "width": 97}
---

# 视频生成/图生视频/Minimaxh3-ltx2.5  fl2va首尾帧4K  Qwen3.8反推 V2_2087829357170610177.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/Minimaxh3-ltx2.5  fl2va首尾帧4K  Qwen3.8反推 V2_2087829357170610177.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（126 个）：
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
- `孤海注释`
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
- `MarkdownNote`
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
- `孤海注释`
- `GetNode`
- `孤海注释`
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
- `孤海注释`
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

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **79%**（100/126）

**有卡**：`RandomNoise`、`KSamplerSelect`、`CFGGuider`、`easy cleanGpuUsed`、`SamplerCustomAdvanced`、`CLIPLoader`、`VAEDecodeAudio`、`VAELoader`、`MiniMaxH3ReferenceToVideo`、`CLIPTextEncode`、`LTXVConditioning`、`LatentUpscaleModelLoader`、`LTXVConcatAVLatent`、`LTXVSeparateAVLatent`、`LTXVAudioVAEDecode`、`VAEDecodeTiled`、`LTXVCropGuides`、`LTXVLatentUpsampler`、`VAEDecode`、`LTXVAddGuideMulti`、`ComfyMathExpression`、`LTXVEmptyLatentAudio`、`VHS_VideoCombine`、`Float`、`CR Text`、`LoadImage`、`VAEEncode`、`GetImageSize`、`ImageResizeKJv2`、`ImageResize+`、`LTXVPreprocess`、`ResolutionSelector`、`UNETLoader`、`LoraLoaderModelOnly`、`LTX2MemoryEfficientSageAttentionPatch`、`LTX2_NAG`、`ManualSigmas`、`BasicScheduler`、`SomethingToString`、`ProcessString`、`llama_cpp_parameters`、`llama_cpp_instruct_adv`、`JoinStrings`、`TextInput_`、`llama_cpp_model_loader`、`ImageConcatMulti`、`CR Prompt Text`、`MiniMaxH3ImageToVideo`、`BasicGuider`、`MiniMaxH3MemoryEfficientSageAttentionPatch`、`SLASageAttention`、`ModelAttentionBackend`、`MinimaxH3LatentUpscaler3D`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、ResolutionSelector、LoadImage、UNETLoader

---
key: 视频生成/图生视频/MINIMAX-H3-ref2va Qwen3.8 27B_2086300234388426753.json
name: MINIMAX-H3-ref2va Qwen3.8 27B_2086300234388426753
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/MINIMAX-H3-ref2va Qwen3.8 27B_2086300234388426753.json
hash: c57c9992d4c019af
coverage: 0.820896
learned_at: 2026-10-16 21:07:16
nodes: [RandomNoise, easy cleanGpuUsed, CLIPLoader, KSamplerSelect, BasicGuider, VAELoader, VAELoader, VAEDecodeAudio, VAEDecode, SetNode, BasicGuider, RandomNoise, easy cleanGpuUsed, VAEDecode, VAEDecodeAudio, easy cleanGpuUsed, KSamplerSelect, SamplerCustomAdvanced, MiniMaxH3ReferenceToVideo, VHS_VideoCombine, VHS_VideoCombine, 孤海注释, ImageResize+, LoadImage, 孤海注释, SetNode, easy cleanGpuUsed, SomethingToString, ProcessString, JoinStrings, PreviewImage, PreviewAny, 孤海注释, ShowText|pysssss, TextInput_, LoadImage, ImageResize+, ImageConcatMulti, SamplerCustomAdvanced, TextInput_, llama_cpp_parameters, llama_cpp_instruct_adv, PrimitiveStringMultiline, ComfyMathExpression, ComfyMathExpression, ComfyMathExpression, GetNode, LTXVConcatAVLatent, llama_cpp_model_loader, LTXVSeparateAVLatent, MinimaxH3LatentUpscaler3D, MiniMaxH3MemoryEfficientSageAttentionPatch, UNETLoader, MarkdownNote, MiniMaxH3ReferenceToVideo, MiniMaxH3SigmaShift, LoraLoaderModelOnly, LoraLoaderModelOnly, SLASageAttention, CR Prompt Text, SLASageAttention, ModelAttentionBackend, BasicScheduler, BasicScheduler, PrimitiveFloat, ResolutionSelector, Float]
patterns: []
missing: []
---

# 视频生成/图生视频/MINIMAX-H3-ref2va Qwen3.8 27B_2086300234388426753.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/MINIMAX-H3-ref2va Qwen3.8 27B_2086300234388426753.json`

## 结构

**生成流程**：Model → Latent → Sampling → Decode → Process → Output → Other

**节点**（67 个）：
- `RandomNoise`
- `easy cleanGpuUsed`
- `CLIPLoader`
- `KSamplerSelect` ★核心
- `BasicGuider`
- `VAELoader`
- `VAELoader`
- `VAEDecodeAudio` ★核心
- `VAEDecode` ★核心
- `SetNode`
- `BasicGuider`
- `RandomNoise`
- `easy cleanGpuUsed`
- `VAEDecode` ★核心
- `VAEDecodeAudio` ★核心
- `easy cleanGpuUsed`
- `KSamplerSelect` ★核心
- `SamplerCustomAdvanced` ★核心
- `MiniMaxH3ReferenceToVideo`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `孤海注释`
- `ImageResize+`
- `LoadImage`
- `孤海注释`
- `SetNode`
- `easy cleanGpuUsed`
- `SomethingToString`
- `ProcessString`
- `JoinStrings`
- `PreviewImage`
- `PreviewAny`
- `孤海注释`
- `ShowText|pysssss`
- `TextInput_`
- `LoadImage`
- `ImageResize+`
- `ImageConcatMulti`
- `SamplerCustomAdvanced` ★核心
- `TextInput_`
- `llama_cpp_parameters`
- `llama_cpp_instruct_adv`
- `PrimitiveStringMultiline`
- `ComfyMathExpression`
- `ComfyMathExpression`
- `ComfyMathExpression`
- `GetNode`
- `LTXVConcatAVLatent`
- `llama_cpp_model_loader`
- `LTXVSeparateAVLatent`
- `MinimaxH3LatentUpscaler3D`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `UNETLoader` ★核心
- `MarkdownNote`
- `MiniMaxH3ReferenceToVideo`
- `MiniMaxH3SigmaShift`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `SLASageAttention`
- `CR Prompt Text`
- `SLASageAttention`
- `ModelAttentionBackend`
- `BasicScheduler`
- `BasicScheduler`
- `PrimitiveFloat`
- `ResolutionSelector`
- `Float`

## 知识

覆盖率 **82%**（55/67）

**有卡**：`RandomNoise`、`easy cleanGpuUsed`、`CLIPLoader`、`KSamplerSelect`、`BasicGuider`、`VAELoader`、`VAEDecodeAudio`、`VAEDecode`、`SamplerCustomAdvanced`、`MiniMaxH3ReferenceToVideo`、`VHS_VideoCombine`、`ImageResize+`、`LoadImage`、`SomethingToString`、`ProcessString`、`JoinStrings`、`TextInput_`、`ImageConcatMulti`、`llama_cpp_parameters`、`llama_cpp_instruct_adv`、`ComfyMathExpression`、`LTXVConcatAVLatent`、`llama_cpp_model_loader`、`LTXVSeparateAVLatent`、`MinimaxH3LatentUpscaler3D`、`MiniMaxH3MemoryEfficientSageAttentionPatch`、`UNETLoader`、`MiniMaxH3SigmaShift`、`LoraLoaderModelOnly`、`SLASageAttention`、`CR Prompt Text`、`ModelAttentionBackend`、`BasicScheduler`、`ResolutionSelector`、`Float`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、ResolutionSelector、LoadImage、UNETLoader、KSamplerSelect

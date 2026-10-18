---
key: 视频生成/图生视频/MiniMax-H3全栈式短剧多图参考自动生成二采提示词自动优化版V2.0_2108461705771708417.json
name: MiniMax-H3全栈式短剧多图参考自动生成二采提示词自动优化版V2.0_2108461705771708417
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/MiniMax-H3全栈式短剧多图参考自动生成二采提示词自动优化版V2.0_2108461705771708417.json
hash: 958a0803c9efe3e9
coverage: 0.402985
learned_at: 2026-10-17 22:49:54
nodes: [GetNode, GetNode, GetNode, SetNode, SetNode, SetNode, SetNode, SetNode, SetNode, GetNode, MarkdownNote, CLIPLoader, YUAN_TXTJsonExtractor, GetNode, GetNode, GetImage, GetImage, GetNode, GetImage, ResolutionSelector, GetNode, YuanTool, SetNode, SetNode, SetNode, GetNode, GetNode, GetNode, SetNode, GetNode, GetNode, PrimitiveInt, SetNode, TextGenerate, StringConcatenate, PrimitiveStringMultiline, SetNode, ResolutionSelector, SetNode, SetNode, SetNode, GetNode, PreviewImage, GetNode, PrimitiveNode, YuanAudioList, PrimitiveStringMultiline, ImageScale, LoadImage, GetNode, Reroute, Reroute, GetNode, GetNode, VAEDecodeAudio, VAEDecode, SamplerCustomAdvanced, SetNode, BasicGuider, SetNode, SetNode, SetNode, GetNode, LTXVConcatAVLatent, GetNode, SamplerCustomAdvanced, GetNode, GetNode, GetNode, GetNode, GetNode, LTXVSeparateAVLatent, RandomNoise, 忽略多组孤海, KSamplerSelect, UNETLoader, SetNode, GetNode, MiniMaxH3MemoryEfficientSageAttentionPatch, LoraLoaderModelOnly, LoraLoaderModelOnly, BasicScheduler, MinimaxH3LatentUpscaler3D, VAEDecode, VAEDecodeAudio, GetNode, GetNode, ComfyMathExpression, easy float, SetNode, MiniMaxH3ReferenceToVideo, PrimitiveFloat, ComfyMathExpression, SetNode, ResolutionSelector, SetNode, SetNode, Note, YuanAudioSplit, PrimitiveFloat, YuanMultiImage, SplitSigmas, SetNode, VAELoader, SetNode, SetNode, SetNode, VAELoader, SetNode, CLIPLoader, SetNode, LoraLoaderModelOnly, SetNode, SetNode, SetNode, VHS_VideoCombine, StringConcatenate, ToString, JoinStringMulti, llama_cpp_model_loader, llama_cpp_parameters, PurgeVRAM_UTK, Any Switch (rgthree), SetNode, PrimitiveStringMultiline, easy showAnything, VHS_VideoCombine, easy showAnything, llama_cpp_instruct_adv, PrimitiveStringMultiline, ShowText|pysssss, SetNode, YUAN_TXTParagraphSplitter, YUAN_TXTShotReplace]
patterns: []
missing: []
---

# 视频生成/图生视频/MiniMax-H3全栈式短剧多图参考自动生成二采提示词自动优化版V2.0_2108461705771708417.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/MiniMax-H3全栈式短剧多图参考自动生成二采提示词自动优化版V2.0_2108461705771708417.json`

## 结构

**生成流程**：Model → Latent → Sampling → Decode → Process → Output → Other

**节点**（134 个）：
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `MarkdownNote`
- `CLIPLoader`
- `YUAN_TXTJsonExtractor`
- `GetNode`
- `GetNode`
- `GetImage`
- `GetImage`
- `GetNode`
- `GetImage`
- `ResolutionSelector`
- `GetNode`
- `YuanTool`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `PrimitiveInt`
- `SetNode`
- `TextGenerate`
- `StringConcatenate`
- `PrimitiveStringMultiline`
- `SetNode`
- `ResolutionSelector`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `PreviewImage`
- `GetNode`
- `PrimitiveNode`
- `YuanAudioList`
- `PrimitiveStringMultiline`
- `ImageScale`
- `LoadImage`
- `GetNode`
- `Reroute`
- `Reroute`
- `GetNode`
- `GetNode`
- `VAEDecodeAudio` ★核心
- `VAEDecode` ★核心
- `SamplerCustomAdvanced` ★核心
- `SetNode`
- `BasicGuider`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `LTXVConcatAVLatent`
- `GetNode`
- `SamplerCustomAdvanced` ★核心
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `LTXVSeparateAVLatent`
- `RandomNoise`
- `忽略多组孤海`
- `KSamplerSelect` ★核心
- `UNETLoader` ★核心
- `SetNode`
- `GetNode`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `BasicScheduler`
- `MinimaxH3LatentUpscaler3D`
- `VAEDecode` ★核心
- `VAEDecodeAudio` ★核心
- `GetNode`
- `GetNode`
- `ComfyMathExpression`
- `easy float`
- `SetNode`
- `MiniMaxH3ReferenceToVideo`
- `PrimitiveFloat`
- `ComfyMathExpression`
- `SetNode`
- `ResolutionSelector`
- `SetNode`
- `SetNode`
- `Note`
- `YuanAudioSplit`
- `PrimitiveFloat`
- `YuanMultiImage`
- `SplitSigmas`
- `SetNode`
- `VAELoader`
- `SetNode`
- `SetNode`
- `SetNode`
- `VAELoader`
- `SetNode`
- `CLIPLoader`
- `SetNode`
- `LoraLoaderModelOnly` ★核心
- `SetNode`
- `SetNode`
- `SetNode`
- `VHS_VideoCombine`
- `StringConcatenate`
- `ToString`
- `JoinStringMulti`
- `llama_cpp_model_loader`
- `llama_cpp_parameters`
- `PurgeVRAM_UTK`
- `Any Switch (rgthree)`
- `SetNode`
- `PrimitiveStringMultiline`
- `easy showAnything`
- `VHS_VideoCombine`
- `easy showAnything`
- `llama_cpp_instruct_adv`
- `PrimitiveStringMultiline`
- `ShowText|pysssss`
- `SetNode`
- `YUAN_TXTParagraphSplitter`
- `YUAN_TXTShotReplace`

## 知识

覆盖率 **40%**（54/134）

**有卡**：`CLIPLoader`、`YUAN_TXTJsonExtractor`、`GetImage`、`ResolutionSelector`、`YuanTool`、`TextGenerate`、`StringConcatenate`、`YuanAudioList`、`ImageScale`、`LoadImage`、`VAEDecodeAudio`、`VAEDecode`、`SamplerCustomAdvanced`、`BasicGuider`、`LTXVConcatAVLatent`、`LTXVSeparateAVLatent`、`RandomNoise`、`忽略多组孤海`、`KSamplerSelect`、`UNETLoader`、`MiniMaxH3MemoryEfficientSageAttentionPatch`、`LoraLoaderModelOnly`、`BasicScheduler`、`MinimaxH3LatentUpscaler3D`、`ComfyMathExpression`、`easy float`、`MiniMaxH3ReferenceToVideo`、`YuanAudioSplit`、`YuanMultiImage`、`SplitSigmas`、`VAELoader`、`VHS_VideoCombine`、`ToString`、`JoinStringMulti`、`llama_cpp_model_loader`、`llama_cpp_parameters`、`PurgeVRAM_UTK`、`llama_cpp_instruct_adv`、`YUAN_TXTParagraphSplitter`、`YUAN_TXTShotReplace`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、ResolutionSelector、LoadImage、UNETLoader、KSamplerSelect

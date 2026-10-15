---
key: 视频生成/文生视频/MiniMax H3 顶级舞蹈视频超频版 I 新提示词增强 I 全模态 v2.0 I 混合模型_2093521519069716482.json
name: MiniMax H3 顶级舞蹈视频超频版 I 新提示词增强 I 全模态 v2.0 I 混合模型_2093521519069716482
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/MiniMax H3 顶级舞蹈视频超频版 I 新提示词增强 I 全模态 v2.0 I 混合模型_2093521519069716482.json
hash: 6c7da843e76f4c7f
coverage: 0.4375
learned_at: 2026-10-15 22:45:43
nodes: [Label (rgthree), Note, VAELoader, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, KSamplerSelect, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, VHS_LoadVideo, VHS_LoadVideo, VHS_LoadVideo, SetNode, LoadImage, LoadImage, LoadImage, LoadImage, SetNode, SetNode, SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, SetNode, SetNode, SetNode, SetNode, SetNode, SetNode, SetNode, SetNode, SetNode, SetNode, ComfyMathExpression, SetNode, SetNode, SetNode, GetNode, GetNode, GetNode, KSamplerSelect, VAEDecodeAudio, SetNode, BasicGuider, SetNode, SetNode, VAELoader, SetNode, Note, VAEDecode, GetImageSize, ComfyMathExpression, SeedVR2, SeedVR2ExtraArgs, SeedVR2BlockSwap, SplitSigmas, SetNode, easy clearCacheAll, LTXVConcatAVLatent, LTXVSeparateAVLatent, easy clearCacheAll, SetNode, MarkdownNote, SetNode, SetNode, RTXVideoSuperResolution, GetNode, GetNode, GetNode, GetNode, MarkdownNote, SetNode, SetNode, GetNode, MinimaxH3LatentUpscaler3D, MathExpression|pysssss, Int, Int, BasicScheduler, RandomNoise, Note, SetNode, GetNode, Fast Groups Bypasser (rgthree), CLIPLoader, LoadImage, LoadImage, String Literal, SamplerCustomAdvanced, LoadImage, KepStringLiteral, LoadImage, MiniMaxH3MemoryEfficientSageAttentionPatch, MiniMaxChunkFeedForward, LoadAudioUI, llama_cpp_parameters, SamplerCustomAdvanced, ModelAttentionBackend, SetNode, MiniMaxLowVRAMAttention, Float, GetNode, BasicGuider, MiniMaxH3ReferenceToVideo, llama_cpp_instruct_adv, easy showAnything, String Literal, String Literal, PrimitiveStringMultiline, VHS_VideoCombine, PrimitiveStringMultiline, Label (rgthree), PrimitiveStringMultiline, PrimitiveStringMultiline, UNETLoader, LoraLoaderModelOnly, SetNode, MarkdownNote, LoadAudioUI, SetNode, LoadImage, Fast Groups Bypasser (rgthree), ResolutionSelector, PrimitiveFloat, VHS_LoadAudioUpload, llama_cpp_model_loader]
patterns: []
missing: []
---

# 视频生成/文生视频/MiniMax H3 顶级舞蹈视频超频版 I 新提示词增强 I 全模态 v2.0 I 混合模型_2093521519069716482.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/MiniMax H3 顶级舞蹈视频超频版 I 新提示词增强 I 全模态 v2.0 I 混合模型_2093521519069716482.json`

## 结构

**生成流程**：Model → Latent → Sampling → Decode → Process → Other

**节点**（144 个）：
- `Label (rgthree)`
- `Note`
- `VAELoader`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `KSamplerSelect` ★核心
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `VHS_LoadVideo`
- `VHS_LoadVideo`
- `VHS_LoadVideo`
- `SetNode`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `ComfyMathExpression`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `KSamplerSelect` ★核心
- `VAEDecodeAudio` ★核心
- `SetNode`
- `BasicGuider`
- `SetNode`
- `SetNode`
- `VAELoader`
- `SetNode`
- `Note`
- `VAEDecode` ★核心
- `GetImageSize`
- `ComfyMathExpression`
- `SeedVR2`
- `SeedVR2ExtraArgs`
- `SeedVR2BlockSwap`
- `SplitSigmas`
- `SetNode`
- `easy clearCacheAll`
- `LTXVConcatAVLatent`
- `LTXVSeparateAVLatent`
- `easy clearCacheAll`
- `SetNode`
- `MarkdownNote`
- `SetNode`
- `SetNode`
- `RTXVideoSuperResolution`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `MarkdownNote`
- `SetNode`
- `SetNode`
- `GetNode`
- `MinimaxH3LatentUpscaler3D`
- `MathExpression|pysssss`
- `Int`
- `Int`
- `BasicScheduler`
- `RandomNoise`
- `Note`
- `SetNode`
- `GetNode`
- `Fast Groups Bypasser (rgthree)`
- `CLIPLoader`
- `LoadImage`
- `LoadImage`
- `String Literal`
- `SamplerCustomAdvanced` ★核心
- `LoadImage`
- `KepStringLiteral`
- `LoadImage`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `MiniMaxChunkFeedForward`
- `LoadAudioUI`
- `llama_cpp_parameters`
- `SamplerCustomAdvanced` ★核心
- `ModelAttentionBackend`
- `SetNode`
- `MiniMaxLowVRAMAttention`
- `Float`
- `GetNode`
- `BasicGuider`
- `MiniMaxH3ReferenceToVideo`
- `llama_cpp_instruct_adv`
- `easy showAnything`
- `String Literal`
- `String Literal`
- `PrimitiveStringMultiline`
- `VHS_VideoCombine`
- `PrimitiveStringMultiline`
- `Label (rgthree)`
- `PrimitiveStringMultiline`
- `PrimitiveStringMultiline`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `SetNode`
- `MarkdownNote`
- `LoadAudioUI`
- `SetNode`
- `LoadImage`
- `Fast Groups Bypasser (rgthree)`
- `ResolutionSelector`
- `PrimitiveFloat`
- `VHS_LoadAudioUpload`
- `llama_cpp_model_loader`

## 知识

覆盖率 **44%**（63/144）

**有卡**：`Label (rgthree)`、`VAELoader`、`KSamplerSelect`、`VHS_LoadVideo`、`LoadImage`、`ComfyMathExpression`、`VAEDecodeAudio`、`BasicGuider`、`VAEDecode`、`GetImageSize`、`SeedVR2`、`SeedVR2ExtraArgs`、`SeedVR2BlockSwap`、`SplitSigmas`、`easy clearCacheAll`、`LTXVConcatAVLatent`、`LTXVSeparateAVLatent`、`RTXVideoSuperResolution`、`MinimaxH3LatentUpscaler3D`、`MathExpression|pysssss`、`Int`、`BasicScheduler`、`RandomNoise`、`CLIPLoader`、`String Literal`、`SamplerCustomAdvanced`、`KepStringLiteral`、`MiniMaxH3MemoryEfficientSageAttentionPatch`、`MiniMaxChunkFeedForward`、`LoadAudioUI`、`llama_cpp_parameters`、`ModelAttentionBackend`、`MiniMaxLowVRAMAttention`、`Float`、`MiniMaxH3ReferenceToVideo`、`llama_cpp_instruct_adv`、`VHS_VideoCombine`、`UNETLoader`、`LoraLoaderModelOnly`、`ResolutionSelector`、`VHS_LoadAudioUpload`、`llama_cpp_model_loader`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、ResolutionSelector、LoadImage、UNETLoader、KSamplerSelect

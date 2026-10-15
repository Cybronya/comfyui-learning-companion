---
key: 视频生成/文生视频/MiniMax H3 顶级舞蹈视频直出 I 新提示词增强 I 全模态 v2.0 I 混合模型 I 极速二采放大 I 官流加速_2092699967201824769.json
name: MiniMax H3 顶级舞蹈视频直出 I 新提示词增强 I 全模态 v2.0 I 混合模型 I 极速二采放大 I 官流加速_2092699967201824769
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/MiniMax H3 顶级舞蹈视频直出 I 新提示词增强 I 全模态 v2.0 I 混合模型 I 极速二采放大 I 官流加速_2092699967201824769.json
hash: 1d908fd462cd369b
coverage: 0.442857
learned_at: 2026-10-15 22:45:43
nodes: [Note, VAELoader, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, KSamplerSelect, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, VHS_LoadVideo, VHS_LoadVideo, VHS_LoadVideo, SetNode, LoadImage, LoadImage, LoadImage, LoadImage, SetNode, SetNode, SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, SetNode, SetNode, SetNode, SetNode, SetNode, SetNode, SetNode, SetNode, SetNode, SetNode, SetNode, ComfyMathExpression, SetNode, SetNode, SetNode, GetNode, GetNode, GetNode, GetNode, BasicGuider, KSamplerSelect, VAEDecodeAudio, SetNode, SetNode, BasicGuider, SetNode, SetNode, VAELoader, SetNode, Note, SamplerCustomAdvanced, VAEDecode, GetImageSize, ComfyMathExpression, SeedVR2, SeedVR2ExtraArgs, SeedVR2BlockSwap, UNETLoader, SplitSigmas, SetNode, easy clearCacheAll, ModelAttentionBackend, SetNode, LTXVConcatAVLatent, LTXVSeparateAVLatent, easy clearCacheAll, SetNode, MarkdownNote, SetNode, SetNode, RTXVideoSuperResolution, GetNode, GetNode, GetNode, GetNode, MarkdownNote, SetNode, SetNode, GetNode, MinimaxH3LatentUpscaler3D, MathExpression|pysssss, LoraLoaderModelOnly, Int, Int, BasicScheduler, RandomNoise, Note, SetNode, GetNode, Fast Groups Bypasser (rgthree), CLIPLoader, llama_cpp_parameters, LoadImage, LoadImage, String Literal, SamplerCustomAdvanced, LoadImage, KepStringLiteral, LoadImage, MiniMaxH3MemoryEfficientSageAttentionPatch, MarkdownNote, MiniMaxChunkFeedForward, MiniMaxLowVRAMAttention, VHS_VideoCombine, LoadImage, Label (rgthree), ResolutionSelector, Float, PrimitiveFloat, Fast Groups Bypasser (rgthree), llama_cpp_instruct_adv, easy showAnything, Label (rgthree), llama_cpp_model_loader, LoadAudioUI, LoadAudioUI, MiniMaxH3ReferenceToVideo, PrimitiveStringMultiline, String Literal, VHS_LoadAudioUpload]
patterns: []
missing: []
---

# 视频生成/文生视频/MiniMax H3 顶级舞蹈视频直出 I 新提示词增强 I 全模态 v2.0 I 混合模型 I 极速二采放大 I 官流加速_2092699967201824769.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/MiniMax H3 顶级舞蹈视频直出 I 新提示词增强 I 全模态 v2.0 I 混合模型 I 极速二采放大 I 官流加速_2092699967201824769.json`

## 结构

**生成流程**：Model → Latent → Sampling → Decode → Process → Other

**节点**（140 个）：
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
- `SetNode`
- `ComfyMathExpression`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `BasicGuider`
- `KSamplerSelect` ★核心
- `VAEDecodeAudio` ★核心
- `SetNode`
- `SetNode`
- `BasicGuider`
- `SetNode`
- `SetNode`
- `VAELoader`
- `SetNode`
- `Note`
- `SamplerCustomAdvanced` ★核心
- `VAEDecode` ★核心
- `GetImageSize`
- `ComfyMathExpression`
- `SeedVR2`
- `SeedVR2ExtraArgs`
- `SeedVR2BlockSwap`
- `UNETLoader` ★核心
- `SplitSigmas`
- `SetNode`
- `easy clearCacheAll`
- `ModelAttentionBackend`
- `SetNode`
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
- `LoraLoaderModelOnly` ★核心
- `Int`
- `Int`
- `BasicScheduler`
- `RandomNoise`
- `Note`
- `SetNode`
- `GetNode`
- `Fast Groups Bypasser (rgthree)`
- `CLIPLoader`
- `llama_cpp_parameters`
- `LoadImage`
- `LoadImage`
- `String Literal`
- `SamplerCustomAdvanced` ★核心
- `LoadImage`
- `KepStringLiteral`
- `LoadImage`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `MarkdownNote`
- `MiniMaxChunkFeedForward`
- `MiniMaxLowVRAMAttention`
- `VHS_VideoCombine`
- `LoadImage`
- `Label (rgthree)`
- `ResolutionSelector`
- `Float`
- `PrimitiveFloat`
- `Fast Groups Bypasser (rgthree)`
- `llama_cpp_instruct_adv`
- `easy showAnything`
- `Label (rgthree)`
- `llama_cpp_model_loader`
- `LoadAudioUI`
- `LoadAudioUI`
- `MiniMaxH3ReferenceToVideo`
- `PrimitiveStringMultiline`
- `String Literal`
- `VHS_LoadAudioUpload`

## 知识

覆盖率 **44%**（62/140）

**有卡**：`VAELoader`、`KSamplerSelect`、`VHS_LoadVideo`、`LoadImage`、`ComfyMathExpression`、`BasicGuider`、`VAEDecodeAudio`、`SamplerCustomAdvanced`、`VAEDecode`、`GetImageSize`、`SeedVR2`、`SeedVR2ExtraArgs`、`SeedVR2BlockSwap`、`UNETLoader`、`SplitSigmas`、`easy clearCacheAll`、`ModelAttentionBackend`、`LTXVConcatAVLatent`、`LTXVSeparateAVLatent`、`RTXVideoSuperResolution`、`MinimaxH3LatentUpscaler3D`、`MathExpression|pysssss`、`LoraLoaderModelOnly`、`Int`、`BasicScheduler`、`RandomNoise`、`CLIPLoader`、`llama_cpp_parameters`、`String Literal`、`KepStringLiteral`、`MiniMaxH3MemoryEfficientSageAttentionPatch`、`MiniMaxChunkFeedForward`、`MiniMaxLowVRAMAttention`、`VHS_VideoCombine`、`Label (rgthree)`、`ResolutionSelector`、`Float`、`llama_cpp_instruct_adv`、`llama_cpp_model_loader`、`LoadAudioUI`、`MiniMaxH3ReferenceToVideo`、`VHS_LoadAudioUpload`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、ResolutionSelector、LoadImage、UNETLoader、KSamplerSelect

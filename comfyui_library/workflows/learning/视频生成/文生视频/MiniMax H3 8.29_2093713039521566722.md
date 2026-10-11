---
key: 视频生成/文生视频/MiniMax H3 8.29_2093713039521566722.json
name: MiniMax H3 8.29_2093713039521566722
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/MiniMax H3 8.29_2093713039521566722.json
hash: 33c848c858483d23
coverage: 0.413043
learned_at: 2026-10-11 21:30:20
nodes: [SetNode, VAELoader, SetNode, VAELoader, SetNode, SetNode, SetNode, GetNode, GetNode, KSamplerSelect, MarkdownNote, SetNode, ComfyMathExpression, SetNode, CLIPLoader, SetNode, SetNode, SetNode, SetNode, SetNode, SetNode, SetNode, SetNode, SetNode, SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, MiniMaxH3ReferenceToVideo, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, SetNode, SetNode, SetNode, LTXVSeparateAVLatent, RandomNoise, GetNode, GetNode, GetNode, BasicGuider, KSamplerSelect, GetNode, GetNode, GetNode, GetNode, MinimaxH3LatentUpscaler3D, Reroute, GetNode, VAEDecode, SetNode, MiniMaxH3MemoryEfficientSageAttentionPatch, UNETLoader, LoraLoaderModelOnly, Fast Groups Bypasser (rgthree), BasicGuider, SetNode, SamplerCustomAdvanced, SamplerCustomAdvanced, LTXVConcatAVLatent, SplitSigmas, SetNode, VAEDecodeAudio, BasicScheduler, Float, VHS_VideoCombine, H3SigmaRefiner, Fast Groups Bypasser (rgthree), Text, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, ResolutionSelector, LoraLoaderModelOnly, MiniMaxH3BlockCacheT8]
patterns: []
missing: []
---

# 视频生成/文生视频/MiniMax H3 8.29_2093713039521566722.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/MiniMax H3 8.29_2093713039521566722.json`

## 结构

**生成流程**：Model → Latent → Sampling → Decode → Process → Other

**节点**（92 个）：
- `SetNode`
- `VAELoader`
- `SetNode`
- `VAELoader`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `KSamplerSelect` ★核心
- `MarkdownNote`
- `SetNode`
- `ComfyMathExpression`
- `SetNode`
- `CLIPLoader`
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
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `MiniMaxH3ReferenceToVideo`
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
- `LTXVSeparateAVLatent`
- `RandomNoise`
- `GetNode`
- `GetNode`
- `GetNode`
- `BasicGuider`
- `KSamplerSelect` ★核心
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `MinimaxH3LatentUpscaler3D`
- `Reroute`
- `GetNode`
- `VAEDecode` ★核心
- `SetNode`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `Fast Groups Bypasser (rgthree)`
- `BasicGuider`
- `SetNode`
- `SamplerCustomAdvanced` ★核心
- `SamplerCustomAdvanced` ★核心
- `LTXVConcatAVLatent`
- `SplitSigmas`
- `SetNode`
- `VAEDecodeAudio` ★核心
- `BasicScheduler`
- `Float`
- `VHS_VideoCombine`
- `H3SigmaRefiner`
- `Fast Groups Bypasser (rgthree)`
- `Text`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `ResolutionSelector`
- `LoraLoaderModelOnly` ★核心
- `MiniMaxH3BlockCacheT8`

## 知识

覆盖率 **41%**（38/92）

**有卡**：`VAELoader`、`KSamplerSelect`、`ComfyMathExpression`、`CLIPLoader`、`MiniMaxH3ReferenceToVideo`、`LTXVSeparateAVLatent`、`RandomNoise`、`BasicGuider`、`MinimaxH3LatentUpscaler3D`、`VAEDecode`、`MiniMaxH3MemoryEfficientSageAttentionPatch`、`UNETLoader`、`LoraLoaderModelOnly`、`SamplerCustomAdvanced`、`LTXVConcatAVLatent`、`SplitSigmas`、`VAEDecodeAudio`、`BasicScheduler`、`Float`、`VHS_VideoCombine`、`H3SigmaRefiner`、`Text`、`LoadImage`、`ResolutionSelector`、`MiniMaxH3BlockCacheT8`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、ResolutionSelector、LoadImage、UNETLoader、KSamplerSelect

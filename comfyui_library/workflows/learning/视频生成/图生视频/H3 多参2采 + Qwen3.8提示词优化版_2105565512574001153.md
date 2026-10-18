---
key: 视频生成/图生视频/H3 多参2采 + Qwen3.8提示词优化版_2105565512574001153.json
name: H3 多参2采 + Qwen3.8提示词优化版_2105565512574001153
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/H3 多参2采 + Qwen3.8提示词优化版_2105565512574001153.json
hash: 2dd4db29f07348d0
coverage: 0.421875
learned_at: 2026-10-17 02:43:43
nodes: [SetNode, VAELoader, VAELoader, SetNode, SetNode, SetNode, SetNode, VHS_LoadVideo, SetNode, SetNode, SetNode, VHS_LoadVideo, VHS_LoadVideo, SetNode, SetNode, LoadImage, LoadImage, LoadImage, SetNode, SetNode, SetNode, Note, GetNode, SetNode, CLIPLoader, Reroute, Reroute, GetNode, GetNode, GetNode, GetNode, GetNode, VAEDecodeAudio, VAEDecode, GetNode, SetNode, SetNode, SetNode, SetNode, BasicGuider, SetNode, SetNode, SetNode, VAEDecode, VAEDecodeAudio, GetNode, LTXVConcatAVLatent, GetNode, SamplerCustomAdvanced, GetNode, GetNode, GetNode, GetNode, GetNode, LTXVSeparateAVLatent, 忽略多组孤海, 忽略多组孤海, Note, LoadAudio, SetNode, LoadAudio, SetNode, LoadAudio, SetNode, Note, RandomNoise, 忽略多组孤海, KSamplerSelect, SetNode, GetNode, VHS_VideoCombine, VHS_VideoCombine, 忽略多组孤海, MinimaxH3LatentUpscaler3D, LoadImage, LoadImage, LoadImage, Note, LoadImage, easy float, GetNode, GetNode, GetNode, GetNode, MiniMaxH3ReferenceToVideo, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, MiniMaxH3MemoryEfficientSageAttentionPatch, easy showAnything, RH_Translator, PreviewAny, easy saveText, easy saveText, SetNode, SetNode, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, UNETLoader, LoadImage, LoadImage, SetNode, ResolutionSelector, ComfyMathExpression, SetNode, Note, MarkdownNote, CR Prompt Text, easy indexTTSForceCleanup, SamplerCustomAdvanced, easy indexTTSForceCleanup, BasicScheduler, SplitSigmas, MiniMaxH3PromptEnhancerT8, PrimitiveFloat, MarkdownNote]
patterns: []
missing: []
---

# 视频生成/图生视频/H3 多参2采 + Qwen3.8提示词优化版_2105565512574001153.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/H3 多参2采 + Qwen3.8提示词优化版_2105565512574001153.json`

## 结构

**生成流程**：Model → Latent → Sampling → Decode → Process → Output → Other

**节点**（128 个）：
- `SetNode`
- `VAELoader`
- `VAELoader`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `VHS_LoadVideo`
- `SetNode`
- `SetNode`
- `SetNode`
- `VHS_LoadVideo`
- `VHS_LoadVideo`
- `SetNode`
- `SetNode`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `SetNode`
- `SetNode`
- `SetNode`
- `Note`
- `GetNode`
- `SetNode`
- `CLIPLoader`
- `Reroute`
- `Reroute`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `VAEDecodeAudio` ★核心
- `VAEDecode` ★核心
- `GetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `BasicGuider`
- `SetNode`
- `SetNode`
- `SetNode`
- `VAEDecode` ★核心
- `VAEDecodeAudio` ★核心
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
- `忽略多组孤海`
- `忽略多组孤海`
- `Note`
- `LoadAudio`
- `SetNode`
- `LoadAudio`
- `SetNode`
- `LoadAudio`
- `SetNode`
- `Note`
- `RandomNoise`
- `忽略多组孤海`
- `KSamplerSelect` ★核心
- `SetNode`
- `GetNode`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `忽略多组孤海`
- `MinimaxH3LatentUpscaler3D`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `Note`
- `LoadImage`
- `easy float`
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
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `easy showAnything`
- `RH_Translator`
- `PreviewAny`
- `easy saveText`
- `easy saveText`
- `SetNode`
- `SetNode`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `LoadImage`
- `LoadImage`
- `SetNode`
- `ResolutionSelector`
- `ComfyMathExpression`
- `SetNode`
- `Note`
- `MarkdownNote`
- `CR Prompt Text`
- `easy indexTTSForceCleanup`
- `SamplerCustomAdvanced` ★核心
- `easy indexTTSForceCleanup`
- `BasicScheduler`
- `SplitSigmas`
- `MiniMaxH3PromptEnhancerT8`
- `PrimitiveFloat`
- `MarkdownNote`

## 知识

覆盖率 **42%**（54/128）

**有卡**：`VAELoader`、`VHS_LoadVideo`、`LoadImage`、`CLIPLoader`、`VAEDecodeAudio`、`VAEDecode`、`BasicGuider`、`LTXVConcatAVLatent`、`SamplerCustomAdvanced`、`LTXVSeparateAVLatent`、`忽略多组孤海`、`LoadAudio`、`RandomNoise`、`KSamplerSelect`、`VHS_VideoCombine`、`MinimaxH3LatentUpscaler3D`、`easy float`、`MiniMaxH3ReferenceToVideo`、`MiniMaxH3MemoryEfficientSageAttentionPatch`、`RH_Translator`、`easy saveText`、`LoraLoaderModelOnly`、`UNETLoader`、`ResolutionSelector`、`ComfyMathExpression`、`CR Prompt Text`、`easy indexTTSForceCleanup`、`BasicScheduler`、`SplitSigmas`、`MiniMaxH3PromptEnhancerT8`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、ResolutionSelector、LoadImage、UNETLoader、KSamplerSelect

---
key: 视频生成/图生视频/H3 多参2采 + Qwen3.8提示词优化版_2098217190175629314.json
name: H3 多参2采 + Qwen3.8提示词优化版_2098217190175629314
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/H3 多参2采 + Qwen3.8提示词优化版_2098217190175629314.json
hash: ad94387e20c76abf
coverage: 0.416
learned_at: 2026-10-17 01:44:23
nodes: [MiniMaxH3PromptEnhancerT8, SetNode, VAELoader, VAELoader, SetNode, SetNode, SetNode, SetNode, SetNode, VHS_LoadVideo, SetNode, SetNode, SetNode, VHS_LoadVideo, VHS_LoadVideo, SetNode, SetNode, LoadImage, LoadImage, LoadImage, SetNode, SetNode, SetNode, Note, GetNode, SetNode, CLIPLoader, Reroute, Reroute, GetNode, GetNode, GetNode, GetNode, GetNode, VAEDecodeAudio, VAEDecode, GetNode, SetNode, SetNode, SetNode, ComfyMathExpression, SamplerCustomAdvanced, SetNode, BasicGuider, SetNode, SetNode, SetNode, VAEDecode, VAEDecodeAudio, GetNode, LTXVConcatAVLatent, GetNode, MarkdownNote, SamplerCustomAdvanced, GetNode, GetNode, GetNode, GetNode, GetNode, LTXVSeparateAVLatent, 忽略多组孤海, 忽略多组孤海, Note, LoadAudio, SetNode, LoadAudio, SetNode, LoadAudio, SetNode, Note, RandomNoise, 忽略多组孤海, KSamplerSelect, SetNode, GetNode, VHS_VideoCombine, BasicScheduler, SplitSigmas, VHS_VideoCombine, 忽略多组孤海, MinimaxH3LatentUpscaler3D, Note, LoadImage, LoadImage, LoadImage, Note, LoadImage, LoadImage, ResolutionSelector, PrimitiveFloat, easy float, GetNode, GetNode, GetNode, GetNode, MiniMaxH3ReferenceToVideo, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, SetNode, UNETLoader, LoraLoaderModelOnly, MiniMaxH3MemoryEfficientSageAttentionPatch, LoraLoaderModelOnly, SetNode, CR Prompt Text, easy showAnything, RH_Translator, PreviewAny, easy saveText, easy saveText, SetNode, Label (rgthree), LoadImage]
patterns: []
missing: []
---

# 视频生成/图生视频/H3 多参2采 + Qwen3.8提示词优化版_2098217190175629314.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/H3 多参2采 + Qwen3.8提示词优化版_2098217190175629314.json`

## 结构

**生成流程**：Model → Latent → Sampling → Decode → Process → Output → Other

**节点**（125 个）：
- `MiniMaxH3PromptEnhancerT8`
- `SetNode`
- `VAELoader`
- `VAELoader`
- `SetNode`
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
- `ComfyMathExpression`
- `SamplerCustomAdvanced` ★核心
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
- `MarkdownNote`
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
- `BasicScheduler`
- `SplitSigmas`
- `VHS_VideoCombine`
- `忽略多组孤海`
- `MinimaxH3LatentUpscaler3D`
- `Note`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `Note`
- `LoadImage`
- `LoadImage`
- `ResolutionSelector`
- `PrimitiveFloat`
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
- `SetNode`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `LoraLoaderModelOnly` ★核心
- `SetNode`
- `CR Prompt Text`
- `easy showAnything`
- `RH_Translator`
- `PreviewAny`
- `easy saveText`
- `easy saveText`
- `SetNode`
- `Label (rgthree)`
- `LoadImage`

## 知识

覆盖率 **42%**（52/125）

**有卡**：`MiniMaxH3PromptEnhancerT8`、`VAELoader`、`VHS_LoadVideo`、`LoadImage`、`CLIPLoader`、`VAEDecodeAudio`、`VAEDecode`、`ComfyMathExpression`、`SamplerCustomAdvanced`、`BasicGuider`、`LTXVConcatAVLatent`、`LTXVSeparateAVLatent`、`忽略多组孤海`、`LoadAudio`、`RandomNoise`、`KSamplerSelect`、`VHS_VideoCombine`、`BasicScheduler`、`SplitSigmas`、`MinimaxH3LatentUpscaler3D`、`ResolutionSelector`、`easy float`、`MiniMaxH3ReferenceToVideo`、`UNETLoader`、`LoraLoaderModelOnly`、`MiniMaxH3MemoryEfficientSageAttentionPatch`、`CR Prompt Text`、`RH_Translator`、`easy saveText`、`Label (rgthree)`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、ResolutionSelector、LoadImage、UNETLoader、KSamplerSelect

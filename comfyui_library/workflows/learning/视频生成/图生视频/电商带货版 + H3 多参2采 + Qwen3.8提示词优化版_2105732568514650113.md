---
key: 视频生成/图生视频/电商带货版 + H3 多参2采 + Qwen3.8提示词优化版_2105732568514650113.json
name: 电商带货版 + H3 多参2采 + Qwen3.8提示词优化版_2105732568514650113
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/电商带货版 + H3 多参2采 + Qwen3.8提示词优化版_2105732568514650113.json
hash: 7596903e1151c688
coverage: 0.438776
learned_at: 2026-10-17 22:20:13
nodes: [SetNode, VAELoader, VAELoader, SetNode, SetNode, SetNode, SetNode, SetNode, SetNode, Note, GetNode, SetNode, CLIPLoader, Reroute, Reroute, GetNode, GetNode, GetNode, GetNode, GetNode, VAEDecodeAudio, VAEDecode, GetNode, SetNode, SetNode, SetNode, SetNode, BasicGuider, SetNode, SetNode, SetNode, VAEDecode, VAEDecodeAudio, GetNode, LTXVConcatAVLatent, GetNode, SamplerCustomAdvanced, GetNode, GetNode, GetNode, GetNode, GetNode, LTXVSeparateAVLatent, Note, RandomNoise, KSamplerSelect, SetNode, GetNode, 忽略多组孤海, MinimaxH3LatentUpscaler3D, LoadImage, LoadImage, LoadImage, Note, LoadImage, easy float, GetNode, MiniMaxH3ReferenceToVideo, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, MiniMaxH3MemoryEfficientSageAttentionPatch, easy showAnything, RH_Translator, PreviewAny, easy saveText, easy saveText, SetNode, SetNode, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, UNETLoader, LoadImage, LoadImage, SetNode, ComfyMathExpression, SetNode, Note, MarkdownNote, easy indexTTSForceCleanup, SamplerCustomAdvanced, easy indexTTSForceCleanup, BasicScheduler, SplitSigmas, PrimitiveFloat, MarkdownNote, CR Prompt Text, MiniMaxH3PromptEnhancerT8, ResolutionSelector, 忽略多组孤海, VHS_VideoCombine, VHS_VideoCombine]
patterns: []
missing: []
---

# 视频生成/图生视频/电商带货版 + H3 多参2采 + Qwen3.8提示词优化版_2105732568514650113.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/电商带货版 + H3 多参2采 + Qwen3.8提示词优化版_2105732568514650113.json`

## 结构

**生成流程**：Model → Latent → Sampling → Decode → Process → Output → Other

**节点**（98 个）：
- `SetNode`
- `VAELoader`
- `VAELoader`
- `SetNode`
- `SetNode`
- `SetNode`
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
- `Note`
- `RandomNoise`
- `KSamplerSelect` ★核心
- `SetNode`
- `GetNode`
- `忽略多组孤海`
- `MinimaxH3LatentUpscaler3D`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `Note`
- `LoadImage`
- `easy float`
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
- `ComfyMathExpression`
- `SetNode`
- `Note`
- `MarkdownNote`
- `easy indexTTSForceCleanup`
- `SamplerCustomAdvanced` ★核心
- `easy indexTTSForceCleanup`
- `BasicScheduler`
- `SplitSigmas`
- `PrimitiveFloat`
- `MarkdownNote`
- `CR Prompt Text`
- `MiniMaxH3PromptEnhancerT8`
- `ResolutionSelector`
- `忽略多组孤海`
- `VHS_VideoCombine`
- `VHS_VideoCombine`

## 知识

覆盖率 **44%**（43/98）

**有卡**：`VAELoader`、`CLIPLoader`、`VAEDecodeAudio`、`VAEDecode`、`BasicGuider`、`LTXVConcatAVLatent`、`SamplerCustomAdvanced`、`LTXVSeparateAVLatent`、`RandomNoise`、`KSamplerSelect`、`忽略多组孤海`、`MinimaxH3LatentUpscaler3D`、`LoadImage`、`easy float`、`MiniMaxH3ReferenceToVideo`、`MiniMaxH3MemoryEfficientSageAttentionPatch`、`RH_Translator`、`easy saveText`、`LoraLoaderModelOnly`、`UNETLoader`、`ComfyMathExpression`、`easy indexTTSForceCleanup`、`BasicScheduler`、`SplitSigmas`、`CR Prompt Text`、`MiniMaxH3PromptEnhancerT8`、`ResolutionSelector`、`VHS_VideoCombine`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、ResolutionSelector、LoadImage、UNETLoader、KSamplerSelect

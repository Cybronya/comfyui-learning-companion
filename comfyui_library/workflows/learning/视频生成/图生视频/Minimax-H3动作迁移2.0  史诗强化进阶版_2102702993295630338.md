---
key: 视频生成/图生视频/Minimax-H3动作迁移2.0  史诗强化进阶版_2102702993295630338.json
name: Minimax-H3动作迁移2.0  史诗强化进阶版_2102702993295630338
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Minimax-H3动作迁移2.0  史诗强化进阶版_2102702993295630338.json
hash: 37ffd4422ca62433
coverage: 0.428571
learned_at: 2026-10-17 02:29:12
nodes: [SetNode, VAELoader, SetNode, SetNode, GetNode, SetNode, Reroute, Reroute, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, SetNode, SetNode, GetNode, GetNode, MiniMaxH3ReferenceToVideo, SetNode, SetNode, SamplerCustomAdvanced, SetNode, BasicGuider, SetNode, SetNode, VAEDecode, GetNode, LTXVConcatAVLatent, SamplerCustomAdvanced, GetNode, GetNode, GetNode, GetNode, GetNode, LTXVSeparateAVLatent, SetNode, SetNode, SetNode, SetNode, GetNode, SetNode, VAEDecode, ComfyMathExpression, LoadAudio, LoadAudio, LoadAudio, SetNode, SetNode, LoadImage, SetNode, MarkdownNote, LoadImage, SetNode, SetNode, LoadImage, 忽略多组孤海, SetNode, MiniMaxH3MemoryEfficientSageAttentionPatch, BasicScheduler, SplitSigmas, LoadImage, KSamplerSelect, GetNode, GetNode, SetNode, LoraLoaderModelOnly, LoraLoaderModelOnly, easy float, UNETLoader, CLIPLoader, VAELoader, VAEDecodeAudio, ResolutionSelector, VHS_VideoCombine, GetNode, GetNode, GetNode, VHS_VideoCombine, SetNode, 忽略多组孤海, 忽略多组孤海, 忽略多组孤海, LoadImage, MinimaxH3LatentUpscaler3D, VAEDecodeAudio, RandomNoise, PrimitiveFloat, VHS_LoadVideo, LoadImage, Text]
patterns: []
missing: []
---

# 视频生成/图生视频/Minimax-H3动作迁移2.0  史诗强化进阶版_2102702993295630338.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/Minimax-H3动作迁移2.0  史诗强化进阶版_2102702993295630338.json`

## 结构

**生成流程**：Model → Latent → Sampling → Decode → Process → Other

**节点**（98 个）：
- `SetNode`
- `VAELoader`
- `SetNode`
- `SetNode`
- `GetNode`
- `SetNode`
- `Reroute`
- `Reroute`
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
- `SetNode`
- `GetNode`
- `GetNode`
- `MiniMaxH3ReferenceToVideo`
- `SetNode`
- `SetNode`
- `SamplerCustomAdvanced` ★核心
- `SetNode`
- `BasicGuider`
- `SetNode`
- `SetNode`
- `VAEDecode` ★核心
- `GetNode`
- `LTXVConcatAVLatent`
- `SamplerCustomAdvanced` ★核心
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `LTXVSeparateAVLatent`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `SetNode`
- `VAEDecode` ★核心
- `ComfyMathExpression`
- `LoadAudio`
- `LoadAudio`
- `LoadAudio`
- `SetNode`
- `SetNode`
- `LoadImage`
- `SetNode`
- `MarkdownNote`
- `LoadImage`
- `SetNode`
- `SetNode`
- `LoadImage`
- `忽略多组孤海`
- `SetNode`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `BasicScheduler`
- `SplitSigmas`
- `LoadImage`
- `KSamplerSelect` ★核心
- `GetNode`
- `GetNode`
- `SetNode`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `easy float`
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `VAEDecodeAudio` ★核心
- `ResolutionSelector`
- `VHS_VideoCombine`
- `GetNode`
- `GetNode`
- `GetNode`
- `VHS_VideoCombine`
- `SetNode`
- `忽略多组孤海`
- `忽略多组孤海`
- `忽略多组孤海`
- `LoadImage`
- `MinimaxH3LatentUpscaler3D`
- `VAEDecodeAudio` ★核心
- `RandomNoise`
- `PrimitiveFloat`
- `VHS_LoadVideo`
- `LoadImage`
- `Text`

## 知识

覆盖率 **43%**（42/98）

**有卡**：`VAELoader`、`MiniMaxH3ReferenceToVideo`、`SamplerCustomAdvanced`、`BasicGuider`、`VAEDecode`、`LTXVConcatAVLatent`、`LTXVSeparateAVLatent`、`ComfyMathExpression`、`LoadAudio`、`LoadImage`、`忽略多组孤海`、`MiniMaxH3MemoryEfficientSageAttentionPatch`、`BasicScheduler`、`SplitSigmas`、`KSamplerSelect`、`LoraLoaderModelOnly`、`easy float`、`UNETLoader`、`CLIPLoader`、`VAEDecodeAudio`、`ResolutionSelector`、`VHS_VideoCombine`、`MinimaxH3LatentUpscaler3D`、`RandomNoise`、`VHS_LoadVideo`、`Text`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、ResolutionSelector、LoadImage、UNETLoader、KSamplerSelect

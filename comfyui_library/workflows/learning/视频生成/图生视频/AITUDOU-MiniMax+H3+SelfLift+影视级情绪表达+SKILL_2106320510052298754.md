---
key: 视频生成/图生视频/AITUDOU-MiniMax+H3+SelfLift+影视级情绪表达+SKILL_2106320510052298754.json
name: AITUDOU-MiniMax+H3+SelfLift+影视级情绪表达+SKILL_2106320510052298754
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/AITUDOU-MiniMax+H3+SelfLift+影视级情绪表达+SKILL_2106320510052298754.json
hash: d01e259c75462a68
coverage: 0.443182
learned_at: 2026-10-07 00:31:03
nodes: [UNETLoader, ModelAttentionBackend, SolAttnMiniMax, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, VAELoader, SetNode, SetNode, SetNode, GetNode, GetNode, SetNode, SetNode, MarkdownNote, SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, SetNode, ConditioningZeroOut, GetNode, GetNode, SetNode, GetNode, KSamplerSelect, GetNode, BasicScheduler, H3SigmaRefiner, GetNode, GetNode, VAEDecodeAudio, ComfyMathExpression, SetNode, GetNode, LoraLoaderModelOnly, LoraLoaderModelOnly, Note, SetNode, CLIPLoader, SetNode, VAEDecode, SetNode, Label (rgthree), Label (rgthree), Label (rgthree), Fast Groups Bypasser (rgthree), MiniMaxH3MemoryEfficientSageAttentionPatch, VAELoader, SetNode, SetNode, SetNode, SetNode, VHS_VideoCombine, LoadImage, SetNode, SetNode, LoadImage, MiniMaxH3ReferenceToVideo, LoadImage, LoadImage, LoadImage, SetNode, LoadImage, LoadImage, LoadImage, Text, Float, LoadAudio, LoadAudio, LoadAudio, ResolutionSelector, SelfLiftH3Sampler, LoadImage, SetNode]
patterns: []
missing: [Label (rgthree), Label (rgthree), Label (rgthree)]
discoveries: [次要节点 `Label (rgthree)` 知识库中没有该节点类型的任何知识, 次要节点 `Label (rgthree)` 知识库中没有该节点类型的任何知识, 次要节点 `Label (rgthree)` 知识库中没有该节点类型的任何知识]
---

# 视频生成/图生视频/AITUDOU-MiniMax+H3+SelfLift+影视级情绪表达+SKILL_2106320510052298754.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/AITUDOU-MiniMax+H3+SelfLift+影视级情绪表达+SKILL_2106320510052298754.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Other

**节点**（88 个）：
- `UNETLoader` ★核心
- `ModelAttentionBackend`
- `SolAttnMiniMax`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `VAELoader`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `MarkdownNote`
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
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `ConditioningZeroOut`
- `GetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `KSamplerSelect` ★核心
- `GetNode`
- `BasicScheduler`
- `H3SigmaRefiner`
- `GetNode`
- `GetNode`
- `VAEDecodeAudio` ★核心
- `ComfyMathExpression`
- `SetNode`
- `GetNode`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `Note`
- `SetNode`
- `CLIPLoader`
- `SetNode`
- `VAEDecode` ★核心
- `SetNode`
- `Label (rgthree)`
- `Label (rgthree)`
- `Label (rgthree)`
- `Fast Groups Bypasser (rgthree)`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `VAELoader`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `VHS_VideoCombine`
- `LoadImage`
- `SetNode`
- `SetNode`
- `LoadImage`
- `MiniMaxH3ReferenceToVideo`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `SetNode`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `Text`
- `Float`
- `LoadAudio`
- `LoadAudio`
- `LoadAudio`
- `ResolutionSelector`
- `SelfLiftH3Sampler` ★核心
- `LoadImage`
- `SetNode`

## 知识

覆盖率 **44%**（39/88）

**有卡**：`UNETLoader`、`ModelAttentionBackend`、`SolAttnMiniMax`、`LoraLoaderModelOnly`、`VAELoader`、`ConditioningZeroOut`、`KSamplerSelect`、`BasicScheduler`、`H3SigmaRefiner`、`VAEDecodeAudio`、`ComfyMathExpression`、`CLIPLoader`、`VAEDecode`、`MiniMaxH3MemoryEfficientSageAttentionPatch`、`VHS_VideoCombine`、`LoadImage`、`MiniMaxH3ReferenceToVideo`、`Text`、`Float`、`LoadAudio`、`ResolutionSelector`、`SelfLiftH3Sampler`

**缺卡**（3）：`Label (rgthree)`、`Label (rgthree)`、`Label (rgthree)`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、ConditioningZeroOut、ResolutionSelector、LoadImage、UNETLoader

## 学习发现

- 次要节点 `Label (rgthree)` 知识库中没有该节点类型的任何知识
- 次要节点 `Label (rgthree)` 知识库中没有该节点类型的任何知识
- 次要节点 `Label (rgthree)` 知识库中没有该节点类型的任何知识

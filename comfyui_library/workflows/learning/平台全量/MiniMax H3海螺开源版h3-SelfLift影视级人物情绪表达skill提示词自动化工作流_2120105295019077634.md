---
key: 平台全量/MiniMax H3海螺开源版h3-SelfLift影视级人物情绪表达skill提示词自动化工作流_2120105295019077634.json
name: MiniMax H3海螺开源版h3-SelfLift影视级人物情绪表达skill提示词自动化工作流_2120105295019077634
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/MiniMax H3海螺开源版h3-SelfLift影视级人物情绪表达skill提示词自动化工作流_2120105295019077634.json
hash: 56605df05bb8c26a
coverage: 0.433735
learned_at: 2026-11-14 00:41:49
nodes: [UNETLoader, MiniMaxH3MemoryEfficientSageAttentionPatch, ModelAttentionBackend, SolAttnMiniMax, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, VAELoader, SetNode, VAELoader, SetNode, SetNode, LoadImage, LoadImage, SetNode, SetNode, SetNode, SetNode, SetNode, SetNode, LoadImage, LoadImage, SetNode, SetNode, LoadImage, LoadImage, LoadImage, GetNode, GetNode, SetNode, SetNode, MarkdownNote, SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, SetNode, ConditioningZeroOut, GetNode, GetNode, SetNode, GetNode, KSamplerSelect, GetNode, BasicScheduler, H3SigmaRefiner, GetNode, GetNode, VAEDecodeAudio, SelfLiftH3Sampler, ComfyMathExpression, SetNode, GetNode, LoraLoaderModelOnly, LoraLoaderModelOnly, Note, SetNode, CLIPLoader, SetNode, MiniMaxH3ReferenceToVideo, VAEDecode, SetNode, Float, ResolutionSelector, VHS_VideoCombine, LoadImage, Fast Groups Bypasser (rgthree), Text, LoadImage, 孤海注释]
patterns: []
missing: []
---

# 平台全量/MiniMax H3海螺开源版h3-SelfLift影视级人物情绪表达skill提示词自动化工作流_2120105295019077634.json

> 来源文件 `comfyui_library/workflows/平台全量/MiniMax H3海螺开源版h3-SelfLift影视级人物情绪表达skill提示词自动化工作流_2120105295019077634.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Other

**节点**（83 个）：
- `UNETLoader` ★核心
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `ModelAttentionBackend`
- `SolAttnMiniMax`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `VAELoader`
- `SetNode`
- `VAELoader`
- `SetNode`
- `SetNode`
- `LoadImage`
- `LoadImage`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `LoadImage`
- `LoadImage`
- `SetNode`
- `SetNode`
- `LoadImage`
- `LoadImage`
- `LoadImage`
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
- `SelfLiftH3Sampler` ★核心
- `ComfyMathExpression`
- `SetNode`
- `GetNode`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `Note`
- `SetNode`
- `CLIPLoader`
- `SetNode`
- `MiniMaxH3ReferenceToVideo`
- `VAEDecode` ★核心
- `SetNode`
- `Float`
- `ResolutionSelector`
- `VHS_VideoCombine`
- `LoadImage`
- `Fast Groups Bypasser (rgthree)`
- `Text`
- `LoadImage`
- `孤海注释`

## 知识

覆盖率 **43%**（36/83）

**有卡**：`UNETLoader`、`MiniMaxH3MemoryEfficientSageAttentionPatch`、`ModelAttentionBackend`、`SolAttnMiniMax`、`LoraLoaderModelOnly`、`VAELoader`、`LoadImage`、`ConditioningZeroOut`、`KSamplerSelect`、`BasicScheduler`、`H3SigmaRefiner`、`VAEDecodeAudio`、`SelfLiftH3Sampler`、`ComfyMathExpression`、`CLIPLoader`、`MiniMaxH3ReferenceToVideo`、`VAEDecode`、`Float`、`ResolutionSelector`、`VHS_VideoCombine`、`Text`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、ConditioningZeroOut、ResolutionSelector、LoadImage、UNETLoader

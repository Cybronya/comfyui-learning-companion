---
key: 视频生成/图生视频/AITUDOU-MiniMax+H3+SelfLift+影视级情绪表达+SKILL_2104111411025764354.json
name: AITUDOU-MiniMax+H3+SelfLift+影视级情绪表达+SKILL_2104111411025764354
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/AITUDOU-MiniMax+H3+SelfLift+影视级情绪表达+SKILL_2104111411025764354.json
hash: e0c88fb183079834
coverage: 0.458824
learned_at: 2026-10-17 02:28:42
nodes: [UNETLoader, MiniMaxH3MemoryEfficientSageAttentionPatch, ModelAttentionBackend, SolAttnMiniMax, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, VAELoader, SetNode, VAELoader, SetNode, SetNode, LoadImage, LoadImage, SetNode, SetNode, SetNode, SetNode, SetNode, SetNode, LoadImage, LoadImage, SetNode, SetNode, LoadImage, LoadImage, LoadImage, GetNode, GetNode, SetNode, SetNode, MarkdownNote, SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, SetNode, ConditioningZeroOut, GetNode, GetNode, SetNode, GetNode, KSamplerSelect, GetNode, BasicScheduler, H3SigmaRefiner, GetNode, GetNode, VAEDecodeAudio, SelfLiftH3Sampler, ComfyMathExpression, SetNode, GetNode, LoraLoaderModelOnly, LoraLoaderModelOnly, Note, SetNode, CLIPLoader, SetNode, MiniMaxH3ReferenceToVideo, VAEDecode, SetNode, Label (rgthree), Label (rgthree), Label (rgthree), Float, ResolutionSelector, VHS_VideoCombine, LoadImage, Fast Groups Bypasser (rgthree), Text, LoadImage]
patterns: []
missing: []
---

# 视频生成/图生视频/AITUDOU-MiniMax+H3+SelfLift+影视级情绪表达+SKILL_2104111411025764354.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/AITUDOU-MiniMax+H3+SelfLift+影视级情绪表达+SKILL_2104111411025764354.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Other

**节点**（85 个）：
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
- `Label (rgthree)`
- `Label (rgthree)`
- `Label (rgthree)`
- `Float`
- `ResolutionSelector`
- `VHS_VideoCombine`
- `LoadImage`
- `Fast Groups Bypasser (rgthree)`
- `Text`
- `LoadImage`

## 知识

覆盖率 **46%**（39/85）

**有卡**：`UNETLoader`、`MiniMaxH3MemoryEfficientSageAttentionPatch`、`ModelAttentionBackend`、`SolAttnMiniMax`、`LoraLoaderModelOnly`、`VAELoader`、`LoadImage`、`ConditioningZeroOut`、`KSamplerSelect`、`BasicScheduler`、`H3SigmaRefiner`、`VAEDecodeAudio`、`SelfLiftH3Sampler`、`ComfyMathExpression`、`CLIPLoader`、`MiniMaxH3ReferenceToVideo`、`VAEDecode`、`Label (rgthree)`、`Float`、`ResolutionSelector`、`VHS_VideoCombine`、`Text`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、ConditioningZeroOut、ResolutionSelector、LoadImage、UNETLoader

---
key: 视频生成/图生视频/MIniMax-H3+DSW+LMS+SelfLift+VDN+SLA极速高动态武戏文戏视频生成_2098794614286274562.json
name: MIniMax-H3+DSW+LMS+SelfLift+VDN+SLA极速高动态武戏文戏视频生成_2098794614286274562
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/MIniMax-H3+DSW+LMS+SelfLift+VDN+SLA极速高动态武戏文戏视频生成_2098794614286274562.json
hash: 2916c8f60d02a529
coverage: 0.931818
learned_at: 2026-10-07 00:33:16
nodes: [CLIPLoader, VAELoader, LoadImage, LoadImage, Int, RH_Screenwriter, ComfyMathExpression, MiniMaxH3MemoryEfficientSageAttentionPatch, ModelAttentionBackend, WujiCleaner, MiniMaxH3SemanticBridgeConfigT8, MiniMaxH3HyperVAE2xLoaderEXPT8, VAEDecode, MiniMaxH3OutputTrimT8, WujiCleaner, MiniMaxH3AVDecodeT8, CM_IntToFloat, VAELoader, PrimitiveStringMultiline, List of strings [Crystools], MiniMaxH3AudioConditioningT8, ResolutionSelector, MiniMaxH3SemanticBridgeApplyT8, ConditioningZeroOut, KSamplerSelect, WujiCleaner, SelfLiftAvatarH3Sampler, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, BlockSparseAttention, H3SigmaRefiner, MiniMaxH3SigmaShift, MiniMaxH3ChunkFeedForwardT8Advanced, LoraLoaderBypassModelOnly, MiniMaxH3VDNRuntimeAuditT8Advanced, LoraLoaderModelOnly, BasicScheduler, LoraLoaderModelOnly, WujiH3PromptEnhancer, VHS_VideoCombine, UNETLoader]
patterns: []
missing: [List of strings [Crystools], MiniMaxH3VDNRuntimeAuditT8Advanced]
discoveries: [次要节点 `List of strings [Crystools]` 知识库中没有该节点类型的任何知识, 次要节点 `MiniMaxH3VDNRuntimeAuditT8Advanced` 知识库中没有该节点类型的任何知识]
---

# 视频生成/图生视频/MIniMax-H3+DSW+LMS+SelfLift+VDN+SLA极速高动态武戏文戏视频生成_2098794614286274562.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/MIniMax-H3+DSW+LMS+SelfLift+VDN+SLA极速高动态武戏文戏视频生成_2098794614286274562.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Other

**节点**（44 个）：
- `CLIPLoader`
- `VAELoader`
- `LoadImage`
- `LoadImage`
- `Int`
- `RH_Screenwriter`
- `ComfyMathExpression`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `ModelAttentionBackend`
- `WujiCleaner`
- `MiniMaxH3SemanticBridgeConfigT8`
- `MiniMaxH3HyperVAE2xLoaderEXPT8`
- `VAEDecode` ★核心
- `MiniMaxH3OutputTrimT8`
- `WujiCleaner`
- `MiniMaxH3AVDecodeT8`
- `CM_IntToFloat`
- `VAELoader`
- `PrimitiveStringMultiline`
- `List of strings [Crystools]`
- `MiniMaxH3AudioConditioningT8`
- `ResolutionSelector`
- `MiniMaxH3SemanticBridgeApplyT8`
- `ConditioningZeroOut`
- `KSamplerSelect` ★核心
- `WujiCleaner`
- `SelfLiftAvatarH3Sampler` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `BlockSparseAttention`
- `H3SigmaRefiner`
- `MiniMaxH3SigmaShift`
- `MiniMaxH3ChunkFeedForwardT8Advanced`
- `LoraLoaderBypassModelOnly` ★核心
- `MiniMaxH3VDNRuntimeAuditT8Advanced`
- `LoraLoaderModelOnly` ★核心
- `BasicScheduler`
- `LoraLoaderModelOnly` ★核心
- `WujiH3PromptEnhancer`
- `VHS_VideoCombine`
- `UNETLoader` ★核心

## 知识

覆盖率 **93%**（41/44）

**有卡**：`CLIPLoader`、`VAELoader`、`LoadImage`、`Int`、`RH_Screenwriter`、`ComfyMathExpression`、`MiniMaxH3MemoryEfficientSageAttentionPatch`、`ModelAttentionBackend`、`WujiCleaner`、`MiniMaxH3SemanticBridgeConfigT8`、`MiniMaxH3HyperVAE2xLoaderEXPT8`、`VAEDecode`、`MiniMaxH3OutputTrimT8`、`MiniMaxH3AVDecodeT8`、`CM_IntToFloat`、`MiniMaxH3AudioConditioningT8`、`ResolutionSelector`、`MiniMaxH3SemanticBridgeApplyT8`、`ConditioningZeroOut`、`KSamplerSelect`、`SelfLiftAvatarH3Sampler`、`LoraLoaderModelOnly`、`BlockSparseAttention`、`H3SigmaRefiner`、`MiniMaxH3SigmaShift`、`MiniMaxH3ChunkFeedForwardT8Advanced`、`LoraLoaderBypassModelOnly`、`BasicScheduler`、`WujiH3PromptEnhancer`、`VHS_VideoCombine`、`UNETLoader`

**缺卡**（2）：`List of strings [Crystools]`、`MiniMaxH3VDNRuntimeAuditT8Advanced`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、ConditioningZeroOut、ResolutionSelector、LoadImage、UNETLoader

## 学习发现

- 次要节点 `List of strings [Crystools]` 知识库中没有该节点类型的任何知识
- 次要节点 `MiniMaxH3VDNRuntimeAuditT8Advanced` 知识库中没有该节点类型的任何知识

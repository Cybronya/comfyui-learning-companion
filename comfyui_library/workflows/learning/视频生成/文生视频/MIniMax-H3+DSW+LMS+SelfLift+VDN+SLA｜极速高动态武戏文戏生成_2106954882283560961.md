---
key: 视频生成/文生视频/MIniMax-H3+DSW+LMS+SelfLift+VDN+SLA｜极速高动态武戏文戏生成_2106954882283560961.json
name: MIniMax-H3+DSW+LMS+SelfLift+VDN+SLA｜极速高动态武戏文戏生成_2106954882283560961
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/MIniMax-H3+DSW+LMS+SelfLift+VDN+SLA｜极速高动态武戏文戏生成_2106954882283560961.json
hash: 25b9d634ecd3ee55
coverage: 0.931034
learned_at: 2026-10-10 00:07:18
nodes: [CLIPLoader, VAELoader, LoadImage, LoadImage, Int, RH_Screenwriter, ComfyMathExpression, MiniMaxH3MemoryEfficientSageAttentionPatch, ModelAttentionBackend, WujiCleaner, MiniMaxH3SemanticBridgeConfigT8, MiniMaxH3HyperVAE2xLoaderEXPT8, VAEDecode, MiniMaxH3OutputTrimT8, WujiCleaner, MiniMaxH3AVDecodeT8, CM_IntToFloat, VAELoader, PrimitiveStringMultiline, List of strings [Crystools], MiniMaxH3AudioConditioningT8, ResolutionSelector, MiniMaxH3SemanticBridgeApplyT8, ConditioningZeroOut, KSamplerSelect, WujiCleaner, SelfLiftAvatarH3Sampler, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, BlockSparseAttention, H3SigmaRefiner, MiniMaxH3SigmaShift, MiniMaxH3ChunkFeedForwardT8Advanced, LoraLoaderBypassModelOnly, MiniMaxH3VDNRuntimeAuditT8Advanced, LoraLoaderModelOnly, BasicScheduler, LoraLoaderModelOnly, WujiH3PromptEnhancer, VHS_VideoCombine, UNETLoader, 孤海注释, 孤海注释, UNETLoader, CLIPLoader, CLIPTextEncode, VAELoader, EmptyLatentImage, KSampler, VAEDecode, solarL_SaveImagesToZip, JjkText, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, CLIPTextEncode, Note]
patterns: [text_to_image]
missing: [List of strings [Crystools]]
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [次要节点 `List of strings [Crystools]` 知识库中没有该节点类型的任何知识, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/文生视频/MIniMax-H3+DSW+LMS+SelfLift+VDN+SLA｜极速高动态武戏文戏生成_2106954882283560961.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/MIniMax-H3+DSW+LMS+SelfLift+VDN+SLA｜极速高动态武戏文戏生成_2106954882283560961.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（87 个）：
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
- `孤海注释`
- `孤海注释`
- `UNETLoader` ★核心
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `VAELoader`
- `EmptyLatentImage` ★核心
- `KSampler` ★核心
- `VAEDecode` ★核心
- `solarL_SaveImagesToZip`
- `JjkText`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `CLIPTextEncode` ★核心
- `Note`

**识别到的模式**：text_to_image

## 关键参数

- `width` = `80`
- `height` = `80`
- `batch_size` = `1`
- `seed` = `598626327129635`
- `steps` = `4`
- `cfg` = `4.5`
- `sampler_name` = `er_sde`
- `scheduler` = `beta`
- `denoise` = `1`

## 知识

覆盖率 **93%**（81/87）

**有卡**：`CLIPLoader`、`VAELoader`、`LoadImage`、`Int`、`RH_Screenwriter`、`ComfyMathExpression`、`MiniMaxH3MemoryEfficientSageAttentionPatch`、`ModelAttentionBackend`、`WujiCleaner`、`MiniMaxH3SemanticBridgeConfigT8`、`MiniMaxH3HyperVAE2xLoaderEXPT8`、`VAEDecode`、`MiniMaxH3OutputTrimT8`、`MiniMaxH3AVDecodeT8`、`CM_IntToFloat`、`MiniMaxH3AudioConditioningT8`、`ResolutionSelector`、`MiniMaxH3SemanticBridgeApplyT8`、`ConditioningZeroOut`、`KSamplerSelect`、`SelfLiftAvatarH3Sampler`、`LoraLoaderModelOnly`、`BlockSparseAttention`、`H3SigmaRefiner`、`MiniMaxH3SigmaShift`、`MiniMaxH3ChunkFeedForwardT8Advanced`、`LoraLoaderBypassModelOnly`、`MiniMaxH3VDNRuntimeAuditT8Advanced`、`BasicScheduler`、`WujiH3PromptEnhancer`、`VHS_VideoCombine`、`UNETLoader`、`CLIPTextEncode`、`EmptyLatentImage`、`KSampler`、`solarL_SaveImagesToZip`

**缺卡**（1）：`List of strings [Crystools]`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、EmptyLatentImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- 次要节点 `List of strings [Crystools]` 知识库中没有该节点类型的任何知识
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

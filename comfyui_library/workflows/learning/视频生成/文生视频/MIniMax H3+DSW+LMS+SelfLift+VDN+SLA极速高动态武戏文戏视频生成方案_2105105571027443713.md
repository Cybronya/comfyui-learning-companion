---
key: 视频生成/文生视频/MIniMax H3+DSW+LMS+SelfLift+VDN+SLA极速高动态武戏文戏视频生成方案_2105105571027443713.json
name: MIniMax H3+DSW+LMS+SelfLift+VDN+SLA极速高动态武戏文戏视频生成方案_2105105571027443713
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/MIniMax H3+DSW+LMS+SelfLift+VDN+SLA极速高动态武戏文戏视频生成方案_2105105571027443713.json
hash: 830352d2cd26c89c
coverage: 0.930556
learned_at: 2026-10-15 22:45:26
nodes: [CLIPLoader, BasicScheduler, VAELoader, LoadImage, LoadImage, Int, RH_Screenwriter, MiniMaxH3VDNRuntimeAuditT8Advanced, ComfyMathExpression, MiniMaxH3MemoryEfficientSageAttentionPatch, ModelAttentionBackend, WujiCleaner, MiniMaxH3SemanticBridgeConfigT8, WujiH3PromptEnhancer, MiniMaxH3HyperVAE2xLoaderEXPT8, VAEDecode, MiniMaxH3OutputTrimT8, WujiCleaner, MiniMaxH3AVDecodeT8, LoraLoaderModelOnly, CM_IntToFloat, VAELoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, PrimitiveStringMultiline, List of strings [Crystools], LoraLoaderModelOnly, MiniMaxH3AudioConditioningT8, VHS_VideoCombine, BlockSparseAttention, ResolutionSelector, MiniMaxH3SemanticBridgeApplyT8, ConditioningZeroOut, KSamplerSelect, H3SigmaRefiner, WujiCleaner, MiniMaxH3ChunkFeedForwardT8Advanced, LoraLoaderBypassModelOnly, SelfLiftAvatarH3Sampler, UNETLoader, 孤海注释, 孤海注释, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, KSampler, EmptyLatentImage, JjkText, CLIPTextEncode, CLIPTextEncode, solarL_SaveImagesToZip, VAEDecode, CLIPLoader, VAELoader, Note, SaveImage]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/文生视频/MIniMax H3+DSW+LMS+SelfLift+VDN+SLA极速高动态武戏文戏视频生成方案_2105105571027443713.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/MIniMax H3+DSW+LMS+SelfLift+VDN+SLA极速高动态武戏文戏视频生成方案_2105105571027443713.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（72 个）：
- `CLIPLoader`
- `BasicScheduler`
- `VAELoader`
- `LoadImage`
- `LoadImage`
- `Int`
- `RH_Screenwriter`
- `MiniMaxH3VDNRuntimeAuditT8Advanced`
- `ComfyMathExpression`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `ModelAttentionBackend`
- `WujiCleaner`
- `MiniMaxH3SemanticBridgeConfigT8`
- `WujiH3PromptEnhancer`
- `MiniMaxH3HyperVAE2xLoaderEXPT8`
- `VAEDecode` ★核心
- `MiniMaxH3OutputTrimT8`
- `WujiCleaner`
- `MiniMaxH3AVDecodeT8`
- `LoraLoaderModelOnly` ★核心
- `CM_IntToFloat`
- `VAELoader`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `PrimitiveStringMultiline`
- `List of strings [Crystools]`
- `LoraLoaderModelOnly` ★核心
- `MiniMaxH3AudioConditioningT8`
- `VHS_VideoCombine`
- `BlockSparseAttention`
- `ResolutionSelector`
- `MiniMaxH3SemanticBridgeApplyT8`
- `ConditioningZeroOut`
- `KSamplerSelect` ★核心
- `H3SigmaRefiner`
- `WujiCleaner`
- `MiniMaxH3ChunkFeedForwardT8Advanced`
- `LoraLoaderBypassModelOnly` ★核心
- `SelfLiftAvatarH3Sampler` ★核心
- `UNETLoader` ★核心
- `孤海注释`
- `孤海注释`
- `UNETLoader` ★核心
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
- `KSampler` ★核心
- `EmptyLatentImage` ★核心
- `JjkText`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `solarL_SaveImagesToZip`
- `VAEDecode` ★核心
- `CLIPLoader`
- `VAELoader`
- `Note`
- `SaveImage`

**识别到的模式**：text_to_image

## 关键参数

- `seed` = `598626327129635`
- `steps` = `4`
- `cfg` = `4.5`
- `sampler_name` = `er_sde`
- `scheduler` = `beta`
- `denoise` = `1`
- `width` = `80`
- `height` = `80`
- `batch_size` = `1`

## 知识

覆盖率 **93%**（67/72）

**有卡**：`CLIPLoader`、`BasicScheduler`、`VAELoader`、`LoadImage`、`Int`、`RH_Screenwriter`、`MiniMaxH3VDNRuntimeAuditT8Advanced`、`ComfyMathExpression`、`MiniMaxH3MemoryEfficientSageAttentionPatch`、`ModelAttentionBackend`、`WujiCleaner`、`MiniMaxH3SemanticBridgeConfigT8`、`WujiH3PromptEnhancer`、`MiniMaxH3HyperVAE2xLoaderEXPT8`、`VAEDecode`、`MiniMaxH3OutputTrimT8`、`MiniMaxH3AVDecodeT8`、`LoraLoaderModelOnly`、`CM_IntToFloat`、`List of strings [Crystools]`、`MiniMaxH3AudioConditioningT8`、`VHS_VideoCombine`、`BlockSparseAttention`、`ResolutionSelector`、`MiniMaxH3SemanticBridgeApplyT8`、`ConditioningZeroOut`、`KSamplerSelect`、`H3SigmaRefiner`、`MiniMaxH3ChunkFeedForwardT8Advanced`、`LoraLoaderBypassModelOnly`、`SelfLiftAvatarH3Sampler`、`UNETLoader`、`KSampler`、`EmptyLatentImage`、`CLIPTextEncode`、`solarL_SaveImagesToZip`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、EmptyLatentImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

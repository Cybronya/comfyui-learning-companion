---
key: 视频生成/文生视频/Minimax H3多合一生视频V6.0｜文生首尾图参二采放大_2098765941927665665.json
name: Minimax H3多合一生视频V6.0｜文生首尾图参二采放大_2098765941927665665
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/Minimax H3多合一生视频V6.0｜文生首尾图参二采放大_2098765941927665665.json
hash: 1d59994066d4ccd2
coverage: 0.592857
learned_at: 2026-10-15 22:46:36
nodes: [SetNode, SetNode, SetNode, SetNode, SetNode, GetNode, SetNode, SetNode, SetNode, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, VHS_LoadVideo, GetNode, LoadAudio, GetNode, SetNode, SetNode, SetNode, GetNode, GetNode, GetNode, SetNode, GetNode, GetNode, GetNode, VAELoader, ComfyMathExpression, SetNode, SetNode, ModelPreviewOverrideKJ, GetNode, GetNode, GetNode, GetNode, 布尔孤海, ResolutionSelector, SolAttnPatch, VAELoader, GetNode, GetNode, GetNode, SetNode, GetNode, SetNode, GetNode, SetNode, SetNode, ImpactConditionalBranch, GetNode, GetNode, GetNode, GetNode, GetNode, ConditioningZeroOut, GetNode, GetNode, GetNode, GetNode, Any Switch (rgthree), VAEDecode, VAEDecodeAudio, MiniMaxH3MemoryEfficientSageAttentionPatch, MiniMaxLowVRAMAttention, PathchSageAttentionKJ, MiniMaxChunkFeedForward, MiniMaxH3SigmaShift, SetNode, ModelAttentionBackend, SetNode, PrimitiveFloat, MiniMaxH3ImageToVideo, MiniMaxH3ReferenceToVideo, GetNode, CLIPLoader, ImageResizeKJv2, ImageResizeKJv2, BasicScheduler, VHS_VideoCombine, RandomNoise, PrimitiveStringMultiline, UNETLoader, LoraLoaderModelOnly, LoadImage, VRGDG_MiniMaxH3AudioDrive, KSamplerSelect, Any Switch (rgthree), H3SigmaRefiner, Int, MathExpression|pysssss, SelfLiftH3Sampler, PrimitiveFloat, LoadImage, 孤海注释, 孤海注释, UNETLoader, CLIPLoader, CLIPTextEncode, VAELoader, EmptyLatentImage, KSampler, VAEDecode, solarL_SaveImagesToZip, JjkText, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, CLIPTextEncode, Note]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/文生视频/Minimax H3多合一生视频V6.0｜文生首尾图参二采放大_2098765941927665665.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/Minimax H3多合一生视频V6.0｜文生首尾图参二采放大_2098765941927665665.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（140 个）：
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `VHS_LoadVideo`
- `GetNode`
- `LoadAudio`
- `GetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `VAELoader`
- `ComfyMathExpression`
- `SetNode`
- `SetNode`
- `ModelPreviewOverrideKJ`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `布尔孤海`
- `ResolutionSelector`
- `SolAttnPatch`
- `VAELoader`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `ImpactConditionalBranch`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `ConditioningZeroOut`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `Any Switch (rgthree)`
- `VAEDecode` ★核心
- `VAEDecodeAudio` ★核心
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `MiniMaxLowVRAMAttention`
- `PathchSageAttentionKJ`
- `MiniMaxChunkFeedForward`
- `MiniMaxH3SigmaShift`
- `SetNode`
- `ModelAttentionBackend`
- `SetNode`
- `PrimitiveFloat`
- `MiniMaxH3ImageToVideo`
- `MiniMaxH3ReferenceToVideo`
- `GetNode`
- `CLIPLoader`
- `ImageResizeKJv2`
- `ImageResizeKJv2`
- `BasicScheduler`
- `VHS_VideoCombine`
- `RandomNoise`
- `PrimitiveStringMultiline`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoadImage`
- `VRGDG_MiniMaxH3AudioDrive`
- `KSamplerSelect` ★核心
- `Any Switch (rgthree)`
- `H3SigmaRefiner`
- `Int`
- `MathExpression|pysssss`
- `SelfLiftH3Sampler` ★核心
- `PrimitiveFloat`
- `LoadImage`
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

覆盖率 **59%**（83/140）

**有卡**：`LoadImage`、`VHS_LoadVideo`、`LoadAudio`、`VAELoader`、`ComfyMathExpression`、`ModelPreviewOverrideKJ`、`布尔孤海`、`ResolutionSelector`、`SolAttnPatch`、`ImpactConditionalBranch`、`ConditioningZeroOut`、`VAEDecode`、`VAEDecodeAudio`、`MiniMaxH3MemoryEfficientSageAttentionPatch`、`MiniMaxLowVRAMAttention`、`PathchSageAttentionKJ`、`MiniMaxChunkFeedForward`、`MiniMaxH3SigmaShift`、`ModelAttentionBackend`、`MiniMaxH3ImageToVideo`、`MiniMaxH3ReferenceToVideo`、`CLIPLoader`、`ImageResizeKJv2`、`BasicScheduler`、`VHS_VideoCombine`、`RandomNoise`、`UNETLoader`、`LoraLoaderModelOnly`、`VRGDG_MiniMaxH3AudioDrive`、`KSamplerSelect`、`H3SigmaRefiner`、`Int`、`MathExpression|pysssss`、`SelfLiftH3Sampler`、`CLIPTextEncode`、`EmptyLatentImage`、`KSampler`、`solarL_SaveImagesToZip`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、EmptyLatentImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

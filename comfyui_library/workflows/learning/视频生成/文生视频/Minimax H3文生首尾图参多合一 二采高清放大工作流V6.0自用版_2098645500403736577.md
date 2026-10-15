---
key: 视频生成/文生视频/Minimax H3文生首尾图参多合一 二采高清放大工作流V6.0自用版_2098645500403736577.json
name: Minimax H3文生首尾图参多合一 二采高清放大工作流V6.0自用版_2098645500403736577
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/Minimax H3文生首尾图参多合一 二采高清放大工作流V6.0自用版_2098645500403736577.json
hash: 5608000fce6e556b
coverage: 0.534351
learned_at: 2026-10-15 22:46:39
nodes: [SetNode, SetNode, SetNode, SetNode, SetNode, GetNode, SetNode, SetNode, SetNode, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, VHS_LoadVideo, GetNode, LoadAudio, GetNode, SetNode, SetNode, SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, SetNode, GetNode, GetNode, GetNode, GetNode, VAELoader, ComfyMathExpression, SetNode, SetNode, ModelPreviewOverrideKJ, GetNode, GetNode, GetNode, GetNode, 布尔孤海, ResolutionSelector, SolAttnPatch, VAELoader, GetNode, GetNode, GetNode, SetNode, GetNode, SetNode, GetNode, SetNode, SetNode, ImpactConditionalBranch, GetNode, GetNode, GetNode, GetNode, GetNode, ConditioningZeroOut, GetNode, GetNode, GetNode, GetNode, GetNode, Any Switch (rgthree), VAEDecode, VAEDecodeAudio, MiniMaxH3MemoryEfficientSageAttentionPatch, MiniMaxLowVRAMAttention, PathchSageAttentionKJ, MiniMaxChunkFeedForward, MiniMaxH3SigmaShift, SetNode, ModelAttentionBackend, SetNode, PrimitiveFloat, MiniMaxH3ImageToVideo, MiniMaxH3ReferenceToVideo, GetNode, CLIPLoader, ImageResizeKJv2, ImageResizeKJv2, BasicScheduler, VHS_VideoCombine, RandomNoise, PrimitiveStringMultiline, UNETLoader, LoraLoaderModelOnly, LoadImage, VRGDG_MiniMaxH3AudioDrive, KSamplerSelect, Any Switch (rgthree), H3SigmaRefiner, Int, MathExpression|pysssss, SelfLiftH3Sampler, PrimitiveFloat, LoadImage, 孤海注释, 孤海注释, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, KSampler, CLIPTextEncode, CLIPLoader, CLIPTextEncode, JjkText, EmptyLatentImage, solarL_SaveImagesToZip, VAEDecode, VAELoader, Note, SaveImage]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/文生视频/Minimax H3文生首尾图参多合一 二采高清放大工作流V6.0自用版_2098645500403736577.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/Minimax H3文生首尾图参多合一 二采高清放大工作流V6.0自用版_2098645500403736577.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（131 个）：
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
- `GetNode`
- `GetNode`
- `SetNode`
- `GetNode`
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
- `CLIPTextEncode` ★核心
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `JjkText`
- `EmptyLatentImage` ★核心
- `solarL_SaveImagesToZip`
- `VAEDecode` ★核心
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

覆盖率 **53%**（70/131）

**有卡**：`LoadImage`、`VHS_LoadVideo`、`LoadAudio`、`VAELoader`、`ComfyMathExpression`、`ModelPreviewOverrideKJ`、`布尔孤海`、`ResolutionSelector`、`SolAttnPatch`、`ImpactConditionalBranch`、`ConditioningZeroOut`、`VAEDecode`、`VAEDecodeAudio`、`MiniMaxH3MemoryEfficientSageAttentionPatch`、`MiniMaxLowVRAMAttention`、`PathchSageAttentionKJ`、`MiniMaxChunkFeedForward`、`MiniMaxH3SigmaShift`、`ModelAttentionBackend`、`MiniMaxH3ImageToVideo`、`MiniMaxH3ReferenceToVideo`、`CLIPLoader`、`ImageResizeKJv2`、`BasicScheduler`、`VHS_VideoCombine`、`RandomNoise`、`UNETLoader`、`LoraLoaderModelOnly`、`VRGDG_MiniMaxH3AudioDrive`、`KSamplerSelect`、`H3SigmaRefiner`、`Int`、`MathExpression|pysssss`、`SelfLiftH3Sampler`、`KSampler`、`CLIPTextEncode`、`EmptyLatentImage`、`solarL_SaveImagesToZip`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、EmptyLatentImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

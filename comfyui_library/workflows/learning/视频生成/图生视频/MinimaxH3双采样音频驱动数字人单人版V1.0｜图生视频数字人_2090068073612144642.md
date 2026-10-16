---
key: 视频生成/图生视频/MinimaxH3双采样音频驱动数字人单人版V1.0｜图生视频数字人_2090068073612144642.json
name: MinimaxH3双采样音频驱动数字人单人版V1.0｜图生视频数字人_2090068073612144642
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/MinimaxH3双采样音频驱动数字人单人版V1.0｜图生视频数字人_2090068073612144642.json
hash: cb026ad143bb5650
coverage: 0.73913
learned_at: 2026-10-16 22:02:09
nodes: [KSamplerSelect, CLIPLoader, BasicGuider, VAEEncode, VAEEncodeAudio, SamplerCustomAdvanced, easy clearCacheAll, SetNode, SetNode, SetNode, VAELoader, VAELoader, SetNode, SetNode, GetNode, GetNode, GetNode, RandomNoise, ExtendIntermediateSigmas, SamplerCustomAdvanced, VHS_VideoCombine, VAEDecode, MiniMaxH3MemoryEfficientSageAttentionPatch, ModelAttentionBackend, VAEDecode, INTConstant, UNETLoader, UNETLoader, MiniMaxH3MemoryEfficientSageAttentionPatch, ModelAttentionBackend, LoraLoaderBypassModelOnly, MiniMaxH3ReferenceToVideo, VRGDG_MiniMaxH3AudioDrive, H3SigmaRefiner, ExtendIntermediateSigmas, SetNode, Reroute, Reroute, H3SigmaRefiner, LoraLoaderBypassModelOnly, BasicGuider, KSamplerSelect, BasicScheduler, PT_H3ConcatAVLatent, GetNode, ImageResizeKJv2, GetNode, GetNode, PrimitiveFloat, ComfyMathExpression, SoundFlow_GetLength, SetNode, INTConstant, BasicScheduler, GetNode, ResolutionSelector, Reroute, Reroute, ResolutionSelector, LoadAudio, AudioCrop, PreviewAudio, PrimitiveStringMultiline, LoadImage, VHS_VideoCombine, 孤海注释, 孤海注释, UNETLoader, CLIPLoader, CLIPTextEncode, VAELoader, EmptyLatentImage, KSampler, VAEDecode, JjkText, solarL_SaveImagesToZip, CLIPTextEncode, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, Note]
patterns: [text_to_image, image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/图生视频/MinimaxH3双采样音频驱动数字人单人版V1.0｜图生视频数字人_2090068073612144642.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/MinimaxH3双采样音频驱动数字人单人版V1.0｜图生视频数字人_2090068073612144642.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（92 个）：
- `KSamplerSelect` ★核心
- `CLIPLoader`
- `BasicGuider`
- `VAEEncode` ★核心
- `VAEEncodeAudio` ★核心
- `SamplerCustomAdvanced` ★核心
- `easy clearCacheAll`
- `SetNode`
- `SetNode`
- `SetNode`
- `VAELoader`
- `VAELoader`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `RandomNoise`
- `ExtendIntermediateSigmas`
- `SamplerCustomAdvanced` ★核心
- `VHS_VideoCombine`
- `VAEDecode` ★核心
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `ModelAttentionBackend`
- `VAEDecode` ★核心
- `INTConstant`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `ModelAttentionBackend`
- `LoraLoaderBypassModelOnly` ★核心
- `MiniMaxH3ReferenceToVideo`
- `VRGDG_MiniMaxH3AudioDrive`
- `H3SigmaRefiner`
- `ExtendIntermediateSigmas`
- `SetNode`
- `Reroute`
- `Reroute`
- `H3SigmaRefiner`
- `LoraLoaderBypassModelOnly` ★核心
- `BasicGuider`
- `KSamplerSelect` ★核心
- `BasicScheduler`
- `PT_H3ConcatAVLatent`
- `GetNode`
- `ImageResizeKJv2`
- `GetNode`
- `GetNode`
- `PrimitiveFloat`
- `ComfyMathExpression`
- `SoundFlow_GetLength`
- `SetNode`
- `INTConstant`
- `BasicScheduler`
- `GetNode`
- `ResolutionSelector`
- `Reroute`
- `Reroute`
- `ResolutionSelector`
- `LoadAudio`
- `AudioCrop`
- `PreviewAudio`
- `PrimitiveStringMultiline`
- `LoadImage`
- `VHS_VideoCombine`
- `孤海注释`
- `孤海注释`
- `UNETLoader` ★核心
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `VAELoader`
- `EmptyLatentImage` ★核心
- `KSampler` ★核心
- `VAEDecode` ★核心
- `JjkText`
- `solarL_SaveImagesToZip`
- `CLIPTextEncode` ★核心
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
- `Note`

**识别到的模式**：text_to_image、image_to_image

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

覆盖率 **74%**（68/92）

**有卡**：`KSamplerSelect`、`CLIPLoader`、`BasicGuider`、`VAEEncode`、`VAEEncodeAudio`、`SamplerCustomAdvanced`、`easy clearCacheAll`、`VAELoader`、`RandomNoise`、`ExtendIntermediateSigmas`、`VHS_VideoCombine`、`VAEDecode`、`MiniMaxH3MemoryEfficientSageAttentionPatch`、`ModelAttentionBackend`、`INTConstant`、`UNETLoader`、`LoraLoaderBypassModelOnly`、`MiniMaxH3ReferenceToVideo`、`VRGDG_MiniMaxH3AudioDrive`、`H3SigmaRefiner`、`BasicScheduler`、`PT_H3ConcatAVLatent`、`ImageResizeKJv2`、`ComfyMathExpression`、`SoundFlow_GetLength`、`ResolutionSelector`、`LoadAudio`、`AudioCrop`、`PreviewAudio`、`LoadImage`、`CLIPTextEncode`、`EmptyLatentImage`、`KSampler`、`solarL_SaveImagesToZip`、`LoraLoaderModelOnly`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage、ResolutionSelector

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

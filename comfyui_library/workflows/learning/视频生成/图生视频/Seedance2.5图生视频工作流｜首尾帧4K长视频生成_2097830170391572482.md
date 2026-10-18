---
key: 视频生成/图生视频/Seedance2.5图生视频工作流｜首尾帧4K长视频生成_2097830170391572482.json
name: Seedance2.5图生视频工作流｜首尾帧4K长视频生成_2097830170391572482
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Seedance2.5图生视频工作流｜首尾帧4K长视频生成_2097830170391572482.json
hash: 93061c427fe9cd6e
coverage: 0.888889
learned_at: 2026-10-17 01:28:23
nodes: [VAELoader, VAELoader, PrimitiveFloat, CLIPLoader, ResolutionSelector, LoadImage, LoadImage, ComfyMathExpression, BasicScheduler, MiniMaxH3ReferenceToVideo, BasicGuider, PrimitiveStringMultiline, KSamplerSelect, RandomNoise, SamplerCustomAdvanced, VAEDecode, VAEDecodeAudio, VHS_VideoCombine, MiniMaxLowVRAMAttention, MiniMaxChunkFeedForward, LoraLoaderModelOnly, ModelAttentionBackend, LoraLoaderModelOnly, UNETLoader, 孤海注释, 孤海注释, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, KSampler, CLIPTextEncode, CLIPLoader, CLIPTextEncode, JjkText, EmptyLatentImage, solarL_SaveImagesToZip, VAEDecode, VAELoader, Note, SaveImage]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/图生视频/Seedance2.5图生视频工作流｜首尾帧4K长视频生成_2097830170391572482.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/Seedance2.5图生视频工作流｜首尾帧4K长视频生成_2097830170391572482.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（54 个）：
- `VAELoader`
- `VAELoader`
- `PrimitiveFloat`
- `CLIPLoader`
- `ResolutionSelector`
- `LoadImage`
- `LoadImage`
- `ComfyMathExpression`
- `BasicScheduler`
- `MiniMaxH3ReferenceToVideo`
- `BasicGuider`
- `PrimitiveStringMultiline`
- `KSamplerSelect` ★核心
- `RandomNoise`
- `SamplerCustomAdvanced` ★核心
- `VAEDecode` ★核心
- `VAEDecodeAudio` ★核心
- `VHS_VideoCombine`
- `MiniMaxLowVRAMAttention`
- `MiniMaxChunkFeedForward`
- `LoraLoaderModelOnly` ★核心
- `ModelAttentionBackend`
- `LoraLoaderModelOnly` ★核心
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

覆盖率 **89%**（48/54）

**有卡**：`VAELoader`、`CLIPLoader`、`ResolutionSelector`、`LoadImage`、`ComfyMathExpression`、`BasicScheduler`、`MiniMaxH3ReferenceToVideo`、`BasicGuider`、`KSamplerSelect`、`RandomNoise`、`SamplerCustomAdvanced`、`VAEDecode`、`VAEDecodeAudio`、`VHS_VideoCombine`、`MiniMaxLowVRAMAttention`、`MiniMaxChunkFeedForward`、`LoraLoaderModelOnly`、`ModelAttentionBackend`、`UNETLoader`、`KSampler`、`CLIPTextEncode`、`EmptyLatentImage`、`solarL_SaveImagesToZip`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage、ResolutionSelector

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

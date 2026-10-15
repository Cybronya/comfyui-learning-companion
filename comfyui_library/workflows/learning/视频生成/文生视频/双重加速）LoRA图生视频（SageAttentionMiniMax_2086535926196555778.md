---
key: 视频生成/文生视频/双重加速）LoRA图生视频（SageAttentionMiniMax_2086535926196555778.json
name: 双重加速）LoRA图生视频（SageAttentionMiniMax_2086535926196555778
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/双重加速）LoRA图生视频（SageAttentionMiniMax_2086535926196555778.json
hash: d8cf7624e2ce6a33
coverage: 0.825
learned_at: 2026-10-15 22:48:20
nodes: [VAELoader, VAELoader, VAEDecodeAudio, VAEDecode, SamplerCustomAdvanced, BasicGuider, CLIPLoader, RandomNoise, CreateVideo, ComfyMathExpression, MarkdownNote, SaveVideo, LoadImage, ResolutionSelector, MiniMaxH3ImageToVideo, UNETLoader, LoadImage, PrimitiveFloat, LoraLoaderBypassModelOnly, MarkdownNote, LoraLoaderBypassModelOnly, LoraLoaderBypassModelOnly, MiniMaxH3MemoryEfficientSageAttentionPatch, BasicScheduler, KSamplerSelect, LoraLoaderModelOnly, LoraLoaderModelOnly, KSampler, UNETLoader, CLIPLoader, solarL_SaveImagesToZip, VAELoader, CLIPTextEncode, CLIPTextEncode, JjkText, VAEDecode, EmptyLatentImage, Note, 孤海注释, 孤海注释]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/文生视频/双重加速）LoRA图生视频（SageAttentionMiniMax_2086535926196555778.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/双重加速）LoRA图生视频（SageAttentionMiniMax_2086535926196555778.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（40 个）：
- `VAELoader`
- `VAELoader`
- `VAEDecodeAudio` ★核心
- `VAEDecode` ★核心
- `SamplerCustomAdvanced` ★核心
- `BasicGuider`
- `CLIPLoader`
- `RandomNoise`
- `CreateVideo`
- `ComfyMathExpression`
- `MarkdownNote`
- `SaveVideo`
- `LoadImage`
- `ResolutionSelector`
- `MiniMaxH3ImageToVideo`
- `UNETLoader` ★核心
- `LoadImage`
- `PrimitiveFloat`
- `LoraLoaderBypassModelOnly` ★核心
- `MarkdownNote`
- `LoraLoaderBypassModelOnly` ★核心
- `LoraLoaderBypassModelOnly` ★核心
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `BasicScheduler`
- `KSamplerSelect` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `KSampler` ★核心
- `UNETLoader` ★核心
- `CLIPLoader`
- `solarL_SaveImagesToZip`
- `VAELoader`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `JjkText`
- `VAEDecode` ★核心
- `EmptyLatentImage` ★核心
- `Note`
- `孤海注释`
- `孤海注释`

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

覆盖率 **82%**（33/40）

**有卡**：`VAELoader`、`VAEDecodeAudio`、`VAEDecode`、`SamplerCustomAdvanced`、`BasicGuider`、`CLIPLoader`、`RandomNoise`、`CreateVideo`、`ComfyMathExpression`、`SaveVideo`、`LoadImage`、`ResolutionSelector`、`MiniMaxH3ImageToVideo`、`UNETLoader`、`LoraLoaderBypassModelOnly`、`MiniMaxH3MemoryEfficientSageAttentionPatch`、`BasicScheduler`、`KSamplerSelect`、`LoraLoaderModelOnly`、`KSampler`、`solarL_SaveImagesToZip`、`CLIPTextEncode`、`EmptyLatentImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage、ResolutionSelector

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

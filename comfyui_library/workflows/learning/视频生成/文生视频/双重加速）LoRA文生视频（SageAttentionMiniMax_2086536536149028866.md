---
key: 视频生成/文生视频/双重加速）LoRA文生视频（SageAttentionMiniMax_2086536536149028866.json
name: 双重加速）LoRA文生视频（SageAttentionMiniMax_2086536536149028866
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/双重加速）LoRA文生视频（SageAttentionMiniMax_2086536536149028866.json
hash: 341f51a0d70b6d28
coverage: 0.815789
learned_at: 2026-10-15 22:48:20
nodes: [VAEDecodeAudio, VAEDecode, SamplerCustomAdvanced, BasicGuider, RandomNoise, CreateVideo, VAELoader, VAELoader, CLIPLoader, ComfyMathExpression, ResolutionSelector, SaveVideo, MiniMaxH3ImageToVideo, MarkdownNote, PrimitiveFloat, MarkdownNote, UNETLoader, MiniMaxH3MemoryEfficientSageAttentionPatch, LoraLoaderBypassModelOnly, LoraLoaderBypassModelOnly, LoraLoaderBypassModelOnly, KSamplerSelect, BasicScheduler, LoraLoaderModelOnly, LoraLoaderModelOnly, KSampler, UNETLoader, CLIPLoader, solarL_SaveImagesToZip, VAELoader, CLIPTextEncode, CLIPTextEncode, JjkText, VAEDecode, EmptyLatentImage, Note, 孤海注释, 孤海注释]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/文生视频/双重加速）LoRA文生视频（SageAttentionMiniMax_2086536536149028866.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/双重加速）LoRA文生视频（SageAttentionMiniMax_2086536536149028866.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（38 个）：
- `VAEDecodeAudio` ★核心
- `VAEDecode` ★核心
- `SamplerCustomAdvanced` ★核心
- `BasicGuider`
- `RandomNoise`
- `CreateVideo`
- `VAELoader`
- `VAELoader`
- `CLIPLoader`
- `ComfyMathExpression`
- `ResolutionSelector`
- `SaveVideo`
- `MiniMaxH3ImageToVideo`
- `MarkdownNote`
- `PrimitiveFloat`
- `MarkdownNote`
- `UNETLoader` ★核心
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `LoraLoaderBypassModelOnly` ★核心
- `LoraLoaderBypassModelOnly` ★核心
- `LoraLoaderBypassModelOnly` ★核心
- `KSamplerSelect` ★核心
- `BasicScheduler`
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

覆盖率 **82%**（31/38）

**有卡**：`VAEDecodeAudio`、`VAEDecode`、`SamplerCustomAdvanced`、`BasicGuider`、`RandomNoise`、`CreateVideo`、`VAELoader`、`CLIPLoader`、`ComfyMathExpression`、`ResolutionSelector`、`SaveVideo`、`MiniMaxH3ImageToVideo`、`UNETLoader`、`MiniMaxH3MemoryEfficientSageAttentionPatch`、`LoraLoaderBypassModelOnly`、`KSamplerSelect`、`BasicScheduler`、`LoraLoaderModelOnly`、`KSampler`、`solarL_SaveImagesToZip`、`CLIPTextEncode`、`EmptyLatentImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage、ResolutionSelector

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

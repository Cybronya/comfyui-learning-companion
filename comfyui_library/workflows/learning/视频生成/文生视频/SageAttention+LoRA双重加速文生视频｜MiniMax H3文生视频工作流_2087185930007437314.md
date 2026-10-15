---
key: 视频生成/文生视频/SageAttention+LoRA双重加速文生视频｜MiniMax H3文生视频工作流_2087185930007437314.json
name: SageAttention+LoRA双重加速文生视频｜MiniMax H3文生视频工作流_2087185930007437314
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/SageAttention+LoRA双重加速文生视频｜MiniMax H3文生视频工作流_2087185930007437314.json
hash: b4f49e630fb89f12
coverage: 0.843137
learned_at: 2026-10-15 22:46:57
nodes: [VAEDecodeAudio, VAEDecode, SamplerCustomAdvanced, BasicGuider, RandomNoise, CreateVideo, VAELoader, VAELoader, CLIPLoader, ComfyMathExpression, SaveVideo, MarkdownNote, MarkdownNote, PrimitiveFloat, MarkdownNote, UNETLoader, MiniMaxH3MemoryEfficientSageAttentionPatch, LoraLoaderBypassModelOnly, LoraLoaderBypassModelOnly, KSamplerSelect, BasicScheduler, ResolutionSelector, LoraLoaderBypassModelOnly, MiniMaxH3ImageToVideo, 孤海注释, 孤海注释, UNETLoader, CLIPLoader, CLIPTextEncode, VAELoader, EmptyLatentImage, KSampler, VAEDecode, JjkText, solarL_SaveImagesToZip, CLIPTextEncode, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, Note]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/文生视频/SageAttention+LoRA双重加速文生视频｜MiniMax H3文生视频工作流_2087185930007437314.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/SageAttention+LoRA双重加速文生视频｜MiniMax H3文生视频工作流_2087185930007437314.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（51 个）：
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
- `SaveVideo`
- `MarkdownNote`
- `MarkdownNote`
- `PrimitiveFloat`
- `MarkdownNote`
- `UNETLoader` ★核心
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `LoraLoaderBypassModelOnly` ★核心
- `LoraLoaderBypassModelOnly` ★核心
- `KSamplerSelect` ★核心
- `BasicScheduler`
- `ResolutionSelector`
- `LoraLoaderBypassModelOnly` ★核心
- `MiniMaxH3ImageToVideo`
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

覆盖率 **84%**（43/51）

**有卡**：`VAEDecodeAudio`、`VAEDecode`、`SamplerCustomAdvanced`、`BasicGuider`、`RandomNoise`、`CreateVideo`、`VAELoader`、`CLIPLoader`、`ComfyMathExpression`、`SaveVideo`、`UNETLoader`、`MiniMaxH3MemoryEfficientSageAttentionPatch`、`LoraLoaderBypassModelOnly`、`KSamplerSelect`、`BasicScheduler`、`ResolutionSelector`、`MiniMaxH3ImageToVideo`、`CLIPTextEncode`、`EmptyLatentImage`、`KSampler`、`solarL_SaveImagesToZip`、`LoraLoaderModelOnly`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage、ResolutionSelector

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

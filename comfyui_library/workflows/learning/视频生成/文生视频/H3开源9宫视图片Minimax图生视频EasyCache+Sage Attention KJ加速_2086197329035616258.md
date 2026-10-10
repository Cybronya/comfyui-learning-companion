---
key: 视频生成/文生视频/H3开源9宫视图片Minimax图生视频EasyCache+Sage Attention KJ加速_2086197329035616258.json
name: H3开源9宫视图片Minimax图生视频EasyCache+Sage Attention KJ加速_2086197329035616258
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/H3开源9宫视图片Minimax图生视频EasyCache+Sage Attention KJ加速_2086197329035616258.json
hash: c953a423d4e22571
coverage: 0.868421
learned_at: 2026-10-10 22:59:40
nodes: [VAELoader, VAELoader, UNETLoader, CLIPLoader, RandomNoise, BasicGuider, KSamplerSelect, BasicScheduler, VAEDecode, VAEDecodeAudio, CreateVideo, LoadImage, LoadImage, MiniMaxH3ReferenceToVideo, ResolutionSelector, LoraLoaderModelOnly, LoraLoaderModelOnly, KSampler, UNETLoader, CLIPLoader, solarL_SaveImagesToZip, VAELoader, CLIPTextEncode, CLIPTextEncode, JjkText, VAEDecode, EmptyLatentImage, Note, MarkdownNote, PrimitiveStringMultiline, EasyCache, PathchSageAttentionKJ, LoadImage, LoadImage, PrimitiveFloat, SamplerCustomAdvanced, SaveVideo, ComfyMathExpression]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/文生视频/H3开源9宫视图片Minimax图生视频EasyCache+Sage Attention KJ加速_2086197329035616258.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/H3开源9宫视图片Minimax图生视频EasyCache+Sage Attention KJ加速_2086197329035616258.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（38 个）：
- `VAELoader`
- `VAELoader`
- `UNETLoader` ★核心
- `CLIPLoader`
- `RandomNoise`
- `BasicGuider`
- `KSamplerSelect` ★核心
- `BasicScheduler`
- `VAEDecode` ★核心
- `VAEDecodeAudio` ★核心
- `CreateVideo`
- `LoadImage`
- `LoadImage`
- `MiniMaxH3ReferenceToVideo`
- `ResolutionSelector`
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
- `MarkdownNote`
- `PrimitiveStringMultiline`
- `EasyCache`
- `PathchSageAttentionKJ`
- `LoadImage`
- `LoadImage`
- `PrimitiveFloat`
- `SamplerCustomAdvanced` ★核心
- `SaveVideo`
- `ComfyMathExpression`

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

覆盖率 **87%**（33/38）

**有卡**：`VAELoader`、`UNETLoader`、`CLIPLoader`、`RandomNoise`、`BasicGuider`、`KSamplerSelect`、`BasicScheduler`、`VAEDecode`、`VAEDecodeAudio`、`CreateVideo`、`LoadImage`、`MiniMaxH3ReferenceToVideo`、`ResolutionSelector`、`LoraLoaderModelOnly`、`KSampler`、`solarL_SaveImagesToZip`、`CLIPTextEncode`、`EmptyLatentImage`、`EasyCache`、`PathchSageAttentionKJ`、`SamplerCustomAdvanced`、`SaveVideo`、`ComfyMathExpression`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage、ResolutionSelector

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

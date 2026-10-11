---
key: 视频生成/文生视频/refV1.2Lora多参考工作流｜MiniMax H3全接口开放开发版_2096716514572460034.json
name: refV1.2Lora多参考工作流｜MiniMax H3全接口开放开发版_2096716514572460034
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/refV1.2Lora多参考工作流｜MiniMax H3全接口开放开发版_2096716514572460034.json
hash: d1ce35cb93874fa9
coverage: 0.847222
learned_at: 2026-10-11 21:41:54
nodes: [KSamplerSelect, BasicGuider, ComfyMathExpression, SetNode, GetNode, VAEDecodeAudio, SetNode, PathchSageAttentionKJ, MiniMaxH3SigmaShift, RandomNoise, CLIPLoader, VAELoader, VAELoader, SamplerCustomAdvanced, UNETLoader, VHS_LoadVideo, SetNode, VAEDecode, BasicScheduler, VHS_LoadVideo, ResolutionSelector, PrimitiveFloat, MiniMaxH3ReferenceToVideo, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, VHS_LoadVideo, VHS_LoadVideo, VHS_LoadVideo, LoadAudio, LoadAudio, LoadAudio, VHS_LoadVideo, VHS_VideoCombine, LoadImage, LoadImage, LoraLoaderModelOnly, PrimitiveFloat, PrimitiveStringMultiline, LoadImage, LoadImage, 孤海注释, 孤海注释, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, KSampler, CLIPTextEncode, CLIPLoader, CLIPTextEncode, JjkText, EmptyLatentImage, solarL_SaveImagesToZip, VAEDecode, VAELoader, Note]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/文生视频/refV1.2Lora多参考工作流｜MiniMax H3全接口开放开发版_2096716514572460034.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/refV1.2Lora多参考工作流｜MiniMax H3全接口开放开发版_2096716514572460034.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（72 个）：
- `KSamplerSelect` ★核心
- `BasicGuider`
- `ComfyMathExpression`
- `SetNode`
- `GetNode`
- `VAEDecodeAudio` ★核心
- `SetNode`
- `PathchSageAttentionKJ`
- `MiniMaxH3SigmaShift`
- `RandomNoise`
- `CLIPLoader`
- `VAELoader`
- `VAELoader`
- `SamplerCustomAdvanced` ★核心
- `UNETLoader` ★核心
- `VHS_LoadVideo`
- `SetNode`
- `VAEDecode` ★核心
- `BasicScheduler`
- `VHS_LoadVideo`
- `ResolutionSelector`
- `PrimitiveFloat`
- `MiniMaxH3ReferenceToVideo`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `VHS_LoadVideo`
- `VHS_LoadVideo`
- `VHS_LoadVideo`
- `LoadAudio`
- `LoadAudio`
- `LoadAudio`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `LoadImage`
- `LoadImage`
- `LoraLoaderModelOnly` ★核心
- `PrimitiveFloat`
- `PrimitiveStringMultiline`
- `LoadImage`
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

覆盖率 **85%**（61/72）

**有卡**：`KSamplerSelect`、`BasicGuider`、`ComfyMathExpression`、`VAEDecodeAudio`、`PathchSageAttentionKJ`、`MiniMaxH3SigmaShift`、`RandomNoise`、`CLIPLoader`、`VAELoader`、`SamplerCustomAdvanced`、`UNETLoader`、`VHS_LoadVideo`、`VAEDecode`、`BasicScheduler`、`ResolutionSelector`、`MiniMaxH3ReferenceToVideo`、`LoadImage`、`LoadAudio`、`VHS_VideoCombine`、`LoraLoaderModelOnly`、`KSampler`、`CLIPTextEncode`、`EmptyLatentImage`、`solarL_SaveImagesToZip`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage、ResolutionSelector

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

---
key: 视频生成/图生视频/留空真人全参工作流｜Seedance2.0地表最强视频生成_2093481519183654913.json
name: 留空真人全参工作流｜Seedance2.0地表最强视频生成_2093481519183654913
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/留空真人全参工作流｜Seedance2.0地表最强视频生成_2093481519183654913.json
hash: b0cf288e83865ccb
coverage: 0.88
learned_at: 2026-10-16 23:43:13
nodes: [SaveVideo, PreviewAny, PreviewAny, LoadVideo, LoadVideo, LoadVideo, LoadVideo, LoadAudio, LoadAudio, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadAudio, LoadVideo, LoadImage, LoadImage, RH_RhartVideoSparkvideo20MultimodalVideo, 孤海注释, 孤海注释, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, KSampler, CLIPTextEncode, CLIPLoader, CLIPTextEncode, JjkText, EmptyLatentImage, solarL_SaveImagesToZip, VAEDecode, VAELoader, Note]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/图生视频/留空真人全参工作流｜Seedance2.0地表最强视频生成_2093481519183654913.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/留空真人全参工作流｜Seedance2.0地表最强视频生成_2093481519183654913.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（50 个）：
- `SaveVideo`
- `PreviewAny`
- `PreviewAny`
- `LoadVideo`
- `LoadVideo`
- `LoadVideo`
- `LoadVideo`
- `LoadAudio`
- `LoadAudio`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadAudio`
- `LoadVideo`
- `LoadImage`
- `LoadImage`
- `RH_RhartVideoSparkvideo20MultimodalVideo`
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

覆盖率 **88%**（44/50）

**有卡**：`SaveVideo`、`LoadVideo`、`LoadAudio`、`LoadImage`、`RH_RhartVideoSparkvideo20MultimodalVideo`、`UNETLoader`、`LoraLoaderModelOnly`、`KSampler`、`CLIPTextEncode`、`CLIPLoader`、`EmptyLatentImage`、`solarL_SaveImagesToZip`、`VAEDecode`、`VAELoader`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage、LoadImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

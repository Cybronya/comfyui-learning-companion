---
key: comfyui-workflow-templates-json/video_humo.json
name: video_humo
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/comfyui-workflow-templates-json/video_humo.json
hash: a262fae454036848
official: true
coverage: 0.85
learned_at: 2026-10-07 21:36:59
nodes: [CLIPLoader, VAELoader, CreateVideo, VAEDecode, LoraLoaderModelOnly, UNETLoader, WanHuMoImageToVideo, AudioEncoderEncode, AudioEncoderLoader, MarkdownNote, CLIPTextEncode, KSampler, ModelSamplingSD3, MarkdownNote, MarkdownNote, CLIPTextEncode, SaveVideo, RecordAudio, LoadImage, LoadAudio]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "uni_pc", "scheduler": "simple", "seed": 1067760026265042, "steps": 6}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# comfyui-workflow-templates-json/video_humo.json

> 来源文件 `comfyui_library/workflows/comfyui-workflow-templates-json/video_humo.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Output → Other

**节点**（20 个）：
- `CLIPLoader`
- `VAELoader`
- `CreateVideo`
- `VAEDecode` ★核心
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `WanHuMoImageToVideo`
- `AudioEncoderEncode`
- `AudioEncoderLoader`
- `MarkdownNote`
- `CLIPTextEncode` ★核心
- `KSampler` ★核心
- `ModelSamplingSD3`
- `MarkdownNote`
- `MarkdownNote`
- `CLIPTextEncode` ★核心
- `SaveVideo`
- `RecordAudio`
- `LoadImage`
- `LoadAudio`

## 关键参数

- `seed` = `1067760026265042`
- `steps` = `6`
- `cfg` = `1`
- `sampler_name` = `uni_pc`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **85%**（17/20）

**有卡**：`CLIPLoader`、`VAELoader`、`CreateVideo`、`VAEDecode`、`LoraLoaderModelOnly`、`UNETLoader`、`WanHuMoImageToVideo`、`AudioEncoderEncode`、`AudioEncoderLoader`、`CLIPTextEncode`、`KSampler`、`ModelSamplingSD3`、`SaveVideo`、`RecordAudio`、`LoadImage`、`LoadAudio`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

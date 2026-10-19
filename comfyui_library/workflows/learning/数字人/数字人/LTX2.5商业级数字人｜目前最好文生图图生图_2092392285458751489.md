---
key: 数字人/数字人/LTX2.5商业级数字人｜目前最好文生图图生图_2092392285458751489.json
name: LTX2.5商业级数字人｜目前最好文生图图生图_2092392285458751489
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/数字人/数字人/LTX2.5商业级数字人｜目前最好文生图图生图_2092392285458751489.json
hash: 9e5987fb7e5ed9a9
coverage: 0.893617
learned_at: 2026-10-18 22:17:11
nodes: [VAELoader, VAELoader, PreviewAny, CreateVideo, UNETLoader, CLIPLoader, MiniMaxH3MemoryEfficientSageAttentionPatch, PathchSageAttentionKJ, LoraLoaderModelOnly, UpscaleModelLoader, UNETLoader, LoraLoaderModelOnly, MiniMaxH3MemoryEfficientSageAttentionPatch, PathchSageAttentionKJ, BasicScheduler, MiniMaxH3Director, SaveVideo, MiniMaxH3DirectorRefine, 孤海注释, 孤海注释, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, UNETLoader, KSampler, CLIPTextEncode, solarL_SaveImagesToZip, VAEDecode, VAELoader, CLIPLoader, EmptyLatentImage, JjkText, CLIPTextEncode, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, Note]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 数字人/数字人/LTX2.5商业级数字人｜目前最好文生图图生图_2092392285458751489.json

> 来源文件 `comfyui_library/workflows/数字人/数字人/LTX2.5商业级数字人｜目前最好文生图图生图_2092392285458751489.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（47 个）：
- `VAELoader`
- `VAELoader`
- `PreviewAny`
- `CreateVideo`
- `UNETLoader` ★核心
- `CLIPLoader`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `PathchSageAttentionKJ`
- `LoraLoaderModelOnly` ★核心
- `UpscaleModelLoader`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `PathchSageAttentionKJ`
- `BasicScheduler`
- `MiniMaxH3Director`
- `SaveVideo`
- `MiniMaxH3DirectorRefine`
- `孤海注释`
- `孤海注释`
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
- `UNETLoader` ★核心
- `KSampler` ★核心
- `CLIPTextEncode` ★核心
- `solarL_SaveImagesToZip`
- `VAEDecode` ★核心
- `VAELoader`
- `CLIPLoader`
- `EmptyLatentImage` ★核心
- `JjkText`
- `CLIPTextEncode` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
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

覆盖率 **89%**（42/47）

**有卡**：`VAELoader`、`CreateVideo`、`UNETLoader`、`CLIPLoader`、`MiniMaxH3MemoryEfficientSageAttentionPatch`、`PathchSageAttentionKJ`、`LoraLoaderModelOnly`、`UpscaleModelLoader`、`BasicScheduler`、`MiniMaxH3Director`、`SaveVideo`、`MiniMaxH3DirectorRefine`、`KSampler`、`CLIPTextEncode`、`solarL_SaveImagesToZip`、`VAEDecode`、`EmptyLatentImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage、UNETLoader

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

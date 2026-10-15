---
key: 图片生成/文生图/wan2.2-14b-4步lora-文生图  ttp放大_1958523002801516545.json
name: wan2.2-14b-4步lora-文生图  ttp放大_1958523002801516545
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/wan2.2-14b-4步lora-文生图  ttp放大_1958523002801516545.json
hash: e7f685dac9cc5297
coverage: 0.928571
learned_at: 2026-10-15 22:27:58
nodes: [CLIPLoader, UNETLoader, UNETLoader, ModelSamplingSD3, MarkdownNote, MarkdownNote, ModelSamplingSD3, VAELoader, EmptyHunyuanLatentVideo, UpscaleImageByUsingModel, UpscaleModelLoader, TTP_Tile_image_size, TTP_Image_Tile_Batch, ImpactImageBatchToImageList, VAEEncode, KSampler, VAEDecode, easy imageListToImageBatch, CLIPTextEncode, VAEDecode, TTP_Image_Assy, KSamplerAdvanced, KSamplerAdvanced, SaveImage, LoraLoaderModelOnly, LoraLoaderModelOnly, CLIPTextEncode, SaveImage]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 12, "denoise": "simple", "sampler_name": 1, "scheduler": "euler", "seed": "disable", "steps": "randomize"}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/wan2.2-14b-4步lora-文生图  ttp放大_1958523002801516545.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/wan2.2-14b-4步lora-文生图  ttp放大_1958523002801516545.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（28 个）：
- `CLIPLoader`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `ModelSamplingSD3`
- `MarkdownNote`
- `MarkdownNote`
- `ModelSamplingSD3`
- `VAELoader`
- `EmptyHunyuanLatentVideo`
- `UpscaleImageByUsingModel`
- `UpscaleModelLoader`
- `TTP_Tile_image_size`
- `TTP_Image_Tile_Batch`
- `ImpactImageBatchToImageList`
- `VAEEncode` ★核心
- `KSampler` ★核心
- `VAEDecode` ★核心
- `easy imageListToImageBatch`
- `CLIPTextEncode` ★核心
- `VAEDecode` ★核心
- `TTP_Image_Assy`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `SaveImage`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `CLIPTextEncode` ★核心
- `SaveImage`

## 关键参数

- `seed` = `disable`
- `steps` = `randomize`
- `cfg` = `12`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **93%**（26/28）

**有卡**：`CLIPLoader`、`UNETLoader`、`ModelSamplingSD3`、`VAELoader`、`EmptyHunyuanLatentVideo`、`UpscaleImageByUsingModel`、`UpscaleModelLoader`、`TTP_Tile_image_size`、`TTP_Image_Tile_Batch`、`ImpactImageBatchToImageList`、`VAEEncode`、`KSampler`、`VAEDecode`、`easy imageListToImageBatch`、`CLIPTextEncode`、`TTP_Image_Assy`、`KSamplerAdvanced`、`SaveImage`、`LoraLoaderModelOnly`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、UNETLoader、KSamplerAdvanced

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

---
key: 图片生成/文生图/Z-Image-BEYOND REALITY SUPER 淡妆浓抹_2029125722060623874.json
name: Z-Image-BEYOND REALITY SUPER 淡妆浓抹_2029125722060623874
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Z-Image-BEYOND REALITY SUPER 淡妆浓抹_2029125722060623874.json
hash: 2e7f9ba0f14caca5
coverage: 0.818182
learned_at: 2026-10-20 23:21:50
nodes: [SaveImage, LoadInvSRModels, InvSRSampler, Image Comparer (rgthree), ZSamplerTurbo //ZImagePowerNodes, HAIGC_SaveImagesToZip, VAEDecode, CLIPLoaderGGUF, ConditioningZeroOut, KSampler, VAELoader, EmptyLatentImage, MarkdownNote, VAEDecode, HAIGC_SaveImagesToZip, CLIPTextEncode, Image Comparer (rgthree), SaveImage, LoadInvSRModels, InvSRSampler, UNETLoader, SaveImage, ModelSamplingAuraFlow, UNETLoader, CLIPLoaderGGUF, VAELoader, EmptyLatentImage, MarkdownNote, CLIPTextEncode, SaveImage, easy promptList, Note, Note]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1472, "sampler_name": "euler", "scheduler": "simple", "seed": 775524044513033, "steps": 9, "width": 1104}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/Z-Image-BEYOND REALITY SUPER 淡妆浓抹_2029125722060623874.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Z-Image-BEYOND REALITY SUPER 淡妆浓抹_2029125722060623874.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（33 个）：
- `SaveImage`
- `LoadInvSRModels`
- `InvSRSampler` ★核心
- `Image Comparer (rgthree)`
- `ZSamplerTurbo //ZImagePowerNodes` ★核心
- `HAIGC_SaveImagesToZip`
- `VAEDecode` ★核心
- `CLIPLoaderGGUF`
- `ConditioningZeroOut`
- `KSampler` ★核心
- `VAELoader`
- `EmptyLatentImage` ★核心
- `MarkdownNote`
- `VAEDecode` ★核心
- `HAIGC_SaveImagesToZip`
- `CLIPTextEncode` ★核心
- `Image Comparer (rgthree)`
- `SaveImage`
- `LoadInvSRModels`
- `InvSRSampler` ★核心
- `UNETLoader` ★核心
- `SaveImage`
- `ModelSamplingAuraFlow`
- `UNETLoader` ★核心
- `CLIPLoaderGGUF`
- `VAELoader`
- `EmptyLatentImage` ★核心
- `MarkdownNote`
- `CLIPTextEncode` ★核心
- `SaveImage`
- `easy promptList`
- `Note`
- `Note`

**识别到的模式**：text_to_image

## 关键参数

- `seed` = `775524044513033`
- `steps` = `9`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `width` = `1104`
- `height` = `1472`
- `batch_size` = `1`

## 知识

覆盖率 **82%**（27/33）

**有卡**：`SaveImage`、`LoadInvSRModels`、`InvSRSampler`、`ZSamplerTurbo //ZImagePowerNodes`、`HAIGC_SaveImagesToZip`、`VAEDecode`、`CLIPLoaderGGUF`、`ConditioningZeroOut`、`KSampler`、`VAELoader`、`EmptyLatentImage`、`CLIPTextEncode`、`UNETLoader`、`ModelSamplingAuraFlow`、`easy promptList`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、ConditioningZeroOut、EmptyLatentImage、UNETLoader、InvSRSampler

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

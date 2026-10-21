---
key: 图片生成/文生图/Z-Image-BEYOND REALITY SUPER-3.0 淡妆浓抹+提示词列表+高清放大_2029081007999164417.json
name: Z-Image-BEYOND REALITY SUPER-3.0 淡妆浓抹+提示词列表+高清放大_2029081007999164417
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Z-Image-BEYOND REALITY SUPER-3.0 淡妆浓抹+提示词列表+高清放大_2029081007999164417.json
hash: 3945e32bdc518b6b
coverage: 0.823529
learned_at: 2026-10-20 23:21:50
nodes: [CLIPLoaderGGUF, KSampler, VAELoader, EmptyLatentImage, MarkdownNote, VAEDecode, HAIGC_SaveImagesToZip, LoadInvSRModels, UNETLoader, InvSRSampler, SaveImage, ConditioningZeroOut, CLIPTextEncode, SaveImage, Image Comparer (rgthree), easy promptList, Note]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1472, "sampler_name": "euler", "scheduler": "simple", "seed": 965507942881950, "steps": 9, "width": 1104}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/Z-Image-BEYOND REALITY SUPER-3.0 淡妆浓抹+提示词列表+高清放大_2029081007999164417.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Z-Image-BEYOND REALITY SUPER-3.0 淡妆浓抹+提示词列表+高清放大_2029081007999164417.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（17 个）：
- `CLIPLoaderGGUF`
- `KSampler` ★核心
- `VAELoader`
- `EmptyLatentImage` ★核心
- `MarkdownNote`
- `VAEDecode` ★核心
- `HAIGC_SaveImagesToZip`
- `LoadInvSRModels`
- `UNETLoader` ★核心
- `InvSRSampler` ★核心
- `SaveImage`
- `ConditioningZeroOut`
- `CLIPTextEncode` ★核心
- `SaveImage`
- `Image Comparer (rgthree)`
- `easy promptList`
- `Note`

**识别到的模式**：text_to_image

## 关键参数

- `seed` = `965507942881950`
- `steps` = `9`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `width` = `1104`
- `height` = `1472`
- `batch_size` = `1`

## 知识

覆盖率 **82%**（14/17）

**有卡**：`CLIPLoaderGGUF`、`KSampler`、`VAELoader`、`EmptyLatentImage`、`VAEDecode`、`HAIGC_SaveImagesToZip`、`LoadInvSRModels`、`UNETLoader`、`InvSRSampler`、`SaveImage`、`ConditioningZeroOut`、`CLIPTextEncode`、`easy promptList`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、ConditioningZeroOut、EmptyLatentImage、UNETLoader、InvSRSampler

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

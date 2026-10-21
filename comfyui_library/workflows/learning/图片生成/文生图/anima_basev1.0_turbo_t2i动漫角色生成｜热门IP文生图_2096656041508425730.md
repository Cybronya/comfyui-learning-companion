---
key: 图片生成/文生图/anima_basev1.0_turbo_t2i动漫角色生成｜热门IP文生图_2096656041508425730.json
name: anima_basev1.0_turbo_t2i动漫角色生成｜热门IP文生图_2096656041508425730
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/anima_basev1.0_turbo_t2i动漫角色生成｜热门IP文生图_2096656041508425730.json
hash: 478379a4b50386e8
coverage: 0.888889
learned_at: 2026-10-20 01:19:37
nodes: [CLIPTextEncode, CLIPLoader, ShowText|pysssss, SDVN Translate, ShowText|pysssss, StringMergeNode, VAEDecode, UNETLoader, CLIPTextEncode, Text Multiline, Text Multiline, FluxKontextImageScale, SaveImage, LatentUpscaleBy, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, KSampler, KSampler, EmptyLatentImage, Text Multiline, SeedGenerator, Text Multiline, VAELoader, 孤海注释, 孤海注释, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, KSampler, CLIPTextEncode, CLIPLoader, CLIPTextEncode, JjkText, EmptyLatentImage, solarL_SaveImagesToZip, VAEDecode, VAELoader, Note]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/anima_basev1.0_turbo_t2i动漫角色生成｜热门IP文生图_2096656041508425730.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/anima_basev1.0_turbo_t2i动漫角色生成｜热门IP文生图_2096656041508425730.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（54 个）：
- `CLIPTextEncode` ★核心
- `CLIPLoader`
- `ShowText|pysssss`
- `SDVN Translate`
- `ShowText|pysssss`
- `StringMergeNode`
- `VAEDecode` ★核心
- `UNETLoader` ★核心
- `CLIPTextEncode` ★核心
- `Text Multiline`
- `Text Multiline`
- `FluxKontextImageScale`
- `SaveImage`
- `LatentUpscaleBy`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `KSampler` ★核心
- `KSampler` ★核心
- `EmptyLatentImage` ★核心
- `Text Multiline`
- `SeedGenerator`
- `Text Multiline`
- `VAELoader`
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

覆盖率 **89%**（48/54）

**有卡**：`CLIPTextEncode`、`CLIPLoader`、`SDVN Translate`、`StringMergeNode`、`VAEDecode`、`UNETLoader`、`Text Multiline`、`FluxKontextImageScale`、`SaveImage`、`LatentUpscaleBy`、`LoraLoaderModelOnly`、`KSampler`、`EmptyLatentImage`、`SeedGenerator`、`VAELoader`、`solarL_SaveImagesToZip`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、CLIPLoader、EmptyLatentImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

---
key: 图片生成/文生图/VividMuse Z-Image-Turbo Dark Dreamcore Style_2060957933088890881.json
name: VividMuse Z-Image-Turbo Dark Dreamcore Style_2060957933088890881
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/VividMuse Z-Image-Turbo Dark Dreamcore Style_2060957933088890881.json
hash: da0d3617f204e67c
coverage: 0.933333
learned_at: 2026-10-19 23:02:49
nodes: [UNETLoader, CLIPLoader, CLIPTextEncode, VAELoader, ConditioningZeroOut, KSampler, VAEDecode, LoraLoaderModelOnly, LoraLoaderModelOnly, EmptyLatentImage, PrimitiveStringMultiline, Seed (rgthree), easy promptList, easy promptList, SaveImage]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 2048, "sampler_name": "euler_ancestral", "scheduler": "sgm_uniform", "seed": 0, "steps": 8, "width": 1536}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/VividMuse Z-Image-Turbo Dark Dreamcore Style_2060957933088890881.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/VividMuse Z-Image-Turbo Dark Dreamcore Style_2060957933088890881.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（15 个）：
- `UNETLoader` ★核心
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `VAELoader`
- `ConditioningZeroOut`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `EmptyLatentImage` ★核心
- `PrimitiveStringMultiline`
- `Seed (rgthree)`
- `easy promptList`
- `easy promptList`
- `SaveImage`

**识别到的模式**：text_to_image

## 关键参数

- `seed` = `0`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler_ancestral`
- `scheduler` = `sgm_uniform`
- `denoise` = `1`
- `width` = `1536`
- `height` = `2048`
- `batch_size` = `1`

## 知识

覆盖率 **93%**（14/15）

**有卡**：`UNETLoader`、`CLIPLoader`、`CLIPTextEncode`、`VAELoader`、`ConditioningZeroOut`、`KSampler`、`VAEDecode`、`LoraLoaderModelOnly`、`EmptyLatentImage`、`Seed (rgthree)`、`easy promptList`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、EmptyLatentImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

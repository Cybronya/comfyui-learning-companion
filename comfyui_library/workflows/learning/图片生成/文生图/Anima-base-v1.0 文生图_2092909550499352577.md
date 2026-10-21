---
key: 图片生成/文生图/Anima-base-v1.0 文生图_2092909550499352577.json
name: Anima-base-v1.0 文生图_2092909550499352577
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Anima-base-v1.0 文生图_2092909550499352577.json
hash: 04b85dfed3d5b42a
coverage: 0.909091
learned_at: 2026-10-20 01:18:43
nodes: [Note, VAELoader, CLIPLoader, KSampler, EmptyLatentImage, VAEDecode, CompressImages, CLIPTextEncode, CLIPTextEncode, UNETLoader, SaveImage]
patterns: [text_to_image]
missing: []
parameters: {"batch_size": 1, "cfg": 4, "denoise": 1, "height": 1536, "sampler_name": "er_sde", "scheduler": "simple", "seed": 980967433821260, "steps": 30, "width": 1152}
---

# 图片生成/文生图/Anima-base-v1.0 文生图_2092909550499352577.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Anima-base-v1.0 文生图_2092909550499352577.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（11 个）：
- `Note`
- `VAELoader`
- `CLIPLoader`
- `KSampler` ★核心
- `EmptyLatentImage` ★核心
- `VAEDecode` ★核心
- `CompressImages`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `UNETLoader` ★核心
- `SaveImage`

**识别到的模式**：text_to_image

## 关键参数

- `seed` = `980967433821260`
- `steps` = `30`
- `cfg` = `4`
- `sampler_name` = `er_sde`
- `scheduler` = `simple`
- `denoise` = `1`
- `width` = `1152`
- `height` = `1536`
- `batch_size` = `1`

## 知识

覆盖率 **91%**（10/11）

**有卡**：`VAELoader`、`CLIPLoader`、`KSampler`、`EmptyLatentImage`、`VAEDecode`、`CompressImages`、`CLIPTextEncode`、`UNETLoader`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、EmptyLatentImage、UNETLoader、SaveImage

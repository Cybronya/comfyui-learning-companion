---
key: 图片生成/文生图/Anima-aesthetic-v1.1 高质量文生图_2092915857054855170.json
name: Anima-aesthetic-v1.1 高质量文生图_2092915857054855170
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Anima-aesthetic-v1.1 高质量文生图_2092915857054855170.json
hash: 6b84630ab12aa200
coverage: 0.909091
learned_at: 2026-10-20 01:18:43
nodes: [VAELoader, CLIPLoader, KSampler, Note, CLIPTextEncode, VAEDecode, SaveImage, CompressImages, CLIPTextEncode, EmptyLatentImage, UNETLoader]
patterns: [text_to_image]
missing: []
parameters: {"batch_size": 1, "cfg": 4, "denoise": 1, "height": 1536, "sampler_name": "euler", "scheduler": "simple", "seed": 980967433821260, "steps": 30, "width": 1152}
---

# 图片生成/文生图/Anima-aesthetic-v1.1 高质量文生图_2092915857054855170.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Anima-aesthetic-v1.1 高质量文生图_2092915857054855170.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（11 个）：
- `VAELoader`
- `CLIPLoader`
- `KSampler` ★核心
- `Note`
- `CLIPTextEncode` ★核心
- `VAEDecode` ★核心
- `SaveImage`
- `CompressImages`
- `CLIPTextEncode` ★核心
- `EmptyLatentImage` ★核心
- `UNETLoader` ★核心

**识别到的模式**：text_to_image

## 关键参数

- `seed` = `980967433821260`
- `steps` = `30`
- `cfg` = `4`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `width` = `1152`
- `height` = `1536`
- `batch_size` = `1`

## 知识

覆盖率 **91%**（10/11）

**有卡**：`VAELoader`、`CLIPLoader`、`KSampler`、`CLIPTextEncode`、`VAEDecode`、`SaveImage`、`CompressImages`、`EmptyLatentImage`、`UNETLoader`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、EmptyLatentImage、UNETLoader、SaveImage

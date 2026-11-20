---
key: 平台全量/Anima-2.9B-preview-v1 文生图_2094062510424018946.json
name: Anima-2.9B-preview-v1 文生图_2094062510424018946
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/平台全量/Anima-2.9B-preview-v1 文生图_2094062510424018946.json
hash: 6ad1a22a3ed52387
coverage: 0.909091
learned_at: 2026-11-14 00:17:49
nodes: [VAELoader, CLIPLoader, EmptyLatentImage, VAEDecode, CLIPTextEncode, UNETLoader, KSampler, SaveImage, CompressImages, CLIPTextEncode, Note]
patterns: [text_to_image]
missing: []
parameters: {"batch_size": 1, "cfg": 4, "denoise": 1, "height": 1536, "sampler_name": "euler", "scheduler": "sgm_uniform", "seed": 980967433821260, "steps": 30, "width": 1152}
---

# 平台全量/Anima-2.9B-preview-v1 文生图_2094062510424018946.json

> 来源文件 `comfyui_library/workflows/平台全量/Anima-2.9B-preview-v1 文生图_2094062510424018946.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（11 个）：
- `VAELoader`
- `CLIPLoader`
- `EmptyLatentImage` ★核心
- `VAEDecode` ★核心
- `CLIPTextEncode` ★核心
- `UNETLoader` ★核心
- `KSampler` ★核心
- `SaveImage`
- `CompressImages`
- `CLIPTextEncode` ★核心
- `Note`

**识别到的模式**：text_to_image

## 关键参数

- `width` = `1152`
- `height` = `1536`
- `batch_size` = `1`
- `seed` = `980967433821260`
- `steps` = `30`
- `cfg` = `4`
- `sampler_name` = `euler`
- `scheduler` = `sgm_uniform`
- `denoise` = `1`

## 知识

覆盖率 **91%**（10/11）

**有卡**：`VAELoader`、`CLIPLoader`、`EmptyLatentImage`、`VAEDecode`、`CLIPTextEncode`、`UNETLoader`、`KSampler`、`SaveImage`、`CompressImages`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPLoader、CLIPTextEncode、EmptyLatentImage、UNETLoader、SaveImage

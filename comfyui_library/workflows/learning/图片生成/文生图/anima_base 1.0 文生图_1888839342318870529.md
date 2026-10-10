---
key: 图片生成/文生图/anima_base 1.0 文生图_1888839342318870529.json
name: anima_base 1.0 文生图_1888839342318870529
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/anima_base 1.0 文生图_1888839342318870529.json
hash: de7acd811fc92867
coverage: 0.875
learned_at: 2026-10-10 23:16:30
nodes: [CLIPLoader, UNETLoader, VAELoader, CLIPTextEncode, VAEDecode, KSampler, Int, KSampler, SaveImage, VAEDecode, SaveImage, RH_Translator, CLIPTextEncode, CR Text Concatenate, JjkText, EmptyLatentImage]
patterns: [text_to_image]
missing: [CR Text Concatenate]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 2048, "sampler_name": "er_sde", "scheduler": "beta", "seed": 662663757313191, "steps": 40, "width": 1024}
discoveries: [次要节点 `CR Text Concatenate` 知识库中没有该节点类型的任何知识]
---

# 图片生成/文生图/anima_base 1.0 文生图_1888839342318870529.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/anima_base 1.0 文生图_1888839342318870529.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（16 个）：
- `CLIPLoader`
- `UNETLoader` ★核心
- `VAELoader`
- `CLIPTextEncode` ★核心
- `VAEDecode` ★核心
- `KSampler` ★核心
- `Int`
- `KSampler` ★核心
- `SaveImage`
- `VAEDecode` ★核心
- `SaveImage`
- `RH_Translator`
- `CLIPTextEncode` ★核心
- `CR Text Concatenate`
- `JjkText`
- `EmptyLatentImage` ★核心

**识别到的模式**：text_to_image

## 关键参数

- `seed` = `662663757313191`
- `steps` = `40`
- `cfg` = `4.5`
- `sampler_name` = `er_sde`
- `scheduler` = `beta`
- `denoise` = `1`
- `width` = `1024`
- `height` = `2048`
- `batch_size` = `1`

## 知识

覆盖率 **88%**（14/16）

**有卡**：`CLIPLoader`、`UNETLoader`、`VAELoader`、`CLIPTextEncode`、`VAEDecode`、`KSampler`、`Int`、`SaveImage`、`RH_Translator`、`EmptyLatentImage`

**缺卡**（1）：`CR Text Concatenate`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、EmptyLatentImage、UNETLoader、SaveImage

## 学习发现

- 次要节点 `CR Text Concatenate` 知识库中没有该节点类型的任何知识

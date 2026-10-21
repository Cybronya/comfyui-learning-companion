---
key: 图片生成/文生图/N-Super Z-image 3.0+lota文生图_2020339880995332097.json
name: N-Super Z-image 3.0+lota文生图_2020339880995332097
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/N-Super Z-image 3.0+lota文生图_2020339880995332097.json
hash: 01e298e42dd442ce
coverage: 0.785714
learned_at: 2026-10-19 22:29:45
nodes: [VAELoader, PrimitiveNode, CLIPLoader, EmptyLatentImage, PrimitiveInt, PrimitiveInt, UNETLoader, LoraLoaderModelOnly, KSampler, CLIPTextEncode, SaveImage, VAEDecode, CLIPTextEncode, DuckHideNode]
patterns: [text_to_image]
missing: []
parameters: {"batch_size": 1, "cfg": 2, "denoise": 1, "height": 1920, "sampler_name": "euler", "scheduler": "simple", "seed": 1090310580870859, "steps": 12, "width": 1080}
---

# 图片生成/文生图/N-Super Z-image 3.0+lota文生图_2020339880995332097.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/N-Super Z-image 3.0+lota文生图_2020339880995332097.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（14 个）：
- `VAELoader`
- `PrimitiveNode`
- `CLIPLoader`
- `EmptyLatentImage` ★核心
- `PrimitiveInt`
- `PrimitiveInt`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `KSampler` ★核心
- `CLIPTextEncode` ★核心
- `SaveImage`
- `VAEDecode` ★核心
- `CLIPTextEncode` ★核心
- `DuckHideNode`

**识别到的模式**：text_to_image

## 关键参数

- `width` = `1080`
- `height` = `1920`
- `batch_size` = `1`
- `seed` = `1090310580870859`
- `steps` = `12`
- `cfg` = `2`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **79%**（11/14）

**有卡**：`VAELoader`、`CLIPLoader`、`EmptyLatentImage`、`UNETLoader`、`LoraLoaderModelOnly`、`KSampler`、`CLIPTextEncode`、`SaveImage`、`VAEDecode`、`DuckHideNode`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage、UNETLoader

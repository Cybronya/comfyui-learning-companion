---
key: 图片生成/文生图/图图的维琳娜·艾嘉德ANIMA专属工作流_Tutu's Velina Airgid Anima_2068357227324469249.json
name: 图图的维琳娜·艾嘉德ANIMA专属工作流_Tutu's Velina Airgid Anima_2068357227324469249
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/图图的维琳娜·艾嘉德ANIMA专属工作流_Tutu's Velina Airgid Anima_2068357227324469249.json
hash: b9d9f5838e7ce8da
coverage: 0.909091
learned_at: 2026-10-19 23:22:59
nodes: [CLIPLoader, VAELoader, CLIPTextEncode, VAEDecode, KSampler, EmptyLatentImage, SaveImage, CLIPTextEncode, UNETLoader, LoraLoaderModelOnly, Note]
patterns: [text_to_image]
missing: []
parameters: {"batch_size": 1, "cfg": 4, "denoise": 1, "height": 1520, "sampler_name": "er_sde", "scheduler": "simple", "seed": 438863594007122, "steps": 45, "width": 1024}
---

# 图片生成/文生图/图图的维琳娜·艾嘉德ANIMA专属工作流_Tutu's Velina Airgid Anima_2068357227324469249.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/图图的维琳娜·艾嘉德ANIMA专属工作流_Tutu's Velina Airgid Anima_2068357227324469249.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（11 个）：
- `CLIPLoader`
- `VAELoader`
- `CLIPTextEncode` ★核心
- `VAEDecode` ★核心
- `KSampler` ★核心
- `EmptyLatentImage` ★核心
- `SaveImage`
- `CLIPTextEncode` ★核心
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `Note`

**识别到的模式**：text_to_image

## 关键参数

- `seed` = `438863594007122`
- `steps` = `45`
- `cfg` = `4`
- `sampler_name` = `er_sde`
- `scheduler` = `simple`
- `denoise` = `1`
- `width` = `1024`
- `height` = `1520`
- `batch_size` = `1`

## 知识

覆盖率 **91%**（10/11）

**有卡**：`CLIPLoader`、`VAELoader`、`CLIPTextEncode`、`VAEDecode`、`KSampler`、`EmptyLatentImage`、`SaveImage`、`UNETLoader`、`LoraLoaderModelOnly`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage、UNETLoader

---
key: 图片生成/文生图/miaomiao RealSkin Anima 1.0 文生图_2114597001806569473.json
name: miaomiao RealSkin Anima 1.0 文生图_2114597001806569473
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/miaomiao RealSkin Anima 1.0 文生图_2114597001806569473.json
hash: 5e1d3f87fec030ab
coverage: 1
learned_at: 2026-10-26 22:09:04
nodes: [UNETLoader, CLIPTextEncode, CLIPTextEncode, CLIPLoader, VAELoader, KSampler, EmptyLatentImage, SaveImage, VAEDecode]
patterns: [text_to_image]
missing: []
parameters: {"batch_size": 1, "cfg": 5, "denoise": 1, "height": 1920, "sampler_name": "euler", "scheduler": "simple", "seed": 917845934816615, "steps": 30, "width": 1080}
---

# 图片生成/文生图/miaomiao RealSkin Anima 1.0 文生图_2114597001806569473.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/miaomiao RealSkin Anima 1.0 文生图_2114597001806569473.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output

**节点**（9 个）：
- `UNETLoader` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `CLIPLoader`
- `VAELoader`
- `KSampler` ★核心
- `EmptyLatentImage` ★核心
- `SaveImage`
- `VAEDecode` ★核心

**识别到的模式**：text_to_image

## 关键参数

- `seed` = `917845934816615`
- `steps` = `30`
- `cfg` = `5`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `width` = `1080`
- `height` = `1920`
- `batch_size` = `1`

## 知识

覆盖率 **100%**（9/9）

**有卡**：`UNETLoader`、`CLIPTextEncode`、`CLIPLoader`、`VAELoader`、`KSampler`、`EmptyLatentImage`、`SaveImage`、`VAEDecode`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、EmptyLatentImage、UNETLoader、SaveImage

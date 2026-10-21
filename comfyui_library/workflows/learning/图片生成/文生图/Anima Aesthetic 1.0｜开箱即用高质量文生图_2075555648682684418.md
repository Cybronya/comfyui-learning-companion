---
key: 图片生成/文生图/Anima Aesthetic 1.0｜开箱即用高质量文生图_2075555648682684418.json
name: Anima Aesthetic 1.0｜开箱即用高质量文生图_2075555648682684418
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Anima Aesthetic 1.0｜开箱即用高质量文生图_2075555648682684418.json
hash: 6865ec10f8526f48
coverage: 0.9
learned_at: 2026-10-20 00:18:44
nodes: [MarkdownNote, CLIPLoader, CLIPTextEncode, EmptyLatentImage, KSampler, VAEDecode, SaveImage, CLIPTextEncode, UNETLoader, VAELoader]
patterns: [text_to_image]
missing: []
parameters: {"batch_size": 1, "cfg": 4, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 875817230929465, "steps": 40, "width": 1024}
---

# 图片生成/文生图/Anima Aesthetic 1.0｜开箱即用高质量文生图_2075555648682684418.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Anima Aesthetic 1.0｜开箱即用高质量文生图_2075555648682684418.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（10 个）：
- `MarkdownNote`
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `EmptyLatentImage` ★核心
- `KSampler` ★核心
- `VAEDecode` ★核心
- `SaveImage`
- `CLIPTextEncode` ★核心
- `UNETLoader` ★核心
- `VAELoader`

**识别到的模式**：text_to_image

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`
- `seed` = `875817230929465`
- `steps` = `40`
- `cfg` = `4`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **90%**（9/10）

**有卡**：`CLIPLoader`、`CLIPTextEncode`、`EmptyLatentImage`、`KSampler`、`VAEDecode`、`SaveImage`、`UNETLoader`、`VAELoader`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、EmptyLatentImage、UNETLoader、SaveImage

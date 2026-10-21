---
key: 图片生成/文生图/Anima Aesthetic 1.0b｜纯审美微调文生图_2075555639908196353.json
name: Anima Aesthetic 1.0b｜纯审美微调文生图_2075555639908196353
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Anima Aesthetic 1.0b｜纯审美微调文生图_2075555639908196353.json
hash: 95898d40ad96caec
coverage: 0.9
learned_at: 2026-10-20 00:18:43
nodes: [MarkdownNote, CLIPLoader, VAELoader, CLIPTextEncode, CLIPTextEncode, EmptyLatentImage, KSampler, VAEDecode, SaveImage, UNETLoader]
patterns: [text_to_image]
missing: []
parameters: {"batch_size": 1, "cfg": 4, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 875817230929465, "steps": 40, "width": 1024}
---

# 图片生成/文生图/Anima Aesthetic 1.0b｜纯审美微调文生图_2075555639908196353.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Anima Aesthetic 1.0b｜纯审美微调文生图_2075555639908196353.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（10 个）：
- `MarkdownNote`
- `CLIPLoader`
- `VAELoader`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `EmptyLatentImage` ★核心
- `KSampler` ★核心
- `VAEDecode` ★核心
- `SaveImage`
- `UNETLoader` ★核心

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

**有卡**：`CLIPLoader`、`VAELoader`、`CLIPTextEncode`、`EmptyLatentImage`、`KSampler`、`VAEDecode`、`SaveImage`、`UNETLoader`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、EmptyLatentImage、UNETLoader、SaveImage

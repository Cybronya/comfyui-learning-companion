---
key: Flux.1-Krea-Dev文生图-无AI味逼真质感_1951288817326215170.json
name: Flux.1-Krea-Dev文生图-无AI味逼真质感_1951288817326215170
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Flux.1-Krea-Dev文生图-无AI味逼真质感_1951288817326215170.json
hash: b824c342d2d9a0b1
coverage: 1
learned_at: 2026-10-10 20:58:36
nodes: [ConditioningZeroOut, VAEDecode, VAELoader, UNETLoader, DualCLIPLoader, EmptyLatentImage, KSampler, SaveImage, CLIPTextEncode]
patterns: [text_to_image]
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1280, "sampler_name": "euler", "scheduler": "simple", "seed": 156098985751864, "steps": 20, "width": 1024}
---

# Flux.1-Krea-Dev文生图-无AI味逼真质感_1951288817326215170.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Flux.1-Krea-Dev文生图-无AI味逼真质感_1951288817326215170.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output

**节点**（9 个）：
- `ConditioningZeroOut`
- `VAEDecode` ★核心
- `VAELoader`
- `UNETLoader` ★核心
- `DualCLIPLoader`
- `EmptyLatentImage` ★核心
- `KSampler` ★核心
- `SaveImage`
- `CLIPTextEncode` ★核心

**识别到的模式**：text_to_image

## 关键参数

- `width` = `1024`
- `height` = `1280`
- `batch_size` = `1`
- `seed` = `156098985751864`
- `steps` = `20`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **100%**（9/9）

**有卡**：`ConditioningZeroOut`、`VAEDecode`、`VAELoader`、`UNETLoader`、`DualCLIPLoader`、`EmptyLatentImage`、`KSampler`、`SaveImage`、`CLIPTextEncode`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、ConditioningZeroOut、EmptyLatentImage、UNETLoader、SaveImage

---
key: 图片生成/文生图/SD1.5 XL 文生图学习基础工作流 （用于学习）_2054889952957214721.json
name: SD1.5 XL 文生图学习基础工作流 （用于学习）_2054889952957214721
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/SD1.5 XL 文生图学习基础工作流 （用于学习）_2054889952957214721.json
hash: 082c8c28be79588a
coverage: 0.913043
learned_at: 2026-10-21 02:54:59
nodes: [VAEDecode, SaveImage, Note, EmptyLatentImage, CLIPSetLastLayer, CLIPTextEncode, CLIPTextEncode, KSampler, SaveImage, VAEDecode, SDXLEmptyLatentSizePicker+, KSampler, SDXL Empty Latent Image (rgthree), EmptyLatentImage, CLIPTextEncode, CLIPTextEncode, easy a1111Loader, KSampler, Fast Groups Bypasser (rgthree), LoadImage, LoadImage, CheckpointLoaderSimple, CheckpointLoaderSimple]
patterns: [text_to_image]
missing: []
parameters: {"batch_size": 1, "cfg": 8, "checkpoint": "RunDiffusionJuggernaut-XL-v9.safetensors", "denoise": 1, "height": 1024, "sampler_name": "dpmpp_2m", "scheduler": "karras", "seed": 562685631352472, "steps": 30, "width": 768}
---

# 图片生成/文生图/SD1.5 XL 文生图学习基础工作流 （用于学习）_2054889952957214721.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/SD1.5 XL 文生图学习基础工作流 （用于学习）_2054889952957214721.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（23 个）：
- `VAEDecode` ★核心
- `SaveImage`
- `Note`
- `EmptyLatentImage` ★核心
- `CLIPSetLastLayer`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `KSampler` ★核心
- `SaveImage`
- `VAEDecode` ★核心
- `SDXLEmptyLatentSizePicker+` ★核心
- `KSampler` ★核心
- `SDXL Empty Latent Image (rgthree)`
- `EmptyLatentImage` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `easy a1111Loader`
- `KSampler` ★核心
- `Fast Groups Bypasser (rgthree)`
- `LoadImage`
- `LoadImage`
- `CheckpointLoaderSimple` ★核心
- `CheckpointLoaderSimple` ★核心

**识别到的模式**：text_to_image

## 关键参数

- `width` = `768`
- `height` = `1024`
- `batch_size` = `1`
- `seed` = `562685631352472`
- `steps` = `30`
- `cfg` = `8`
- `sampler_name` = `dpmpp_2m`
- `scheduler` = `karras`
- `denoise` = `1`
- `checkpoint` = `RunDiffusionJuggernaut-XL-v9.safetensors`

## 知识

覆盖率 **91%**（21/23）

**有卡**：`VAEDecode`、`SaveImage`、`EmptyLatentImage`、`CLIPSetLastLayer`、`CLIPTextEncode`、`KSampler`、`SDXLEmptyLatentSizePicker+`、`SDXL Empty Latent Image (rgthree)`、`easy a1111Loader`、`LoadImage`、`CheckpointLoaderSimple`

**用到的条目**：KSampler、VAEDecode、CheckpointLoaderSimple、CLIPTextEncode、EmptyLatentImage、LoadImage、SDXL Empty Latent Image (rgthree)、SDXLEmptyLatentSizePicker+

---
key: 图片生成/图生图/Qwen-Image-2.1 一键扩图 图生图_2116857605678260225.json
name: Qwen-Image-2.1 一键扩图 图生图_2116857605678260225
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen-Image-2.1 一键扩图 图生图_2116857605678260225.json
hash: 2165c00d76c75449
coverage: 0.875
learned_at: 2026-11-02 19:12:51
nodes: [CLIPLoader, CLIPLoader, BatchImagesNode, EmptyLatentImage, ComfySwitchNode, VAEDecode, KSampler, QwenImage21Cache, TextGenerateLTX2Prompt, TextEncodeQwenImage21, UNETLoader, VAELoader, SaveImage, ResolutionSelector, JjkText, LoadImage]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 934017569869526, "steps": 50, "width": 1024}
---

# 图片生成/图生图/Qwen-Image-2.1 一键扩图 图生图_2116857605678260225.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen-Image-2.1 一键扩图 图生图_2116857605678260225.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（16 个）：
- `CLIPLoader`
- `CLIPLoader`
- `BatchImagesNode`
- `EmptyLatentImage` ★核心
- `ComfySwitchNode`
- `VAEDecode` ★核心
- `KSampler` ★核心
- `QwenImage21Cache`
- `TextGenerateLTX2Prompt`
- `TextEncodeQwenImage21`
- `UNETLoader` ★核心
- `VAELoader`
- `SaveImage`
- `ResolutionSelector`
- `JjkText`
- `LoadImage`

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`
- `seed` = `934017569869526`
- `steps` = `50`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **88%**（14/16）

**有卡**：`CLIPLoader`、`BatchImagesNode`、`EmptyLatentImage`、`VAEDecode`、`KSampler`、`QwenImage21Cache`、`TextGenerateLTX2Prompt`、`TextEncodeQwenImage21`、`UNETLoader`、`VAELoader`、`SaveImage`、`ResolutionSelector`、`LoadImage`

**用到的条目**：KSampler、TextEncodeQwenImage21、VAEDecode、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、LoadImage

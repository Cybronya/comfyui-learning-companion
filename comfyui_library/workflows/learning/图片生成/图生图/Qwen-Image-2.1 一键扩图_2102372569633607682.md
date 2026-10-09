---
key: 图片生成/图生图/Qwen-Image-2.1 一键扩图_2102372569633607682.json
name: Qwen-Image-2.1 一键扩图_2102372569633607682.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen-Image-2.1 一键扩图_2102372569633607682.json
hash: 28fc287377719abd
coverage: 0.875
learned_at: 2026-10-09 22:27:12
nodes: [KSampler, QwenImage21Cache, TextEncodeQwenImage21, SaveImage, UNETLoader, CLIPLoader, CLIPLoader, VAELoader, EmptyLatentImage, TextGenerateLTX2Prompt, ResolutionSelector, JjkText, LoadImage, BatchImagesNode, ComfySwitchNode, VAEDecode]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 851091223269555, "steps": 50, "width": 1024}
---

# 图片生成/图生图/Qwen-Image-2.1 一键扩图_2102372569633607682.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/2102372569633607682.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（16 个）：
- `KSampler` ★核心
- `QwenImage21Cache`
- `TextEncodeQwenImage21`
- `SaveImage`
- `UNETLoader` ★核心
- `CLIPLoader`
- `CLIPLoader`
- `VAELoader`
- `EmptyLatentImage` ★核心
- `TextGenerateLTX2Prompt`
- `ResolutionSelector`
- `JjkText`
- `LoadImage`
- `BatchImagesNode`
- `ComfySwitchNode`
- `VAEDecode` ★核心

## 关键参数

- `seed` = `851091223269555`
- `steps` = `50`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`

## 知识

覆盖率 **88%**（14/16）

**有卡**：`KSampler`、`QwenImage21Cache`、`TextEncodeQwenImage21`、`SaveImage`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`EmptyLatentImage`、`TextGenerateLTX2Prompt`、`ResolutionSelector`、`LoadImage`、`BatchImagesNode`、`VAEDecode`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、LoadImage

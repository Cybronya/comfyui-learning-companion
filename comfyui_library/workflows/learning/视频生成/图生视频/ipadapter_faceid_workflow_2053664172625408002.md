---
key: 视频生成/图生视频/ipadapter_faceid_workflow_2053664172625408002.json
name: ipadapter_faceid_workflow_2053664172625408002.json
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2053664172625408002.json
hash: f30949f1f0a18a70
coverage: 1
learned_at: 2026-10-15 22:37:41
nodes: [CheckpointLoaderSimple, IPAdapterUnifiedLoader, LoadImage, IPAdapterAdvanced, CLIPTextEncode, CLIPTextEncode, EmptyLatentImage, KSampler, VAEDecode, SaveImage]
patterns: [text_to_image]
missing: []
parameters: {"batch_size": 1, "cfg": 7, "checkpoint": "RealVisXL_V4.0.safetensors", "denoise": 1, "height": 720, "sampler_name": "euler", "scheduler": "normal", "seed": 42, "steps": 25, "width": 1280}
---

# 视频生成/图生视频/ipadapter_faceid_workflow_2053664172625408002.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2053664172625408002.json`

## 结构

**生成流程**：Model → Condition → Latent → Control → Sampling → Decode → Output → Other

**节点**（10 个）：
- `CheckpointLoaderSimple` ★核心
- `IPAdapterUnifiedLoader`
- `LoadImage`
- `IPAdapterAdvanced`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `EmptyLatentImage` ★核心
- `KSampler` ★核心
- `VAEDecode` ★核心
- `SaveImage`

**识别到的模式**：text_to_image

## 关键参数

- `checkpoint` = `RealVisXL_V4.0.safetensors`
- `width` = `1280`
- `height` = `720`
- `batch_size` = `1`
- `seed` = `42`
- `steps` = `25`
- `cfg` = `7`
- `sampler_name` = `euler`
- `scheduler` = `normal`
- `denoise` = `1`

## 知识

覆盖率 **100%**（10/10）

**有卡**：`CheckpointLoaderSimple`、`IPAdapterUnifiedLoader`、`LoadImage`、`IPAdapterAdvanced`、`CLIPTextEncode`、`EmptyLatentImage`、`KSampler`、`VAEDecode`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、CheckpointLoaderSimple、CLIPTextEncode、EmptyLatentImage、LoadImage、IPAdapterAdvanced、IPAdapterUnifiedLoader

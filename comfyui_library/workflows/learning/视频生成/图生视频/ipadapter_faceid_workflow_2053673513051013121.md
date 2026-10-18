---
key: 视频生成/图生视频/ipadapter_faceid_workflow_2053673513051013121.json
name: ipadapter_faceid_workflow_2053673513051013121.json
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/ipadapter_faceid_workflow_2053673513051013121.json
hash: bbf77de634d7c588
coverage: 1
learned_at: 2026-10-15 22:37:42
nodes: [EmptyLatentImage, IPAdapterUnifiedLoader, IPAdapterAdvanced, CLIPTextEncode, CLIPTextEncode, SaveImage, VAEDecode, KSampler, CheckpointLoaderSimple, LoadImage]
patterns: [text_to_image]
missing: []
parameters: {"batch_size": 1, "cfg": 7, "checkpoint": "epicrealism_pureEvolutionV5-inpainting.safetensors", "denoise": 1, "height": 720, "sampler_name": "euler", "scheduler": "normal", "seed": 42, "steps": 25, "width": 1280}
---

# 视频生成/图生视频/ipadapter_faceid_workflow_2053673513051013121.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2053673513051013121.json`

## 结构

**生成流程**：Model → Condition → Latent → Control → Sampling → Decode → Output → Other

**节点**（10 个）：
- `EmptyLatentImage` ★核心
- `IPAdapterUnifiedLoader`
- `IPAdapterAdvanced`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `SaveImage`
- `VAEDecode` ★核心
- `KSampler` ★核心
- `CheckpointLoaderSimple` ★核心
- `LoadImage`

**识别到的模式**：text_to_image

## 关键参数

- `width` = `1280`
- `height` = `720`
- `batch_size` = `1`
- `seed` = `42`
- `steps` = `25`
- `cfg` = `7`
- `sampler_name` = `euler`
- `scheduler` = `normal`
- `denoise` = `1`
- `checkpoint` = `epicrealism_pureEvolutionV5-inpainting.safetensors`

## 知识

覆盖率 **100%**（10/10）

**有卡**：`EmptyLatentImage`、`IPAdapterUnifiedLoader`、`IPAdapterAdvanced`、`CLIPTextEncode`、`SaveImage`、`VAEDecode`、`KSampler`、`CheckpointLoaderSimple`、`LoadImage`

**用到的条目**：KSampler、VAEDecode、CheckpointLoaderSimple、CLIPTextEncode、EmptyLatentImage、LoadImage、IPAdapterAdvanced、IPAdapterUnifiedLoader

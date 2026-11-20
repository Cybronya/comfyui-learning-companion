---
key: 平台全量/Workflow 18 (Silhouette- Juggernaut XI)_1867466563682271234.json
name: Workflow 18 (Silhouette- Juggernaut XI)_1867466563682271234
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/平台全量/Workflow 18 (Silhouette- Juggernaut XI)_1867466563682271234.json
hash: 5294d08f006a203a
coverage: 0.9
learned_at: 2026-11-14 01:07:30
nodes: [CheckpointLoaderSimple, EmptyLatentImage, VAELoader, CLIPSetLastLayer, CLIPTextEncode, KSampler, CLIPTextEncode, SaveImage, VAEDecode, PreviewImage]
patterns: [text_to_image]
missing: []
parameters: {"batch_size": 4, "cfg": 5.5, "checkpoint": "juggernautXL_v9Rdphoto2Lightning.safetensors", "denoise": 1, "height": 1024, "sampler_name": "dpmpp_2m", "scheduler": "normal", "seed": 695550282377772, "steps": 30, "width": 1024}
---

# 平台全量/Workflow 18 (Silhouette- Juggernaut XI)_1867466563682271234.json

> 来源文件 `comfyui_library/workflows/平台全量/Workflow 18 (Silhouette- Juggernaut XI)_1867466563682271234.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（10 个）：
- `CheckpointLoaderSimple` ★核心
- `EmptyLatentImage` ★核心
- `VAELoader`
- `CLIPSetLastLayer`
- `CLIPTextEncode` ★核心
- `KSampler` ★核心
- `CLIPTextEncode` ★核心
- `SaveImage`
- `VAEDecode` ★核心
- `PreviewImage`

**识别到的模式**：text_to_image

## 关键参数

- `checkpoint` = `juggernautXL_v9Rdphoto2Lightning.safetensors`
- `width` = `1024`
- `height` = `1024`
- `batch_size` = `4`
- `seed` = `695550282377772`
- `steps` = `30`
- `cfg` = `5.5`
- `sampler_name` = `dpmpp_2m`
- `scheduler` = `normal`
- `denoise` = `1`

## 知识

覆盖率 **90%**（9/10）

**有卡**：`CheckpointLoaderSimple`、`EmptyLatentImage`、`VAELoader`、`CLIPSetLastLayer`、`CLIPTextEncode`、`KSampler`、`SaveImage`、`VAEDecode`

**用到的条目**：KSampler、VAEDecode、VAELoader、CheckpointLoaderSimple、CLIPTextEncode、EmptyLatentImage、CLIPSetLastLayer、SaveImage

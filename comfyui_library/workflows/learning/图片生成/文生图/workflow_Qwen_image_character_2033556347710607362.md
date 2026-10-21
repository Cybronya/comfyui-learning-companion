---
key: 图片生成/文生图/workflow_Qwen_image_character_2033556347710607362.json
name: workflow_Qwen_image_character_2033556347710607362
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/workflow_Qwen_image_character_2033556347710607362.json
hash: 946a24a0b9907515
coverage: 0.888889
learned_at: 2026-10-21 02:57:41
nodes: [CheckpointLoaderSimple, VAELoader, CLIPTextEncode, CLIPTextEncode, EmptyLatentImage, KSampler, VAEDecode, Note, SaveImage]
patterns: [text_to_image]
missing: []
parameters: {"batch_size": 4, "cfg": 6, "checkpoint": "Dream Anime XL _ 筑梦动漫XL_v3.0 - 心动信号.safetensors", "denoise": 1, "height": 1152, "sampler_name": "euler_ancestral", "scheduler": "karras", "seed": 20260314, "steps": 28, "width": 896}
---

# 图片生成/文生图/workflow_Qwen_image_character_2033556347710607362.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/workflow_Qwen_image_character_2033556347710607362.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（9 个）：
- `CheckpointLoaderSimple` ★核心
- `VAELoader`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `EmptyLatentImage` ★核心
- `KSampler` ★核心
- `VAEDecode` ★核心
- `Note`
- `SaveImage`

**识别到的模式**：text_to_image

## 关键参数

- `checkpoint` = `Dream Anime XL _ 筑梦动漫XL_v3.0 - 心动信号.safetensors`
- `width` = `896`
- `height` = `1152`
- `batch_size` = `4`
- `seed` = `20260314`
- `steps` = `28`
- `cfg` = `6`
- `sampler_name` = `euler_ancestral`
- `scheduler` = `karras`
- `denoise` = `1`

## 知识

覆盖率 **89%**（8/9）

**有卡**：`CheckpointLoaderSimple`、`VAELoader`、`CLIPTextEncode`、`EmptyLatentImage`、`KSampler`、`VAEDecode`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、CheckpointLoaderSimple、CLIPTextEncode、EmptyLatentImage、SaveImage、sd15-t2i-basic

---
key: 图片生成/图生图/SDXL4.0_2095753350984851457.json
name: SDXL4.0_2095753350984851457
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/SDXL4.0_2095753350984851457.json
hash: 81575b6210226665
coverage: 1
learned_at: 2026-10-21 00:44:16
nodes: [CLIPTextEncode, CLIPTextEncode, VAEEncode, VAEDecode, SaveImage, LoadImage, LayerUtility: ImageScaleByAspectRatio V2, KSampler, CheckpointLoaderSimple]
patterns: [image_to_image]
missing: []
parameters: {"cfg": 7, "checkpoint": "真境写真XL Apex _ 商业电商摄影真实写实大师_真境写真XL_v4.safetensors", "denoise": 0.20000000000000004, "sampler_name": "euler_ancestral", "scheduler": "normal", "seed": 15485491666254, "steps": 18}
---

# 图片生成/图生图/SDXL4.0_2095753350984851457.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/SDXL4.0_2095753350984851457.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（9 个）：
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `VAEEncode` ★核心
- `VAEDecode` ★核心
- `SaveImage`
- `LoadImage`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `KSampler` ★核心
- `CheckpointLoaderSimple` ★核心

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `15485491666254`
- `steps` = `18`
- `cfg` = `7`
- `sampler_name` = `euler_ancestral`
- `scheduler` = `normal`
- `denoise` = `0.20000000000000004`
- `checkpoint` = `真境写真XL Apex _ 商业电商摄影真实写实大师_真境写真XL_v4.safetensors`

## 知识

覆盖率 **100%**（9/9）

**有卡**：`CLIPTextEncode`、`VAEEncode`、`VAEDecode`、`SaveImage`、`LoadImage`、`LayerUtility: ImageScaleByAspectRatio V2`、`KSampler`、`CheckpointLoaderSimple`

**用到的条目**：KSampler、VAEDecode、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、VAEEncode、SaveImage、LayerUtility: ImageScaleByAspectRatio V2

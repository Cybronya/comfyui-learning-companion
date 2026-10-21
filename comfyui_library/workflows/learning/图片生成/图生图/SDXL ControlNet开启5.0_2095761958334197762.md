---
key: 图片生成/图生图/SDXL ControlNet开启5.0_2095761958334197762.json
name: SDXL ControlNet开启5.0_2095761958334197762
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/SDXL ControlNet开启5.0_2095761958334197762.json
hash: 5c92495861cf8c9f
coverage: 1
learned_at: 2026-10-21 00:44:16
nodes: [CLIPTextEncode, CLIPTextEncode, VAEEncode, AIO_Preprocessor, ControlNetApplySD3, ControlNetLoader, VAEDecode, SaveImage, LoadImage, LayerUtility: ImageScaleByAspectRatio V2, KSampler, CheckpointLoaderSimple]
patterns: [image_to_image]
missing: []
parameters: {"cfg": 7, "checkpoint": "真境写真XL Apex _ 商业电商摄影真实写实大师_真境写真XL_v4.safetensors", "controlnet_strength": 1, "denoise": 0.20000000000000004, "sampler_name": "euler_ancestral", "scheduler": "normal", "seed": 820590104518009, "steps": 18}
---

# 图片生成/图生图/SDXL ControlNet开启5.0_2095761958334197762.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/SDXL ControlNet开启5.0_2095761958334197762.json`

## 结构

**生成流程**：Model → Encode → Condition → Control → Sampling → Decode → Process → Output → Other

**节点**（12 个）：
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `VAEEncode` ★核心
- `AIO_Preprocessor`
- `ControlNetApplySD3` ★核心
- `ControlNetLoader`
- `VAEDecode` ★核心
- `SaveImage`
- `LoadImage`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `KSampler` ★核心
- `CheckpointLoaderSimple` ★核心

**识别到的模式**：image_to_image

## 关键参数

- `controlnet_strength` = `1`
- `seed` = `820590104518009`
- `steps` = `18`
- `cfg` = `7`
- `sampler_name` = `euler_ancestral`
- `scheduler` = `normal`
- `denoise` = `0.20000000000000004`
- `checkpoint` = `真境写真XL Apex _ 商业电商摄影真实写实大师_真境写真XL_v4.safetensors`

## 知识

覆盖率 **100%**（12/12）

**有卡**：`CLIPTextEncode`、`VAEEncode`、`AIO_Preprocessor`、`ControlNetApplySD3`、`ControlNetLoader`、`VAEDecode`、`SaveImage`、`LoadImage`、`LayerUtility: ImageScaleByAspectRatio V2`、`KSampler`、`CheckpointLoaderSimple`

**用到的条目**：KSampler、VAEDecode、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、ControlNetLoader、ControlNetApplySD3、VAEEncode

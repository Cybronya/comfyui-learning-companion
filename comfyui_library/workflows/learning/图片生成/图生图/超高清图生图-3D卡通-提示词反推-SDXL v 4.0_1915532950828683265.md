---
key: 图片生成/图生图/超高清图生图-3D卡通-提示词反推-SDXL v 4.0_1915532950828683265.json
name: 超高清图生图-3D卡通-提示词反推-SDXL v 4.0_1915532950828683265
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/超高清图生图-3D卡通-提示词反推-SDXL v 4.0_1915532950828683265.json
hash: c8660ac8536e42fa
coverage: 0.916667
learned_at: 2026-10-23 13:29:53
nodes: [SaveImage, VAEDecode, RH_Captioner, CR Text Concatenate, DF_Text_Box, KSampler, VAEEncode, CLIPTextEncode, CLIPTextEncode, CheckpointLoaderSimple, ShowText|pysssss, LoadImage]
patterns: [image_to_image]
missing: []
parameters: {"cfg": 8, "checkpoint": "samaritan3dCartoon_v40SDXL.safetensors", "denoise": 0.44, "sampler_name": "euler_ancestral", "scheduler": "normal", "seed": 922997381794256, "steps": 20}
---

# 图片生成/图生图/超高清图生图-3D卡通-提示词反推-SDXL v 4.0_1915532950828683265.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/超高清图生图-3D卡通-提示词反推-SDXL v 4.0_1915532950828683265.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Output → Other

**节点**（12 个）：
- `SaveImage`
- `VAEDecode` ★核心
- `RH_Captioner`
- `CR Text Concatenate`
- `DF_Text_Box`
- `KSampler` ★核心
- `VAEEncode` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `CheckpointLoaderSimple` ★核心
- `ShowText|pysssss`
- `LoadImage`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `922997381794256`
- `steps` = `20`
- `cfg` = `8`
- `sampler_name` = `euler_ancestral`
- `scheduler` = `normal`
- `denoise` = `0.44`
- `checkpoint` = `samaritan3dCartoon_v40SDXL.safetensors`

## 知识

覆盖率 **92%**（11/12）

**有卡**：`SaveImage`、`VAEDecode`、`RH_Captioner`、`CR Text Concatenate`、`DF_Text_Box`、`KSampler`、`VAEEncode`、`CLIPTextEncode`、`CheckpointLoaderSimple`、`LoadImage`

**用到的条目**：KSampler、VAEDecode、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、VAEEncode、SaveImage、DF_Text_Box

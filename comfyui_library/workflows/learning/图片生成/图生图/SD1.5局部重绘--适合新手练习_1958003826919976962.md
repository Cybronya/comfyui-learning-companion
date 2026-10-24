---
key: 图片生成/图生图/SD1.5局部重绘--适合新手练习_1958003826919976962.json
name: SD1.5局部重绘--适合新手练习_1958003826919976962
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/SD1.5局部重绘--适合新手练习_1958003826919976962.json
hash: a26be77f41e831ed
coverage: 1
learned_at: 2026-10-23 11:23:41
nodes: [ControlNetApplyAdvanced, ControlNetLoader, CLIPTextEncode, CheckpointLoaderSimple, DifferentialDiffusion, InpaintPreprocessor, KSampler, VAEDecode, SaveImage, SetLatentNoiseMask, MaskBlur+, GrowMask, LoadImage, CLIPSeg, VAEEncode, CLIPTextEncode]
patterns: [image_to_image]
missing: []
parameters: {"cfg": 8, "checkpoint": "epicrealism_pureEvolutionV5-inpainting.safetensors", "controlnet_strength": 1, "denoise": 1, "sampler_name": "dpmpp_2m", "scheduler": "karras", "seed": 728432435352025, "steps": 20}
---

# 图片生成/图生图/SD1.5局部重绘--适合新手练习_1958003826919976962.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/SD1.5局部重绘--适合新手练习_1958003826919976962.json`

## 结构

**生成流程**：Model → Encode → Condition → Control → Sampling → Decode → Output → Other

**节点**（16 个）：
- `ControlNetApplyAdvanced` ★核心
- `ControlNetLoader`
- `CLIPTextEncode` ★核心
- `CheckpointLoaderSimple` ★核心
- `DifferentialDiffusion`
- `InpaintPreprocessor`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `SaveImage`
- `SetLatentNoiseMask`
- `MaskBlur+`
- `GrowMask`
- `LoadImage`
- `CLIPSeg`
- `VAEEncode` ★核心
- `CLIPTextEncode` ★核心

**识别到的模式**：image_to_image

## 关键参数

- `controlnet_strength` = `1`
- `checkpoint` = `epicrealism_pureEvolutionV5-inpainting.safetensors`
- `seed` = `728432435352025`
- `steps` = `20`
- `cfg` = `8`
- `sampler_name` = `dpmpp_2m`
- `scheduler` = `karras`
- `denoise` = `1`

## 知识

覆盖率 **100%**（16/16）

**有卡**：`ControlNetApplyAdvanced`、`ControlNetLoader`、`CLIPTextEncode`、`CheckpointLoaderSimple`、`DifferentialDiffusion`、`InpaintPreprocessor`、`KSampler`、`VAEDecode`、`SaveImage`、`SetLatentNoiseMask`、`MaskBlur+`、`GrowMask`、`LoadImage`、`CLIPSeg`、`VAEEncode`

**用到的条目**：KSampler、VAEDecode、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、ControlNetApplyAdvanced、ControlNetLoader、SetLatentNoiseMask

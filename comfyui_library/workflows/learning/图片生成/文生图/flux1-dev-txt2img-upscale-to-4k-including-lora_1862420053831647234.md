---
key: 图片生成/文生图/flux1-dev-txt2img-upscale-to-4k-including-lora_1862420053831647234.json
name: flux1-dev-txt2img-upscale-to-4k-including-lora_1862420053831647234
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/flux1-dev-txt2img-upscale-to-4k-including-lora_1862420053831647234.json
hash: 2f73f94e867734ea
coverage: 0.782609
learned_at: 2026-10-10 20:59:19
nodes: [FluxGuidance, Reroute, ConditioningZeroOut, Reroute, VAEDecode, SDXLAspectRatioSelector, Reroute, CLIPTextEncode, Int, Int, EmptySD3LatentImage, Image Comparer (rgthree), FL_SDUltimate_Slices, KSampler, Reroute, SaveImage, SaveImage, UltimateSDUpscale, UNETLoader, VAELoader, LoraLoader, UpscaleModelLoader, DualCLIPLoader]
patterns: [lora]
missing: []
parameters: {"cfg": 1, "denoise": 1, "lora_name": "aidmaImageUpgrader-FLUX-V0.2.safetensors", "sampler_name": "euler", "scheduler": "simple", "seed": 497529703472631, "steps": 60, "strength_clip": 1, "strength_model": 1}
---

# 图片生成/文生图/flux1-dev-txt2img-upscale-to-4k-including-lora_1862420053831647234.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/flux1-dev-txt2img-upscale-to-4k-including-lora_1862420053831647234.json`

## 结构

**节点**（23 个）：
- `FluxGuidance`
- `Reroute`
- `ConditioningZeroOut`
- `Reroute`
- `VAEDecode`
- `SDXLAspectRatioSelector`
- `Reroute`
- `CLIPTextEncode`
- `Int`
- `Int`
- `EmptySD3LatentImage`
- `Image Comparer (rgthree)`
- `FL_SDUltimate_Slices`
- `KSampler`
- `Reroute`
- `SaveImage`
- `SaveImage`
- `UltimateSDUpscale`
- `UNETLoader`
- `VAELoader`
- `LoraLoader`
- `UpscaleModelLoader`
- `DualCLIPLoader`

**识别到的模式**：lora

## 关键参数

- `cfg` = `1`
- `denoise` = `1`
- `lora_name` = `aidmaImageUpgrader-FLUX-V0.2.safetensors`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `seed` = `497529703472631`
- `steps` = `60`
- `strength_clip` = `1`
- `strength_model` = `1`

## 知识

覆盖率 **78%**（18/23）

**有卡**：`FluxGuidance`、`Reroute`、`ConditioningZeroOut`、`VAEDecode`、`SDXLAspectRatioSelector`、`CLIPTextEncode`、`Int`、`EmptySD3LatentImage`、`Image Comparer (rgthree)`、`FL_SDUltimate_Slices`、`KSampler`、`SaveImage`、`UltimateSDUpscale`

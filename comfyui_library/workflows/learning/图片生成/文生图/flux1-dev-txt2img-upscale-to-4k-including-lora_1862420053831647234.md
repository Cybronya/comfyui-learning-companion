---
key: 图片生成/文生图/flux1-dev-txt2img-upscale-to-4k-including-lora_1862420053831647234.json
name: flux1-dev-txt2img-upscale-to-4k-including-lora_1862420053831647234
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/flux1-dev-txt2img-upscale-to-4k-including-lora_1862420053831647234.json
hash: 2f73f94e867734ea
coverage: 0.73913
learned_at: 2026-10-07 03:05:01
nodes: [FluxGuidance, Reroute, ConditioningZeroOut, Reroute, VAEDecode, SDXLAspectRatioSelector, Reroute, CLIPTextEncode, Int, Int, EmptySD3LatentImage, Image Comparer (rgthree), FL_SDUltimate_Slices, KSampler, Reroute, SaveImage, SaveImage, UltimateSDUpscale, UNETLoader, VAELoader, LoraLoader, UpscaleModelLoader, DualCLIPLoader]
patterns: [lora]
missing: [FL_SDUltimate_Slices]
parameters: {"cfg": 1, "denoise": 1, "lora_name": "aidmaImageUpgrader-FLUX-V0.2.safetensors", "sampler_name": "euler", "scheduler": "simple", "seed": 497529703472631, "steps": 60, "strength_clip": 1, "strength_model": 1}
discoveries: [次要节点 `FL_SDUltimate_Slices` 知识库中没有该节点类型的任何知识]
---

# 图片生成/文生图/flux1-dev-txt2img-upscale-to-4k-including-lora_1862420053831647234.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/flux1-dev-txt2img-upscale-to-4k-including-lora_1862420053831647234.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（23 个）：
- `FluxGuidance`
- `Reroute`
- `ConditioningZeroOut`
- `Reroute`
- `VAEDecode` ★核心
- `SDXLAspectRatioSelector`
- `Reroute`
- `CLIPTextEncode` ★核心
- `Int`
- `Int`
- `EmptySD3LatentImage`
- `Image Comparer (rgthree)`
- `FL_SDUltimate_Slices`
- `KSampler` ★核心
- `Reroute`
- `SaveImage`
- `SaveImage`
- `UltimateSDUpscale`
- `UNETLoader` ★核心
- `VAELoader`
- `LoraLoader` ★核心
- `UpscaleModelLoader`
- `DualCLIPLoader`

**识别到的模式**：lora

## 关键参数

- `seed` = `497529703472631`
- `steps` = `60`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `lora_name` = `aidmaImageUpgrader-FLUX-V0.2.safetensors`
- `strength_model` = `1`
- `strength_clip` = `1`

## 知识

覆盖率 **74%**（17/23）

**有卡**：`FluxGuidance`、`ConditioningZeroOut`、`VAEDecode`、`SDXLAspectRatioSelector`、`CLIPTextEncode`、`Int`、`EmptySD3LatentImage`、`KSampler`、`SaveImage`、`UltimateSDUpscale`、`UNETLoader`、`VAELoader`、`LoraLoader`、`UpscaleModelLoader`、`DualCLIPLoader`

**缺卡**（1）：`FL_SDUltimate_Slices`

**用到的条目**：KSampler、VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、ConditioningZeroOut、FluxGuidance、LoraLoader

## 学习发现

- 次要节点 `FL_SDUltimate_Slices` 知识库中没有该节点类型的任何知识

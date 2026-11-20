---
key: 平台全量/Fix Blurry Backgrounds in Flux Outputs修复 Flux 输出模糊_1863471676968337409.json
name: Fix Blurry Backgrounds in Flux Outputs修复 Flux 输出模糊_1863471676968337409
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/Fix Blurry Backgrounds in Flux Outputs修复 Flux 输出模糊_1863471676968337409.json
hash: 2eb7e305868477bc
coverage: 0.923077
learned_at: 2026-11-14 00:26:48
nodes: [FluxGuidance, ConditioningZeroOut, EmptySD3LatentImage, SaveImage, LayerUtility: PurgeVRAM, KSampler, CLIPTextEncode, CR SDXL Aspect Ratio, VAELoader, LoraLoaderModelOnly, CheckpointLoaderSimple, PreviewImage, VAEDecode]
patterns: []
missing: []
parameters: {"cfg": 1, "checkpoint": "flux1-dev-fp8-Comfy-Org.safetensors", "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 757502867902915, "steps": 24}
---

# 平台全量/Fix Blurry Backgrounds in Flux Outputs修复 Flux 输出模糊_1863471676968337409.json

> 来源文件 `comfyui_library/workflows/平台全量/Fix Blurry Backgrounds in Flux Outputs修复 Flux 输出模糊_1863471676968337409.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（13 个）：
- `FluxGuidance`
- `ConditioningZeroOut`
- `EmptySD3LatentImage`
- `SaveImage`
- `LayerUtility: PurgeVRAM`
- `KSampler` ★核心
- `CLIPTextEncode` ★核心
- `CR SDXL Aspect Ratio`
- `VAELoader`
- `LoraLoaderModelOnly` ★核心
- `CheckpointLoaderSimple` ★核心
- `PreviewImage`
- `VAEDecode` ★核心

## 关键参数

- `seed` = `757502867902915`
- `steps` = `24`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `checkpoint` = `flux1-dev-fp8-Comfy-Org.safetensors`

## 知识

覆盖率 **92%**（12/13）

**有卡**：`FluxGuidance`、`ConditioningZeroOut`、`EmptySD3LatentImage`、`SaveImage`、`LayerUtility: PurgeVRAM`、`KSampler`、`CLIPTextEncode`、`CR SDXL Aspect Ratio`、`VAELoader`、`LoraLoaderModelOnly`、`CheckpointLoaderSimple`、`VAEDecode`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、ConditioningZeroOut、FluxGuidance

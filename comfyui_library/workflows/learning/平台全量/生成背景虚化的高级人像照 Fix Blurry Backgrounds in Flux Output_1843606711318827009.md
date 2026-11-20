---
key: 平台全量/生成背景虚化的高级人像照 Fix Blurry Backgrounds in Flux Output_1843606711318827009.json
name: 生成背景虚化的高级人像照 Fix Blurry Backgrounds in Flux Output_1843606711318827009
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/生成背景虚化的高级人像照 Fix Blurry Backgrounds in Flux Output_1843606711318827009.json
hash: 0d761f926343aeee
coverage: 0.875
learned_at: 2026-11-14 02:22:12
nodes: [FluxGuidance, EmptySD3LatentImage, LayerUtility: PurgeVRAM, KSampler, CR SDXL Aspect Ratio, CheckpointLoaderSimple, VAELoader, LoraLoaderModelOnly, ConditioningZeroOut, CLIPTextEncode, SeargePromptText, VAEDecode, SaveImage, PreviewImage, RH_Prompter, ShowText|pysssss]
patterns: []
missing: []
parameters: {"cfg": 1, "checkpoint": "flux1-dev-fp8-Comfy-Org.safetensors", "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 757502867902915, "steps": 24}
---

# 平台全量/生成背景虚化的高级人像照 Fix Blurry Backgrounds in Flux Output_1843606711318827009.json

> 来源文件 `comfyui_library/workflows/平台全量/生成背景虚化的高级人像照 Fix Blurry Backgrounds in Flux Output_1843606711318827009.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（16 个）：
- `FluxGuidance`
- `EmptySD3LatentImage`
- `LayerUtility: PurgeVRAM`
- `KSampler` ★核心
- `CR SDXL Aspect Ratio`
- `CheckpointLoaderSimple` ★核心
- `VAELoader`
- `LoraLoaderModelOnly` ★核心
- `ConditioningZeroOut`
- `CLIPTextEncode` ★核心
- `SeargePromptText`
- `VAEDecode` ★核心
- `SaveImage`
- `PreviewImage`
- `RH_Prompter`
- `ShowText|pysssss`

## 关键参数

- `seed` = `757502867902915`
- `steps` = `24`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `checkpoint` = `flux1-dev-fp8-Comfy-Org.safetensors`

## 知识

覆盖率 **88%**（14/16）

**有卡**：`FluxGuidance`、`EmptySD3LatentImage`、`LayerUtility: PurgeVRAM`、`KSampler`、`CR SDXL Aspect Ratio`、`CheckpointLoaderSimple`、`VAELoader`、`LoraLoaderModelOnly`、`ConditioningZeroOut`、`CLIPTextEncode`、`SeargePromptText`、`VAEDecode`、`SaveImage`、`RH_Prompter`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、ConditioningZeroOut、FluxGuidance

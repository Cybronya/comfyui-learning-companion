---
key: 图片生成/文生图/Z-image  SeedVR2.5.1写实AI短剧定妆照文生图_2013072564117049346.json
name: Z-image  SeedVR2.5.1写实AI短剧定妆照文生图_2013072564117049346
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Z-image  SeedVR2.5.1写实AI短剧定妆照文生图_2013072564117049346.json
hash: 609d63028b6bae9e
coverage: 0.882353
learned_at: 2026-10-19 22:15:28
nodes: [EmptySD3LatentImage, VAEDecode, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, LayerUtility: PurgeVRAM V2, SeedVR2VideoUpscaler, SaveImage, KSampler, LoraLoaderModelOnly, CheckpointLoaderSimple, RHHiddenNodes, ShowText|pysssss, easy promptConcat, CLIPTextEncode, ConditioningZeroOut, PresetTextSelector, PrimitiveStringMultiline]
patterns: []
missing: []
parameters: {"cfg": 1, "checkpoint": "darkBeastZDBZUpdatedDEC21_dbzAIOV10.safetensors", "denoise": 1, "sampler_name": "euler", "scheduler": "FlowMatchEulerDiscreteScheduler", "seed": 385151523144196, "steps": 10}
---

# 图片生成/文生图/Z-image  SeedVR2.5.1写实AI短剧定妆照文生图_2013072564117049346.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Z-image  SeedVR2.5.1写实AI短剧定妆照文生图_2013072564117049346.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（17 个）：
- `EmptySD3LatentImage`
- `VAEDecode` ★核心
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `LayerUtility: PurgeVRAM V2`
- `SeedVR2VideoUpscaler`
- `SaveImage`
- `KSampler` ★核心
- `LoraLoaderModelOnly` ★核心
- `CheckpointLoaderSimple` ★核心
- `RHHiddenNodes`
- `ShowText|pysssss`
- `easy promptConcat`
- `CLIPTextEncode` ★核心
- `ConditioningZeroOut`
- `PresetTextSelector`
- `PrimitiveStringMultiline`

## 关键参数

- `seed` = `385151523144196`
- `steps` = `10`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `FlowMatchEulerDiscreteScheduler`
- `denoise` = `1`
- `checkpoint` = `darkBeastZDBZUpdatedDEC21_dbzAIOV10.safetensors`

## 知识

覆盖率 **88%**（15/17）

**有卡**：`EmptySD3LatentImage`、`VAEDecode`、`SeedVR2LoadDiTModel`、`SeedVR2LoadVAEModel`、`LayerUtility: PurgeVRAM V2`、`SeedVR2VideoUpscaler`、`SaveImage`、`KSampler`、`LoraLoaderModelOnly`、`CheckpointLoaderSimple`、`RHHiddenNodes`、`easy promptConcat`、`CLIPTextEncode`、`ConditioningZeroOut`、`PresetTextSelector`

**用到的条目**：KSampler、VAEDecode、LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、ConditioningZeroOut、SeedVR2LoadDiTModel、SeedVR2LoadVAEModel

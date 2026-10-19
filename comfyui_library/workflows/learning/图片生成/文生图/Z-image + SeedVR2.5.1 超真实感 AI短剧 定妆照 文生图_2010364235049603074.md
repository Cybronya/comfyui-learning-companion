---
key: 图片生成/文生图/Z-image + SeedVR2.5.1 超真实感 AI短剧 定妆照 文生图_2010364235049603074.json
name: Z-image + SeedVR2.5.1 超真实感 AI短剧 定妆照 文生图_2010364235049603074
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Z-image + SeedVR2.5.1 超真实感 AI短剧 定妆照 文生图_2010364235049603074.json
hash: 41afefe53de44ba5
coverage: 0.833333
learned_at: 2026-10-19 22:01:03
nodes: [EmptySD3LatentImage, VAEDecode, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, LayerUtility: PurgeVRAM V2, SeedVR2VideoUpscaler, SaveImage, KSampler, LoraLoaderModelOnly, CheckpointLoaderSimple, Note, PrimitiveStringMultiline, RHHiddenNodes, ShowText|pysssss, easy promptConcat, CLIPTextEncode, ConditioningZeroOut, PresetTextSelector]
patterns: []
missing: []
parameters: {"cfg": 1, "checkpoint": "darkBeastZDBZUpdatedDEC21_dbzAIOV10.safetensors", "denoise": 1, "sampler_name": "euler", "scheduler": "FlowMatchEulerDiscreteScheduler", "seed": 1112080457136658, "steps": 10}
---

# 图片生成/文生图/Z-image + SeedVR2.5.1 超真实感 AI短剧 定妆照 文生图_2010364235049603074.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Z-image + SeedVR2.5.1 超真实感 AI短剧 定妆照 文生图_2010364235049603074.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（18 个）：
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
- `Note`
- `PrimitiveStringMultiline`
- `RHHiddenNodes`
- `ShowText|pysssss`
- `easy promptConcat`
- `CLIPTextEncode` ★核心
- `ConditioningZeroOut`
- `PresetTextSelector`

## 关键参数

- `seed` = `1112080457136658`
- `steps` = `10`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `FlowMatchEulerDiscreteScheduler`
- `denoise` = `1`
- `checkpoint` = `darkBeastZDBZUpdatedDEC21_dbzAIOV10.safetensors`

## 知识

覆盖率 **83%**（15/18）

**有卡**：`EmptySD3LatentImage`、`VAEDecode`、`SeedVR2LoadDiTModel`、`SeedVR2LoadVAEModel`、`LayerUtility: PurgeVRAM V2`、`SeedVR2VideoUpscaler`、`SaveImage`、`KSampler`、`LoraLoaderModelOnly`、`CheckpointLoaderSimple`、`RHHiddenNodes`、`easy promptConcat`、`CLIPTextEncode`、`ConditioningZeroOut`、`PresetTextSelector`

**用到的条目**：KSampler、VAEDecode、LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、ConditioningZeroOut、SeedVR2LoadDiTModel、SeedVR2LoadVAEModel

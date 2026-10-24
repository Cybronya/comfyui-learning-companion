---
key: 图片生成/图生图/FLUX.Krea半身模糊变清晰_1937332253624049665.json
name: FLUX.Krea半身模糊变清晰_1937332253624049665
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/FLUX.Krea半身模糊变清晰_1937332253624049665.json
hash: b3885077d7ad439a
coverage: 0.888889
learned_at: 2026-10-23 10:54:16
nodes: [SUPIR_model_loader_v2, SUPIR_encode, SUPIR_conditioner, SUPIR_decode, NunchakuFluxDiTLoader, NunchakuTextEncoderLoaderV2, VAELoader, UpscaleModelLoader, ImageUpscaleWithModel, ImageResize+, UltimateSDUpscaleNoUpscale, ImageResize+, UpscaleModelLoader, Note, UltimateSDUpscale, SUPIR_first_stage, easy imageColorMatch, CheckpointLoaderSimple, easy int, ImageResize+, Note, LoadImage, Image Comparer (rgthree), SaveImage, SUPIR_sample, CLIPTextEncode, ConditioningZeroOut]
patterns: []
missing: []
parameters: {"checkpoint": "XLL dreamshaperXL_lightningDPMSDE.safetensors"}
---

# 图片生成/图生图/FLUX.Krea半身模糊变清晰_1937332253624049665.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/FLUX.Krea半身模糊变清晰_1937332253624049665.json`

## 结构

**生成流程**：Model → Condition → Process → Output → Other

**节点**（27 个）：
- `SUPIR_model_loader_v2`
- `SUPIR_encode`
- `SUPIR_conditioner`
- `SUPIR_decode`
- `NunchakuFluxDiTLoader`
- `NunchakuTextEncoderLoaderV2`
- `VAELoader`
- `UpscaleModelLoader`
- `ImageUpscaleWithModel`
- `ImageResize+`
- `UltimateSDUpscaleNoUpscale`
- `ImageResize+`
- `UpscaleModelLoader`
- `Note`
- `UltimateSDUpscale`
- `SUPIR_first_stage`
- `easy imageColorMatch`
- `CheckpointLoaderSimple` ★核心
- `easy int`
- `ImageResize+`
- `Note`
- `LoadImage`
- `Image Comparer (rgthree)`
- `SaveImage`
- `SUPIR_sample`
- `CLIPTextEncode` ★核心
- `ConditioningZeroOut`

## 关键参数

- `checkpoint` = `XLL dreamshaperXL_lightningDPMSDE.safetensors`

## 知识

覆盖率 **89%**（24/27）

**有卡**：`SUPIR_model_loader_v2`、`SUPIR_encode`、`SUPIR_conditioner`、`SUPIR_decode`、`NunchakuFluxDiTLoader`、`NunchakuTextEncoderLoaderV2`、`VAELoader`、`UpscaleModelLoader`、`ImageUpscaleWithModel`、`ImageResize+`、`UltimateSDUpscaleNoUpscale`、`UltimateSDUpscale`、`SUPIR_first_stage`、`easy imageColorMatch`、`CheckpointLoaderSimple`、`easy int`、`LoadImage`、`SaveImage`、`SUPIR_sample`、`CLIPTextEncode`、`ConditioningZeroOut`

**用到的条目**：VAELoader、CheckpointLoaderSimple、CLIPTextEncode、ConditioningZeroOut、LoadImage、SUPIR_decode、SUPIR_encode、NunchakuTextEncoderLoaderV2

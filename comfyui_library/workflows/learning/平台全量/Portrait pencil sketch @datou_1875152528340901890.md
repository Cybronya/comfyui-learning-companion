---
key: 平台全量/Portrait pencil sketch @datou_1875152528340901890.json
name: Portrait pencil sketch @datou_1875152528340901890
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/Portrait pencil sketch @datou_1875152528340901890.json
hash: 73db962e3392f0e5
coverage: 0.884615
learned_at: 2026-11-14 00:48:30
nodes: [CLIPVisionLoader, PulidFluxModelLoader, SaveImage, PulidFluxEvaClipLoader, PulidFluxInsightFaceLoader, Florence2Run, ShowText|pysssss, CR Text Concatenate, CR Text, DownloadAndLoadFlorence2Model, ConditioningZeroOut, StyleModelLoader, ApplyPulidFlux, ReduxAdvanced, DepthAnythingV2Preprocessor, PreviewImage, InstructPixToPixConditioning, VAEDecode, CLIPTextEncode, FluxGuidance, ImageScaleToTotalPixels, KSampler, CheckpointLoaderSimple, Note, Power Lora Loader (rgthree), LoadImage]
patterns: []
missing: []
parameters: {"cfg": 1, "checkpoint": "flux1-dev-fp8.safetensors", "denoise": 1, "sampler_name": "dpmpp_2m", "scheduler": "beta", "seed": 428394422622066, "steps": 12}
---

# 平台全量/Portrait pencil sketch @datou_1875152528340901890.json

> 来源文件 `comfyui_library/workflows/平台全量/Portrait pencil sketch @datou_1875152528340901890.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（26 个）：
- `CLIPVisionLoader`
- `PulidFluxModelLoader`
- `SaveImage`
- `PulidFluxEvaClipLoader`
- `PulidFluxInsightFaceLoader`
- `Florence2Run`
- `ShowText|pysssss`
- `CR Text Concatenate`
- `CR Text`
- `DownloadAndLoadFlorence2Model`
- `ConditioningZeroOut`
- `StyleModelLoader`
- `ApplyPulidFlux`
- `ReduxAdvanced`
- `DepthAnythingV2Preprocessor`
- `PreviewImage`
- `InstructPixToPixConditioning`
- `VAEDecode` ★核心
- `CLIPTextEncode` ★核心
- `FluxGuidance`
- `ImageScaleToTotalPixels`
- `KSampler` ★核心
- `CheckpointLoaderSimple` ★核心
- `Note`
- `Power Lora Loader (rgthree)`
- `LoadImage`

## 关键参数

- `seed` = `428394422622066`
- `steps` = `12`
- `cfg` = `1`
- `sampler_name` = `dpmpp_2m`
- `scheduler` = `beta`
- `denoise` = `1`
- `checkpoint` = `flux1-dev-fp8.safetensors`

## 知识

覆盖率 **88%**（23/26）

**有卡**：`CLIPVisionLoader`、`PulidFluxModelLoader`、`SaveImage`、`PulidFluxEvaClipLoader`、`PulidFluxInsightFaceLoader`、`Florence2Run`、`CR Text Concatenate`、`CR Text`、`DownloadAndLoadFlorence2Model`、`ConditioningZeroOut`、`StyleModelLoader`、`ApplyPulidFlux`、`ReduxAdvanced`、`DepthAnythingV2Preprocessor`、`InstructPixToPixConditioning`、`VAEDecode`、`CLIPTextEncode`、`FluxGuidance`、`ImageScaleToTotalPixels`、`KSampler`、`CheckpointLoaderSimple`、`Power Lora Loader (rgthree)`、`LoadImage`

**用到的条目**：KSampler、VAEDecode、CheckpointLoaderSimple、CLIPTextEncode、ConditioningZeroOut、LoadImage、DepthAnythingV2Preprocessor、FluxGuidance

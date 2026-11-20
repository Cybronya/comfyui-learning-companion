---
key: 平台全量/EcomID Face Changing FLUX Hand Repair_1875909734850351105.json
name: EcomID Face Changing FLUX Hand Repair_1875909734850351105
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/EcomID Face Changing FLUX Hand Repair_1875909734850351105.json
hash: b7119d875d9e4c99
coverage: 0.931034
learned_at: 2026-11-14 00:23:57
nodes: [CR Aspect Ratio, InstantIDModelLoader, EcomID_PulidModelLoader, PulidEvaClipLoader, EcomIDFaceAnalysis, CLIPTextEncode, CLIPTextEncode, VAEDecode, KSampler, PreviewImage, CLIPTextEncode, ApplyEcomIDAdvanced, CLIPTextEncode, CLIPTextEncode, UltralyticsDetectorProvider, CheckpointLoaderSimple, VAELoader, FaceDetailer, UltralyticsDetectorProvider, CLIPTextEncode, FluxGuidance, UNETLoader, DualCLIPLoader, ControlNetLoader, SDXLPromptStyler, FaceDetailer, SaveImage, PreviewImage, LoadImage]
patterns: []
missing: []
parameters: {"cfg": 6, "checkpoint": "realvisxlV40_v40Bakedvae.safetensors", "denoise": 1, "sampler_name": "dpmpp_sde", "scheduler": "karras", "seed": 222683137897402, "steps": 30}
---

# 平台全量/EcomID Face Changing FLUX Hand Repair_1875909734850351105.json

> 来源文件 `comfyui_library/workflows/平台全量/EcomID Face Changing FLUX Hand Repair_1875909734850351105.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Output → Other

**节点**（29 个）：
- `CR Aspect Ratio`
- `InstantIDModelLoader`
- `EcomID_PulidModelLoader`
- `PulidEvaClipLoader`
- `EcomIDFaceAnalysis`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `VAEDecode` ★核心
- `KSampler` ★核心
- `PreviewImage`
- `CLIPTextEncode` ★核心
- `ApplyEcomIDAdvanced`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `UltralyticsDetectorProvider`
- `CheckpointLoaderSimple` ★核心
- `VAELoader`
- `FaceDetailer`
- `UltralyticsDetectorProvider`
- `CLIPTextEncode` ★核心
- `FluxGuidance`
- `UNETLoader` ★核心
- `DualCLIPLoader`
- `ControlNetLoader`
- `SDXLPromptStyler`
- `FaceDetailer`
- `SaveImage`
- `PreviewImage`
- `LoadImage`

## 关键参数

- `seed` = `222683137897402`
- `steps` = `30`
- `cfg` = `6`
- `sampler_name` = `dpmpp_sde`
- `scheduler` = `karras`
- `denoise` = `1`
- `checkpoint` = `realvisxlV40_v40Bakedvae.safetensors`

## 知识

覆盖率 **93%**（27/29）

**有卡**：`CR Aspect Ratio`、`InstantIDModelLoader`、`EcomID_PulidModelLoader`、`PulidEvaClipLoader`、`EcomIDFaceAnalysis`、`CLIPTextEncode`、`VAEDecode`、`KSampler`、`ApplyEcomIDAdvanced`、`UltralyticsDetectorProvider`、`CheckpointLoaderSimple`、`VAELoader`、`FaceDetailer`、`FluxGuidance`、`UNETLoader`、`DualCLIPLoader`、`ControlNetLoader`、`SDXLPromptStyler`、`SaveImage`、`LoadImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、CheckpointLoaderSimple、UNETLoader、CLIPTextEncode、LoadImage、ControlNetLoader

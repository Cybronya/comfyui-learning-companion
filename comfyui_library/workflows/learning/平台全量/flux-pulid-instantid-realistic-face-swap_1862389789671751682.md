---
key: 平台全量/flux-pulid-instantid-realistic-face-swap_1862389789671751682.json
name: flux-pulid-instantid-realistic-face-swap_1862389789671751682
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/平台全量/flux-pulid-instantid-realistic-face-swap_1862389789671751682.json
hash: 595d96687b534eb4
coverage: 0.909091
learned_at: 2026-11-14 01:10:56
nodes: [PulidFluxModelLoader, PulidFluxEvaClipLoader, UltralyticsDetectorProvider, InstantIDModelLoader, InstantIDFaceAnalysis, ImageUpscaleWithModel, ImageScaleBy, easy fullLoader, CLIPTextEncode, ConditioningZeroOut, CLIPTextEncode, CLIPTextEncode, String, VAEDecode, CR SDXL Aspect Ratio, PulidFluxInsightFaceLoader, ApplyPulidFlux, PreviewImage, VAEEncode, KSampler, SAMLoader, ApplyInstantID, FaceDetailer, CLIPTextEncode, LoadImage, UpscaleModelLoader, ControlNetLoader, CheckpointLoaderSimple, SaveImage, VAEDecode, KSampler, PreviewImage, PreviewImage]
patterns: [image_to_image]
missing: []
parameters: {"cfg": 1, "checkpoint": "flux1-dev-fp8-Comfy-Org.safetensors", "denoise": 1, "sampler_name": "deis", "scheduler": "beta", "seed": 421399925472183, "steps": 30}
---

# 平台全量/flux-pulid-instantid-realistic-face-swap_1862389789671751682.json

> 来源文件 `comfyui_library/workflows/平台全量/flux-pulid-instantid-realistic-face-swap_1862389789671751682.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（33 个）：
- `PulidFluxModelLoader`
- `PulidFluxEvaClipLoader`
- `UltralyticsDetectorProvider`
- `InstantIDModelLoader`
- `InstantIDFaceAnalysis`
- `ImageUpscaleWithModel`
- `ImageScaleBy`
- `easy fullLoader`
- `CLIPTextEncode` ★核心
- `ConditioningZeroOut`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `String`
- `VAEDecode` ★核心
- `CR SDXL Aspect Ratio`
- `PulidFluxInsightFaceLoader`
- `ApplyPulidFlux`
- `PreviewImage`
- `VAEEncode` ★核心
- `KSampler` ★核心
- `SAMLoader`
- `ApplyInstantID`
- `FaceDetailer`
- `CLIPTextEncode` ★核心
- `LoadImage`
- `UpscaleModelLoader`
- `ControlNetLoader`
- `CheckpointLoaderSimple` ★核心
- `SaveImage`
- `VAEDecode` ★核心
- `KSampler` ★核心
- `PreviewImage`
- `PreviewImage`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `421399925472183`
- `steps` = `30`
- `cfg` = `1`
- `sampler_name` = `deis`
- `scheduler` = `beta`
- `denoise` = `1`
- `checkpoint` = `flux1-dev-fp8-Comfy-Org.safetensors`

## 知识

覆盖率 **91%**（30/33）

**有卡**：`PulidFluxModelLoader`、`PulidFluxEvaClipLoader`、`UltralyticsDetectorProvider`、`InstantIDModelLoader`、`InstantIDFaceAnalysis`、`ImageUpscaleWithModel`、`ImageScaleBy`、`easy fullLoader`、`CLIPTextEncode`、`ConditioningZeroOut`、`String`、`VAEDecode`、`CR SDXL Aspect Ratio`、`PulidFluxInsightFaceLoader`、`ApplyPulidFlux`、`VAEEncode`、`KSampler`、`SAMLoader`、`ApplyInstantID`、`FaceDetailer`、`LoadImage`、`UpscaleModelLoader`、`ControlNetLoader`、`CheckpointLoaderSimple`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、CheckpointLoaderSimple、CLIPTextEncode、ConditioningZeroOut、LoadImage、ControlNetLoader、VAEEncode

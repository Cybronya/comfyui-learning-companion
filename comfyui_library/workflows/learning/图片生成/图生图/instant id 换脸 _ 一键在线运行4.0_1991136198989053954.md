---
key: 图片生成/图生图/instant id 换脸 _ 一键在线运行4.0_1991136198989053954.json
name: instant id 换脸 _ 一键在线运行4.0_1991136198989053954
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/instant id 换脸 _ 一键在线运行4.0_1991136198989053954.json
hash: bc6d10af3bc93ade
coverage: 0.842105
learned_at: 2026-10-23 11:37:59
nodes: [ControlNetApplyAdvanced, PreviewImage, FaceBoundingBox, FaceAnalysisModels, PreviewImage, CLIPTextEncode, CLIPTextEncode, AIO_Preprocessor, InstantIDFaceAnalysis, ApplyInstantID, InpaintModelConditioning, RepeatLatentBatch, KSampler, VAEDecode, ImageResize+, Reroute, Reroute, Reroute, Reroute, CropMask, MaskBlur+, GrowMask, LayerUtility: CropBoxResolve, LayerUtility: RestoreCropBox, ImageResize+, LoadImage, CheckpointLoaderSimple, ControlNetLoader, InstantIDModelLoader, ControlNetLoader, SaveImage, ColorMatch, SUPIR_Upscale, LayerMask: MaskPreview, LayerMask: MaskPreview, LayerUtility: CropByMask V2, LayerMask: PersonMaskUltra V2, LoadImage]
patterns: []
missing: []
parameters: {"cfg": 1.5, "checkpoint": "XLL dreamshaperXL_lightningDPMSDE.safetensors", "controlnet_strength": 0.45, "denoise": 0.6, "sampler_name": "euler_ancestral", "scheduler": "sgm_uniform", "seed": 1023566739764980, "steps": 15}
---

# 图片生成/图生图/instant id 换脸 _ 一键在线运行4.0_1991136198989053954.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/instant id 换脸 _ 一键在线运行4.0_1991136198989053954.json`

## 结构

**生成流程**：Model → Condition → Control → Sampling → Decode → Process → Output → Other

**节点**（38 个）：
- `ControlNetApplyAdvanced` ★核心
- `PreviewImage`
- `FaceBoundingBox`
- `FaceAnalysisModels`
- `PreviewImage`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `AIO_Preprocessor`
- `InstantIDFaceAnalysis`
- `ApplyInstantID`
- `InpaintModelConditioning`
- `RepeatLatentBatch`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `ImageResize+`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `CropMask`
- `MaskBlur+`
- `GrowMask`
- `LayerUtility: CropBoxResolve`
- `LayerUtility: RestoreCropBox`
- `ImageResize+`
- `LoadImage`
- `CheckpointLoaderSimple` ★核心
- `ControlNetLoader`
- `InstantIDModelLoader`
- `ControlNetLoader`
- `SaveImage`
- `ColorMatch`
- `SUPIR_Upscale`
- `LayerMask: MaskPreview`
- `LayerMask: MaskPreview`
- `LayerUtility: CropByMask V2`
- `LayerMask: PersonMaskUltra V2`
- `LoadImage`

## 关键参数

- `controlnet_strength` = `0.45`
- `seed` = `1023566739764980`
- `steps` = `15`
- `cfg` = `1.5`
- `sampler_name` = `euler_ancestral`
- `scheduler` = `sgm_uniform`
- `denoise` = `0.6`
- `checkpoint` = `XLL dreamshaperXL_lightningDPMSDE.safetensors`

## 知识

覆盖率 **84%**（32/38）

**有卡**：`ControlNetApplyAdvanced`、`FaceBoundingBox`、`FaceAnalysisModels`、`CLIPTextEncode`、`AIO_Preprocessor`、`InstantIDFaceAnalysis`、`ApplyInstantID`、`InpaintModelConditioning`、`RepeatLatentBatch`、`KSampler`、`VAEDecode`、`ImageResize+`、`CropMask`、`MaskBlur+`、`GrowMask`、`LayerUtility: CropBoxResolve`、`LayerUtility: RestoreCropBox`、`LoadImage`、`CheckpointLoaderSimple`、`ControlNetLoader`、`InstantIDModelLoader`、`SaveImage`、`ColorMatch`、`SUPIR_Upscale`、`LayerMask: MaskPreview`、`LayerUtility: CropByMask V2`、`LayerMask: PersonMaskUltra V2`

**用到的条目**：KSampler、VAEDecode、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、ControlNetApplyAdvanced、ControlNetLoader、RepeatLatentBatch

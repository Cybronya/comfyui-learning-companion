---
key: 图片生成/图生图/AI摄影_人像图超强换脸V2.6_1955536036283781121.json
name: AI摄影_人像图超强换脸V2.6_1955536036283781121
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/AI摄影_人像图超强换脸V2.6_1955536036283781121.json
hash: 2cbd55e374947b8f
coverage: 0.852941
learned_at: 2026-10-23 10:50:36
nodes: [InstantIDFaceAnalysis, InstantIDModelLoader, ControlNetLoader, ControlNetLoader, LayerUtility: CropByMask V2, ImageResize+, GrowMask, LayerMask: PersonMaskUltra V2, LayerUtility: CropBoxResolve, CropMask, FeatheredMask, MaskBlur+, LayerUtility: RestoreCropBox, Reroute, ImageColorMatch+, ImageResize+, RepeatLatentBatch, CheckpointLoaderSimple, CLIPTextEncode, CLIPTextEncode, VAEDecode, AIO_Preprocessor, Reroute, PreviewImage, LoadImage, LoadImage, SaveImage, Image Comparer (rgthree), ControlNetApplyAdvanced, ApplyInstantID, InpaintModelConditioning, LayerMask: MaskPreview, KSampler, Note]
patterns: []
missing: []
parameters: {"cfg": 1.5, "checkpoint": "dreamshaperXL_v21TurboDPMSDE.safetensors", "controlnet_strength": 0.45, "denoise": 0.6, "sampler_name": "euler_ancestral", "scheduler": "sgm_uniform", "seed": 1010766099833290, "steps": 15}
---

# 图片生成/图生图/AI摄影_人像图超强换脸V2.6_1955536036283781121.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/AI摄影_人像图超强换脸V2.6_1955536036283781121.json`

## 结构

**生成流程**：Model → Condition → Control → Sampling → Decode → Process → Output → Other

**节点**（34 个）：
- `InstantIDFaceAnalysis`
- `InstantIDModelLoader`
- `ControlNetLoader`
- `ControlNetLoader`
- `LayerUtility: CropByMask V2`
- `ImageResize+`
- `GrowMask`
- `LayerMask: PersonMaskUltra V2`
- `LayerUtility: CropBoxResolve`
- `CropMask`
- `FeatheredMask`
- `MaskBlur+`
- `LayerUtility: RestoreCropBox`
- `Reroute`
- `ImageColorMatch+`
- `ImageResize+`
- `RepeatLatentBatch`
- `CheckpointLoaderSimple` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `VAEDecode` ★核心
- `AIO_Preprocessor`
- `Reroute`
- `PreviewImage`
- `LoadImage`
- `LoadImage`
- `SaveImage`
- `Image Comparer (rgthree)`
- `ControlNetApplyAdvanced` ★核心
- `ApplyInstantID`
- `InpaintModelConditioning`
- `LayerMask: MaskPreview`
- `KSampler` ★核心
- `Note`

## 关键参数

- `checkpoint` = `dreamshaperXL_v21TurboDPMSDE.safetensors`
- `controlnet_strength` = `0.45`
- `seed` = `1010766099833290`
- `steps` = `15`
- `cfg` = `1.5`
- `sampler_name` = `euler_ancestral`
- `scheduler` = `sgm_uniform`
- `denoise` = `0.6`

## 知识

覆盖率 **85%**（29/34）

**有卡**：`InstantIDFaceAnalysis`、`InstantIDModelLoader`、`ControlNetLoader`、`LayerUtility: CropByMask V2`、`ImageResize+`、`GrowMask`、`LayerMask: PersonMaskUltra V2`、`LayerUtility: CropBoxResolve`、`CropMask`、`FeatheredMask`、`MaskBlur+`、`LayerUtility: RestoreCropBox`、`ImageColorMatch+`、`RepeatLatentBatch`、`CheckpointLoaderSimple`、`CLIPTextEncode`、`VAEDecode`、`AIO_Preprocessor`、`LoadImage`、`SaveImage`、`ControlNetApplyAdvanced`、`ApplyInstantID`、`InpaintModelConditioning`、`LayerMask: MaskPreview`、`KSampler`

**用到的条目**：KSampler、VAEDecode、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、ControlNetApplyAdvanced、ControlNetLoader、RepeatLatentBatch

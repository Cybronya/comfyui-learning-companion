---
key: 图片生成/图生图/Nunchaku极速换装Fill+ACE+Redux_1943999439797125121.json
name: Nunchaku极速换装Fill+ACE+Redux_1943999439797125121
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Nunchaku极速换装Fill+ACE+Redux_1943999439797125121.json
hash: 6ed032ba9359186b
coverage: 0.813953
learned_at: 2026-10-23 11:10:06
nodes: [PreviewImage, PreviewImage, PreviewImage, MaskToImage, PreviewImage, easy imageConcat, easy imageConcat, CR Color Panel, Int, CLIPVisionEncode, CLIPVisionLoader, StyleModelLoader, LayerUtility: ImageScaleByAspectRatio V2, NunchakuTextEncoderLoader, ConditioningZeroOut, FluxGuidance, VAEDecode, InpaintModelConditioning, StyleModelApply, SaveImage, VAELoader, DifferentialDiffusion, ImageToMask, PreviewImage, ModelSamplingFlux, NunchakuFluxLoraLoader, PreviewImage, DownloadAndLoadFlorence2Model, LayerMask: SegmentAnythingUltra V2, KSampler, NunchakuFluxDiTLoader, SaveImage, ImageCrop, Image Comparer (rgthree), Florence2Run, easy showAnything, CLIPTextEncode, LayerUtility: TextJoin, DeepTranslatorTextNode, LayerUtility: ImageRemoveAlpha, LoadImage, LoadImage, LayerUtility: ImageScaleByAspectRatio V2]
patterns: []
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "normal", "seed": 503616962176774, "steps": 25}
---

# 图片生成/图生图/Nunchaku极速换装Fill+ACE+Redux_1943999439797125121.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Nunchaku极速换装Fill+ACE+Redux_1943999439797125121.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（43 个）：
- `PreviewImage`
- `PreviewImage`
- `PreviewImage`
- `MaskToImage`
- `PreviewImage`
- `easy imageConcat`
- `easy imageConcat`
- `CR Color Panel`
- `Int`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `StyleModelLoader`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `NunchakuTextEncoderLoader`
- `ConditioningZeroOut`
- `FluxGuidance`
- `VAEDecode` ★核心
- `InpaintModelConditioning`
- `StyleModelApply`
- `SaveImage`
- `VAELoader`
- `DifferentialDiffusion`
- `ImageToMask`
- `PreviewImage`
- `ModelSamplingFlux`
- `NunchakuFluxLoraLoader` ★核心
- `PreviewImage`
- `DownloadAndLoadFlorence2Model`
- `LayerMask: SegmentAnythingUltra V2`
- `KSampler` ★核心
- `NunchakuFluxDiTLoader`
- `SaveImage`
- `ImageCrop`
- `Image Comparer (rgthree)`
- `Florence2Run`
- `easy showAnything`
- `CLIPTextEncode` ★核心
- `LayerUtility: TextJoin`
- `DeepTranslatorTextNode`
- `LayerUtility: ImageRemoveAlpha`
- `LoadImage`
- `LoadImage`
- `LayerUtility: ImageScaleByAspectRatio V2`

## 关键参数

- `seed` = `503616962176774`
- `steps` = `25`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `normal`
- `denoise` = `1`

## 知识

覆盖率 **81%**（35/43）

**有卡**：`MaskToImage`、`easy imageConcat`、`CR Color Panel`、`Int`、`CLIPVisionEncode`、`CLIPVisionLoader`、`StyleModelLoader`、`LayerUtility: ImageScaleByAspectRatio V2`、`NunchakuTextEncoderLoader`、`ConditioningZeroOut`、`FluxGuidance`、`VAEDecode`、`InpaintModelConditioning`、`StyleModelApply`、`SaveImage`、`VAELoader`、`DifferentialDiffusion`、`ImageToMask`、`ModelSamplingFlux`、`NunchakuFluxLoraLoader`、`DownloadAndLoadFlorence2Model`、`LayerMask: SegmentAnythingUltra V2`、`KSampler`、`NunchakuFluxDiTLoader`、`ImageCrop`、`Florence2Run`、`CLIPTextEncode`、`LayerUtility: TextJoin`、`DeepTranslatorTextNode`、`LayerUtility: ImageRemoveAlpha`、`LoadImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、ConditioningZeroOut、LoadImage、FluxGuidance、CLIPVisionEncode

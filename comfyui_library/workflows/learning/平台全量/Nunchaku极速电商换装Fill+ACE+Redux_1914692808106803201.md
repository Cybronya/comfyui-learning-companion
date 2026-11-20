---
key: 平台全量/Nunchaku极速电商换装Fill+ACE+Redux_1914692808106803201.json
name: Nunchaku极速电商换装Fill+ACE+Redux_1914692808106803201
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/Nunchaku极速电商换装Fill+ACE+Redux_1914692808106803201.json
hash: c460726670cd5f4b
coverage: 0.813953
learned_at: 2026-11-14 00:47:14
nodes: [PreviewImage, PreviewImage, PreviewImage, MaskToImage, PreviewImage, easy imageConcat, easy imageConcat, CR Color Panel, Int, CLIPVisionEncode, CLIPVisionLoader, StyleModelLoader, LayerUtility: ImageScaleByAspectRatio V2, NunchakuTextEncoderLoader, ConditioningZeroOut, FluxGuidance, VAEDecode, InpaintModelConditioning, StyleModelApply, SaveImage, VAELoader, DifferentialDiffusion, ImageToMask, PreviewImage, ModelSamplingFlux, NunchakuFluxLoraLoader, PreviewImage, LayerUtility: ImageRemoveAlpha, DownloadAndLoadFlorence2Model, LayerMask: SegmentAnythingUltra V2, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: TextJoin, LoadImage, KSampler, easy showAnything, NunchakuFluxDiTLoader, SaveImage, ImageCrop, Image Comparer (rgthree), LoadImage, DeepTranslatorTextNode, CLIPTextEncode, Florence2Run]
patterns: []
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "normal", "seed": 731190547046958, "steps": 25}
---

# 平台全量/Nunchaku极速电商换装Fill+ACE+Redux_1914692808106803201.json

> 来源文件 `comfyui_library/workflows/平台全量/Nunchaku极速电商换装Fill+ACE+Redux_1914692808106803201.json`

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
- `LayerUtility: ImageRemoveAlpha`
- `DownloadAndLoadFlorence2Model`
- `LayerMask: SegmentAnythingUltra V2`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: TextJoin`
- `LoadImage`
- `KSampler` ★核心
- `easy showAnything`
- `NunchakuFluxDiTLoader`
- `SaveImage`
- `ImageCrop`
- `Image Comparer (rgthree)`
- `LoadImage`
- `DeepTranslatorTextNode`
- `CLIPTextEncode` ★核心
- `Florence2Run`

## 关键参数

- `seed` = `731190547046958`
- `steps` = `25`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `normal`
- `denoise` = `1`

## 知识

覆盖率 **81%**（35/43）

**有卡**：`MaskToImage`、`easy imageConcat`、`CR Color Panel`、`Int`、`CLIPVisionEncode`、`CLIPVisionLoader`、`StyleModelLoader`、`LayerUtility: ImageScaleByAspectRatio V2`、`NunchakuTextEncoderLoader`、`ConditioningZeroOut`、`FluxGuidance`、`VAEDecode`、`InpaintModelConditioning`、`StyleModelApply`、`SaveImage`、`VAELoader`、`DifferentialDiffusion`、`ImageToMask`、`ModelSamplingFlux`、`NunchakuFluxLoraLoader`、`LayerUtility: ImageRemoveAlpha`、`DownloadAndLoadFlorence2Model`、`LayerMask: SegmentAnythingUltra V2`、`LayerUtility: TextJoin`、`LoadImage`、`KSampler`、`NunchakuFluxDiTLoader`、`ImageCrop`、`DeepTranslatorTextNode`、`CLIPTextEncode`、`Florence2Run`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、ConditioningZeroOut、LoadImage、FluxGuidance、CLIPVisionEncode

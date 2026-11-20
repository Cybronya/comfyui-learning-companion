---
key: 平台全量/Nunchaku极速万物迁移工作流-FLUX模型Fill+ACE+Redux_1912179012544753665.json
name: Nunchaku极速万物迁移工作流-FLUX模型Fill+ACE+Redux_1912179012544753665
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/Nunchaku极速万物迁移工作流-FLUX模型Fill+ACE+Redux_1912179012544753665.json
hash: 446c2e4aa8fbcea8
coverage: 0.840909
learned_at: 2026-11-14 00:47:14
nodes: [PreviewImage, PreviewImage, PreviewImage, MaskToImage, PreviewImage, easy imageConcat, easy imageConcat, CR Color Panel, RembgByBiRefNet, AutoDownloadBiRefNetModel, PreviewImage, Int, CLIPVisionEncode, CLIPVisionLoader, StyleModelLoader, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageRemoveAlpha, NunchakuTextEncoderLoader, ConditioningZeroOut, FluxGuidance, SaveImage, ImageCrop, VAEDecode, InpaintModelConditioning, StyleModelApply, SaveImage, LayerUtility: ImageScaleByAspectRatio V2, DownloadAndLoadFlorence2Model, Florence2Run, VAELoader, DifferentialDiffusion, ImageToMask, PreviewImage, LoadImage, easy showAnything, LoadImage, LayerUtility: TextJoin, CLIPTextEncode, DeepTranslatorTextNode, ModelSamplingFlux, NunchakuFluxLoraLoader, NunchakuFluxDiTLoader, KSampler, easy cleanGpuUsed]
patterns: []
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "dpmpp_2m", "scheduler": "simple", "seed": 888216100244241, "steps": 25}
---

# 平台全量/Nunchaku极速万物迁移工作流-FLUX模型Fill+ACE+Redux_1912179012544753665.json

> 来源文件 `comfyui_library/workflows/平台全量/Nunchaku极速万物迁移工作流-FLUX模型Fill+ACE+Redux_1912179012544753665.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（44 个）：
- `PreviewImage`
- `PreviewImage`
- `PreviewImage`
- `MaskToImage`
- `PreviewImage`
- `easy imageConcat`
- `easy imageConcat`
- `CR Color Panel`
- `RembgByBiRefNet`
- `AutoDownloadBiRefNetModel`
- `PreviewImage`
- `Int`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `StyleModelLoader`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: ImageRemoveAlpha`
- `NunchakuTextEncoderLoader`
- `ConditioningZeroOut`
- `FluxGuidance`
- `SaveImage`
- `ImageCrop`
- `VAEDecode` ★核心
- `InpaintModelConditioning`
- `StyleModelApply`
- `SaveImage`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `DownloadAndLoadFlorence2Model`
- `Florence2Run`
- `VAELoader`
- `DifferentialDiffusion`
- `ImageToMask`
- `PreviewImage`
- `LoadImage`
- `easy showAnything`
- `LoadImage`
- `LayerUtility: TextJoin`
- `CLIPTextEncode` ★核心
- `DeepTranslatorTextNode`
- `ModelSamplingFlux`
- `NunchakuFluxLoraLoader` ★核心
- `NunchakuFluxDiTLoader`
- `KSampler` ★核心
- `easy cleanGpuUsed`

## 关键参数

- `seed` = `888216100244241`
- `steps` = `25`
- `cfg` = `1`
- `sampler_name` = `dpmpp_2m`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **84%**（37/44）

**有卡**：`MaskToImage`、`easy imageConcat`、`CR Color Panel`、`RembgByBiRefNet`、`AutoDownloadBiRefNetModel`、`Int`、`CLIPVisionEncode`、`CLIPVisionLoader`、`StyleModelLoader`、`LayerUtility: ImageScaleByAspectRatio V2`、`LayerUtility: ImageRemoveAlpha`、`NunchakuTextEncoderLoader`、`ConditioningZeroOut`、`FluxGuidance`、`SaveImage`、`ImageCrop`、`VAEDecode`、`InpaintModelConditioning`、`StyleModelApply`、`DownloadAndLoadFlorence2Model`、`Florence2Run`、`VAELoader`、`DifferentialDiffusion`、`ImageToMask`、`LoadImage`、`LayerUtility: TextJoin`、`CLIPTextEncode`、`DeepTranslatorTextNode`、`ModelSamplingFlux`、`NunchakuFluxLoraLoader`、`NunchakuFluxDiTLoader`、`KSampler`、`easy cleanGpuUsed`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、ConditioningZeroOut、LoadImage、FluxGuidance、CLIPVisionEncode

---
key: 平台全量/Flux Nunchaku ACE万物迁移极速换背景-StarAI_1912341497436434433.json
name: Flux Nunchaku ACE万物迁移极速换背景-StarAI_1912341497436434433
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/Flux Nunchaku ACE万物迁移极速换背景-StarAI_1912341497436434433.json
hash: 8edbe17f8daf6f23
coverage: 0.886364
learned_at: 2026-11-14 00:28:00
nodes: [StyleModelLoader, CLIPVisionLoader, StyleModelApply, CLIPVisionEncode, ModelSamplingFlux, InpaintModelConditioning, CR Color Panel, PreviewImage, easy imageConcat, ImageToMask, easy imageConcat, MaskToImage, NunchakuTextEncoderLoader, LayerUtility: ImageRemoveAlpha, LayerUtility: CropByMask V2, RMBG, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, DifferentialDiffusion, VAEDecode, NunchakuFluxDiTLoader, LoadImage, SaveImage, ImageCrop, Image Comparer (rgthree), Note Plus (mtb), LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageScaleByAspectRatio V2, Int, Florence2Run, easy showAnything, DownloadAndLoadFlorence2Model, KSampler, VAELoader, CLIPTextEncode, ConditioningZeroOut, LoraLoaderModelOnly, LoraLoaderModelOnly, LayerUtility: TextJoin, FluxGuidance, PreviewImage, MaskPreview+, CR Text, Fast Groups Bypasser (rgthree)]
patterns: []
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 698721659396645, "steps": 10}
---

# 平台全量/Flux Nunchaku ACE万物迁移极速换背景-StarAI_1912341497436434433.json

> 来源文件 `comfyui_library/workflows/平台全量/Flux Nunchaku ACE万物迁移极速换背景-StarAI_1912341497436434433.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（44 个）：
- `StyleModelLoader`
- `CLIPVisionLoader`
- `StyleModelApply`
- `CLIPVisionEncode`
- `ModelSamplingFlux`
- `InpaintModelConditioning`
- `CR Color Panel`
- `PreviewImage`
- `easy imageConcat`
- `ImageToMask`
- `easy imageConcat`
- `MaskToImage`
- `NunchakuTextEncoderLoader`
- `LayerUtility: ImageRemoveAlpha`
- `LayerUtility: CropByMask V2`
- `RMBG`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `DifferentialDiffusion`
- `VAEDecode` ★核心
- `NunchakuFluxDiTLoader`
- `LoadImage`
- `SaveImage`
- `ImageCrop`
- `Image Comparer (rgthree)`
- `Note Plus (mtb)`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `Int`
- `Florence2Run`
- `easy showAnything`
- `DownloadAndLoadFlorence2Model`
- `KSampler` ★核心
- `VAELoader`
- `CLIPTextEncode` ★核心
- `ConditioningZeroOut`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LayerUtility: TextJoin`
- `FluxGuidance`
- `PreviewImage`
- `MaskPreview+`
- `CR Text`
- `Fast Groups Bypasser (rgthree)`

## 关键参数

- `seed` = `698721659396645`
- `steps` = `10`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **89%**（39/44）

**有卡**：`StyleModelLoader`、`CLIPVisionLoader`、`StyleModelApply`、`CLIPVisionEncode`、`ModelSamplingFlux`、`InpaintModelConditioning`、`CR Color Panel`、`easy imageConcat`、`ImageToMask`、`MaskToImage`、`NunchakuTextEncoderLoader`、`LayerUtility: ImageRemoveAlpha`、`LayerUtility: CropByMask V2`、`RMBG`、`LayerUtility: ImageScaleByAspectRatio V2`、`LoadImage`、`DifferentialDiffusion`、`VAEDecode`、`NunchakuFluxDiTLoader`、`SaveImage`、`ImageCrop`、`Note Plus (mtb)`、`Int`、`Florence2Run`、`DownloadAndLoadFlorence2Model`、`KSampler`、`VAELoader`、`CLIPTextEncode`、`ConditioningZeroOut`、`LoraLoaderModelOnly`、`LayerUtility: TextJoin`、`FluxGuidance`、`MaskPreview+`、`CR Text`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、ConditioningZeroOut、LoadImage、FluxGuidance

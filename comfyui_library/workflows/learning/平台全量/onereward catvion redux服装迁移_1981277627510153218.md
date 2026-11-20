---
key: 平台全量/onereward catvion redux服装迁移_1981277627510153218.json
name: onereward catvion redux服装迁移_1981277627510153218
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/onereward catvion redux服装迁移_1981277627510153218.json
hash: 7d5391c1fd326bcf
coverage: 0.878788
learned_at: 2026-11-14 01:15:37
nodes: [ConditioningZeroOut, DualCLIPLoader, ReduxAdvanced, InpaintModelConditioning, DifferentialDiffusion, ApplyFBCacheOnModel, LayerUtility: CropByMask V2, StyleModelLoader, CLIPVisionLoader, UNETLoader, LoraLoaderModelOnly, VAELoader, PreviewImage, LayerUtility: CropByMask V2, MaskPreview+, LayerUtility: ICMask, ImageResizeKJv2, ImageResizeKJv2, LayerUtility: ICMaskCropBack, Image Comparer (rgthree), LayerMask: SegmentAnythingUltra V2, ImageConcatMulti, PreviewImage, LoadImage, CLIPTextEncodeFlux, LayerUtility: PurgeVRAM, KSampler, VAEDecode, LayerUtility: RestoreCropBox, LayerUtility: PurgeVRAM V2, SaveImage, LoadImage, Note]
patterns: []
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "normal", "seed": 169930343153371, "steps": 35}
---

# 平台全量/onereward catvion redux服装迁移_1981277627510153218.json

> 来源文件 `comfyui_library/workflows/平台全量/onereward catvion redux服装迁移_1981277627510153218.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（33 个）：
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `ReduxAdvanced`
- `InpaintModelConditioning`
- `DifferentialDiffusion`
- `ApplyFBCacheOnModel`
- `LayerUtility: CropByMask V2`
- `StyleModelLoader`
- `CLIPVisionLoader`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `VAELoader`
- `PreviewImage`
- `LayerUtility: CropByMask V2`
- `MaskPreview+`
- `LayerUtility: ICMask`
- `ImageResizeKJv2`
- `ImageResizeKJv2`
- `LayerUtility: ICMaskCropBack`
- `Image Comparer (rgthree)`
- `LayerMask: SegmentAnythingUltra V2`
- `ImageConcatMulti`
- `PreviewImage`
- `LoadImage`
- `CLIPTextEncodeFlux` ★核心
- `LayerUtility: PurgeVRAM`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `LayerUtility: RestoreCropBox`
- `LayerUtility: PurgeVRAM V2`
- `SaveImage`
- `LoadImage`
- `Note`

## 关键参数

- `seed` = `169930343153371`
- `steps` = `35`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `normal`
- `denoise` = `1`

## 知识

覆盖率 **88%**（29/33）

**有卡**：`ConditioningZeroOut`、`DualCLIPLoader`、`ReduxAdvanced`、`InpaintModelConditioning`、`DifferentialDiffusion`、`ApplyFBCacheOnModel`、`LayerUtility: CropByMask V2`、`StyleModelLoader`、`CLIPVisionLoader`、`UNETLoader`、`LoraLoaderModelOnly`、`VAELoader`、`MaskPreview+`、`LayerUtility: ICMask`、`ImageResizeKJv2`、`LayerUtility: ICMaskCropBack`、`LayerMask: SegmentAnythingUltra V2`、`ImageConcatMulti`、`LoadImage`、`CLIPTextEncodeFlux`、`LayerUtility: PurgeVRAM`、`KSampler`、`VAEDecode`、`LayerUtility: RestoreCropBox`、`LayerUtility: PurgeVRAM V2`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、ConditioningZeroOut、LoadImage、CLIPTextEncodeFlux

---
key: 平台全量/FLUX.电商产品指定场景背景工作流_1899382074204405762.json
name: FLUX.电商产品指定场景背景工作流_1899382074204405762
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/FLUX.电商产品指定场景背景工作流_1899382074204405762.json
hash: 4f1a0a374219800b
coverage: 0.885714
learned_at: 2026-11-14 00:25:15
nodes: [ConditioningZeroOut, InpaintModelConditioning, KSampler, MaskToImage, ImageConcanate, ImageToMask, VAEDecode, GrowMask, LayerUtility: ColorImage, PreviewImage, InpaintStitch, PreviewImage, InspyrenetRembg, CLIPTextEncodeFlux, InpaintCrop, ImageScale, ImageResize+, ImageConcanate, PreviewImage, LoadImage, LoadImage, LayerMask: SegmentAnythingUltra V2, LayerMask: SegmentAnythingUltra V2, MaskPreview+, StyleModelLoader, CLIPVisionLoader, ReduxAdvanced, VAELoader, DualCLIPLoader, UNETLoader, LoraLoaderModelOnly, LayerUtility: ImageRemoveAlpha, SaveImage, PreviewImage, ImageCrop+]
patterns: []
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "normal", "seed": 494884193650298, "steps": 20}
---

# 平台全量/FLUX.电商产品指定场景背景工作流_1899382074204405762.json

> 来源文件 `comfyui_library/workflows/平台全量/FLUX.电商产品指定场景背景工作流_1899382074204405762.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（35 个）：
- `ConditioningZeroOut`
- `InpaintModelConditioning`
- `KSampler` ★核心
- `MaskToImage`
- `ImageConcanate`
- `ImageToMask`
- `VAEDecode` ★核心
- `GrowMask`
- `LayerUtility: ColorImage`
- `PreviewImage`
- `InpaintStitch`
- `PreviewImage`
- `InspyrenetRembg`
- `CLIPTextEncodeFlux` ★核心
- `InpaintCrop`
- `ImageScale`
- `ImageResize+`
- `ImageConcanate`
- `PreviewImage`
- `LoadImage`
- `LoadImage`
- `LayerMask: SegmentAnythingUltra V2`
- `LayerMask: SegmentAnythingUltra V2`
- `MaskPreview+`
- `StyleModelLoader`
- `CLIPVisionLoader`
- `ReduxAdvanced`
- `VAELoader`
- `DualCLIPLoader`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `LayerUtility: ImageRemoveAlpha`
- `SaveImage`
- `PreviewImage`
- `ImageCrop+`

## 关键参数

- `seed` = `494884193650298`
- `steps` = `20`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `normal`
- `denoise` = `1`

## 知识

覆盖率 **89%**（31/35）

**有卡**：`ConditioningZeroOut`、`InpaintModelConditioning`、`KSampler`、`MaskToImage`、`ImageConcanate`、`ImageToMask`、`VAEDecode`、`GrowMask`、`LayerUtility: ColorImage`、`InpaintStitch`、`InspyrenetRembg`、`CLIPTextEncodeFlux`、`InpaintCrop`、`ImageScale`、`ImageResize+`、`LoadImage`、`LayerMask: SegmentAnythingUltra V2`、`MaskPreview+`、`StyleModelLoader`、`CLIPVisionLoader`、`ReduxAdvanced`、`VAELoader`、`DualCLIPLoader`、`UNETLoader`、`LoraLoaderModelOnly`、`LayerUtility: ImageRemoveAlpha`、`SaveImage`、`ImageCrop+`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、ConditioningZeroOut、LoadImage、CLIPTextEncodeFlux

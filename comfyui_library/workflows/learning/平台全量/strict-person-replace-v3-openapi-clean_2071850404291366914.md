---
key: 平台全量/strict-person-replace-v3-openapi-clean_2071850404291366914.json
name: strict-person-replace-v3-openapi-clean_2071850404291366914
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/strict-person-replace-v3-openapi-clean_2071850404291366914.json
hash: e687200ea23656a5
coverage: 0.617284
learned_at: 2026-11-14 01:18:12
nodes: [EmptyImage, LayerUtility: ColorPicker, InspyrenetRembg, easy imageSize, LayerUtility: ImageRemoveAlpha, PreviewImage, GetNode, PreviewImage, EmptyImage, PreviewImage, ImageConcanate, ImageToMask, SetNode, SetNode, ImageConcanate, FluxGuidance, GetNode, StyleModelApply, CLIPVisionEncode, CLIPTextEncode, InpaintModelConditioning, GetNode, DifferentialDiffusion, VAEDecode, MaskToImage, easy imageSize, ImageScale, easy imageSize, CLIPTextEncode, CLIPTextEncode, UpscaleModelLoader, PreviewImage, GetNode, GetNode, PreviewImage, GetNode, VAELoader, SetNode, GetNode, GetNode, GetNode, GetNode, InpaintCrop, ImageCrop, easy imageSize, GetNode, GetNode, easy imageScaleDownToSize, SetNode, ReActorRestoreFace, PreviewImage, InpaintStitch, SetNode, LayerUtility: ImageReel, DualCLIPLoader, StyleModelLoader, CLIPVisionLoader, LayerMask: SegmentAnythingUltra V2, UNETLoader, ImageResize+, LayerUtility: ImageMaskScaleAs, LayerUtility: ImageReelComposit, easy imageSize, easy imageSize, SetNode, SetNode, LoadImage, LoadImage, KSampler, SetNode, CLIPTextEncode, SetNode, SetNode, PreviewImage, GetNode, LoraLoaderModelOnly, UltimateSDUpscale, SetNode, SaveImage, LayerMask: SegmentAnythingUltra V2, ReActorFaceSwap]
patterns: []
missing: []
parameters: {"cfg": 1.15, "denoise": 0.72, "sampler_name": "euler", "scheduler": "simple", "seed": 1782726180775, "steps": 28}
---

# 平台全量/strict-person-replace-v3-openapi-clean_2071850404291366914.json

> 来源文件 `comfyui_library/workflows/平台全量/strict-person-replace-v3-openapi-clean_2071850404291366914.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（81 个）：
- `EmptyImage`
- `LayerUtility: ColorPicker`
- `InspyrenetRembg`
- `easy imageSize`
- `LayerUtility: ImageRemoveAlpha`
- `PreviewImage`
- `GetNode`
- `PreviewImage`
- `EmptyImage`
- `PreviewImage`
- `ImageConcanate`
- `ImageToMask`
- `SetNode`
- `SetNode`
- `ImageConcanate`
- `FluxGuidance`
- `GetNode`
- `StyleModelApply`
- `CLIPVisionEncode`
- `CLIPTextEncode` ★核心
- `InpaintModelConditioning`
- `GetNode`
- `DifferentialDiffusion`
- `VAEDecode` ★核心
- `MaskToImage`
- `easy imageSize`
- `ImageScale`
- `easy imageSize`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `UpscaleModelLoader`
- `PreviewImage`
- `GetNode`
- `GetNode`
- `PreviewImage`
- `GetNode`
- `VAELoader`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `InpaintCrop`
- `ImageCrop`
- `easy imageSize`
- `GetNode`
- `GetNode`
- `easy imageScaleDownToSize`
- `SetNode`
- `ReActorRestoreFace`
- `PreviewImage`
- `InpaintStitch`
- `SetNode`
- `LayerUtility: ImageReel`
- `DualCLIPLoader`
- `StyleModelLoader`
- `CLIPVisionLoader`
- `LayerMask: SegmentAnythingUltra V2`
- `UNETLoader` ★核心
- `ImageResize+`
- `LayerUtility: ImageMaskScaleAs`
- `LayerUtility: ImageReelComposit`
- `easy imageSize`
- `easy imageSize`
- `SetNode`
- `SetNode`
- `LoadImage`
- `LoadImage`
- `KSampler` ★核心
- `SetNode`
- `CLIPTextEncode` ★核心
- `SetNode`
- `SetNode`
- `PreviewImage`
- `GetNode`
- `LoraLoaderModelOnly` ★核心
- `UltimateSDUpscale`
- `SetNode`
- `SaveImage`
- `LayerMask: SegmentAnythingUltra V2`
- `ReActorFaceSwap`

## 关键参数

- `seed` = `1782726180775`
- `steps` = `28`
- `cfg` = `1.15`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `0.72`

## 知识

覆盖率 **62%**（50/81）

**有卡**：`EmptyImage`、`LayerUtility: ColorPicker`、`InspyrenetRembg`、`easy imageSize`、`LayerUtility: ImageRemoveAlpha`、`ImageConcanate`、`ImageToMask`、`FluxGuidance`、`StyleModelApply`、`CLIPVisionEncode`、`CLIPTextEncode`、`InpaintModelConditioning`、`DifferentialDiffusion`、`VAEDecode`、`MaskToImage`、`ImageScale`、`UpscaleModelLoader`、`VAELoader`、`InpaintCrop`、`ImageCrop`、`easy imageScaleDownToSize`、`ReActorRestoreFace`、`InpaintStitch`、`LayerUtility: ImageReel`、`DualCLIPLoader`、`StyleModelLoader`、`CLIPVisionLoader`、`LayerMask: SegmentAnythingUltra V2`、`UNETLoader`、`ImageResize+`、`LayerUtility: ImageMaskScaleAs`、`LayerUtility: ImageReelComposit`、`LoadImage`、`KSampler`、`LoraLoaderModelOnly`、`UltimateSDUpscale`、`SaveImage`、`ReActorFaceSwap`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、LoadImage、FluxGuidance

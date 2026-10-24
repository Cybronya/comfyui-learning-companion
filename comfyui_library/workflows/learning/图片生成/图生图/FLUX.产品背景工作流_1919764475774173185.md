---
key: 图片生成/图生图/FLUX.产品背景工作流_1919764475774173185.json
name: FLUX.产品背景工作流_1919764475774173185
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/FLUX.产品背景工作流_1919764475774173185.json
hash: fd6545f74b59fce0
coverage: 0.837838
learned_at: 2026-10-23 10:54:18
nodes: [MaskToImage, ImageConcanate, ImageToMask, GrowMask, LayerUtility: ColorImage, InspyrenetRembg, InpaintCrop, ImageScale, ImageConcanate, PreviewImage, LayerMask: SegmentAnythingUltra V2, MaskPreview+, PreviewImage, ImageResize+, LayerUtility: ImageRemoveAlpha, UNETLoader, LayerMask: SegmentAnythingUltra V2, LoraLoaderModelOnly, DualCLIPLoader, VAELoader, CLIPTextEncodeFlux, ReduxAdvanced, CLIPVisionLoader, StyleModelLoader, ConditioningZeroOut, InpaintModelConditioning, InpaintStitch, ImageCrop+, PreviewImage, VAEDecode, PreviewImage, RHHiddenNodes, SaveImage, LoadImage, Note, Note, LoadImage]
patterns: []
missing: []
---

# 图片生成/图生图/FLUX.产品背景工作流_1919764475774173185.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/FLUX.产品背景工作流_1919764475774173185.json`

## 结构

**生成流程**：Model → Condition → Decode → Process → Output → Other

**节点**（37 个）：
- `MaskToImage`
- `ImageConcanate`
- `ImageToMask`
- `GrowMask`
- `LayerUtility: ColorImage`
- `InspyrenetRembg`
- `InpaintCrop`
- `ImageScale`
- `ImageConcanate`
- `PreviewImage`
- `LayerMask: SegmentAnythingUltra V2`
- `MaskPreview+`
- `PreviewImage`
- `ImageResize+`
- `LayerUtility: ImageRemoveAlpha`
- `UNETLoader` ★核心
- `LayerMask: SegmentAnythingUltra V2`
- `LoraLoaderModelOnly` ★核心
- `DualCLIPLoader`
- `VAELoader`
- `CLIPTextEncodeFlux` ★核心
- `ReduxAdvanced`
- `CLIPVisionLoader`
- `StyleModelLoader`
- `ConditioningZeroOut`
- `InpaintModelConditioning`
- `InpaintStitch`
- `ImageCrop+`
- `PreviewImage`
- `VAEDecode` ★核心
- `PreviewImage`
- `RHHiddenNodes`
- `SaveImage`
- `LoadImage`
- `Note`
- `Note`
- `LoadImage`

## 知识

覆盖率 **84%**（31/37）

**有卡**：`MaskToImage`、`ImageConcanate`、`ImageToMask`、`GrowMask`、`LayerUtility: ColorImage`、`InspyrenetRembg`、`InpaintCrop`、`ImageScale`、`LayerMask: SegmentAnythingUltra V2`、`MaskPreview+`、`ImageResize+`、`LayerUtility: ImageRemoveAlpha`、`UNETLoader`、`LoraLoaderModelOnly`、`DualCLIPLoader`、`VAELoader`、`CLIPTextEncodeFlux`、`ReduxAdvanced`、`CLIPVisionLoader`、`StyleModelLoader`、`ConditioningZeroOut`、`InpaintModelConditioning`、`InpaintStitch`、`ImageCrop+`、`VAEDecode`、`RHHiddenNodes`、`SaveImage`、`LoadImage`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、ConditioningZeroOut、LoadImage、CLIPTextEncodeFlux、StyleModelLoader

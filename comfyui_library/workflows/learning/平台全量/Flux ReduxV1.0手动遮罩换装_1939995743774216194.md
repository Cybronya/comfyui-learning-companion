---
key: 平台全量/Flux ReduxV1.0手动遮罩换装_1939995743774216194.json
name: Flux ReduxV1.0手动遮罩换装_1939995743774216194
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/Flux ReduxV1.0手动遮罩换装_1939995743774216194.json
hash: 9f396ada7bebdac8
coverage: 0.894737
learned_at: 2026-11-14 00:28:04
nodes: [MaskToImage, ImageToMask, MaskToImage, DifferentialDiffusion, ImageResize+, ImageResize+, LayerUtility: ColorImage, LayerUtility: ColorImage, ImageConcanate, InpaintCrop, ImageResize+, ImageConcanate, ImageConcanate, PreviewImage, InpaintModelConditioning, CLIPTextEncode, CLIPTextEncode, easy imageSize, FluxGuidance, ImageToMask, VAEDecode, InpaintStitch, CLIPVisionEncode, StyleModelApply, ImageCrop+, VAELoader, Note, DualCLIPLoader, KSampler, StyleModelLoader, CLIPVisionLoader, LayerMask: SegmentAnythingUltra V2, UNETLoader, LoadImage, LoadImage, SaveImage, Image Comparer (rgthree), PreviewImage]
patterns: []
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 455148138234660, "steps": 20}
---

# 平台全量/Flux ReduxV1.0手动遮罩换装_1939995743774216194.json

> 来源文件 `comfyui_library/workflows/平台全量/Flux ReduxV1.0手动遮罩换装_1939995743774216194.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（38 个）：
- `MaskToImage`
- `ImageToMask`
- `MaskToImage`
- `DifferentialDiffusion`
- `ImageResize+`
- `ImageResize+`
- `LayerUtility: ColorImage`
- `LayerUtility: ColorImage`
- `ImageConcanate`
- `InpaintCrop`
- `ImageResize+`
- `ImageConcanate`
- `ImageConcanate`
- `PreviewImage`
- `InpaintModelConditioning`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `easy imageSize`
- `FluxGuidance`
- `ImageToMask`
- `VAEDecode` ★核心
- `InpaintStitch`
- `CLIPVisionEncode`
- `StyleModelApply`
- `ImageCrop+`
- `VAELoader`
- `Note`
- `DualCLIPLoader`
- `KSampler` ★核心
- `StyleModelLoader`
- `CLIPVisionLoader`
- `LayerMask: SegmentAnythingUltra V2`
- `UNETLoader` ★核心
- `LoadImage`
- `LoadImage`
- `SaveImage`
- `Image Comparer (rgthree)`
- `PreviewImage`

## 关键参数

- `seed` = `455148138234660`
- `steps` = `20`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **89%**（34/38）

**有卡**：`MaskToImage`、`ImageToMask`、`DifferentialDiffusion`、`ImageResize+`、`LayerUtility: ColorImage`、`ImageConcanate`、`InpaintCrop`、`InpaintModelConditioning`、`CLIPTextEncode`、`easy imageSize`、`FluxGuidance`、`VAEDecode`、`InpaintStitch`、`CLIPVisionEncode`、`StyleModelApply`、`ImageCrop+`、`VAELoader`、`DualCLIPLoader`、`KSampler`、`StyleModelLoader`、`CLIPVisionLoader`、`LayerMask: SegmentAnythingUltra V2`、`UNETLoader`、`LoadImage`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、LoadImage、FluxGuidance、CLIPVisionEncode

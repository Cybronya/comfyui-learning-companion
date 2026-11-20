---
key: 平台全量/FLUX+fill+ACE电商产品换装2.0FLUX+fill+ACE换装1_1931224249976205313.json
name: FLUX+fill+ACE电商产品换装2.0FLUX+fill+ACE换装1_1931224249976205313
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/FLUX+fill+ACE电商产品换装2.0FLUX+fill+ACE换装1_1931224249976205313.json
hash: 1c774714feef798f
coverage: 0.956522
learned_at: 2026-11-14 00:24:50
nodes: [StyleModelApply, ImageResize+, LayerUtility: ImageRemoveAlpha, StyleModelApply, CLIPTextEncode, FluxGuidance, CLIPTextEncode, DifferentialDiffusion, KSampler, VAEDecode, GetImageSize_, InpaintModelConditioning, MaskPreview+, DifferentialDiffusion, CLIPTextEncode, CLIPTextEncode, FluxGuidance, Florence2Run, easy makeImageForICLora, CLIPVisionEncode, LayerMask: BiRefNetUltra, Fast Groups Bypasser (rgthree), CLIPVisionEncode, InpaintModelConditioning, KSampler, GetImageSize_, VAEDecode, Florence2ModelLoader, ImageCrop, ImageCrop, SaveImage, SaveImage, LoadImage, LoadImage, Note, CLIPVisionLoader, VAELoader, LoraLoaderModelOnly, StyleModelLoader, CLIPVisionLoader, DualCLIPLoader, StyleModelLoader, DualCLIPLoader, VAELoader, UNETLoader, UNETLoader]
patterns: []
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 604983840309880, "steps": 28}
---

# 平台全量/FLUX+fill+ACE电商产品换装2.0FLUX+fill+ACE换装1_1931224249976205313.json

> 来源文件 `comfyui_library/workflows/平台全量/FLUX+fill+ACE电商产品换装2.0FLUX+fill+ACE换装1_1931224249976205313.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（46 个）：
- `StyleModelApply`
- `ImageResize+`
- `LayerUtility: ImageRemoveAlpha`
- `StyleModelApply`
- `CLIPTextEncode` ★核心
- `FluxGuidance`
- `CLIPTextEncode` ★核心
- `DifferentialDiffusion`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `GetImageSize_`
- `InpaintModelConditioning`
- `MaskPreview+`
- `DifferentialDiffusion`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `FluxGuidance`
- `Florence2Run`
- `easy makeImageForICLora`
- `CLIPVisionEncode`
- `LayerMask: BiRefNetUltra`
- `Fast Groups Bypasser (rgthree)`
- `CLIPVisionEncode`
- `InpaintModelConditioning`
- `KSampler` ★核心
- `GetImageSize_`
- `VAEDecode` ★核心
- `Florence2ModelLoader`
- `ImageCrop`
- `ImageCrop`
- `SaveImage`
- `SaveImage`
- `LoadImage`
- `LoadImage`
- `Note`
- `CLIPVisionLoader`
- `VAELoader`
- `LoraLoaderModelOnly` ★核心
- `StyleModelLoader`
- `CLIPVisionLoader`
- `DualCLIPLoader`
- `StyleModelLoader`
- `DualCLIPLoader`
- `VAELoader`
- `UNETLoader` ★核心
- `UNETLoader` ★核心

## 关键参数

- `seed` = `604983840309880`
- `steps` = `28`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **96%**（44/46）

**有卡**：`StyleModelApply`、`ImageResize+`、`LayerUtility: ImageRemoveAlpha`、`CLIPTextEncode`、`FluxGuidance`、`DifferentialDiffusion`、`KSampler`、`VAEDecode`、`GetImageSize_`、`InpaintModelConditioning`、`MaskPreview+`、`Florence2Run`、`easy makeImageForICLora`、`CLIPVisionEncode`、`LayerMask: BiRefNetUltra`、`Florence2ModelLoader`、`ImageCrop`、`SaveImage`、`LoadImage`、`CLIPVisionLoader`、`VAELoader`、`LoraLoaderModelOnly`、`StyleModelLoader`、`DualCLIPLoader`、`UNETLoader`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、LoadImage、FluxGuidance

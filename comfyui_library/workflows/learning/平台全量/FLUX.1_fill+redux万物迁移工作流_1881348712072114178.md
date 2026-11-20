---
key: 平台全量/FLUX.1_fill+redux万物迁移工作流_1881348712072114178.json
name: FLUX.1_fill+redux万物迁移工作流_1881348712072114178
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/FLUX.1_fill+redux万物迁移工作流_1881348712072114178.json
hash: 7b279bfbd664e050
coverage: 0.875
learned_at: 2026-11-14 00:25:06
nodes: [DifferentialDiffusion, CLIPTextEncode, CLIPTextEncode, FluxGuidance, InpaintModelConditioning, KSampler, GetImageSize+, ImageCrop, StyleModelApply, VAEDecode, PreviewImage, MaskToImage, ImageToMask, SaveImage, PreviewImage, easy int, LayerUtility: ImageScaleByAspectRatio V2, RMBG, LoadImage, LoadImage, Fast Groups Bypasser (rgthree), UNETLoader, DualCLIPLoader, VAELoader, ImageConcanate, EmptyImage, LayerUtility: ImageScaleByAspectRatio V2, PreviewImage, ImageConcanate, CLIPVisionEncode, StyleModelLoader, CLIPVisionLoader]
patterns: []
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "normal", "seed": 886769084000781, "steps": 20}
---

# 平台全量/FLUX.1_fill+redux万物迁移工作流_1881348712072114178.json

> 来源文件 `comfyui_library/workflows/平台全量/FLUX.1_fill+redux万物迁移工作流_1881348712072114178.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（32 个）：
- `DifferentialDiffusion`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `FluxGuidance`
- `InpaintModelConditioning`
- `KSampler` ★核心
- `GetImageSize+`
- `ImageCrop`
- `StyleModelApply`
- `VAEDecode` ★核心
- `PreviewImage`
- `MaskToImage`
- `ImageToMask`
- `SaveImage`
- `PreviewImage`
- `easy int`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `RMBG`
- `LoadImage`
- `LoadImage`
- `Fast Groups Bypasser (rgthree)`
- `UNETLoader` ★核心
- `DualCLIPLoader`
- `VAELoader`
- `ImageConcanate`
- `EmptyImage`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `PreviewImage`
- `ImageConcanate`
- `CLIPVisionEncode`
- `StyleModelLoader`
- `CLIPVisionLoader`

## 关键参数

- `seed` = `886769084000781`
- `steps` = `20`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `normal`
- `denoise` = `1`

## 知识

覆盖率 **88%**（28/32）

**有卡**：`DifferentialDiffusion`、`CLIPTextEncode`、`FluxGuidance`、`InpaintModelConditioning`、`KSampler`、`GetImageSize+`、`ImageCrop`、`StyleModelApply`、`VAEDecode`、`MaskToImage`、`ImageToMask`、`SaveImage`、`easy int`、`LayerUtility: ImageScaleByAspectRatio V2`、`RMBG`、`LoadImage`、`UNETLoader`、`DualCLIPLoader`、`VAELoader`、`ImageConcanate`、`EmptyImage`、`CLIPVisionEncode`、`StyleModelLoader`、`CLIPVisionLoader`

**用到的条目**：KSampler、VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、LoadImage、FluxGuidance、CLIPVisionEncode

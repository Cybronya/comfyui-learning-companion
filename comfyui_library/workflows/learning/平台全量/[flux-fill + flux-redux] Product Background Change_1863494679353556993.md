---
key: 平台全量/[flux-fill + flux-redux] Product Background Change_1863494679353556993.json
name: [flux-fill + flux-redux] Product Background Change_1863494679353556993
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/[flux-fill + flux-redux] Product Background Change_1863494679353556993.json
hash: f29df92d42b3ff92
coverage: 0.9375
learned_at: 2026-11-14 01:08:55
nodes: [LoadImage, ImageResizeKJ, Florence2toCoordinates, Mask Invert, MaskBlur+, JoinImageWithAlpha, LoadImage, Florence2Run, easy showAnything, Florence2Run, Sam2Segmentation, CLIPTextEncode, CLIPTextEncode, FluxGuidance, SaveImage, MaskPreview+, CLIPVisionEncode, StyleModelApply, DifferentialDiffusion, InpaintModelConditioning, KSampler, VAEDecode, SaveImage, Note, UNETLoader, DualCLIPLoader, Florence2ModelLoader, VAELoader, DownloadAndLoadFlorence2Model, DownloadAndLoadSAM2Model, StyleModelLoader, CLIPVisionLoader]
patterns: []
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "normal", "seed": 658049484953983, "steps": 20}
---

# 平台全量/[flux-fill + flux-redux] Product Background Change_1863494679353556993.json

> 来源文件 `comfyui_library/workflows/平台全量/[flux-fill + flux-redux] Product Background Change_1863494679353556993.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（32 个）：
- `LoadImage`
- `ImageResizeKJ`
- `Florence2toCoordinates`
- `Mask Invert`
- `MaskBlur+`
- `JoinImageWithAlpha`
- `LoadImage`
- `Florence2Run`
- `easy showAnything`
- `Florence2Run`
- `Sam2Segmentation`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `FluxGuidance`
- `SaveImage`
- `MaskPreview+`
- `CLIPVisionEncode`
- `StyleModelApply`
- `DifferentialDiffusion`
- `InpaintModelConditioning`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `SaveImage`
- `Note`
- `UNETLoader` ★核心
- `DualCLIPLoader`
- `Florence2ModelLoader`
- `VAELoader`
- `DownloadAndLoadFlorence2Model`
- `DownloadAndLoadSAM2Model`
- `StyleModelLoader`
- `CLIPVisionLoader`

## 关键参数

- `seed` = `658049484953983`
- `steps` = `20`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `normal`
- `denoise` = `1`

## 知识

覆盖率 **94%**（30/32）

**有卡**：`LoadImage`、`ImageResizeKJ`、`Florence2toCoordinates`、`Mask Invert`、`MaskBlur+`、`JoinImageWithAlpha`、`Florence2Run`、`Sam2Segmentation`、`CLIPTextEncode`、`FluxGuidance`、`SaveImage`、`MaskPreview+`、`CLIPVisionEncode`、`StyleModelApply`、`DifferentialDiffusion`、`InpaintModelConditioning`、`KSampler`、`VAEDecode`、`UNETLoader`、`DualCLIPLoader`、`Florence2ModelLoader`、`VAELoader`、`DownloadAndLoadFlorence2Model`、`DownloadAndLoadSAM2Model`、`StyleModelLoader`、`CLIPVisionLoader`

**用到的条目**：KSampler、VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、LoadImage、FluxGuidance、CLIPVisionEncode

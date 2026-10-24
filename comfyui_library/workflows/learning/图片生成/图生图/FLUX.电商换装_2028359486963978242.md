---
key: 图片生成/图生图/FLUX.电商换装_2028359486963978242.json
name: FLUX.电商换装_2028359486963978242
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/FLUX.电商换装_2028359486963978242.json
hash: 776444dee8c03eb8
coverage: 1
learned_at: 2026-10-23 10:54:18
nodes: [DownloadAndLoadSAM2Model, DownloadAndLoadFlorence2Model, StyleModelApply, CLIPTextEncode, StyleModelLoader, CLIPVisionEncode, CLIPVisionLoader, InpaintModelConditioning, ConditioningZeroOut, FluxGuidance, UnetLoaderGGUF, VAEDecode, INPAINT_ExpandMask, Sam2Segmentation, Florence2toCoordinates, Florence2Run, MaskPreview+, SimpleCondition+, GetImageSize+, ImageResize+, SimpleComparison+, ImageCrop+, LoadImage, SaveImage, ImageCrop+, KSampler, DualCLIPLoaderGGUF, VAELoader, AddMaskForICLora, LoadImage]
patterns: []
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "normal", "seed": 846745413171847, "steps": 20}
---

# 图片生成/图生图/FLUX.电商换装_2028359486963978242.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/FLUX.电商换装_2028359486963978242.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（30 个）：
- `DownloadAndLoadSAM2Model`
- `DownloadAndLoadFlorence2Model`
- `StyleModelApply`
- `CLIPTextEncode` ★核心
- `StyleModelLoader`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `InpaintModelConditioning`
- `ConditioningZeroOut`
- `FluxGuidance`
- `UnetLoaderGGUF` ★核心
- `VAEDecode` ★核心
- `INPAINT_ExpandMask`
- `Sam2Segmentation`
- `Florence2toCoordinates`
- `Florence2Run`
- `MaskPreview+`
- `SimpleCondition+`
- `GetImageSize+`
- `ImageResize+`
- `SimpleComparison+`
- `ImageCrop+`
- `LoadImage`
- `SaveImage`
- `ImageCrop+`
- `KSampler` ★核心
- `DualCLIPLoaderGGUF`
- `VAELoader`
- `AddMaskForICLora`
- `LoadImage`

## 关键参数

- `seed` = `846745413171847`
- `steps` = `20`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `normal`
- `denoise` = `1`

## 知识

覆盖率 **100%**（30/30）

**有卡**：`DownloadAndLoadSAM2Model`、`DownloadAndLoadFlorence2Model`、`StyleModelApply`、`CLIPTextEncode`、`StyleModelLoader`、`CLIPVisionEncode`、`CLIPVisionLoader`、`InpaintModelConditioning`、`ConditioningZeroOut`、`FluxGuidance`、`UnetLoaderGGUF`、`VAEDecode`、`INPAINT_ExpandMask`、`Sam2Segmentation`、`Florence2toCoordinates`、`Florence2Run`、`MaskPreview+`、`SimpleCondition+`、`GetImageSize+`、`ImageResize+`、`SimpleComparison+`、`ImageCrop+`、`LoadImage`、`SaveImage`、`KSampler`、`DualCLIPLoaderGGUF`、`VAELoader`、`AddMaskForICLora`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、ConditioningZeroOut、LoadImage、FluxGuidance、CLIPVisionEncode

---
key: 平台全量/FLUX.电商换装_1891866706665705473.json
name: FLUX.电商换装_1891866706665705473
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/FLUX.电商换装_1891866706665705473.json
hash: d9ce04cd17ee41f6
coverage: 1
learned_at: 2026-11-14 00:25:16
nodes: [DownloadAndLoadSAM2Model, DownloadAndLoadFlorence2Model, StyleModelApply, CLIPTextEncode, StyleModelLoader, CLIPVisionEncode, CLIPVisionLoader, InpaintModelConditioning, ConditioningZeroOut, FluxGuidance, UnetLoaderGGUF, VAEDecode, INPAINT_ExpandMask, Sam2Segmentation, Florence2toCoordinates, Florence2Run, MaskPreview+, SimpleCondition+, GetImageSize+, ImageResize+, SimpleComparison+, ImageCrop+, LoadImage, LoadImage, SaveImage, ImageCrop+, KSampler, DualCLIPLoaderGGUF, VAELoader, AddMaskForICLora]
patterns: []
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "normal", "seed": 846745413171847, "steps": 20}
---

# 平台全量/FLUX.电商换装_1891866706665705473.json

> 来源文件 `comfyui_library/workflows/平台全量/FLUX.电商换装_1891866706665705473.json`

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
- `LoadImage`
- `SaveImage`
- `ImageCrop+`
- `KSampler` ★核心
- `DualCLIPLoaderGGUF`
- `VAELoader`
- `AddMaskForICLora`

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

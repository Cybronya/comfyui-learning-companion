---
key: 平台全量/除水印 Remove Text Or Watermark_1863787080831680514.json
name: 除水印 Remove Text Or Watermark_1863787080831680514
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/除水印 Remove Text Or Watermark_1863787080831680514.json
hash: 32c58be7f40a619d
coverage: 0.692308
learned_at: 2026-11-14 02:49:45
nodes: [GroundingDinoSAMSegment (segment anything), GroundingDinoModelLoader (segment anything), SAMModelLoader (segment anything), Note, AddMask, MaskToImage, LoadImage, MaskPreview+, PreviewImage, GrowMaskWithBlur, INPAINT_MaskedFill, INPAINT_MaskedBlur, Note, PreviewImage, ImageGenResolutionFromImage, SaveImage, Image Comparer (rgthree), INPAINT_VAEEncodeInpaintConditioning, Reroute, VAEDecode, PreviewImage, easy applyFooocusInpaint, ImageCompositeMasked, PreviewImage, Efficient Loader, KSampler]
patterns: []
missing: []
parameters: {"cfg": 6.98, "denoise": 0.25, "sampler_name": "dpmpp_2m", "scheduler": "karras", "seed": 762692654114122, "steps": 10}
---

# 平台全量/除水印 Remove Text Or Watermark_1863787080831680514.json

> 来源文件 `comfyui_library/workflows/平台全量/除水印 Remove Text Or Watermark_1863787080831680514.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（26 个）：
- `GroundingDinoSAMSegment (segment anything)`
- `GroundingDinoModelLoader (segment anything)`
- `SAMModelLoader (segment anything)`
- `Note`
- `AddMask`
- `MaskToImage`
- `LoadImage`
- `MaskPreview+`
- `PreviewImage`
- `GrowMaskWithBlur`
- `INPAINT_MaskedFill`
- `INPAINT_MaskedBlur`
- `Note`
- `PreviewImage`
- `ImageGenResolutionFromImage`
- `SaveImage`
- `Image Comparer (rgthree)`
- `INPAINT_VAEEncodeInpaintConditioning` ★核心
- `Reroute`
- `VAEDecode` ★核心
- `PreviewImage`
- `easy applyFooocusInpaint`
- `ImageCompositeMasked`
- `PreviewImage`
- `Efficient Loader`
- `KSampler` ★核心

## 关键参数

- `seed` = `762692654114122`
- `steps` = `10`
- `cfg` = `6.98`
- `sampler_name` = `dpmpp_2m`
- `scheduler` = `karras`
- `denoise` = `0.25`

## 知识

覆盖率 **69%**（18/26）

**有卡**：`GroundingDinoSAMSegment (segment anything)`、`GroundingDinoModelLoader (segment anything)`、`SAMModelLoader (segment anything)`、`AddMask`、`MaskToImage`、`LoadImage`、`MaskPreview+`、`GrowMaskWithBlur`、`INPAINT_MaskedFill`、`INPAINT_MaskedBlur`、`ImageGenResolutionFromImage`、`SaveImage`、`INPAINT_VAEEncodeInpaintConditioning`、`VAEDecode`、`easy applyFooocusInpaint`、`ImageCompositeMasked`、`Efficient Loader`、`KSampler`

**用到的条目**：KSampler、VAEDecode、LoadImage、INPAINT_VAEEncodeInpaintConditioning、ImageGenResolutionFromImage、MaskPreview+、SaveImage、AddMask

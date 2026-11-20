---
key: 平台全量/Oiled - Shiny - Sweaty_ Skin Enhance Workflow_1894204731424702466.json
name: Oiled - Shiny - Sweaty_ Skin Enhance Workflow_1894204731424702466
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/Oiled - Shiny - Sweaty_ Skin Enhance Workflow_1894204731424702466.json
hash: f02f9359d7366337
coverage: 0.896552
learned_at: 2026-11-14 00:47:29
nodes: [CR Apply Multi-ControlNet, AIO_Preprocessor, UltralyticsDetectorProvider, SAMLoader, APersonMaskGenerator, ImageUpscaleWithModel, UpscaleModelLoader, ToBasicPipe, ImageCompositeMasked, PreviewImage, CR Multi-ControlNet Stack, ImpactSimpleDetectorSEGS, DetailerForEachDebugPipe, GrowMaskWithBlur, MaskToSEGS, ConstrainImage|pysssss, PreviewImage, CR Simple Image Compare, SaveImage, Note, AIO_Preprocessor, VAELoader, CheckpointLoaderSimple, CR Apply LoRA Stack, CLIPTextEncode, CLIPTextEncode, SEGSSwitch, LoadImage, CR LoRA Stack]
patterns: []
missing: []
parameters: {"checkpoint": "majicmixRealistic_v7.safetensors"}
---

# 平台全量/Oiled - Shiny - Sweaty_ Skin Enhance Workflow_1894204731424702466.json

> 来源文件 `comfyui_library/workflows/平台全量/Oiled - Shiny - Sweaty_ Skin Enhance Workflow_1894204731424702466.json`

## 结构

**生成流程**：Model → Condition → Control → Process → Output → Other

**节点**（29 个）：
- `CR Apply Multi-ControlNet`
- `AIO_Preprocessor`
- `UltralyticsDetectorProvider`
- `SAMLoader`
- `APersonMaskGenerator`
- `ImageUpscaleWithModel`
- `UpscaleModelLoader`
- `ToBasicPipe`
- `ImageCompositeMasked`
- `PreviewImage`
- `CR Multi-ControlNet Stack`
- `ImpactSimpleDetectorSEGS`
- `DetailerForEachDebugPipe`
- `GrowMaskWithBlur`
- `MaskToSEGS`
- `ConstrainImage|pysssss`
- `PreviewImage`
- `CR Simple Image Compare`
- `SaveImage`
- `Note`
- `AIO_Preprocessor`
- `VAELoader`
- `CheckpointLoaderSimple` ★核心
- `CR Apply LoRA Stack`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `SEGSSwitch`
- `LoadImage`
- `CR LoRA Stack`

## 关键参数

- `checkpoint` = `majicmixRealistic_v7.safetensors`

## 知识

覆盖率 **90%**（26/29）

**有卡**：`CR Apply Multi-ControlNet`、`AIO_Preprocessor`、`UltralyticsDetectorProvider`、`SAMLoader`、`APersonMaskGenerator`、`ImageUpscaleWithModel`、`UpscaleModelLoader`、`ToBasicPipe`、`ImageCompositeMasked`、`CR Multi-ControlNet Stack`、`ImpactSimpleDetectorSEGS`、`DetailerForEachDebugPipe`、`GrowMaskWithBlur`、`MaskToSEGS`、`ConstrainImage|pysssss`、`CR Simple Image Compare`、`SaveImage`、`VAELoader`、`CheckpointLoaderSimple`、`CR Apply LoRA Stack`、`CLIPTextEncode`、`SEGSSwitch`、`LoadImage`、`CR LoRA Stack`

**用到的条目**：VAELoader、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、CR Apply Multi-ControlNet、CR Multi-ControlNet Stack、CR Apply LoRA Stack、CR LoRA Stack
